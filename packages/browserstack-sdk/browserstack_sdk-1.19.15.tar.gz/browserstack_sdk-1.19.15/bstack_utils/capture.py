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
import sys
class bstack1l11l11111_opy_:
    def __init__(self, handler):
        self._11l1ll111l_opy_ = sys.stdout.write
        self._11l1ll1111_opy_ = sys.stderr.write
        self.handler = handler
        self._started = False
    def start(self):
        if self._started:
            return
        self._started = True
        sys.stdout.write = self.bstack11l1l1lll1_opy_
        sys.stdout.error = self.bstack11l1l1llll_opy_
    def bstack11l1l1lll1_opy_(self, _str):
        self._11l1ll111l_opy_(_str)
        if self.handler:
            self.handler({bstack1l111l1_opy_ (u"ࠬࡲࡥࡷࡧ࡯ࠫໞ"): bstack1l111l1_opy_ (u"࠭ࡉࡏࡈࡒࠫໟ"), bstack1l111l1_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨ໠"): _str})
    def bstack11l1l1llll_opy_(self, _str):
        self._11l1ll1111_opy_(_str)
        if self.handler:
            self.handler({bstack1l111l1_opy_ (u"ࠨ࡮ࡨࡺࡪࡲࠧ໡"): bstack1l111l1_opy_ (u"ࠩࡈࡖࡗࡕࡒࠨ໢"), bstack1l111l1_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫ໣"): _str})
    def reset(self):
        if not self._started:
            return
        self._started = False
        sys.stdout.write = self._11l1ll111l_opy_
        sys.stderr.write = self._11l1ll1111_opy_