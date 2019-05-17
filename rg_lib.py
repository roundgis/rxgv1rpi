import sys
from twisted.internet import defer
from twisted.python import failure, log
from cyclone import web as cyclone_web
from cyclone import jsonrpc as cyclone_jsonrpc
from cyclone import escape as cyclone_escape


class RGError(Exception):
    def __init__(self, message):
        self.message = message


class ErrorType:
    @classmethod
    def DeclaredType(cls, name):
        return {"declaredType": name, 'msg': ''}

    @classmethod
    def IsErrorType(cls, obj):
        return isinstance(obj, dict) and "declaredType" in obj

    @classmethod
    def NoMethod(cls):
        return cls.DeclaredType("NoMethod")

    @classmethod
    def ServerErr(cls, message):
        temp = cls.DeclaredType("ServerErr")
        temp["msg"] = message
        return temp


class BaseRpcHandler(cyclone_jsonrpc.JsonrpcRequestHandler):
    def _cbResult(self, result, jsonid):
        if isinstance(result, failure.Failure):
            if isinstance(result.value, RGError):
                error = result.value.message
            else:
                error = ErrorType.ServerErr("server error")
            result = None
        elif isinstance(result, AttributeError):
            error = ErrorType.NoMethod()
            result = None
        else:
            error = None
        data = {"result": result, "error": error, "id": jsonid}
        self.finish(cyclone_escape.json_encode(data))


class AsyncDynFuncHandler(BaseRpcHandler):
    def GetFunc(self, func_name):
        raise NotImplementedError()

    def post(self, *args):
        self._auto_finish = False
        try:
            req = cyclone_escape.json_decode(self.request.body)
            jsonid = req["id"]
            method = req["method"]
            assert isinstance(method, str), \
                              "Invalid method type: %s" % type(method)
            params = req.get("params", [])
            assert isinstance(params, (list, tuple)), \
                              "Invalid params type: %s" % type(params)
        except Exception as e:
            log.msg("Bad Request: %s" % str(e))
            raise cyclone_web.HTTPError(400)

        func = self.GetFunc(method)
        if callable(func):
            args = list(args) + params
            d = defer.ensureDeferred(func(*args))
            d.addBoth(self._cbResult, jsonid)
        else:
            self._cbResult(AttributeError("method not found: %s" % method),
                           jsonid)


class Cyclone:
    @classmethod
    def HandleErr(cls, exc_info_obj):
        log.err(exc_info_obj[1])
        raise exc_info_obj[0].with_traceback(exc_info_obj[1], exc_info_obj[2])

    @classmethod
    def HandleErrInException(cls):
        exc_info_obj = sys.exc_info()
        err_msg = getattr(exc_info_obj[1], "message", None)
        if ErrorType.IsErrorType(err_msg):
            raise RGError(err_msg)
        else:
            cls.HandleErr(exc_info_obj)


class Process:
    @classmethod
    def Kill(cls, pid):
        import os
        import signal
        os.kill(int(pid), signal.SIGTERM)


