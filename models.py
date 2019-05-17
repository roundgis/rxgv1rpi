# -*- coding: utf-8 -*-

import rg_lib


class ErrorTypes:
    @classmethod
    def UnsupportedOp(cls):
        return rg_lib.ErrorType.DeclaredType("UnsupportedOp")

    @classmethod
    def InvalidNetworkId(cls):
        return rg_lib.ErrorType.DeclaredType("InvalidNetworkId")

    @classmethod
    def NoZbModule(cls):
        return rg_lib.ErrorType.DeclaredType("NoZbModule")
