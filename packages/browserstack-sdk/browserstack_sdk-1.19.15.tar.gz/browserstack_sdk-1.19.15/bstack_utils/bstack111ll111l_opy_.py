# coding: UTF-8
import sys
bstack1l1l11_opy_ = sys.version_info [0] == 2
bstack11l1l1l_opy_ = 2048
bstack1ll1ll_opy_ = 7
def bstack1l111l1_opy_ (bstack1ll1lll_opy_):
    global bstack1lll1l1_opy_
    bstack1ll1ll1_opy_ = ord (bstack1ll1lll_opy_ [-1])
    bstack1111l1_opy_ = bstack1ll1lll_opy_ [:-1]
    bstack11l1ll_opy_ = bstack1ll1ll1_opy_ % len (bstack1111l1_opy_)
    bstack1l11l1l_opy_ = bstack1111l1_opy_ [:bstack11l1ll_opy_] + bstack1111l1_opy_ [bstack11l1ll_opy_:]
    if bstack1l1l11_opy_:
        bstack111ll11_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1l1l_opy_ - (bstack11l1_opy_ + bstack1ll1ll1_opy_) % bstack1ll1ll_opy_) for bstack11l1_opy_, char in enumerate (bstack1l11l1l_opy_)])
    else:
        bstack111ll11_opy_ = str () .join ([chr (ord (char) - bstack11l1l1l_opy_ - (bstack11l1_opy_ + bstack1ll1ll1_opy_) % bstack1ll1ll_opy_) for bstack11l1_opy_, char in enumerate (bstack1l11l1l_opy_)])
    return eval (bstack111ll11_opy_)
class bstack1l1l1111l_opy_:
    def __init__(self, handler):
        self._1lllll111l1_opy_ = None
        self.handler = handler
        self._1lllll11111_opy_ = self.bstack1lllll111ll_opy_()
        self.patch()
    def patch(self):
        self._1lllll111l1_opy_ = self._1lllll11111_opy_.execute
        self._1lllll11111_opy_.execute = self.bstack1lllll1111l_opy_()
    def bstack1lllll1111l_opy_(self):
        def execute(this, driver_command, *args, **kwargs):
            self.handler(bstack1l111l1_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࠧᑫ"), driver_command, None, this, args)
            response = self._1lllll111l1_opy_(this, driver_command, *args, **kwargs)
            self.handler(bstack1l111l1_opy_ (u"ࠨࡡࡧࡶࡨࡶࠧᑬ"), driver_command, response)
            return response
        return execute
    def reset(self):
        self._1lllll11111_opy_.execute = self._1lllll111l1_opy_
    @staticmethod
    def bstack1lllll111ll_opy_():
        from selenium.webdriver.remote.webdriver import WebDriver
        return WebDriver