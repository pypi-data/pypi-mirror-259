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
from browserstack_sdk.bstack11l1ll11_opy_ import bstack11llll11l_opy_
from browserstack_sdk.bstack11lllll1l1_opy_ import RobotHandler
def bstack1111ll1l_opy_(framework):
    if framework.lower() == bstack1l111l1_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬᅷ"):
        return bstack11llll11l_opy_.version()
    elif framework.lower() == bstack1l111l1_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬᅸ"):
        return RobotHandler.version()
    elif framework.lower() == bstack1l111l1_opy_ (u"ࠧࡣࡧ࡫ࡥࡻ࡫ࠧᅹ"):
        import behave
        return behave.__version__
    else:
        return bstack1l111l1_opy_ (u"ࠨࡷࡱ࡯ࡳࡵࡷ࡯ࠩᅺ")