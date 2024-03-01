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
import datetime
import json
import logging
import os
import threading
from bstack_utils.helper import bstack11ll1l1111_opy_, bstack11111l11l_opy_, get_host_info, bstack11l1llll11_opy_, bstack11ll11l1ll_opy_, bstack11l11lll11_opy_, \
    bstack11l111111l_opy_, bstack11l11l1lll_opy_, bstack1ll1llll1_opy_, bstack11l111l11l_opy_, bstack1l1l1ll111_opy_, bstack1l1111lll1_opy_
from bstack_utils.bstack1lllll11lll_opy_ import bstack1lllll11l1l_opy_
from bstack_utils.bstack11llll1lll_opy_ import bstack1l111lllll_opy_
import bstack_utils.bstack1lll11l11l_opy_ as bstack1l1lll11l1_opy_
from bstack_utils.constants import bstack11l1l11lll_opy_
bstack1llll111l1l_opy_ = [
    bstack1l111l1_opy_ (u"ࠩࡏࡳ࡬ࡉࡲࡦࡣࡷࡩࡩ࠭ᓟ"), bstack1l111l1_opy_ (u"ࠪࡇࡇ࡚ࡓࡦࡵࡶ࡭ࡴࡴࡃࡳࡧࡤࡸࡪࡪࠧᓠ"), bstack1l111l1_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡋ࡯࡮ࡪࡵ࡫ࡩࡩ࠭ᓡ"), bstack1l111l1_opy_ (u"࡚ࠬࡥࡴࡶࡕࡹࡳ࡙࡫ࡪࡲࡳࡩࡩ࠭ᓢ"),
    bstack1l111l1_opy_ (u"࠭ࡈࡰࡱ࡮ࡖࡺࡴࡆࡪࡰ࡬ࡷ࡭࡫ࡤࠨᓣ"), bstack1l111l1_opy_ (u"ࠧࡕࡧࡶࡸࡗࡻ࡮ࡔࡶࡤࡶࡹ࡫ࡤࠨᓤ"), bstack1l111l1_opy_ (u"ࠨࡊࡲࡳࡰࡘࡵ࡯ࡕࡷࡥࡷࡺࡥࡥࠩᓥ")
]
bstack1lll1lll11l_opy_ = bstack1l111l1_opy_ (u"ࠩ࡫ࡸࡹࡶࡳ࠻࠱࠲ࡧࡴࡲ࡬ࡦࡥࡷࡳࡷ࠳࡯ࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮ࠩᓦ")
logger = logging.getLogger(__name__)
class bstack1l1111l1l_opy_:
    bstack1lllll11lll_opy_ = None
    bs_config = None
    @classmethod
    @bstack1l1111lll1_opy_(class_method=True)
    def launch(cls, bs_config, bstack1lll1lll1l1_opy_):
        cls.bs_config = bs_config
        cls.bstack1lll1ll1l1l_opy_()
        bstack11ll11l11l_opy_ = bstack11l1llll11_opy_(bs_config)
        bstack11ll11111l_opy_ = bstack11ll11l1ll_opy_(bs_config)
        bstack111111lll_opy_ = False
        bstack1ll1ll1111_opy_ = False
        if bstack1l111l1_opy_ (u"ࠪࡥࡵࡶࠧᓧ") in bs_config:
            bstack111111lll_opy_ = True
        else:
            bstack1ll1ll1111_opy_ = True
        bstack1l1l111ll_opy_ = {
            bstack1l111l1_opy_ (u"ࠫࡴࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࠫᓨ"): cls.bstack11l1llll1_opy_() and cls.bstack1lll1lll111_opy_(bstack1lll1lll1l1_opy_.get(bstack1l111l1_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡷࡶࡩࡩ࠭ᓩ"), bstack1l111l1_opy_ (u"࠭ࠧᓪ"))),
            bstack1l111l1_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧᓫ"): bstack1l1lll11l1_opy_.bstack1111l1ll_opy_(bs_config),
            bstack1l111l1_opy_ (u"ࠨࡲࡨࡶࡨࡿࠧᓬ"): bs_config.get(bstack1l111l1_opy_ (u"ࠩࡳࡩࡷࡩࡹࠨᓭ"), False),
            bstack1l111l1_opy_ (u"ࠪࡥࡺࡺ࡯࡮ࡣࡷࡩࠬᓮ"): bstack1ll1ll1111_opy_,
            bstack1l111l1_opy_ (u"ࠫࡦࡶࡰࡠࡣࡸࡸࡴࡳࡡࡵࡧࠪᓯ"): bstack111111lll_opy_
        }
        data = {
            bstack1l111l1_opy_ (u"ࠬ࡬࡯ࡳ࡯ࡤࡸࠬᓰ"): bstack1l111l1_opy_ (u"࠭ࡪࡴࡱࡱࠫᓱ"),
            bstack1l111l1_opy_ (u"ࠧࡱࡴࡲ࡮ࡪࡩࡴࡠࡰࡤࡱࡪ࠭ᓲ"): bs_config.get(bstack1l111l1_opy_ (u"ࠨࡲࡵࡳ࡯࡫ࡣࡵࡐࡤࡱࡪ࠭ᓳ"), bstack1l111l1_opy_ (u"ࠩࠪᓴ")),
            bstack1l111l1_opy_ (u"ࠪࡲࡦࡳࡥࠨᓵ"): bs_config.get(bstack1l111l1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧᓶ"), os.path.basename(os.path.abspath(os.getcwd()))),
            bstack1l111l1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡣ࡮ࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨᓷ"): bs_config.get(bstack1l111l1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨᓸ")),
            bstack1l111l1_opy_ (u"ࠧࡥࡧࡶࡧࡷ࡯ࡰࡵ࡫ࡲࡲࠬᓹ"): bs_config.get(bstack1l111l1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡄࡦࡵࡦࡶ࡮ࡶࡴࡪࡱࡱࠫᓺ"), bstack1l111l1_opy_ (u"ࠩࠪᓻ")),
            bstack1l111l1_opy_ (u"ࠪࡷࡹࡧࡲࡵࡡࡷ࡭ࡲ࡫ࠧᓼ"): datetime.datetime.now().isoformat(),
            bstack1l111l1_opy_ (u"ࠫࡹࡧࡧࡴࠩᓽ"): bstack11l11lll11_opy_(bs_config),
            bstack1l111l1_opy_ (u"ࠬ࡮࡯ࡴࡶࡢ࡭ࡳ࡬࡯ࠨᓾ"): get_host_info(),
            bstack1l111l1_opy_ (u"࠭ࡣࡪࡡ࡬ࡲ࡫ࡵࠧᓿ"): bstack11111l11l_opy_(),
            bstack1l111l1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡥࡲࡶࡰࡢ࡭ࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧᔀ"): os.environ.get(bstack1l111l1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡃࡗࡌࡐࡉࡥࡒࡖࡐࡢࡍࡉࡋࡎࡕࡋࡉࡍࡊࡘࠧᔁ")),
            bstack1l111l1_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࡡࡷࡩࡸࡺࡳࡠࡴࡨࡶࡺࡴࠧᔂ"): os.environ.get(bstack1l111l1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡕࡉࡗ࡛ࡎࠨᔃ"), False),
            bstack1l111l1_opy_ (u"ࠫࡻ࡫ࡲࡴ࡫ࡲࡲࡤࡩ࡯࡯ࡶࡵࡳࡱ࠭ᔄ"): bstack11ll1l1111_opy_(),
            bstack1l111l1_opy_ (u"ࠬࡶࡲࡰࡦࡸࡧࡹࡥ࡭ࡢࡲࠪᔅ"): bstack1l1l111ll_opy_,
            bstack1l111l1_opy_ (u"࠭࡯ࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾࡥࡶࡦࡴࡶ࡭ࡴࡴࠧᔆ"): {
                bstack1l111l1_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡑࡥࡲ࡫ࠧᔇ"): bstack1lll1lll1l1_opy_.get(bstack1l111l1_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡳࡧ࡭ࡦࠩᔈ"), bstack1l111l1_opy_ (u"ࠩࡓࡽࡹ࡫ࡳࡵࠩᔉ")),
                bstack1l111l1_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ᔊ"): bstack1lll1lll1l1_opy_.get(bstack1l111l1_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨᔋ")),
                bstack1l111l1_opy_ (u"ࠬࡹࡤ࡬ࡘࡨࡶࡸ࡯࡯࡯ࠩᔌ"): bstack1lll1lll1l1_opy_.get(bstack1l111l1_opy_ (u"࠭ࡳࡥ࡭ࡢࡺࡪࡸࡳࡪࡱࡱࠫᔍ"))
            }
        }
        config = {
            bstack1l111l1_opy_ (u"ࠧࡢࡷࡷ࡬ࠬᔎ"): (bstack11ll11l11l_opy_, bstack11ll11111l_opy_),
            bstack1l111l1_opy_ (u"ࠨࡪࡨࡥࡩ࡫ࡲࡴࠩᔏ"): cls.default_headers()
        }
        response = bstack1ll1llll1_opy_(bstack1l111l1_opy_ (u"ࠩࡓࡓࡘ࡚ࠧᔐ"), cls.request_url(bstack1l111l1_opy_ (u"ࠪࡥࡵ࡯࠯ࡷ࠳࠲ࡦࡺ࡯࡬ࡥࡵࠪᔑ")), data, config)
        if response.status_code != 200:
            os.environ[bstack1l111l1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩᔒ")] = bstack1l111l1_opy_ (u"ࠬࡴࡵ࡭࡮ࠪᔓ")
            os.environ[bstack1l111l1_opy_ (u"࠭ࡂࡔࡡࡗࡉࡘ࡚ࡏࡑࡕࡢࡆ࡚ࡏࡌࡅࡡࡆࡓࡒࡖࡌࡆࡖࡈࡈࠬᔔ")] = bstack1l111l1_opy_ (u"ࠧࡧࡣ࡯ࡷࡪ࠭ᔕ")
            os.environ[bstack1l111l1_opy_ (u"ࠨࡄࡖࡣ࡙ࡋࡓࡕࡑࡓࡗࡤࡐࡗࡕࠩᔖ")] = bstack1l111l1_opy_ (u"ࠩࡱࡹࡱࡲࠧᔗ")
            os.environ[bstack1l111l1_opy_ (u"ࠪࡆࡘࡥࡔࡆࡕࡗࡓࡕ࡙࡟ࡃࡗࡌࡐࡉࡥࡈࡂࡕࡋࡉࡉࡥࡉࡅࠩᔘ")] = bstack1l111l1_opy_ (u"ࠦࡳࡻ࡬࡭ࠤᔙ")
            os.environ[bstack1l111l1_opy_ (u"ࠬࡈࡓࡠࡖࡈࡗ࡙ࡕࡐࡔࡡࡄࡐࡑࡕࡗࡠࡕࡆࡖࡊࡋࡎࡔࡊࡒࡘࡘ࠭ᔚ")] = bstack1l111l1_opy_ (u"ࠨ࡮ࡶ࡮࡯ࠦᔛ")
            bstack1lll1llllll_opy_ = response.json()
            if bstack1lll1llllll_opy_ and bstack1lll1llllll_opy_[bstack1l111l1_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨᔜ")]:
                error_message = bstack1lll1llllll_opy_[bstack1l111l1_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩᔝ")]
                if bstack1lll1llllll_opy_[bstack1l111l1_opy_ (u"ࠩࡨࡶࡷࡵࡲࡕࡻࡳࡩࠬᔞ")] == bstack1l111l1_opy_ (u"ࠪࡉࡗࡘࡏࡓࡡࡌࡒ࡛ࡇࡌࡊࡆࡢࡇࡗࡋࡄࡆࡐࡗࡍࡆࡒࡓࠨᔟ"):
                    logger.error(error_message)
                elif bstack1lll1llllll_opy_[bstack1l111l1_opy_ (u"ࠫࡪࡸࡲࡰࡴࡗࡽࡵ࡫ࠧᔠ")] == bstack1l111l1_opy_ (u"ࠬࡋࡒࡓࡑࡕࡣࡆࡉࡃࡆࡕࡖࡣࡉࡋࡎࡊࡇࡇࠫᔡ"):
                    logger.info(error_message)
                elif bstack1lll1llllll_opy_[bstack1l111l1_opy_ (u"࠭ࡥࡳࡴࡲࡶ࡙ࡿࡰࡦࠩᔢ")] == bstack1l111l1_opy_ (u"ࠧࡆࡔࡕࡓࡗࡥࡓࡅࡍࡢࡈࡊࡖࡒࡆࡅࡄࡘࡊࡊࠧᔣ"):
                    logger.error(error_message)
                else:
                    logger.error(error_message)
            else:
                logger.error(bstack1l111l1_opy_ (u"ࠣࡆࡤࡸࡦࠦࡵࡱ࡮ࡲࡥࡩࠦࡴࡰࠢࡅࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࠡࡖࡨࡷࡹࠦࡏࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾࠦࡦࡢ࡫࡯ࡩࡩࠦࡤࡶࡧࠣࡸࡴࠦࡳࡰ࡯ࡨࠤࡪࡸࡲࡰࡴࠥᔤ"))
            return [None, None, None]
        bstack1lll1llllll_opy_ = response.json()
        os.environ[bstack1l111l1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧᔥ")] = bstack1lll1llllll_opy_[bstack1l111l1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡡ࡫ࡥࡸ࡮ࡥࡥࡡ࡬ࡨࠬᔦ")]
        if cls.bstack11l1llll1_opy_() is True and cls.bstack1lll1lll111_opy_(bstack1lll1lll1l1_opy_.get(bstack1l111l1_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡶࡵࡨࡨࠬᔧ"), bstack1l111l1_opy_ (u"ࠬ࠭ᔨ"))):
            logger.debug(bstack1l111l1_opy_ (u"࠭ࡔࡦࡵࡷࠤࡔࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࠤࡇࡻࡩ࡭ࡦࠣࡧࡷ࡫ࡡࡵ࡫ࡲࡲ࡙ࠥࡵࡤࡥࡨࡷࡸ࡬ࡵ࡭ࠣࠪᔩ"))
            os.environ[bstack1l111l1_opy_ (u"ࠧࡃࡕࡢࡘࡊ࡙ࡔࡐࡒࡖࡣࡇ࡛ࡉࡍࡆࡢࡇࡔࡓࡐࡍࡇࡗࡉࡉ࠭ᔪ")] = bstack1l111l1_opy_ (u"ࠨࡶࡵࡹࡪ࠭ᔫ")
            if bstack1lll1llllll_opy_.get(bstack1l111l1_opy_ (u"ࠩ࡭ࡻࡹ࠭ᔬ")):
                os.environ[bstack1l111l1_opy_ (u"ࠪࡆࡘࡥࡔࡆࡕࡗࡓࡕ࡙࡟ࡋ࡙ࡗࠫᔭ")] = bstack1lll1llllll_opy_[bstack1l111l1_opy_ (u"ࠫ࡯ࡽࡴࠨᔮ")]
                os.environ[bstack1l111l1_opy_ (u"ࠬࡉࡒࡆࡆࡈࡒ࡙ࡏࡁࡍࡕࡢࡊࡔࡘ࡟ࡄࡔࡄࡗࡍࡥࡒࡆࡒࡒࡖ࡙ࡏࡎࡈࠩᔯ")] = json.dumps({
                    bstack1l111l1_opy_ (u"࠭ࡵࡴࡧࡵࡲࡦࡳࡥࠨᔰ"): bstack11ll11l11l_opy_,
                    bstack1l111l1_opy_ (u"ࠧࡱࡣࡶࡷࡼࡵࡲࡥࠩᔱ"): bstack11ll11111l_opy_
                })
            if bstack1lll1llllll_opy_.get(bstack1l111l1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪ࡟ࡩࡣࡶ࡬ࡪࡪ࡟ࡪࡦࠪᔲ")):
                os.environ[bstack1l111l1_opy_ (u"ࠩࡅࡗࡤ࡚ࡅࡔࡖࡒࡔࡘࡥࡂࡖࡋࡏࡈࡤࡎࡁࡔࡊࡈࡈࡤࡏࡄࠨᔳ")] = bstack1lll1llllll_opy_[bstack1l111l1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡡ࡫ࡥࡸ࡮ࡥࡥࡡ࡬ࡨࠬᔴ")]
            if bstack1lll1llllll_opy_.get(bstack1l111l1_opy_ (u"ࠫࡦࡲ࡬ࡰࡹࡢࡷࡨࡸࡥࡦࡰࡶ࡬ࡴࡺࡳࠨᔵ")):
                os.environ[bstack1l111l1_opy_ (u"ࠬࡈࡓࡠࡖࡈࡗ࡙ࡕࡐࡔࡡࡄࡐࡑࡕࡗࡠࡕࡆࡖࡊࡋࡎࡔࡊࡒࡘࡘ࠭ᔶ")] = str(bstack1lll1llllll_opy_[bstack1l111l1_opy_ (u"࠭ࡡ࡭࡮ࡲࡻࡤࡹࡣࡳࡧࡨࡲࡸ࡮࡯ࡵࡵࠪᔷ")])
        return [bstack1lll1llllll_opy_[bstack1l111l1_opy_ (u"ࠧ࡫ࡹࡷࠫᔸ")], bstack1lll1llllll_opy_[bstack1l111l1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪ࡟ࡩࡣࡶ࡬ࡪࡪ࡟ࡪࡦࠪᔹ")], bstack1lll1llllll_opy_[bstack1l111l1_opy_ (u"ࠩࡤࡰࡱࡵࡷࡠࡵࡦࡶࡪ࡫࡮ࡴࡪࡲࡸࡸ࠭ᔺ")]]
    @classmethod
    @bstack1l1111lll1_opy_(class_method=True)
    def stop(cls):
        if not cls.on():
            return
        if os.environ[bstack1l111l1_opy_ (u"ࠪࡆࡘࡥࡔࡆࡕࡗࡓࡕ࡙࡟ࡋ࡙ࡗࠫᔻ")] == bstack1l111l1_opy_ (u"ࠦࡳࡻ࡬࡭ࠤᔼ") or os.environ[bstack1l111l1_opy_ (u"ࠬࡈࡓࡠࡖࡈࡗ࡙ࡕࡐࡔࡡࡅ࡙ࡎࡒࡄࡠࡊࡄࡗࡍࡋࡄࡠࡋࡇࠫᔽ")] == bstack1l111l1_opy_ (u"ࠨ࡮ࡶ࡮࡯ࠦᔾ"):
            print(bstack1l111l1_opy_ (u"ࠧࡆ࡚ࡆࡉࡕ࡚ࡉࡐࡐࠣࡍࡓࠦࡳࡵࡱࡳࡆࡺ࡯࡬ࡥࡗࡳࡷࡹࡸࡥࡢ࡯ࠣࡖࡊࡗࡕࡆࡕࡗࠤ࡙ࡕࠠࡕࡇࡖࡘࠥࡕࡂࡔࡇࡕ࡚ࡆࡈࡉࡍࡋࡗ࡝ࠥࡀࠠࡎ࡫ࡶࡷ࡮ࡴࡧࠡࡣࡸࡸ࡭࡫࡮ࡵ࡫ࡦࡥࡹ࡯࡯࡯ࠢࡷࡳࡰ࡫࡮ࠨᔿ"))
            return {
                bstack1l111l1_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨᕀ"): bstack1l111l1_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨᕁ"),
                bstack1l111l1_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫᕂ"): bstack1l111l1_opy_ (u"࡙ࠫࡵ࡫ࡦࡰ࠲ࡦࡺ࡯࡬ࡥࡋࡇࠤ࡮ࡹࠠࡶࡰࡧࡩ࡫࡯࡮ࡦࡦ࠯ࠤࡧࡻࡩ࡭ࡦࠣࡧࡷ࡫ࡡࡵ࡫ࡲࡲࠥࡳࡩࡨࡪࡷࠤ࡭ࡧࡶࡦࠢࡩࡥ࡮ࡲࡥࡥࠩᕃ")
            }
        else:
            cls.bstack1lllll11lll_opy_.shutdown()
            data = {
                bstack1l111l1_opy_ (u"ࠬࡹࡴࡰࡲࡢࡸ࡮ࡳࡥࠨᕄ"): datetime.datetime.now().isoformat()
            }
            config = {
                bstack1l111l1_opy_ (u"࠭ࡨࡦࡣࡧࡩࡷࡹࠧᕅ"): cls.default_headers()
            }
            bstack111lll1l11_opy_ = bstack1l111l1_opy_ (u"ࠧࡢࡲ࡬࠳ࡻ࠷࠯ࡣࡷ࡬ࡰࡩࡹ࠯ࡼࡿ࠲ࡷࡹࡵࡰࠨᕆ").format(os.environ[bstack1l111l1_opy_ (u"ࠣࡄࡖࡣ࡙ࡋࡓࡕࡑࡓࡗࡤࡈࡕࡊࡎࡇࡣࡍࡇࡓࡉࡇࡇࡣࡎࡊࠢᕇ")])
            bstack1llll111lll_opy_ = cls.request_url(bstack111lll1l11_opy_)
            response = bstack1ll1llll1_opy_(bstack1l111l1_opy_ (u"ࠩࡓ࡙࡙࠭ᕈ"), bstack1llll111lll_opy_, data, config)
            if not response.ok:
                raise Exception(bstack1l111l1_opy_ (u"ࠥࡗࡹࡵࡰࠡࡴࡨࡵࡺ࡫ࡳࡵࠢࡱࡳࡹࠦ࡯࡬ࠤᕉ"))
    @classmethod
    def bstack1l1111l11l_opy_(cls):
        if cls.bstack1lllll11lll_opy_ is None:
            return
        cls.bstack1lllll11lll_opy_.shutdown()
    @classmethod
    def bstack11111l1ll_opy_(cls):
        if cls.on():
            print(
                bstack1l111l1_opy_ (u"࡛ࠫ࡯ࡳࡪࡶࠣ࡬ࡹࡺࡰࡴ࠼࠲࠳ࡴࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳ࠯ࡣࡷ࡬ࡰࡩࡹ࠯ࡼࡿࠣࡸࡴࠦࡶࡪࡧࡺࠤࡧࡻࡩ࡭ࡦࠣࡶࡪࡶ࡯ࡳࡶ࠯ࠤ࡮ࡴࡳࡪࡩ࡫ࡸࡸ࠲ࠠࡢࡰࡧࠤࡲࡧ࡮ࡺࠢࡰࡳࡷ࡫ࠠࡥࡧࡥࡹ࡬࡭ࡩ࡯ࡩࠣ࡭ࡳ࡬࡯ࡳ࡯ࡤࡸ࡮ࡵ࡮ࠡࡣ࡯ࡰࠥࡧࡴࠡࡱࡱࡩࠥࡶ࡬ࡢࡥࡨࠥࡡࡴࠧᕊ").format(os.environ[bstack1l111l1_opy_ (u"ࠧࡈࡓࡠࡖࡈࡗ࡙ࡕࡐࡔࡡࡅ࡙ࡎࡒࡄࡠࡊࡄࡗࡍࡋࡄࡠࡋࡇࠦᕋ")]))
    @classmethod
    def bstack1lll1ll1l1l_opy_(cls):
        if cls.bstack1lllll11lll_opy_ is not None:
            return
        cls.bstack1lllll11lll_opy_ = bstack1lllll11l1l_opy_(cls.bstack1llll111l11_opy_)
        cls.bstack1lllll11lll_opy_.start()
    @classmethod
    def bstack11llll1l1l_opy_(cls, bstack11llll11ll_opy_, bstack1lll1lllll1_opy_=bstack1l111l1_opy_ (u"࠭ࡡࡱ࡫࠲ࡺ࠶࠵ࡢࡢࡶࡦ࡬ࠬᕌ")):
        if not cls.on():
            return
        bstack1lll1ll1l1_opy_ = bstack11llll11ll_opy_[bstack1l111l1_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡴࡺࡲࡨࠫᕍ")]
        bstack1lll1lll1ll_opy_ = {
            bstack1l111l1_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡕࡷࡥࡷࡺࡥࡥࠩᕎ"): bstack1l111l1_opy_ (u"ࠩࡗࡩࡸࡺ࡟ࡔࡶࡤࡶࡹࡥࡕࡱ࡮ࡲࡥࡩ࠭ᕏ"),
            bstack1l111l1_opy_ (u"ࠪࡘࡪࡹࡴࡓࡷࡱࡊ࡮ࡴࡩࡴࡪࡨࡨࠬᕐ"): bstack1l111l1_opy_ (u"࡙ࠫ࡫ࡳࡵࡡࡈࡲࡩࡥࡕࡱ࡮ࡲࡥࡩ࠭ᕑ"),
            bstack1l111l1_opy_ (u"࡚ࠬࡥࡴࡶࡕࡹࡳ࡙࡫ࡪࡲࡳࡩࡩ࠭ᕒ"): bstack1l111l1_opy_ (u"࠭ࡔࡦࡵࡷࡣࡘࡱࡩࡱࡲࡨࡨࡤ࡛ࡰ࡭ࡱࡤࡨࠬᕓ"),
            bstack1l111l1_opy_ (u"ࠧࡍࡱࡪࡇࡷ࡫ࡡࡵࡧࡧࠫᕔ"): bstack1l111l1_opy_ (u"ࠨࡎࡲ࡫ࡤ࡛ࡰ࡭ࡱࡤࡨࠬᕕ"),
            bstack1l111l1_opy_ (u"ࠩࡋࡳࡴࡱࡒࡶࡰࡖࡸࡦࡸࡴࡦࡦࠪᕖ"): bstack1l111l1_opy_ (u"ࠪࡌࡴࡵ࡫ࡠࡕࡷࡥࡷࡺ࡟ࡖࡲ࡯ࡳࡦࡪࠧᕗ"),
            bstack1l111l1_opy_ (u"ࠫࡍࡵ࡯࡬ࡔࡸࡲࡋ࡯࡮ࡪࡵ࡫ࡩࡩ࠭ᕘ"): bstack1l111l1_opy_ (u"ࠬࡎ࡯ࡰ࡭ࡢࡉࡳࡪ࡟ࡖࡲ࡯ࡳࡦࡪࠧᕙ"),
            bstack1l111l1_opy_ (u"࠭ࡃࡃࡖࡖࡩࡸࡹࡩࡰࡰࡆࡶࡪࡧࡴࡦࡦࠪᕚ"): bstack1l111l1_opy_ (u"ࠧࡄࡄࡗࡣ࡚ࡶ࡬ࡰࡣࡧࠫᕛ")
        }.get(bstack1lll1ll1l1_opy_)
        if bstack1lll1lllll1_opy_ == bstack1l111l1_opy_ (u"ࠨࡣࡳ࡭࠴ࡼ࠱࠰ࡤࡤࡸࡨ࡮ࠧᕜ"):
            cls.bstack1lll1ll1l1l_opy_()
            cls.bstack1lllll11lll_opy_.add(bstack11llll11ll_opy_)
        elif bstack1lll1lllll1_opy_ == bstack1l111l1_opy_ (u"ࠩࡤࡴ࡮࠵ࡶ࠲࠱ࡶࡧࡷ࡫ࡥ࡯ࡵ࡫ࡳࡹࡹࠧᕝ"):
            cls.bstack1llll111l11_opy_([bstack11llll11ll_opy_], bstack1lll1lllll1_opy_)
    @classmethod
    @bstack1l1111lll1_opy_(class_method=True)
    def bstack1llll111l11_opy_(cls, bstack11llll11ll_opy_, bstack1lll1lllll1_opy_=bstack1l111l1_opy_ (u"ࠪࡥࡵ࡯࠯ࡷ࠳࠲ࡦࡦࡺࡣࡩࠩᕞ")):
        config = {
            bstack1l111l1_opy_ (u"ࠫ࡭࡫ࡡࡥࡧࡵࡷࠬᕟ"): cls.default_headers()
        }
        response = bstack1ll1llll1_opy_(bstack1l111l1_opy_ (u"ࠬࡖࡏࡔࡖࠪᕠ"), cls.request_url(bstack1lll1lllll1_opy_), bstack11llll11ll_opy_, config)
        bstack11ll11lll1_opy_ = response.json()
    @classmethod
    @bstack1l1111lll1_opy_(class_method=True)
    def bstack1lll1ll111_opy_(cls, bstack11llll1111_opy_):
        bstack1llll11l111_opy_ = []
        for log in bstack11llll1111_opy_:
            bstack1llll1111ll_opy_ = {
                bstack1l111l1_opy_ (u"࠭࡫ࡪࡰࡧࠫᕡ"): bstack1l111l1_opy_ (u"ࠧࡕࡇࡖࡘࡤࡒࡏࡈࠩᕢ"),
                bstack1l111l1_opy_ (u"ࠨ࡮ࡨࡺࡪࡲࠧᕣ"): log[bstack1l111l1_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨᕤ")],
                bstack1l111l1_opy_ (u"ࠪࡸ࡮ࡳࡥࡴࡶࡤࡱࡵ࠭ᕥ"): log[bstack1l111l1_opy_ (u"ࠫࡹ࡯࡭ࡦࡵࡷࡥࡲࡶࠧᕦ")],
                bstack1l111l1_opy_ (u"ࠬ࡮ࡴࡵࡲࡢࡶࡪࡹࡰࡰࡰࡶࡩࠬᕧ"): {},
                bstack1l111l1_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧᕨ"): log[bstack1l111l1_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨᕩ")],
            }
            if bstack1l111l1_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨᕪ") in log:
                bstack1llll1111ll_opy_[bstack1l111l1_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩᕫ")] = log[bstack1l111l1_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪᕬ")]
            elif bstack1l111l1_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫᕭ") in log:
                bstack1llll1111ll_opy_[bstack1l111l1_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬᕮ")] = log[bstack1l111l1_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ᕯ")]
            bstack1llll11l111_opy_.append(bstack1llll1111ll_opy_)
        cls.bstack11llll1l1l_opy_({
            bstack1l111l1_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡴࡺࡲࡨࠫᕰ"): bstack1l111l1_opy_ (u"ࠨࡎࡲ࡫ࡈࡸࡥࡢࡶࡨࡨࠬᕱ"),
            bstack1l111l1_opy_ (u"ࠩ࡯ࡳ࡬ࡹࠧᕲ"): bstack1llll11l111_opy_
        })
    @classmethod
    @bstack1l1111lll1_opy_(class_method=True)
    def bstack1lll1ll1lll_opy_(cls, steps):
        bstack1llll11111l_opy_ = []
        for step in steps:
            bstack1llll111ll1_opy_ = {
                bstack1l111l1_opy_ (u"ࠪ࡯࡮ࡴࡤࠨᕳ"): bstack1l111l1_opy_ (u"࡙ࠫࡋࡓࡕࡡࡖࡘࡊࡖࠧᕴ"),
                bstack1l111l1_opy_ (u"ࠬࡲࡥࡷࡧ࡯ࠫᕵ"): step[bstack1l111l1_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬᕶ")],
                bstack1l111l1_opy_ (u"ࠧࡵ࡫ࡰࡩࡸࡺࡡ࡮ࡲࠪᕷ"): step[bstack1l111l1_opy_ (u"ࠨࡶ࡬ࡱࡪࡹࡴࡢ࡯ࡳࠫᕸ")],
                bstack1l111l1_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪᕹ"): step[bstack1l111l1_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫᕺ")],
                bstack1l111l1_opy_ (u"ࠫࡩࡻࡲࡢࡶ࡬ࡳࡳ࠭ᕻ"): step[bstack1l111l1_opy_ (u"ࠬࡪࡵࡳࡣࡷ࡭ࡴࡴࠧᕼ")]
            }
            if bstack1l111l1_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ᕽ") in step:
                bstack1llll111ll1_opy_[bstack1l111l1_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧᕾ")] = step[bstack1l111l1_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨᕿ")]
            elif bstack1l111l1_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩᖀ") in step:
                bstack1llll111ll1_opy_[bstack1l111l1_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪᖁ")] = step[bstack1l111l1_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫᖂ")]
            bstack1llll11111l_opy_.append(bstack1llll111ll1_opy_)
        cls.bstack11llll1l1l_opy_({
            bstack1l111l1_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦࠩᖃ"): bstack1l111l1_opy_ (u"࠭ࡌࡰࡩࡆࡶࡪࡧࡴࡦࡦࠪᖄ"),
            bstack1l111l1_opy_ (u"ࠧ࡭ࡱࡪࡷࠬᖅ"): bstack1llll11111l_opy_
        })
    @classmethod
    @bstack1l1111lll1_opy_(class_method=True)
    def bstack1ll1l1l1l1_opy_(cls, screenshot):
        cls.bstack11llll1l1l_opy_({
            bstack1l111l1_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡵࡻࡳࡩࠬᖆ"): bstack1l111l1_opy_ (u"ࠩࡏࡳ࡬ࡉࡲࡦࡣࡷࡩࡩ࠭ᖇ"),
            bstack1l111l1_opy_ (u"ࠪࡰࡴ࡭ࡳࠨᖈ"): [{
                bstack1l111l1_opy_ (u"ࠫࡰ࡯࡮ࡥࠩᖉ"): bstack1l111l1_opy_ (u"࡚ࠬࡅࡔࡖࡢࡗࡈࡘࡅࡆࡐࡖࡌࡔ࡚ࠧᖊ"),
                bstack1l111l1_opy_ (u"࠭ࡴࡪ࡯ࡨࡷࡹࡧ࡭ࡱࠩᖋ"): datetime.datetime.utcnow().isoformat() + bstack1l111l1_opy_ (u"࡛ࠧࠩᖌ"),
                bstack1l111l1_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩᖍ"): screenshot[bstack1l111l1_opy_ (u"ࠩ࡬ࡱࡦ࡭ࡥࠨᖎ")],
                bstack1l111l1_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪᖏ"): screenshot[bstack1l111l1_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫᖐ")]
            }]
        }, bstack1lll1lllll1_opy_=bstack1l111l1_opy_ (u"ࠬࡧࡰࡪ࠱ࡹ࠵࠴ࡹࡣࡳࡧࡨࡲࡸ࡮࡯ࡵࡵࠪᖑ"))
    @classmethod
    @bstack1l1111lll1_opy_(class_method=True)
    def bstack11lll111l_opy_(cls, driver):
        current_test_uuid = cls.current_test_uuid()
        if not current_test_uuid:
            return
        cls.bstack11llll1l1l_opy_({
            bstack1l111l1_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡺࡹࡱࡧࠪᖒ"): bstack1l111l1_opy_ (u"ࠧࡄࡄࡗࡗࡪࡹࡳࡪࡱࡱࡇࡷ࡫ࡡࡵࡧࡧࠫᖓ"),
            bstack1l111l1_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࠪᖔ"): {
                bstack1l111l1_opy_ (u"ࠤࡸࡹ࡮ࡪࠢᖕ"): cls.current_test_uuid(),
                bstack1l111l1_opy_ (u"ࠥ࡭ࡳࡺࡥࡨࡴࡤࡸ࡮ࡵ࡮ࡴࠤᖖ"): cls.bstack1l111lll1l_opy_(driver)
            }
        })
    @classmethod
    def on(cls):
        if os.environ.get(bstack1l111l1_opy_ (u"ࠫࡇ࡙࡟ࡕࡇࡖࡘࡔࡖࡓࡠࡌ࡚ࡘࠬᖗ"), None) is None or os.environ[bstack1l111l1_opy_ (u"ࠬࡈࡓࡠࡖࡈࡗ࡙ࡕࡐࡔࡡࡍ࡛࡙࠭ᖘ")] == bstack1l111l1_opy_ (u"ࠨ࡮ࡶ࡮࡯ࠦᖙ"):
            return False
        return True
    @classmethod
    def bstack11l1llll1_opy_(cls):
        return bstack1l1l1ll111_opy_(cls.bs_config.get(bstack1l111l1_opy_ (u"ࠧࡵࡧࡶࡸࡔࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࠫᖚ"), False))
    @classmethod
    def bstack1lll1lll111_opy_(cls, framework):
        return framework in bstack11l1l11lll_opy_
    @staticmethod
    def request_url(url):
        return bstack1l111l1_opy_ (u"ࠨࡽࢀ࠳ࢀࢃࠧᖛ").format(bstack1lll1lll11l_opy_, url)
    @staticmethod
    def default_headers():
        headers = {
            bstack1l111l1_opy_ (u"ࠩࡆࡳࡳࡺࡥ࡯ࡶ࠰ࡘࡾࡶࡥࠨᖜ"): bstack1l111l1_opy_ (u"ࠪࡥࡵࡶ࡬ࡪࡥࡤࡸ࡮ࡵ࡮࠰࡬ࡶࡳࡳ࠭ᖝ"),
            bstack1l111l1_opy_ (u"ࠫ࡝࠳ࡂࡔࡖࡄࡇࡐ࠳ࡔࡆࡕࡗࡓࡕ࡙ࠧᖞ"): bstack1l111l1_opy_ (u"ࠬࡺࡲࡶࡧࠪᖟ")
        }
        if os.environ.get(bstack1l111l1_opy_ (u"࠭ࡂࡔࡡࡗࡉࡘ࡚ࡏࡑࡕࡢࡎ࡜࡚ࠧᖠ"), None):
            headers[bstack1l111l1_opy_ (u"ࠧࡂࡷࡷ࡬ࡴࡸࡩࡻࡣࡷ࡭ࡴࡴࠧᖡ")] = bstack1l111l1_opy_ (u"ࠨࡄࡨࡥࡷ࡫ࡲࠡࡽࢀࠫᖢ").format(os.environ[bstack1l111l1_opy_ (u"ࠤࡅࡗࡤ࡚ࡅࡔࡖࡒࡔࡘࡥࡊࡘࡖࠥᖣ")])
        return headers
    @staticmethod
    def current_test_uuid():
        return getattr(threading.current_thread(), bstack1l111l1_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡࡸࡹ࡮ࡪࠧᖤ"), None)
    @staticmethod
    def current_hook_uuid():
        return getattr(threading.current_thread(), bstack1l111l1_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤ࡮࡯ࡰ࡭ࡢࡹࡺ࡯ࡤࠨᖥ"), None)
    @staticmethod
    def bstack11llllll1l_opy_():
        if getattr(threading.current_thread(), bstack1l111l1_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣࡺࡻࡩࡥࠩᖦ"), None):
            return {
                bstack1l111l1_opy_ (u"࠭ࡴࡺࡲࡨࠫᖧ"): bstack1l111l1_opy_ (u"ࠧࡵࡧࡶࡸࠬᖨ"),
                bstack1l111l1_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨᖩ"): getattr(threading.current_thread(), bstack1l111l1_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡸࡪࡹࡴࡠࡷࡸ࡭ࡩ࠭ᖪ"), None)
            }
        if getattr(threading.current_thread(), bstack1l111l1_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣ࡭ࡵ࡯࡬ࡡࡸࡹ࡮ࡪࠧᖫ"), None):
            return {
                bstack1l111l1_opy_ (u"ࠫࡹࡿࡰࡦࠩᖬ"): bstack1l111l1_opy_ (u"ࠬ࡮࡯ࡰ࡭ࠪᖭ"),
                bstack1l111l1_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ᖮ"): getattr(threading.current_thread(), bstack1l111l1_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡪࡲࡳࡰࡥࡵࡶ࡫ࡧࠫᖯ"), None)
            }
        return None
    @staticmethod
    def bstack1l111lll1l_opy_(driver):
        return {
            bstack11l11l1lll_opy_(): bstack11l111111l_opy_(driver)
        }
    @staticmethod
    def bstack1llll111111_opy_(exception_info, report):
        return [{bstack1l111l1_opy_ (u"ࠨࡤࡤࡧࡰࡺࡲࡢࡥࡨࠫᖰ"): [exception_info.exconly(), report.longreprtext]}]
    @staticmethod
    def bstack11ll1l1l11_opy_(typename):
        if bstack1l111l1_opy_ (u"ࠤࡄࡷࡸ࡫ࡲࡵ࡫ࡲࡲࠧᖱ") in typename:
            return bstack1l111l1_opy_ (u"ࠥࡅࡸࡹࡥࡳࡶ࡬ࡳࡳࡋࡲࡳࡱࡵࠦᖲ")
        return bstack1l111l1_opy_ (u"࡚ࠦࡴࡨࡢࡰࡧࡰࡪࡪࡅࡳࡴࡲࡶࠧᖳ")
    @staticmethod
    def bstack1llll1111l1_opy_(func):
        def wrap(*args, **kwargs):
            if bstack1l1111l1l_opy_.on():
                return func(*args, **kwargs)
            return
        return wrap
    @staticmethod
    def bstack11lll1l111_opy_(test, hook_name=None):
        bstack1lll1llll1l_opy_ = test.parent
        if hook_name in [bstack1l111l1_opy_ (u"ࠬࡹࡥࡵࡷࡳࡣࡨࡲࡡࡴࡵࠪᖴ"), bstack1l111l1_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࡠࡥ࡯ࡥࡸࡹࠧᖵ"), bstack1l111l1_opy_ (u"ࠧࡴࡧࡷࡹࡵࡥ࡭ࡰࡦࡸࡰࡪ࠭ᖶ"), bstack1l111l1_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡱࡴࡪࡵ࡭ࡧࠪᖷ")]:
            bstack1lll1llll1l_opy_ = test
        scope = []
        while bstack1lll1llll1l_opy_ is not None:
            scope.append(bstack1lll1llll1l_opy_.name)
            bstack1lll1llll1l_opy_ = bstack1lll1llll1l_opy_.parent
        scope.reverse()
        return scope[2:]
    @staticmethod
    def bstack1lll1llll11_opy_(hook_type):
        if hook_type == bstack1l111l1_opy_ (u"ࠤࡅࡉࡋࡕࡒࡆࡡࡈࡅࡈࡎࠢᖸ"):
            return bstack1l111l1_opy_ (u"ࠥࡗࡪࡺࡵࡱࠢ࡫ࡳࡴࡱࠢᖹ")
        elif hook_type == bstack1l111l1_opy_ (u"ࠦࡆࡌࡔࡆࡔࡢࡉࡆࡉࡈࠣᖺ"):
            return bstack1l111l1_opy_ (u"࡚ࠧࡥࡢࡴࡧࡳࡼࡴࠠࡩࡱࡲ࡯ࠧᖻ")
    @staticmethod
    def bstack1lll1ll1ll1_opy_(bstack1l1111111_opy_):
        try:
            if not bstack1l1111l1l_opy_.on():
                return bstack1l1111111_opy_
            if os.environ.get(bstack1l111l1_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡘࡅࡓࡗࡑࠦᖼ"), None) == bstack1l111l1_opy_ (u"ࠢࡵࡴࡸࡩࠧᖽ"):
                tests = os.environ.get(bstack1l111l1_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡓࡇࡕ࡙ࡓࡥࡔࡆࡕࡗࡗࠧᖾ"), None)
                if tests is None or tests == bstack1l111l1_opy_ (u"ࠤࡱࡹࡱࡲࠢᖿ"):
                    return bstack1l1111111_opy_
                bstack1l1111111_opy_ = tests.split(bstack1l111l1_opy_ (u"ࠪ࠰ࠬᗀ"))
                return bstack1l1111111_opy_
        except Exception as exc:
            print(bstack1l111l1_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡶࡪࡸࡵ࡯ࠢ࡫ࡥࡳࡪ࡬ࡦࡴ࠽ࠤࠧᗁ"), str(exc))
        return bstack1l1111111_opy_
    @classmethod
    def bstack1l1111l111_opy_(cls, event: str, bstack11llll11ll_opy_: bstack1l111lllll_opy_):
        bstack1l1111ll11_opy_ = {
            bstack1l111l1_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦࠩᗂ"): event,
            bstack11llll11ll_opy_.bstack11llllll11_opy_(): bstack11llll11ll_opy_.bstack11llll11l1_opy_(event)
        }
        bstack1l1111l1l_opy_.bstack11llll1l1l_opy_(bstack1l1111ll11_opy_)