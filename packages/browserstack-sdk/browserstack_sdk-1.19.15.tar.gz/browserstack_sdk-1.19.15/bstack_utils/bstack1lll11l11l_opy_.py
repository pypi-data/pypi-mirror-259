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
import requests
import logging
from urllib.parse import urlparse
from datetime import datetime
from bstack_utils.constants import bstack11ll111ll1_opy_ as bstack11ll111lll_opy_
from bstack_utils.bstack1lll1l1l1_opy_ import bstack1lll1l1l1_opy_
from bstack_utils.helper import bstack1lll11llll_opy_, bstack1ll1l1ll1l_opy_, bstack11l1llll11_opy_, bstack11ll11l1ll_opy_, bstack11111l11l_opy_, get_host_info, bstack11ll1l1111_opy_, bstack1ll1llll1_opy_, bstack1l1111lll1_opy_
from browserstack_sdk._version import __version__
logger = logging.getLogger(__name__)
@bstack1l1111lll1_opy_(class_method=False)
def _11ll1l11ll_opy_(driver, bstack1ll111ll1_opy_):
  response = {}
  try:
    caps = driver.capabilities
    response = {
        bstack1l111l1_opy_ (u"ࠧࡰࡵࡢࡲࡦࡳࡥࠨส"): caps.get(bstack1l111l1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡑࡥࡲ࡫ࠧห"), None),
        bstack1l111l1_opy_ (u"ࠩࡲࡷࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭ฬ"): bstack1ll111ll1_opy_.get(bstack1l111l1_opy_ (u"ࠪࡳࡸ࡜ࡥࡳࡵ࡬ࡳࡳ࠭อ"), None),
        bstack1l111l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡤࡴࡡ࡮ࡧࠪฮ"): caps.get(bstack1l111l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪฯ"), None),
        bstack1l111l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨะ"): caps.get(bstack1l111l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨั"), None)
    }
  except Exception as error:
    logger.debug(bstack1l111l1_opy_ (u"ࠨࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡧࡧࡷࡧ࡭࡯࡮ࡨࠢࡳࡰࡦࡺࡦࡰࡴࡰࠤࡩ࡫ࡴࡢ࡫࡯ࡷࠥࡽࡩࡵࡪࠣࡩࡷࡸ࡯ࡳࠢ࠽ࠤࠬา") + str(error))
  return response
def bstack1111l1ll_opy_(config):
  return config.get(bstack1l111l1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩำ"), False) or any([p.get(bstack1l111l1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪิ"), False) == True for p in config.get(bstack1l111l1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧี"), [])])
def bstack1lllll1ll_opy_(config, bstack1l1l11l11l_opy_):
  try:
    if not bstack1ll1l1ll1l_opy_(config):
      return False
    bstack11ll11l111_opy_ = config.get(bstack1l111l1_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬึ"), False)
    bstack11ll11llll_opy_ = config[bstack1l111l1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩื")][bstack1l1l11l11l_opy_].get(bstack1l111l1_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿุࠧ"), None)
    if bstack11ll11llll_opy_ != None:
      bstack11ll11l111_opy_ = bstack11ll11llll_opy_
    bstack11ll11ll1l_opy_ = os.getenv(bstack1l111l1_opy_ (u"ࠨࡄࡖࡣࡆ࠷࠱࡚ࡡࡍู࡛࡙࠭")) is not None and len(os.getenv(bstack1l111l1_opy_ (u"ࠩࡅࡗࡤࡇ࠱࠲࡛ࡢࡎ࡜ฺ࡚ࠧ"))) > 0 and os.getenv(bstack1l111l1_opy_ (u"ࠪࡆࡘࡥࡁ࠲࠳࡜ࡣࡏ࡝ࡔࠨ฻")) != bstack1l111l1_opy_ (u"ࠫࡳࡻ࡬࡭ࠩ฼")
    return bstack11ll11l111_opy_ and bstack11ll11ll1l_opy_
  except Exception as error:
    logger.debug(bstack1l111l1_opy_ (u"ࠬࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡻ࡫ࡲࡪࡨࡼ࡭ࡳ࡭ࠠࡵࡪࡨࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡽࡩࡵࡪࠣࡩࡷࡸ࡯ࡳࠢ࠽ࠤࠬ฽") + str(error))
  return False
def bstack1l1l111l_opy_(bstack11ll1l11l1_opy_, test_tags):
  bstack11ll1l11l1_opy_ = os.getenv(bstack1l111l1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡢࡅࡈࡉࡅࡔࡕࡌࡆࡎࡒࡉࡕ࡛ࡢࡇࡔࡔࡆࡊࡉࡘࡖࡆ࡚ࡉࡐࡐࡢ࡝ࡒࡒࠧ฾"))
  if bstack11ll1l11l1_opy_ is None:
    return True
  bstack11ll1l11l1_opy_ = json.loads(bstack11ll1l11l1_opy_)
  try:
    include_tags = bstack11ll1l11l1_opy_[bstack1l111l1_opy_ (u"ࠧࡪࡰࡦࡰࡺࡪࡥࡕࡣࡪࡷࡎࡴࡔࡦࡵࡷ࡭ࡳ࡭ࡓࡤࡱࡳࡩࠬ฿")] if bstack1l111l1_opy_ (u"ࠨ࡫ࡱࡧࡱࡻࡤࡦࡖࡤ࡫ࡸࡏ࡮ࡕࡧࡶࡸ࡮ࡴࡧࡔࡥࡲࡴࡪ࠭เ") in bstack11ll1l11l1_opy_ and isinstance(bstack11ll1l11l1_opy_[bstack1l111l1_opy_ (u"ࠩ࡬ࡲࡨࡲࡵࡥࡧࡗࡥ࡬ࡹࡉ࡯ࡖࡨࡷࡹ࡯࡮ࡨࡕࡦࡳࡵ࡫ࠧแ")], list) else []
    exclude_tags = bstack11ll1l11l1_opy_[bstack1l111l1_opy_ (u"ࠪࡩࡽࡩ࡬ࡶࡦࡨࡘࡦ࡭ࡳࡊࡰࡗࡩࡸࡺࡩ࡯ࡩࡖࡧࡴࡶࡥࠨโ")] if bstack1l111l1_opy_ (u"ࠫࡪࡾࡣ࡭ࡷࡧࡩ࡙ࡧࡧࡴࡋࡱࡘࡪࡹࡴࡪࡰࡪࡗࡨࡵࡰࡦࠩใ") in bstack11ll1l11l1_opy_ and isinstance(bstack11ll1l11l1_opy_[bstack1l111l1_opy_ (u"ࠬ࡫ࡸࡤ࡮ࡸࡨࡪ࡚ࡡࡨࡵࡌࡲ࡙࡫ࡳࡵ࡫ࡱ࡫ࡘࡩ࡯ࡱࡧࠪไ")], list) else []
    excluded = any(tag in exclude_tags for tag in test_tags)
    included = len(include_tags) == 0 or any(tag in include_tags for tag in test_tags)
    return not excluded and included
  except Exception as error:
    logger.debug(bstack1l111l1_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡽࡨࡪ࡮ࡨࠤࡻࡧ࡬ࡪࡦࡤࡸ࡮ࡴࡧࠡࡶࡨࡷࡹࠦࡣࡢࡵࡨࠤ࡫ࡵࡲࠡࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡤࡨࡪࡴࡸࡥࠡࡵࡦࡥࡳࡴࡩ࡯ࡩ࠱ࠤࡊࡸࡲࡰࡴࠣ࠾ࠥࠨๅ") + str(error))
  return False
def bstack1ll11l11l1_opy_(config, bstack11l1lll1ll_opy_, bstack11ll111l1l_opy_, bstack11l1lll11l_opy_):
  bstack11ll11l11l_opy_ = bstack11l1llll11_opy_(config)
  bstack11ll11111l_opy_ = bstack11ll11l1ll_opy_(config)
  if bstack11ll11l11l_opy_ is None or bstack11ll11111l_opy_ is None:
    logger.error(bstack1l111l1_opy_ (u"ࠧࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡻ࡭࡯࡬ࡦࠢࡦࡶࡪࡧࡴࡪࡰࡪࠤࡹ࡫ࡳࡵࠢࡵࡹࡳࠦࡦࡰࡴࠣࡆࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡀࠠࡎ࡫ࡶࡷ࡮ࡴࡧࠡࡣࡸࡸ࡭࡫࡮ࡵ࡫ࡦࡥࡹ࡯࡯࡯ࠢࡷࡳࡰ࡫࡮ࠨๆ"))
    return [None, None]
  try:
    settings = json.loads(os.getenv(bstack1l111l1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡤࡇࡃࡄࡇࡖࡗࡎࡈࡉࡍࡋࡗ࡝ࡤࡉࡏࡏࡈࡌࡋ࡚ࡘࡁࡕࡋࡒࡒࡤ࡟ࡍࡍࠩ็"), bstack1l111l1_opy_ (u"ࠩࡾࢁ่ࠬ")))
    data = {
        bstack1l111l1_opy_ (u"ࠪࡴࡷࡵࡪࡦࡥࡷࡒࡦࡳࡥࠨ้"): config[bstack1l111l1_opy_ (u"ࠫࡵࡸ࡯࡫ࡧࡦࡸࡓࡧ࡭ࡦ๊ࠩ")],
        bstack1l111l1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨ๋"): config.get(bstack1l111l1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩ์"), os.path.basename(os.getcwd())),
        bstack1l111l1_opy_ (u"ࠧࡴࡶࡤࡶࡹ࡚ࡩ࡮ࡧࠪํ"): bstack1lll11llll_opy_(),
        bstack1l111l1_opy_ (u"ࠨࡦࡨࡷࡨࡸࡩࡱࡶ࡬ࡳࡳ࠭๎"): config.get(bstack1l111l1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡅࡧࡶࡧࡷ࡯ࡰࡵ࡫ࡲࡲࠬ๏"), bstack1l111l1_opy_ (u"ࠪࠫ๐")),
        bstack1l111l1_opy_ (u"ࠫࡸࡵࡵࡳࡥࡨࠫ๑"): {
            bstack1l111l1_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡏࡣࡰࡩࠬ๒"): bstack11l1lll1ll_opy_,
            bstack1l111l1_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡘࡨࡶࡸ࡯࡯࡯ࠩ๓"): bstack11ll111l1l_opy_,
            bstack1l111l1_opy_ (u"ࠧࡴࡦ࡮࡚ࡪࡸࡳࡪࡱࡱࠫ๔"): __version__,
            bstack1l111l1_opy_ (u"ࠨ࡮ࡤࡲ࡬ࡻࡡࡨࡧࠪ๕"): bstack1l111l1_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯ࠩ๖"),
            bstack1l111l1_opy_ (u"ࠪࡸࡪࡹࡴࡇࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪ๗"): bstack1l111l1_opy_ (u"ࠫࡸ࡫࡬ࡦࡰ࡬ࡹࡲ࠭๘"),
            bstack1l111l1_opy_ (u"ࠬࡺࡥࡴࡶࡉࡶࡦࡳࡥࡸࡱࡵ࡯࡛࡫ࡲࡴ࡫ࡲࡲࠬ๙"): bstack11l1lll11l_opy_
        },
        bstack1l111l1_opy_ (u"࠭ࡳࡦࡶࡷ࡭ࡳ࡭ࡳࠨ๚"): settings,
        bstack1l111l1_opy_ (u"ࠧࡷࡧࡵࡷ࡮ࡵ࡮ࡄࡱࡱࡸࡷࡵ࡬ࠨ๛"): bstack11ll1l1111_opy_(),
        bstack1l111l1_opy_ (u"ࠨࡥ࡬ࡍࡳ࡬࡯ࠨ๜"): bstack11111l11l_opy_(),
        bstack1l111l1_opy_ (u"ࠩ࡫ࡳࡸࡺࡉ࡯ࡨࡲࠫ๝"): get_host_info(),
        bstack1l111l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠬ๞"): bstack1ll1l1ll1l_opy_(config)
    }
    headers = {
        bstack1l111l1_opy_ (u"ࠫࡈࡵ࡮ࡵࡧࡱࡸ࠲࡚ࡹࡱࡧࠪ๟"): bstack1l111l1_opy_ (u"ࠬࡧࡰࡱ࡮࡬ࡧࡦࡺࡩࡰࡰ࠲࡮ࡸࡵ࡮ࠨ๠"),
    }
    config = {
        bstack1l111l1_opy_ (u"࠭ࡡࡶࡶ࡫ࠫ๡"): (bstack11ll11l11l_opy_, bstack11ll11111l_opy_),
        bstack1l111l1_opy_ (u"ࠧࡩࡧࡤࡨࡪࡸࡳࠨ๢"): headers
    }
    response = bstack1ll1llll1_opy_(bstack1l111l1_opy_ (u"ࠨࡒࡒࡗ࡙࠭๣"), bstack11ll111lll_opy_ + bstack1l111l1_opy_ (u"ࠩ࠲ࡺ࠷࠵ࡴࡦࡵࡷࡣࡷࡻ࡮ࡴࠩ๤"), data, config)
    bstack11ll11lll1_opy_ = response.json()
    if bstack11ll11lll1_opy_[bstack1l111l1_opy_ (u"ࠪࡷࡺࡩࡣࡦࡵࡶࠫ๥")]:
      parsed = json.loads(os.getenv(bstack1l111l1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡠࡃࡆࡇࡊ࡙ࡓࡊࡄࡌࡐࡎ࡚࡙ࡠࡅࡒࡒࡋࡏࡇࡖࡔࡄࡘࡎࡕࡎࡠ࡛ࡐࡐࠬ๦"), bstack1l111l1_opy_ (u"ࠬࢁࡽࠨ๧")))
      parsed[bstack1l111l1_opy_ (u"࠭ࡳࡤࡣࡱࡲࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧ๨")] = bstack11ll11lll1_opy_[bstack1l111l1_opy_ (u"ࠧࡥࡣࡷࡥࠬ๩")][bstack1l111l1_opy_ (u"ࠨࡵࡦࡥࡳࡴࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩ๪")]
      os.environ[bstack1l111l1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡥࡁࡄࡅࡈࡗࡘࡏࡂࡊࡎࡌࡘ࡞ࡥࡃࡐࡐࡉࡍࡌ࡛ࡒࡂࡖࡌࡓࡓࡥ࡙ࡎࡎࠪ๫")] = json.dumps(parsed)
      bstack1lll1l1l1_opy_.bstack11ll1111l1_opy_(bstack11ll11lll1_opy_[bstack1l111l1_opy_ (u"ࠪࡨࡦࡺࡡࠨ๬")][bstack1l111l1_opy_ (u"ࠫࡸࡩࡲࡪࡲࡷࡷࠬ๭")])
      bstack1lll1l1l1_opy_.bstack11l1llllll_opy_(bstack11ll11lll1_opy_[bstack1l111l1_opy_ (u"ࠬࡪࡡࡵࡣࠪ๮")][bstack1l111l1_opy_ (u"࠭ࡣࡰ࡯ࡰࡥࡳࡪࡳࠨ๯")])
      bstack1lll1l1l1_opy_.store()
      return bstack11ll11lll1_opy_[bstack1l111l1_opy_ (u"ࠧࡥࡣࡷࡥࠬ๰")][bstack1l111l1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡕࡱ࡮ࡩࡳ࠭๱")], bstack11ll11lll1_opy_[bstack1l111l1_opy_ (u"ࠩࡧࡥࡹࡧࠧ๲")][bstack1l111l1_opy_ (u"ࠪ࡭ࡩ࠭๳")]
    else:
      logger.error(bstack1l111l1_opy_ (u"ࠫࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡸࡪ࡬ࡰࡪࠦࡲࡶࡰࡱ࡭ࡳ࡭ࠠࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰ࠽ࠤࠬ๴") + bstack11ll11lll1_opy_[bstack1l111l1_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭๵")])
      if bstack11ll11lll1_opy_[bstack1l111l1_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧ๶")] == bstack1l111l1_opy_ (u"ࠧࡊࡰࡹࡥࡱ࡯ࡤࠡࡥࡲࡲ࡫࡯ࡧࡶࡴࡤࡸ࡮ࡵ࡮ࠡࡲࡤࡷࡸ࡫ࡤ࠯ࠩ๷"):
        for bstack11l1lll1l1_opy_ in bstack11ll11lll1_opy_[bstack1l111l1_opy_ (u"ࠨࡧࡵࡶࡴࡸࡳࠨ๸")]:
          logger.error(bstack11l1lll1l1_opy_[bstack1l111l1_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪ๹")])
      return None, None
  except Exception as error:
    logger.error(bstack1l111l1_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡷࡩ࡫࡯ࡩࠥࡩࡲࡦࡣࡷ࡭ࡳ࡭ࠠࡵࡧࡶࡸࠥࡸࡵ࡯ࠢࡩࡳࡷࠦࡂࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯࠼ࠣࠦ๺") +  str(error))
    return None, None
def bstack1l1l1l111l_opy_():
  if os.getenv(bstack1l111l1_opy_ (u"ࠫࡇ࡙࡟ࡂ࠳࠴࡝ࡤࡐࡗࡕࠩ๻")) is None:
    return {
        bstack1l111l1_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬ๼"): bstack1l111l1_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬ๽"),
        bstack1l111l1_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨ๾"): bstack1l111l1_opy_ (u"ࠨࡄࡸ࡭ࡱࡪࠠࡤࡴࡨࡥࡹ࡯࡯࡯ࠢ࡫ࡥࡩࠦࡦࡢ࡫࡯ࡩࡩ࠴ࠧ๿")
    }
  data = {bstack1l111l1_opy_ (u"ࠩࡨࡲࡩ࡚ࡩ࡮ࡧࠪ຀"): bstack1lll11llll_opy_()}
  headers = {
      bstack1l111l1_opy_ (u"ࠪࡅࡺࡺࡨࡰࡴ࡬ࡾࡦࡺࡩࡰࡰࠪກ"): bstack1l111l1_opy_ (u"ࠫࡇ࡫ࡡࡳࡧࡵࠤࠬຂ") + os.getenv(bstack1l111l1_opy_ (u"ࠧࡈࡓࡠࡃ࠴࠵࡞ࡥࡊࡘࡖࠥ຃")),
      bstack1l111l1_opy_ (u"࠭ࡃࡰࡰࡷࡩࡳࡺ࠭ࡕࡻࡳࡩࠬຄ"): bstack1l111l1_opy_ (u"ࠧࡢࡲࡳࡰ࡮ࡩࡡࡵ࡫ࡲࡲ࠴ࡰࡳࡰࡰࠪ຅")
  }
  response = bstack1ll1llll1_opy_(bstack1l111l1_opy_ (u"ࠨࡒࡘࡘࠬຆ"), bstack11ll111lll_opy_ + bstack1l111l1_opy_ (u"ࠩ࠲ࡸࡪࡹࡴࡠࡴࡸࡲࡸ࠵ࡳࡵࡱࡳࠫງ"), data, { bstack1l111l1_opy_ (u"ࠪ࡬ࡪࡧࡤࡦࡴࡶࠫຈ"): headers })
  try:
    if response.status_code == 200:
      logger.info(bstack1l111l1_opy_ (u"ࠦࡇࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡕࡧࡶࡸࠥࡘࡵ࡯ࠢࡰࡥࡷࡱࡥࡥࠢࡤࡷࠥࡩ࡯࡮ࡲ࡯ࡩࡹ࡫ࡤࠡࡣࡷࠤࠧຉ") + datetime.utcnow().isoformat() + bstack1l111l1_opy_ (u"ࠬࡠࠧຊ"))
      return {bstack1l111l1_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭຋"): bstack1l111l1_opy_ (u"ࠧࡴࡷࡦࡧࡪࡹࡳࠨຌ"), bstack1l111l1_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩຍ"): bstack1l111l1_opy_ (u"ࠩࠪຎ")}
    else:
      response.raise_for_status()
  except requests.RequestException as error:
    logger.error(bstack1l111l1_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡷࡩ࡫࡯ࡩࠥࡳࡡࡳ࡭࡬ࡲ࡬ࠦࡣࡰ࡯ࡳࡰࡪࡺࡩࡰࡰࠣࡳ࡫ࠦࡂࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡗࡩࡸࡺࠠࡓࡷࡱ࠾ࠥࠨຏ") + str(error))
    return {
        bstack1l111l1_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫຐ"): bstack1l111l1_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫຑ"),
        bstack1l111l1_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧຒ"): str(error)
    }
def bstack1lllll1l11_opy_(caps, options):
  try:
    bstack11ll11l1l1_opy_ = caps.get(bstack1l111l1_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨຓ"), {}).get(bstack1l111l1_opy_ (u"ࠨࡦࡨࡺ࡮ࡩࡥࡏࡣࡰࡩࠬດ"), caps.get(bstack1l111l1_opy_ (u"ࠩࡧࡩࡻ࡯ࡣࡦࠩຕ"), bstack1l111l1_opy_ (u"ࠪࠫຖ")))
    if bstack11ll11l1l1_opy_:
      logger.warn(bstack1l111l1_opy_ (u"ࠦࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡹ࡬ࡰࡱࠦࡲࡶࡰࠣࡳࡳࡲࡹࠡࡱࡱࠤࡉ࡫ࡳ࡬ࡶࡲࡴࠥࡨࡲࡰࡹࡶࡩࡷࡹ࠮ࠣທ"))
      return False
    browser = caps.get(bstack1l111l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪຘ"), bstack1l111l1_opy_ (u"࠭ࠧນ")).lower()
    if browser != bstack1l111l1_opy_ (u"ࠧࡤࡪࡵࡳࡲ࡫ࠧບ"):
      logger.warn(bstack1l111l1_opy_ (u"ࠣࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡽࡩ࡭࡮ࠣࡶࡺࡴࠠࡰࡰ࡯ࡽࠥࡵ࡮ࠡࡅ࡫ࡶࡴࡳࡥࠡࡤࡵࡳࡼࡹࡥࡳࡵ࠱ࠦປ"))
      return False
    browser_version = caps.get(bstack1l111l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪຜ"), caps.get(bstack1l111l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬຝ")))
    if browser_version and browser_version != bstack1l111l1_opy_ (u"ࠫࡱࡧࡴࡦࡵࡷࠫພ") and int(browser_version.split(bstack1l111l1_opy_ (u"ࠬ࠴ࠧຟ"))[0]) <= 94:
      logger.warn(bstack1l111l1_opy_ (u"ࠨࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣࡻ࡮ࡲ࡬ࠡࡴࡸࡲࠥࡵ࡮࡭ࡻࠣࡳࡳࠦࡃࡩࡴࡲࡱࡪࠦࡢࡳࡱࡺࡷࡪࡸࠠࡷࡧࡵࡷ࡮ࡵ࡮ࠡࡩࡵࡩࡦࡺࡥࡳࠢࡷ࡬ࡦࡴࠠ࠺࠶࠱ࠦຠ"))
      return False
    if not options is None:
      bstack11ll1111ll_opy_ = options.to_capabilities().get(bstack1l111l1_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬມ"), {})
      if bstack1l111l1_opy_ (u"ࠨ࠯࠰࡬ࡪࡧࡤ࡭ࡧࡶࡷࠬຢ") in bstack11ll1111ll_opy_.get(bstack1l111l1_opy_ (u"ࠩࡤࡶ࡬ࡹࠧຣ"), []):
        logger.warn(bstack1l111l1_opy_ (u"ࠥࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡸ࡫࡯ࡰࠥࡴ࡯ࡵࠢࡵࡹࡳࠦ࡯࡯ࠢ࡯ࡩ࡬ࡧࡣࡺࠢ࡫ࡩࡦࡪ࡬ࡦࡵࡶࠤࡲࡵࡤࡦ࠰ࠣࡗࡼ࡯ࡴࡤࡪࠣࡸࡴࠦ࡮ࡦࡹࠣ࡬ࡪࡧࡤ࡭ࡧࡶࡷࠥࡳ࡯ࡥࡧࠣࡳࡷࠦࡡࡷࡱ࡬ࡨࠥࡻࡳࡪࡰࡪࠤ࡭࡫ࡡࡥ࡮ࡨࡷࡸࠦ࡭ࡰࡦࡨ࠲ࠧ຤"))
        return False
    return True
  except Exception as error:
    logger.debug(bstack1l111l1_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡺࡦࡲࡩࡥࡣࡷࡩࠥࡧ࠱࠲ࡻࠣࡷࡺࡶࡰࡰࡴࡷࠤ࠿ࠨລ") + str(error))
    return False
def set_capabilities(caps, config):
  try:
    bstack11ll11ll11_opy_ = config.get(bstack1l111l1_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡔࡶࡴࡪࡱࡱࡷࠬ຦"), {})
    bstack11ll11ll11_opy_[bstack1l111l1_opy_ (u"࠭ࡡࡶࡶ࡫ࡘࡴࡱࡥ࡯ࠩວ")] = os.getenv(bstack1l111l1_opy_ (u"ࠧࡃࡕࡢࡅ࠶࠷࡙ࡠࡌ࡚ࡘࠬຨ"))
    bstack11l1lllll1_opy_ = json.loads(os.getenv(bstack1l111l1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡤࡇࡃࡄࡇࡖࡗࡎࡈࡉࡍࡋࡗ࡝ࡤࡉࡏࡏࡈࡌࡋ࡚ࡘࡁࡕࡋࡒࡒࡤ࡟ࡍࡍࠩຩ"), bstack1l111l1_opy_ (u"ࠩࡾࢁࠬສ"))).get(bstack1l111l1_opy_ (u"ࠪࡷࡨࡧ࡮࡯ࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫຫ"))
    caps[bstack1l111l1_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫຬ")] = True
    if bstack1l111l1_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭ອ") in caps:
      caps[bstack1l111l1_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧຮ")][bstack1l111l1_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹࠧຯ")] = bstack11ll11ll11_opy_
      caps[bstack1l111l1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩະ")][bstack1l111l1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩັ")][bstack1l111l1_opy_ (u"ࠪࡷࡨࡧ࡮࡯ࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫາ")] = bstack11l1lllll1_opy_
    else:
      caps[bstack1l111l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪຳ")] = bstack11ll11ll11_opy_
      caps[bstack1l111l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫິ")][bstack1l111l1_opy_ (u"࠭ࡳࡤࡣࡱࡲࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧີ")] = bstack11l1lllll1_opy_
  except Exception as error:
    logger.debug(bstack1l111l1_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡻ࡭࡯࡬ࡦࠢࡶࡩࡹࡺࡩ࡯ࡩࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸ࠴ࠠࡆࡴࡵࡳࡷࡀࠠࠣຶ") +  str(error))
def bstack11111ll1_opy_(driver, bstack11ll111111_opy_):
  try:
    setattr(driver, bstack1l111l1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡂ࠳࠴ࡽࡘ࡮࡯ࡶ࡮ࡧࡗࡨࡧ࡮ࠨື"), True)
    session = driver.session_id
    if session:
      bstack11ll111l11_opy_ = True
      current_url = driver.current_url
      try:
        url = urlparse(current_url)
      except Exception as e:
        bstack11ll111l11_opy_ = False
      bstack11ll111l11_opy_ = url.scheme in [bstack1l111l1_opy_ (u"ࠤ࡫ࡸࡹࡶຸࠢ"), bstack1l111l1_opy_ (u"ࠥ࡬ࡹࡺࡰࡴࠤູ")]
      if bstack11ll111l11_opy_:
        if bstack11ll111111_opy_:
          logger.info(bstack1l111l1_opy_ (u"ࠦࡘ࡫ࡴࡶࡲࠣࡪࡴࡸࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡵࡧࡶࡸ࡮ࡴࡧࠡࡪࡤࡷࠥࡹࡴࡢࡴࡷࡩࡩ࠴ࠠࡂࡷࡷࡳࡲࡧࡴࡦࠢࡷࡩࡸࡺࠠࡤࡣࡶࡩࠥ࡫ࡸࡦࡥࡸࡸ࡮ࡵ࡮ࠡࡹ࡬ࡰࡱࠦࡢࡦࡩ࡬ࡲࠥࡳ࡯࡮ࡧࡱࡸࡦࡸࡩ࡭ࡻ࠱຺ࠦ"))
      return bstack11ll111111_opy_
  except Exception as e:
    logger.error(bstack1l111l1_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡸࡺࡡࡳࡶ࡬ࡲ࡬ࠦࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣࡷࡨࡧ࡮ࠡࡨࡲࡶࠥࡺࡨࡪࡵࠣࡸࡪࡹࡴࠡࡥࡤࡷࡪࡀࠠࠣົ") + str(e))
    return False
def bstack11l1l111l_opy_(driver, class_name, name, module_name, path, bstack1ll111ll1_opy_):
  try:
    bstack11lll111ll_opy_ = [class_name] if not class_name is None else []
    bstack11ll1l111l_opy_ = {
        bstack1l111l1_opy_ (u"ࠨࡳࡢࡸࡨࡖࡪࡹࡵ࡭ࡶࡶࠦຼ"): True,
        bstack1l111l1_opy_ (u"ࠢࡵࡧࡶࡸࡉ࡫ࡴࡢ࡫࡯ࡷࠧຽ"): {
            bstack1l111l1_opy_ (u"ࠣࡰࡤࡱࡪࠨ຾"): name,
            bstack1l111l1_opy_ (u"ࠤࡷࡩࡸࡺࡒࡶࡰࡌࡨࠧ຿"): os.environ.get(bstack1l111l1_opy_ (u"ࠪࡆࡘࡥࡁ࠲࠳࡜ࡣ࡙ࡋࡓࡕࡡࡕ࡙ࡓࡥࡉࡅࠩເ")),
            bstack1l111l1_opy_ (u"ࠦ࡫࡯࡬ࡦࡒࡤࡸ࡭ࠨແ"): str(path),
            bstack1l111l1_opy_ (u"ࠧࡹࡣࡰࡲࡨࡐ࡮ࡹࡴࠣໂ"): [module_name, *bstack11lll111ll_opy_, name],
        },
        bstack1l111l1_opy_ (u"ࠨࡰ࡭ࡣࡷࡪࡴࡸ࡭ࠣໃ"): _11ll1l11ll_opy_(driver, bstack1ll111ll1_opy_)
    }
    logger.debug(bstack1l111l1_opy_ (u"ࠧࡑࡧࡵࡪࡴࡸ࡭ࡪࡰࡪࠤࡸࡩࡡ࡯ࠢࡥࡩ࡫ࡵࡲࡦࠢࡶࡥࡻ࡯࡮ࡨࠢࡵࡩࡸࡻ࡬ࡵࡵࠪໄ"))
    logger.debug(driver.execute_async_script(bstack1lll1l1l1_opy_.perform_scan, {bstack1l111l1_opy_ (u"ࠣ࡯ࡨࡸ࡭ࡵࡤࠣ໅"): name}))
    logger.debug(driver.execute_async_script(bstack1lll1l1l1_opy_.bstack11l1llll1l_opy_, bstack11ll1l111l_opy_))
    logger.info(bstack1l111l1_opy_ (u"ࠤࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡷࡩࡸࡺࡩ࡯ࡩࠣࡪࡴࡸࠠࡵࡪ࡬ࡷࠥࡺࡥࡴࡶࠣࡧࡦࡹࡥࠡࡪࡤࡷࠥ࡫࡮ࡥࡧࡧ࠲ࠧໆ"))
  except Exception as bstack11l1lll111_opy_:
    logger.error(bstack1l111l1_opy_ (u"ࠥࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡶࡪࡹࡵ࡭ࡶࡶࠤࡨࡵࡵ࡭ࡦࠣࡲࡴࡺࠠࡣࡧࠣࡴࡷࡵࡣࡦࡵࡶࡩࡩࠦࡦࡰࡴࠣࡸ࡭࡫ࠠࡵࡧࡶࡸࠥࡩࡡࡴࡧ࠽ࠤࠧ໇") + str(path) + bstack1l111l1_opy_ (u"ࠦࠥࡋࡲࡳࡱࡵࠤ࠿ࠨ່") + str(bstack11l1lll111_opy_))