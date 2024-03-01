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
from collections import deque
from bstack_utils.constants import *
class bstack1ll1l11111_opy_:
    def __init__(self):
        self._111111l111_opy_ = deque()
        self._111111l1ll_opy_ = {}
        self._111111llll_opy_ = False
    def bstack111111l11l_opy_(self, test_name, bstack11111l111l_opy_):
        bstack111111ll11_opy_ = self._111111l1ll_opy_.get(test_name, {})
        return bstack111111ll11_opy_.get(bstack11111l111l_opy_, 0)
    def bstack1111111ll1_opy_(self, test_name, bstack11111l111l_opy_):
        bstack11111l11ll_opy_ = self.bstack111111l11l_opy_(test_name, bstack11111l111l_opy_)
        self.bstack1111111l1l_opy_(test_name, bstack11111l111l_opy_)
        return bstack11111l11ll_opy_
    def bstack1111111l1l_opy_(self, test_name, bstack11111l111l_opy_):
        if test_name not in self._111111l1ll_opy_:
            self._111111l1ll_opy_[test_name] = {}
        bstack111111ll11_opy_ = self._111111l1ll_opy_[test_name]
        bstack11111l11ll_opy_ = bstack111111ll11_opy_.get(bstack11111l111l_opy_, 0)
        bstack111111ll11_opy_[bstack11111l111l_opy_] = bstack11111l11ll_opy_ + 1
    def bstack1lll1l1l11_opy_(self, bstack111111lll1_opy_, bstack11111l11l1_opy_):
        bstack1111111lll_opy_ = self.bstack1111111ll1_opy_(bstack111111lll1_opy_, bstack11111l11l1_opy_)
        bstack111111ll1l_opy_ = bstack11l1l1111l_opy_[bstack11111l11l1_opy_]
        bstack11111l1111_opy_ = bstack1l111l1_opy_ (u"ࠢࡼࡿ࠰ࡿࢂ࠳ࡻࡾࠤᐒ").format(bstack111111lll1_opy_, bstack111111ll1l_opy_, bstack1111111lll_opy_)
        self._111111l111_opy_.append(bstack11111l1111_opy_)
    def bstack1lll11ll1_opy_(self):
        return len(self._111111l111_opy_) == 0
    def bstack1ll1ll1l11_opy_(self):
        bstack111111l1l1_opy_ = self._111111l111_opy_.popleft()
        return bstack111111l1l1_opy_
    def capturing(self):
        return self._111111llll_opy_
    def bstack1ll1l1l111_opy_(self):
        self._111111llll_opy_ = True
    def bstack1lll11l1ll_opy_(self):
        self._111111llll_opy_ = False