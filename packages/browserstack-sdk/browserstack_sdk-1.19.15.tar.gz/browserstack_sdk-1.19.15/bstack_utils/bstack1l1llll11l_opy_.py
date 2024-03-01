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
import json
import os
import threading
from bstack_utils.config import Config
from bstack_utils.helper import bstack111lllll11_opy_, bstack11ll1ll1l_opy_, bstack1ll1ll1l1_opy_, bstack11l1l1l1l_opy_, \
    bstack11l11ll1ll_opy_
def bstack1l1lll111l_opy_(bstack1llll1llll1_opy_):
    for driver in bstack1llll1llll1_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
def bstack11l11111l_opy_(driver, status, reason=bstack1l111l1_opy_ (u"ࠧࠨᑭ")):
    bstack11111111_opy_ = Config.bstack1ll1l11ll_opy_()
    if bstack11111111_opy_.bstack11lll11ll1_opy_():
        return
    bstack1ll111l1l_opy_ = bstack1ll11111l1_opy_(bstack1l111l1_opy_ (u"ࠨࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡘࡺࡡࡵࡷࡶࠫᑮ"), bstack1l111l1_opy_ (u"ࠩࠪᑯ"), status, reason, bstack1l111l1_opy_ (u"ࠪࠫᑰ"), bstack1l111l1_opy_ (u"ࠫࠬᑱ"))
    driver.execute_script(bstack1ll111l1l_opy_)
def bstack1111l1lll_opy_(page, status, reason=bstack1l111l1_opy_ (u"ࠬ࠭ᑲ")):
    try:
        if page is None:
            return
        bstack11111111_opy_ = Config.bstack1ll1l11ll_opy_()
        if bstack11111111_opy_.bstack11lll11ll1_opy_():
            return
        bstack1ll111l1l_opy_ = bstack1ll11111l1_opy_(bstack1l111l1_opy_ (u"࠭ࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡖࡸࡦࡺࡵࡴࠩᑳ"), bstack1l111l1_opy_ (u"ࠧࠨᑴ"), status, reason, bstack1l111l1_opy_ (u"ࠨࠩᑵ"), bstack1l111l1_opy_ (u"ࠩࠪᑶ"))
        page.evaluate(bstack1l111l1_opy_ (u"ࠥࡣࠥࡃ࠾ࠡࡽࢀࠦᑷ"), bstack1ll111l1l_opy_)
    except Exception as e:
        print(bstack1l111l1_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡷࡪࡺࡴࡪࡰࡪࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡹࡴࡢࡶࡸࡷࠥ࡬࡯ࡳࠢࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࠦࡻࡾࠤᑸ"), e)
def bstack1ll11111l1_opy_(type, name, status, reason, bstack1llll1ll1l_opy_, bstack11ll111l_opy_):
    bstack1l11lll1l1_opy_ = {
        bstack1l111l1_opy_ (u"ࠬࡧࡣࡵ࡫ࡲࡲࠬᑹ"): type,
        bstack1l111l1_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩᑺ"): {}
    }
    if type == bstack1l111l1_opy_ (u"ࠧࡢࡰࡱࡳࡹࡧࡴࡦࠩᑻ"):
        bstack1l11lll1l1_opy_[bstack1l111l1_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫᑼ")][bstack1l111l1_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨᑽ")] = bstack1llll1ll1l_opy_
        bstack1l11lll1l1_opy_[bstack1l111l1_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭ᑾ")][bstack1l111l1_opy_ (u"ࠫࡩࡧࡴࡢࠩᑿ")] = json.dumps(str(bstack11ll111l_opy_))
    if type == bstack1l111l1_opy_ (u"ࠬࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭ᒀ"):
        bstack1l11lll1l1_opy_[bstack1l111l1_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩᒁ")][bstack1l111l1_opy_ (u"ࠧ࡯ࡣࡰࡩࠬᒂ")] = name
    if type == bstack1l111l1_opy_ (u"ࠨࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡘࡺࡡࡵࡷࡶࠫᒃ"):
        bstack1l11lll1l1_opy_[bstack1l111l1_opy_ (u"ࠩࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠬᒄ")][bstack1l111l1_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪᒅ")] = status
        if status == bstack1l111l1_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫᒆ") and str(reason) != bstack1l111l1_opy_ (u"ࠧࠨᒇ"):
            bstack1l11lll1l1_opy_[bstack1l111l1_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩᒈ")][bstack1l111l1_opy_ (u"ࠧࡳࡧࡤࡷࡴࡴࠧᒉ")] = json.dumps(str(reason))
    bstack1ll11lll_opy_ = bstack1l111l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࢂ࠭ᒊ").format(json.dumps(bstack1l11lll1l1_opy_))
    return bstack1ll11lll_opy_
def bstack11lllll11_opy_(url, config, logger, bstack11ll111l1_opy_=False):
    hostname = bstack11ll1ll1l_opy_(url)
    is_private = bstack11l1l1l1l_opy_(hostname)
    try:
        if is_private or bstack11ll111l1_opy_:
            file_path = bstack111lllll11_opy_(bstack1l111l1_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩᒋ"), bstack1l111l1_opy_ (u"ࠪ࠲ࡧࡹࡴࡢࡥ࡮࠱ࡨࡵ࡮ࡧ࡫ࡪ࠲࡯ࡹ࡯࡯ࠩᒌ"), logger)
            if os.environ.get(bstack1l111l1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡐࡔࡉࡁࡍࡡࡑࡓ࡙ࡥࡓࡆࡖࡢࡉࡗࡘࡏࡓࠩᒍ")) and eval(
                    os.environ.get(bstack1l111l1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡑࡕࡃࡂࡎࡢࡒࡔ࡚࡟ࡔࡇࡗࡣࡊࡘࡒࡐࡔࠪᒎ"))):
                return
            if (bstack1l111l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪᒏ") in config and not config[bstack1l111l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫᒐ")]):
                os.environ[bstack1l111l1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡍࡑࡆࡅࡑࡥࡎࡐࡖࡢࡗࡊ࡚࡟ࡆࡔࡕࡓࡗ࠭ᒑ")] = str(True)
                bstack1llll1lllll_opy_ = {bstack1l111l1_opy_ (u"ࠩ࡫ࡳࡸࡺ࡮ࡢ࡯ࡨࠫᒒ"): hostname}
                bstack11l11ll1ll_opy_(bstack1l111l1_opy_ (u"ࠪ࠲ࡧࡹࡴࡢࡥ࡮࠱ࡨࡵ࡮ࡧ࡫ࡪ࠲࡯ࡹ࡯࡯ࠩᒓ"), bstack1l111l1_opy_ (u"ࠫࡳࡻࡤࡨࡧࡢࡰࡴࡩࡡ࡭ࠩᒔ"), bstack1llll1lllll_opy_, logger)
    except Exception as e:
        pass
def bstack111ll1111_opy_(caps, bstack1llll1lll11_opy_):
    if bstack1l111l1_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭ᒕ") in caps:
        caps[bstack1l111l1_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧᒖ")][bstack1l111l1_opy_ (u"ࠧ࡭ࡱࡦࡥࡱ࠭ᒗ")] = True
        if bstack1llll1lll11_opy_:
            caps[bstack1l111l1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩᒘ")][bstack1l111l1_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫᒙ")] = bstack1llll1lll11_opy_
    else:
        caps[bstack1l111l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰࡯ࡳࡨࡧ࡬ࠨᒚ")] = True
        if bstack1llll1lll11_opy_:
            caps[bstack1l111l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬᒛ")] = bstack1llll1lll11_opy_
def bstack1llllll1111_opy_(bstack1l111lll11_opy_):
    bstack1llll1lll1l_opy_ = bstack1ll1ll1l1_opy_(threading.current_thread(), bstack1l111l1_opy_ (u"ࠬࡺࡥࡴࡶࡖࡸࡦࡺࡵࡴࠩᒜ"), bstack1l111l1_opy_ (u"࠭ࠧᒝ"))
    if bstack1llll1lll1l_opy_ == bstack1l111l1_opy_ (u"ࠧࠨᒞ") or bstack1llll1lll1l_opy_ == bstack1l111l1_opy_ (u"ࠨࡵ࡮࡭ࡵࡶࡥࡥࠩᒟ"):
        threading.current_thread().testStatus = bstack1l111lll11_opy_
    else:
        if bstack1l111lll11_opy_ == bstack1l111l1_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩᒠ"):
            threading.current_thread().testStatus = bstack1l111lll11_opy_