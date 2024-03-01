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
import json
class bstack11l1ll11l1_opy_(object):
  bstack11l111111_opy_ = os.path.join(os.path.expanduser(bstack1l111l1_opy_ (u"ࠬࢄ້ࠧ")), bstack1l111l1_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ໊࠭"))
  bstack11l1ll11ll_opy_ = os.path.join(bstack11l111111_opy_, bstack1l111l1_opy_ (u"ࠧࡤࡱࡰࡱࡦࡴࡤࡴ࠰࡭ࡷࡴࡴ໋ࠧ"))
  bstack11l1ll1lll_opy_ = None
  perform_scan = None
  bstack1l11ll11_opy_ = None
  bstack1l11lll1_opy_ = None
  bstack11l1llll1l_opy_ = None
  def __new__(cls):
    if not hasattr(cls, bstack1l111l1_opy_ (u"ࠨ࡫ࡱࡷࡹࡧ࡮ࡤࡧࠪ໌")):
      cls.instance = super(bstack11l1ll11l1_opy_, cls).__new__(cls)
      cls.instance.bstack11l1ll1ll1_opy_()
    return cls.instance
  def bstack11l1ll1ll1_opy_(self):
    try:
      with open(self.bstack11l1ll11ll_opy_, bstack1l111l1_opy_ (u"ࠩࡵࠫໍ")) as bstack11ll1ll11_opy_:
        bstack11l1ll1l11_opy_ = bstack11ll1ll11_opy_.read()
        data = json.loads(bstack11l1ll1l11_opy_)
        if bstack1l111l1_opy_ (u"ࠪࡧࡴࡳ࡭ࡢࡰࡧࡷࠬ໎") in data:
          self.bstack11l1llllll_opy_(data[bstack1l111l1_opy_ (u"ࠫࡨࡵ࡭࡮ࡣࡱࡨࡸ࠭໏")])
        if bstack1l111l1_opy_ (u"ࠬࡹࡣࡳ࡫ࡳࡸࡸ࠭໐") in data:
          self.bstack11ll1111l1_opy_(data[bstack1l111l1_opy_ (u"࠭ࡳࡤࡴ࡬ࡴࡹࡹࠧ໑")])
    except:
      pass
  def bstack11ll1111l1_opy_(self, scripts):
    if scripts != None:
      self.perform_scan = scripts[bstack1l111l1_opy_ (u"ࠧࡴࡥࡤࡲࠬ໒")]
      self.bstack1l11ll11_opy_ = scripts[bstack1l111l1_opy_ (u"ࠨࡩࡨࡸࡗ࡫ࡳࡶ࡮ࡷࡷࠬ໓")]
      self.bstack1l11lll1_opy_ = scripts[bstack1l111l1_opy_ (u"ࠩࡪࡩࡹࡘࡥࡴࡷ࡯ࡸࡸ࡙ࡵ࡮࡯ࡤࡶࡾ࠭໔")]
      self.bstack11l1llll1l_opy_ = scripts[bstack1l111l1_opy_ (u"ࠪࡷࡦࡼࡥࡓࡧࡶࡹࡱࡺࡳࠨ໕")]
  def bstack11l1llllll_opy_(self, bstack11l1ll1lll_opy_):
    if bstack11l1ll1lll_opy_ != None and len(bstack11l1ll1lll_opy_) != 0:
      self.bstack11l1ll1lll_opy_ = bstack11l1ll1lll_opy_
  def store(self):
    try:
      with open(self.bstack11l1ll11ll_opy_, bstack1l111l1_opy_ (u"ࠫࡼ࠭໖")) as file:
        json.dump({
          bstack1l111l1_opy_ (u"ࠧࡩ࡯࡮࡯ࡤࡲࡩࡹࠢ໗"): self.bstack11l1ll1lll_opy_,
          bstack1l111l1_opy_ (u"ࠨࡳࡤࡴ࡬ࡴࡹࡹࠢ໘"): {
            bstack1l111l1_opy_ (u"ࠢࡴࡥࡤࡲࠧ໙"): self.perform_scan,
            bstack1l111l1_opy_ (u"ࠣࡩࡨࡸࡗ࡫ࡳࡶ࡮ࡷࡷࠧ໚"): self.bstack1l11ll11_opy_,
            bstack1l111l1_opy_ (u"ࠤࡪࡩࡹࡘࡥࡴࡷ࡯ࡸࡸ࡙ࡵ࡮࡯ࡤࡶࡾࠨ໛"): self.bstack1l11lll1_opy_,
            bstack1l111l1_opy_ (u"ࠥࡷࡦࡼࡥࡓࡧࡶࡹࡱࡺࡳࠣໜ"): self.bstack11l1llll1l_opy_
          }
        }, file)
    except:
      pass
  def bstack1l1l1ll1ll_opy_(self, bstack11l1ll1l1l_opy_):
    try:
      return any(command.get(bstack1l111l1_opy_ (u"ࠫࡳࡧ࡭ࡦࠩໝ")) == bstack11l1ll1l1l_opy_ for command in self.bstack11l1ll1lll_opy_)
    except:
      return False
bstack1lll1l1l1_opy_ = bstack11l1ll11l1_opy_()