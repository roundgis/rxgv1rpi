import sys
from twisted.internet import reactor, defer
from twisted.python import log, logfile
import web_app
import settings
import xy_lib


def InitWebService():
    reactor.listenTCP(settings.HTTP_PORT, web_app.App())


async def Init():
    await xy_lib.API.ProbeModule()
    InitWebService()


def main():
    try:
        log.startLogging(logfile.DailyLogFile.fromFullPath(settings.LOG_PATH + "/" +
                                                           "rxg" +''.join([i for i in settings.HOST if i != '.']) + "_log.txt"),
                         setStdout=False)
        reactor.callLater(1, defer.ensureDeferred, Init())
        reactor.run()
    except Exception:
        log.err()


if __name__ == "__main__":
    args = sys.argv
    main()

