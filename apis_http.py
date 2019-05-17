import functools
from twisted.python import log
import rg_lib
import xy_lib
import models


class _XY:
    @classmethod
    async def GetModules(cls, req_handler, para):
        return xy_lib.API.GetModules()

    @classmethod
    async def GetModule(cls, req_handler, para):
        return xy_lib.API.GetModule(para['moduleid'])

    @classmethod
    async def ProbeDevice(cls, req_handler, para):
        """
        :param req_handler:
        :param para: {moduleid, nid}
        :return:
        """
        try:
            return await xy_lib.API.ProbeDevice(para['moduleid'])
        except xy_lib.NoModuleError:
            raise rg_lib.RGError(models.ErrorTypes.NoZbModule())
        except Exception:
            rg_lib.Cyclone.HandleErrInException()

    @classmethod
    async def GetSwitchStatus(cls, req_handler, para):
        """
        :param req_handler:
        :param para: {"arg": {moduleid, nid}}
        :return:
        """
        try:
            return await xy_lib.API.GetSwitchStatus(para['moduleid'], para['nid'])
        except xy_lib.NoModuleError:
            raise rg_lib.RGError(models.ErrorTypes.NoZbModule())
        except Exception:
            rg_lib.Cyclone.HandleErrInException()

    @classmethod
    async def SetSwitchStatus(cls, req_handler, para):
        """
        :param req_handler:
        :param para: {moduleid, nid, on_off}
        :return:
        """
        try:
            return await xy_lib.API.SetSwitchStatus(para['moduleid'], para['nid'], para['on_off'])
        except xy_lib.NoModuleError:
            raise rg_lib.RGError(models.ErrorTypes.NoZbModule())
        except Exception:
            rg_lib.Cyclone.HandleErrInException()

    @classmethod
    async def RemoveDevice(cls, req_handler, para):
        """
        :param req_handler:
        :param para: {moduleid, nid, deviceid}
        :return:
        """
        try:
            return await xy_lib.API.RemoveDevice(para['moduleid'], para['nid'], para['deviceid'])
        except xy_lib.NoModuleError:
            raise rg_lib.RGError(models.ErrorTypes.NoZbModule())
        except Exception:
            rg_lib.Cyclone.HandleErrInException()

    @classmethod
    async def GetDeviceNId(cls, req_handler, para):
        """
        :param req_handler:
        :param para: {moduleid, deviceid}
        :return:
        """
        try:
            return await xy_lib.API.GetDeviceNId(para['moduleid'], para['deviceid'])
        except xy_lib.NoModuleError:
            raise rg_lib.RGError(models.ErrorTypes.NoZbModule())
        except Exception:
            rg_lib.Cyclone.HandleErrInException()

    @classmethod
    async def GetTemperatureHumidity(cls, req_handler, para):
        """
        :param req_handler:
        :param para: {moduleid, nid}
        :return:
        """
        try:
            return await xy_lib.API.GetTemperatureHumidity(para['moduleid'],
                                                           para['nid'])
        except xy_lib.NoModuleError:
            raise rg_lib.RGError(models.ErrorTypes.NoZbModule())
        except Exception:
            rg_lib.Cyclone.HandleErrInException()

    @classmethod
    async def GetLiquidLevel(cls, req_handler, para):
        """
        :param req_handler:
        :param para: {moduleid, deviceid}
        :return:
        """
        try:
            return await xy_lib.API.GetLiquidLevel(para['moduleid'], para['nid'])
        except xy_lib.NoModuleError:
            raise rg_lib.RGError(models.ErrorTypes.NoZbModule())
        except Exception:
            rg_lib.Cyclone.HandleErrInException()

    @classmethod
    async def GetSoil3IN1(cls, req_handler, para):
        """
        :param req_handler:
        :param para: {moduleid, deviceid}
        :return:
        """
        try:
            return await xy_lib.API.GetSoil3IN1(para['moduleid'], para['nid'])
        except xy_lib.NoModuleError:
            raise rg_lib.RGError(models.ErrorTypes.NoZbModule())
        except Exception:
            rg_lib.Cyclone.HandleErrInException()

    @classmethod
    async def GetAnalog(cls, req_handler, para):
        """
        :param req_handler:
        :param para: {moduleid, deviceid}
        :return:
        """
        try:
            return await xy_lib.API.GetAnalog(para['moduleid'], para['nid'])
        except xy_lib.NoModuleError:
            raise rg_lib.RGError(models.ErrorTypes.NoZbModule())
        except Exception:
            rg_lib.Cyclone.HandleErrInException()

    @classmethod
    async def RebootDevice(cls, req_handler, para):
        """
        :param req_handler:
        :param para: {moduleid, deviceid}
        :return:
        """
        try:
            return await xy_lib.API.RebootDevice(para['moduleid'], para['nid'])
        except xy_lib.NoModuleError:
            raise rg_lib.RGError(models.ErrorTypes.NoZbModule())
        except Exception:
            rg_lib.Cyclone.HandleErrInException()

    @classmethod
    async def RebootModule(cls, req_handler, para):
        """
        :param req_handler:
        :param para: {moduleid}
        :return:
        """
        try:
            return await xy_lib.API.RebootModule(para['moduleid'])
        except xy_lib.NoModuleError:
            raise rg_lib.RGError(models.ErrorTypes.NoZbModule())
        except Exception:
            rg_lib.Cyclone.HandleErrInException()

    @classmethod
    async def RebootAll(cls, req_handler, para):
        """
        :param req_handler:
        :param para: {}
        :return:
        """
        try:
            return await xy_lib.API.RebootAll()
        except xy_lib.NoModuleError:
            raise rg_lib.RGError(models.ErrorTypes.NoZbModule())
        except Exception:
            rg_lib.Cyclone.HandleErrInException()

    @classmethod
    async def ClearModule(cls, req_handler, para):
        """
        :param req_handler:
        :param para: {moduleid}
        :return:
        """
        try:
            return await xy_lib.API.ClearModule(para['moduleid'])
        except xy_lib.NoModuleError:
            raise rg_lib.RGError(models.ErrorTypes.NoZbModule())
        except Exception:
            rg_lib.Cyclone.HandleErrInException()

    @classmethod
    async def BackupModule(cls, req_handler, para):
        """
        :param req_handler:
        :param para: {"arg": {moduleid}}
        :return:
        """
        try:
            return await xy_lib.API.BackupModule(para['moduleid'])
        except xy_lib.NoModuleError:
            raise rg_lib.RGError(models.ErrorTypes.NoZbModule())
        except Exception:
            rg_lib.Cyclone.HandleErrInException()

    @classmethod
    async def RestoreModule(cls, req_handler, para):
        """
        :param req_handler:
        :param para: {moduleid, backup}
        :return:
        """
        try:
            return await xy_lib.API.RestoreModule(para['moduleid'], para['backup'])
        except xy_lib.NoModuleError:
            raise rg_lib.RGError(models.ErrorTypes.NoZbModule())
        except Exception:
            rg_lib.Cyclone.HandleErrInException()

    @classmethod
    async def RestartRXG(cls, req_handler):
        import os
        try:
            rg_lib.Process.Kill(os.getpid())
            return 'ok'
        except Exception:
            rg_lib.Cyclone.HandleErrInException()


class Base(rg_lib.AsyncDynFuncHandler):
    def initialize(self, **kwargs):
        self.FUNC_TBL = {}

    def GetFunc(self, func_name):
        return self.FUNC_TBL[func_name] if func_name in self.FUNC_TBL else None


class XY(Base):
    def initialize(self, **kwargs):
        self.FUNC_TBL = {"GetSwitchStatus": functools.partial(_XY.GetSwitchStatus, self),
                         "GetTemperatureHumidity": functools.partial(_XY.GetTemperatureHumidity, self),
                         "GetLiquidLevel": functools.partial(_XY.GetLiquidLevel, self),
                         "GetSoil3IN1": functools.partial(_XY.GetSoil3IN1, self),
                         'GetAnalog': functools.partial(_XY.GetAnalog, self),
                         'SetSwitchStatus': functools.partial(_XY.SetSwitchStatus, self),
                         'ProbeDevice': functools.partial(_XY.ProbeDevice, self),
                         'RemoveDevice': functools.partial(_XY.RemoveDevice, self),
                         'GetDeviceNId': functools.partial(_XY.GetDeviceNId, self),
                         'RebootDevice': functools.partial(_XY.RebootDevice, self),
                         'RebootModule': functools.partial(_XY.RebootModule, self),
                         'RebootAll': functools.partial(_XY.RebootAll, self),
                         'ClearModule': functools.partial(_XY.ClearModule, self),
                         'BackupModule': functools.partial(_XY.BackupModule, self),
                         'RestoreModule': functools.partial(_XY.RestoreModule, self),
                         'GetModules': functools.partial(_XY.GetModules, self),
                         'GetModule': functools.partial(_XY.GetModule, self),
                         'RestartRXG': functools.partial(_XY.RestartRXG, self)}
