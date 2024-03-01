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
import multiprocessing
import os
import json
from time import sleep
import bstack_utils.bstack1lll11l11l_opy_ as bstack1l1lll11l1_opy_
from browserstack_sdk.bstack1llll1111_opy_ import *
from bstack_utils.config import Config
from bstack_utils.messages import bstack111llllll_opy_
class bstack11llll11l_opy_:
    def __init__(self, args, logger, bstack11lll11l1l_opy_, bstack11lll111l1_opy_):
        self.args = args
        self.logger = logger
        self.bstack11lll11l1l_opy_ = bstack11lll11l1l_opy_
        self.bstack11lll111l1_opy_ = bstack11lll111l1_opy_
        self._prepareconfig = None
        self.Config = None
        self.runner = None
        self.bstack1l1111111_opy_ = []
        self.bstack11ll1lll11_opy_ = None
        self.bstack111l1lll1_opy_ = []
        self.bstack11lll1111l_opy_ = self.bstack11111l1l_opy_()
        self.bstack1l1l11l11_opy_ = -1
    def bstack11llll1ll_opy_(self, bstack11ll1llll1_opy_):
        self.parse_args()
        self.bstack11lll11111_opy_()
        self.bstack11lll11l11_opy_(bstack11ll1llll1_opy_)
    @staticmethod
    def version():
        import pytest
        return pytest.__version__
    def bstack11ll1ll11l_opy_(self, arg):
        if arg in self.args:
            i = self.args.index(arg)
            self.args.pop(i + 1)
            self.args.pop(i)
    def parse_args(self):
        self.bstack1l1l11l11_opy_ = -1
        if bstack1l111l1_opy_ (u"ࠨࡲࡤࡶࡦࡲ࡬ࡦ࡮ࡶࡔࡪࡸࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨจ") in self.bstack11lll11l1l_opy_:
            self.bstack1l1l11l11_opy_ = int(self.bstack11lll11l1l_opy_[bstack1l111l1_opy_ (u"ࠩࡳࡥࡷࡧ࡬࡭ࡧ࡯ࡷࡕ࡫ࡲࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩฉ")])
        try:
            bstack11ll1ll1ll_opy_ = [bstack1l111l1_opy_ (u"ࠪ࠱࠲ࡪࡲࡪࡸࡨࡶࠬช"), bstack1l111l1_opy_ (u"ࠫ࠲࠳ࡰ࡭ࡷࡪ࡭ࡳࡹࠧซ"), bstack1l111l1_opy_ (u"ࠬ࠳ࡰࠨฌ")]
            if self.bstack1l1l11l11_opy_ >= 0:
                bstack11ll1ll1ll_opy_.extend([bstack1l111l1_opy_ (u"࠭࠭࠮ࡰࡸࡱࡵࡸ࡯ࡤࡧࡶࡷࡪࡹࠧญ"), bstack1l111l1_opy_ (u"ࠧ࠮ࡰࠪฎ")])
            for arg in bstack11ll1ll1ll_opy_:
                self.bstack11ll1ll11l_opy_(arg)
        except Exception as exc:
            self.logger.error(str(exc))
    def get_args(self):
        return self.args
    def bstack11lll11111_opy_(self):
        bstack11ll1lll11_opy_ = [os.path.normpath(item) for item in self.args]
        self.bstack11ll1lll11_opy_ = bstack11ll1lll11_opy_
        return bstack11ll1lll11_opy_
    def bstack11llll1l1_opy_(self):
        try:
            from _pytest.config import _prepareconfig
            from _pytest.config import Config
            from _pytest import runner
            import importlib
            bstack11ll1ll1l1_opy_ = importlib.find_loader(bstack1l111l1_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࡠࡵࡨࡰࡪࡴࡩࡶ࡯ࠪฏ"))
            self._prepareconfig = _prepareconfig
            self.Config = Config
            self.runner = runner
        except Exception as e:
            self.logger.warn(e, bstack111llllll_opy_)
    def bstack11lll11l11_opy_(self, bstack11ll1llll1_opy_):
        bstack11111111_opy_ = Config.bstack1ll1l11ll_opy_()
        if bstack11ll1llll1_opy_:
            self.bstack11ll1lll11_opy_.append(bstack1l111l1_opy_ (u"ࠩ࠰࠱ࡸࡱࡩࡱࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭ฐ"))
            self.bstack11ll1lll11_opy_.append(bstack1l111l1_opy_ (u"ࠪࡘࡷࡻࡥࠨฑ"))
        if bstack11111111_opy_.bstack11lll11ll1_opy_():
            self.bstack11ll1lll11_opy_.append(bstack1l111l1_opy_ (u"ࠫ࠲࠳ࡳ࡬࡫ࡳࡗࡪࡹࡳࡪࡱࡱࡗࡹࡧࡴࡶࡵࠪฒ"))
            self.bstack11ll1lll11_opy_.append(bstack1l111l1_opy_ (u"࡚ࠬࡲࡶࡧࠪณ"))
        self.bstack11ll1lll11_opy_.append(bstack1l111l1_opy_ (u"࠭࠭ࡱࠩด"))
        self.bstack11ll1lll11_opy_.append(bstack1l111l1_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺ࡟ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡶ࡬ࡶࡩ࡬ࡲࠬต"))
        self.bstack11ll1lll11_opy_.append(bstack1l111l1_opy_ (u"ࠨ࠯࠰ࡨࡷ࡯ࡶࡦࡴࠪถ"))
        self.bstack11ll1lll11_opy_.append(bstack1l111l1_opy_ (u"ࠩࡦ࡬ࡷࡵ࡭ࡦࠩท"))
        if self.bstack1l1l11l11_opy_ > 1:
            self.bstack11ll1lll11_opy_.append(bstack1l111l1_opy_ (u"ࠪ࠱ࡳ࠭ธ"))
            self.bstack11ll1lll11_opy_.append(str(self.bstack1l1l11l11_opy_))
    def bstack11ll1ll111_opy_(self):
        bstack111l1lll1_opy_ = []
        for spec in self.bstack1l1111111_opy_:
            bstack11ll11l1l_opy_ = [spec]
            bstack11ll11l1l_opy_ += self.bstack11ll1lll11_opy_
            bstack111l1lll1_opy_.append(bstack11ll11l1l_opy_)
        self.bstack111l1lll1_opy_ = bstack111l1lll1_opy_
        return bstack111l1lll1_opy_
    def bstack11111l1l_opy_(self):
        try:
            from pytest_bdd import reporting
            self.bstack11lll1111l_opy_ = True
            return True
        except Exception as e:
            self.bstack11lll1111l_opy_ = False
        return self.bstack11lll1111l_opy_
    def bstack1lllll11_opy_(self, bstack11ll1lll1l_opy_, bstack11llll1ll_opy_):
        bstack11llll1ll_opy_[bstack1l111l1_opy_ (u"ࠫࡈࡕࡎࡇࡋࡊࠫน")] = self.bstack11lll11l1l_opy_
        multiprocessing.set_start_method(bstack1l111l1_opy_ (u"ࠬࡹࡰࡢࡹࡱࠫบ"))
        if bstack1l111l1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩป") in self.bstack11lll11l1l_opy_:
            bstack1ll111111l_opy_ = []
            manager = multiprocessing.Manager()
            bstack1l1l11ll1l_opy_ = manager.list()
            for index, platform in enumerate(self.bstack11lll11l1l_opy_[bstack1l111l1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪผ")]):
                bstack1ll111111l_opy_.append(multiprocessing.Process(name=str(index),
                                                           target=bstack11ll1lll1l_opy_,
                                                           args=(self.bstack11ll1lll11_opy_, bstack11llll1ll_opy_, bstack1l1l11ll1l_opy_)))
            i = 0
            bstack11ll1lllll_opy_ = len(self.bstack11lll11l1l_opy_[bstack1l111l1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫฝ")])
            for t in bstack1ll111111l_opy_:
                os.environ[bstack1l111l1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡍࡓࡊࡅ࡙ࠩพ")] = str(i)
                os.environ[bstack1l111l1_opy_ (u"ࠪࡇ࡚ࡘࡒࡆࡐࡗࡣࡕࡒࡁࡕࡈࡒࡖࡒࡥࡄࡂࡖࡄࠫฟ")] = json.dumps(self.bstack11lll11l1l_opy_[bstack1l111l1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧภ")][i % bstack11ll1lllll_opy_])
                i += 1
                t.start()
            for t in bstack1ll111111l_opy_:
                t.join()
            return list(bstack1l1l11ll1l_opy_)
    @staticmethod
    def bstack1111l1ll1_opy_(driver, bstack1ll111ll1_opy_, logger, item=None, wait=False):
        item = item or getattr(threading.current_thread(), bstack1l111l1_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣ࡮ࡺࡥ࡮ࠩม"), None)
        if item and getattr(item, bstack1l111l1_opy_ (u"࠭࡟ࡢ࠳࠴ࡽࡤࡺࡥࡴࡶࡢࡧࡦࡹࡥࠨย"), None) and not getattr(item, bstack1l111l1_opy_ (u"ࠧࡠࡣ࠴࠵ࡾࡥࡳࡵࡱࡳࡣࡩࡵ࡮ࡦࠩร"), False):
            logger.info(
                bstack1l111l1_opy_ (u"ࠣࡃࡸࡸࡴࡳࡡࡵࡧࠣࡸࡪࡹࡴࠡࡥࡤࡷࡪࠦࡥࡹࡧࡦࡹࡹ࡯࡯࡯ࠢ࡫ࡥࡸࠦࡥ࡯ࡦࡨࡨ࠳ࠦࡐࡳࡱࡦࡩࡸࡹࡩ࡯ࡩࠣࡪࡴࡸࠠࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡵࡧࡶࡸ࡮ࡴࡧࠡ࡫ࡶࠤࡺࡴࡤࡦࡴࡺࡥࡾ࠴ࠢฤ"))
            bstack11lll111ll_opy_ = item.cls.__name__ if not item.cls is None else None
            bstack1l1lll11l1_opy_.bstack11l1l111l_opy_(driver, bstack11lll111ll_opy_, item.name, item.module.__name__, item.path, bstack1ll111ll1_opy_)
            item._a11y_stop_done = True
            if wait:
                sleep(2)