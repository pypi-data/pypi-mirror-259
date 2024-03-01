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
import os
class RobotHandler():
    def __init__(self, args, logger, bstack11lll11l1l_opy_, bstack11lll111l1_opy_):
        self.args = args
        self.logger = logger
        self.bstack11lll11l1l_opy_ = bstack11lll11l1l_opy_
        self.bstack11lll111l1_opy_ = bstack11lll111l1_opy_
    @staticmethod
    def version():
        import robot
        return robot.__version__
    @staticmethod
    def bstack11lll1l111_opy_(bstack11ll1l1lll_opy_):
        bstack11ll1l1ll1_opy_ = []
        if bstack11ll1l1lll_opy_:
            tokens = str(os.path.basename(bstack11ll1l1lll_opy_)).split(bstack1l111l1_opy_ (u"ࠤࡢࠦล"))
            camelcase_name = bstack1l111l1_opy_ (u"ࠥࠤࠧฦ").join(t.title() for t in tokens)
            suite_name, bstack11ll1l1l1l_opy_ = os.path.splitext(camelcase_name)
            bstack11ll1l1ll1_opy_.append(suite_name)
        return bstack11ll1l1ll1_opy_
    @staticmethod
    def bstack11ll1l1l11_opy_(typename):
        if bstack1l111l1_opy_ (u"ࠦࡆࡹࡳࡦࡴࡷ࡭ࡴࡴࠢว") in typename:
            return bstack1l111l1_opy_ (u"ࠧࡇࡳࡴࡧࡵࡸ࡮ࡵ࡮ࡆࡴࡵࡳࡷࠨศ")
        return bstack1l111l1_opy_ (u"ࠨࡕ࡯ࡪࡤࡲࡩࡲࡥࡥࡇࡵࡶࡴࡸࠢษ")