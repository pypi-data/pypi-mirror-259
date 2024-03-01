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
import re
from bstack_utils.bstack1l1llll11l_opy_ import bstack1llllll1111_opy_
def bstack1llllllll11_opy_(fixture_name):
    if fixture_name.startswith(bstack1l111l1_opy_ (u"ࠪࡣࡽࡻ࡮ࡪࡶࡢࡷࡪࡺࡵࡱࡡࡩࡹࡳࡩࡴࡪࡱࡱࡣ࡫࡯ࡸࡵࡷࡵࡩࠬᐸ")):
        return bstack1l111l1_opy_ (u"ࠫࡸ࡫ࡴࡶࡲ࠰ࡪࡺࡴࡣࡵ࡫ࡲࡲࠬᐹ")
    elif fixture_name.startswith(bstack1l111l1_opy_ (u"ࠬࡥࡸࡶࡰ࡬ࡸࡤࡹࡥࡵࡷࡳࡣࡲࡵࡤࡶ࡮ࡨࡣ࡫࡯ࡸࡵࡷࡵࡩࠬᐺ")):
        return bstack1l111l1_opy_ (u"࠭ࡳࡦࡶࡸࡴ࠲ࡳ࡯ࡥࡷ࡯ࡩࠬᐻ")
    elif fixture_name.startswith(bstack1l111l1_opy_ (u"ࠧࡠࡺࡸࡲ࡮ࡺ࡟ࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡩࡹࡳࡩࡴࡪࡱࡱࡣ࡫࡯ࡸࡵࡷࡵࡩࠬᐼ")):
        return bstack1l111l1_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰ࠰ࡪࡺࡴࡣࡵ࡫ࡲࡲࠬᐽ")
    elif fixture_name.startswith(bstack1l111l1_opy_ (u"ࠩࡢࡼࡺࡴࡩࡵࡡࡷࡩࡦࡸࡤࡰࡹࡱࡣ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࡥࡦࡪࡺࡷࡹࡷ࡫ࠧᐾ")):
        return bstack1l111l1_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲ࠲ࡳ࡯ࡥࡷ࡯ࡩࠬᐿ")
def bstack1llllllll1l_opy_(fixture_name):
    return bool(re.match(bstack1l111l1_opy_ (u"ࠫࡣࡥࡸࡶࡰ࡬ࡸࡤ࠮ࡳࡦࡶࡸࡴࢁࡺࡥࡢࡴࡧࡳࡼࡴࠩࡠࠪࡩࡹࡳࡩࡴࡪࡱࡱࢀࡲࡵࡤࡶ࡮ࡨ࠭ࡤ࡬ࡩࡹࡶࡸࡶࡪࡥ࠮ࠫࠩᑀ"), fixture_name))
def bstack1llllll11ll_opy_(fixture_name):
    return bool(re.match(bstack1l111l1_opy_ (u"ࠬࡤ࡟ࡹࡷࡱ࡭ࡹࡥࠨࡴࡧࡷࡹࡵࢂࡴࡦࡣࡵࡨࡴࡽ࡮ࠪࡡࡰࡳࡩࡻ࡬ࡦࡡࡩ࡭ࡽࡺࡵࡳࡧࡢ࠲࠯࠭ᑁ"), fixture_name))
def bstack1llllll111l_opy_(fixture_name):
    return bool(re.match(bstack1l111l1_opy_ (u"࠭࡞ࡠࡺࡸࡲ࡮ࡺ࡟ࠩࡵࡨࡸࡺࡶࡼࡵࡧࡤࡶࡩࡵࡷ࡯ࠫࡢࡧࡱࡧࡳࡴࡡࡩ࡭ࡽࡺࡵࡳࡧࡢ࠲࠯࠭ᑂ"), fixture_name))
def bstack1lllllll111_opy_(fixture_name):
    if fixture_name.startswith(bstack1l111l1_opy_ (u"ࠧࡠࡺࡸࡲ࡮ࡺ࡟ࡴࡧࡷࡹࡵࡥࡦࡶࡰࡦࡸ࡮ࡵ࡮ࡠࡨ࡬ࡼࡹࡻࡲࡦࠩᑃ")):
        return bstack1l111l1_opy_ (u"ࠨࡵࡨࡸࡺࡶ࠭ࡧࡷࡱࡧࡹ࡯࡯࡯ࠩᑄ"), bstack1l111l1_opy_ (u"ࠩࡅࡉࡋࡕࡒࡆࡡࡈࡅࡈࡎࠧᑅ")
    elif fixture_name.startswith(bstack1l111l1_opy_ (u"ࠪࡣࡽࡻ࡮ࡪࡶࡢࡷࡪࡺࡵࡱࡡࡰࡳࡩࡻ࡬ࡦࡡࡩ࡭ࡽࡺࡵࡳࡧࠪᑆ")):
        return bstack1l111l1_opy_ (u"ࠫࡸ࡫ࡴࡶࡲ࠰ࡱࡴࡪࡵ࡭ࡧࠪᑇ"), bstack1l111l1_opy_ (u"ࠬࡈࡅࡇࡑࡕࡉࡤࡇࡌࡍࠩᑈ")
    elif fixture_name.startswith(bstack1l111l1_opy_ (u"࠭࡟ࡹࡷࡱ࡭ࡹࡥࡴࡦࡣࡵࡨࡴࡽ࡮ࡠࡨࡸࡲࡨࡺࡩࡰࡰࡢࡪ࡮ࡾࡴࡶࡴࡨࠫᑉ")):
        return bstack1l111l1_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯࠯ࡩࡹࡳࡩࡴࡪࡱࡱࠫᑊ"), bstack1l111l1_opy_ (u"ࠨࡃࡉࡘࡊࡘ࡟ࡆࡃࡆࡌࠬᑋ")
    elif fixture_name.startswith(bstack1l111l1_opy_ (u"ࠩࡢࡼࡺࡴࡩࡵࡡࡷࡩࡦࡸࡤࡰࡹࡱࡣࡲࡵࡤࡶ࡮ࡨࡣ࡫࡯ࡸࡵࡷࡵࡩࠬᑌ")):
        return bstack1l111l1_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲ࠲ࡳ࡯ࡥࡷ࡯ࡩࠬᑍ"), bstack1l111l1_opy_ (u"ࠫࡆࡌࡔࡆࡔࡢࡅࡑࡒࠧᑎ")
    return None, None
def bstack1llllll1l1l_opy_(hook_name):
    if hook_name in [bstack1l111l1_opy_ (u"ࠬࡹࡥࡵࡷࡳࠫᑏ"), bstack1l111l1_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࠨᑐ")]:
        return hook_name.capitalize()
    return hook_name
def bstack1lllllll1ll_opy_(hook_name):
    if hook_name in [bstack1l111l1_opy_ (u"ࠧࡴࡧࡷࡹࡵࡥࡦࡶࡰࡦࡸ࡮ࡵ࡮ࠨᑑ"), bstack1l111l1_opy_ (u"ࠨࡵࡨࡸࡺࡶ࡟࡮ࡧࡷ࡬ࡴࡪࠧᑒ")]:
        return bstack1l111l1_opy_ (u"ࠩࡅࡉࡋࡕࡒࡆࡡࡈࡅࡈࡎࠧᑓ")
    elif hook_name in [bstack1l111l1_opy_ (u"ࠪࡷࡪࡺࡵࡱࡡࡰࡳࡩࡻ࡬ࡦࠩᑔ"), bstack1l111l1_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࡢࡧࡱࡧࡳࡴࠩᑕ")]:
        return bstack1l111l1_opy_ (u"ࠬࡈࡅࡇࡑࡕࡉࡤࡇࡌࡍࠩᑖ")
    elif hook_name in [bstack1l111l1_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࡠࡨࡸࡲࡨࡺࡩࡰࡰࠪᑗ"), bstack1l111l1_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡰࡩࡹ࡮࡯ࡥࠩᑘ")]:
        return bstack1l111l1_opy_ (u"ࠨࡃࡉࡘࡊࡘ࡟ࡆࡃࡆࡌࠬᑙ")
    elif hook_name in [bstack1l111l1_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࡣࡲࡵࡤࡶ࡮ࡨࠫᑚ"), bstack1l111l1_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࡤࡩ࡬ࡢࡵࡶࠫᑛ")]:
        return bstack1l111l1_opy_ (u"ࠫࡆࡌࡔࡆࡔࡢࡅࡑࡒࠧᑜ")
    return hook_name
def bstack1llllll11l1_opy_(node, scenario):
    if hasattr(node, bstack1l111l1_opy_ (u"ࠬࡩࡡ࡭࡮ࡶࡴࡪࡩࠧᑝ")):
        parts = node.nodeid.rsplit(bstack1l111l1_opy_ (u"ࠨ࡛ࠣᑞ"))
        params = parts[-1]
        return bstack1l111l1_opy_ (u"ࠢࡼࡿࠣ࡟ࢀࢃࠢᑟ").format(scenario.name, params)
    return scenario.name
def bstack1llllll1lll_opy_(node):
    try:
        examples = []
        if hasattr(node, bstack1l111l1_opy_ (u"ࠨࡥࡤࡰࡱࡹࡰࡦࡥࠪᑠ")):
            examples = list(node.callspec.params[bstack1l111l1_opy_ (u"ࠩࡢࡴࡾࡺࡥࡴࡶࡢࡦࡩࡪ࡟ࡦࡺࡤࡱࡵࡲࡥࠨᑡ")].values())
        return examples
    except:
        return []
def bstack1lllllll11l_opy_(feature, scenario):
    return list(feature.tags) + list(scenario.tags)
def bstack1llllll1ll1_opy_(report):
    try:
        status = bstack1l111l1_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪᑢ")
        if report.passed or (report.failed and hasattr(report, bstack1l111l1_opy_ (u"ࠦࡼࡧࡳࡹࡨࡤ࡭ࡱࠨᑣ"))):
            status = bstack1l111l1_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬᑤ")
        elif report.skipped:
            status = bstack1l111l1_opy_ (u"࠭ࡳ࡬࡫ࡳࡴࡪࡪࠧᑥ")
        bstack1llllll1111_opy_(status)
    except:
        pass
def bstack11ll1l111_opy_(status):
    try:
        bstack1lllllll1l1_opy_ = bstack1l111l1_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧᑦ")
        if status == bstack1l111l1_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨᑧ"):
            bstack1lllllll1l1_opy_ = bstack1l111l1_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩᑨ")
        elif status == bstack1l111l1_opy_ (u"ࠪࡷࡰ࡯ࡰࡱࡧࡧࠫᑩ"):
            bstack1lllllll1l1_opy_ = bstack1l111l1_opy_ (u"ࠫࡸࡱࡩࡱࡲࡨࡨࠬᑪ")
        bstack1llllll1111_opy_(bstack1lllllll1l1_opy_)
    except:
        pass
def bstack1llllll1l11_opy_(item=None, report=None, summary=None, extra=None):
    return