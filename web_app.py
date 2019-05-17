import cyclone.web as cyclone_web
import apis_http
import rxg_consts


def GetApi():
    return [(rxg_consts.URLs.API_XY, apis_http.XY)]


class App(cyclone_web.Application):
    def __init__(self):
        cyclone_web.Application.__init__(self, GetApi(), gzip=True)
