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
import atexit
import datetime
import inspect
import logging
import os
import signal
import sys
import threading
from uuid import uuid4
from bstack_utils.percy_sdk import PercySDK
import tempfile
import pytest
from packaging import version
from browserstack_sdk.__init__ import (bstack111ll1l1l_opy_, bstack11l1ll1l1_opy_, update, bstack1111l11l_opy_,
                                       bstack1lll1l1ll1_opy_, bstack1ll11l11l_opy_, bstack1l11llll1_opy_, bstack1l1l11ll1_opy_,
                                       bstack111l1ll1l_opy_, bstack1l11l1llll_opy_, bstack111l11l1l_opy_, bstack1lll1l11ll_opy_,
                                       bstack1l1lll11ll_opy_, getAccessibilityResults, getAccessibilityResultsSummary, perform_scan, bstack1ll11ll11l_opy_)
from browserstack_sdk.bstack11l1ll11_opy_ import bstack11llll11l_opy_
from browserstack_sdk._version import __version__
from bstack_utils import bstack1ll111l1l1_opy_
from bstack_utils.capture import bstack1l11l11111_opy_
from bstack_utils.config import Config
from bstack_utils.constants import bstack1l1llll1l_opy_, bstack1l1l1l1l1l_opy_, bstack1ll11l111_opy_, \
    bstack1ll1ll11ll_opy_
from bstack_utils.helper import bstack1ll1ll1l1_opy_, bstack1l1111l11_opy_, bstack11l11l1111_opy_, bstack1lll11llll_opy_, \
    bstack11l11l1ll1_opy_, \
    bstack11l11l111l_opy_, bstack1l1ll11lll_opy_, bstack11ll1l1l1_opy_, bstack111lllllll_opy_, bstack1lll11l1l_opy_, Notset, \
    bstack111l11l1_opy_, bstack11l1111ll1_opy_, bstack11l11l11ll_opy_, Result, bstack11l11l1l1l_opy_, bstack11l111ll11_opy_, bstack1l1111lll1_opy_, \
    bstack1lll11l111_opy_, bstack1l1l111l1_opy_, bstack1l1l1ll111_opy_, bstack11l11111l1_opy_
from bstack_utils.bstack111ll1111l_opy_ import bstack111ll1l1l1_opy_
from bstack_utils.messages import bstack1l11ll11l1_opy_, bstack1ll11l111l_opy_, bstack1l1ll1l1ll_opy_, bstack1lll1111ll_opy_, bstack111llllll_opy_, \
    bstack1l1ll11111_opy_, bstack1l11l11l1_opy_, bstack11lll1111_opy_, bstack1ll11ll11_opy_, bstack11l111l1_opy_, \
    bstack1llll11ll_opy_, bstack1ll11l1ll1_opy_
from bstack_utils.proxy import bstack1l11l1ll1l_opy_, bstack11l1l1111_opy_
from bstack_utils.bstack111l1lll_opy_ import bstack1llllll1l11_opy_, bstack1llllll1l1l_opy_, bstack1lllllll1ll_opy_, bstack1llllll11ll_opy_, \
    bstack1llllll111l_opy_, bstack1llllll11l1_opy_, bstack1lllllll11l_opy_, bstack11ll1l111_opy_, bstack1llllll1ll1_opy_
from bstack_utils.bstack111ll111l_opy_ import bstack1l1l1111l_opy_
from bstack_utils.bstack1l1llll11l_opy_ import bstack1ll11111l1_opy_, bstack11lllll11_opy_, bstack111ll1111_opy_, \
    bstack11l11111l_opy_, bstack1111l1lll_opy_
from bstack_utils.bstack11llll1lll_opy_ import bstack1l111l1l11_opy_
from bstack_utils.bstack11ll11l11_opy_ import bstack1l1111l1l_opy_
import bstack_utils.bstack1lll11l11l_opy_ as bstack1l1lll11l1_opy_
from bstack_utils.bstack1lll1l1l1_opy_ import bstack1lll1l1l1_opy_
bstack1lllll111_opy_ = None
bstack1l11ll1ll_opy_ = None
bstack11lll11ll_opy_ = None
bstack1llll1llll_opy_ = None
bstack1l11l1111_opy_ = None
bstack1l1l1ll1_opy_ = None
bstack11111lll1_opy_ = None
bstack1111ll1ll_opy_ = None
bstack1lll11ll_opy_ = None
bstack11111ll1l_opy_ = None
bstack1ll111ll11_opy_ = None
bstack111l111ll_opy_ = None
bstack1l11l1l11l_opy_ = None
bstack11l1l11ll_opy_ = bstack1l111l1_opy_ (u"࠭ࠧᗃ")
CONFIG = {}
bstack1l1llll1l1_opy_ = False
bstack1l1l11111_opy_ = bstack1l111l1_opy_ (u"ࠧࠨᗄ")
bstack1l1l11l111_opy_ = bstack1l111l1_opy_ (u"ࠨࠩᗅ")
bstack1ll1l11lll_opy_ = False
bstack11lll1l1_opy_ = []
bstack1llll11ll1_opy_ = bstack1l1llll1l_opy_
bstack1lll11ll1ll_opy_ = bstack1l111l1_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩᗆ")
bstack1lll1l1l11l_opy_ = False
bstack1l1lll111_opy_ = {}
bstack1lll1l11l_opy_ = False
logger = bstack1ll111l1l1_opy_.get_logger(__name__, bstack1llll11ll1_opy_)
store = {
    bstack1l111l1_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣ࡭ࡵ࡯࡬ࡡࡸࡹ࡮ࡪࠧᗇ"): []
}
bstack1lll1l1ll11_opy_ = False
try:
    from playwright.sync_api import (
        BrowserContext,
        Page
    )
except:
    pass
import json
_1l11l111l1_opy_ = {}
current_test_uuid = None
def bstack1lll11111l_opy_(page, bstack11l1lll1_opy_):
    try:
        page.evaluate(bstack1l111l1_opy_ (u"ࠦࡤࠦ࠽࠿ࠢࡾࢁࠧᗈ"),
                      bstack1l111l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪࠨࠬࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼࠤࡱࡥࡲ࡫ࠢ࠻ࠩᗉ") + json.dumps(
                          bstack11l1lll1_opy_) + bstack1l111l1_opy_ (u"ࠨࡽࡾࠤᗊ"))
    except Exception as e:
        print(bstack1l111l1_opy_ (u"ࠢࡦࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠣࡷࡪࡹࡳࡪࡱࡱࠤࡳࡧ࡭ࡦࠢࡾࢁࠧᗋ"), e)
def bstack11ll111ll_opy_(page, message, level):
    try:
        page.evaluate(bstack1l111l1_opy_ (u"ࠣࡡࠣࡁࡃࠦࡻࡾࠤᗌ"), bstack1l111l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡤࡲࡳࡵࡴࡢࡶࡨࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢࡥࡣࡷࡥࠧࡀࠧᗍ") + json.dumps(
            message) + bstack1l111l1_opy_ (u"ࠪ࠰ࠧࡲࡥࡷࡧ࡯ࠦ࠿࠭ᗎ") + json.dumps(level) + bstack1l111l1_opy_ (u"ࠫࢂࢃࠧᗏ"))
    except Exception as e:
        print(bstack1l111l1_opy_ (u"ࠧ࡫ࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠡࡣࡱࡲࡴࡺࡡࡵ࡫ࡲࡲࠥࢁࡽࠣᗐ"), e)
def pytest_configure(config):
    bstack11111111_opy_ = Config.bstack1ll1l11ll_opy_()
    config.args = bstack1l1111l1l_opy_.bstack1lll1ll1ll1_opy_(config.args)
    bstack11111111_opy_.bstack1l1l1lllll_opy_(bstack1l1l1ll111_opy_(config.getoption(bstack1l111l1_opy_ (u"࠭ࡳ࡬࡫ࡳࡗࡪࡹࡳࡪࡱࡱࡗࡹࡧࡴࡶࡵࠪᗑ"))))
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    bstack1lll1l1ll1l_opy_ = item.config.getoption(bstack1l111l1_opy_ (u"ࠧࡴ࡭࡬ࡴࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩᗒ"))
    plugins = item.config.getoption(bstack1l111l1_opy_ (u"ࠣࡲ࡯ࡹ࡬࡯࡮ࡴࠤᗓ"))
    report = outcome.get_result()
    bstack1lll1l1l1l1_opy_(item, call, report)
    if bstack1l111l1_opy_ (u"ࠤࡳࡽࡹ࡫ࡳࡵࡡࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡱ࡮ࡸ࡫࡮ࡴࠢᗔ") not in plugins or bstack1lll11l1l_opy_():
        return
    summary = []
    driver = getattr(item, bstack1l111l1_opy_ (u"ࠥࡣࡩࡸࡩࡷࡧࡵࠦᗕ"), None)
    page = getattr(item, bstack1l111l1_opy_ (u"ࠦࡤࡶࡡࡨࡧࠥᗖ"), None)
    try:
        if (driver == None):
            driver = threading.current_thread().bstackSessionDriver
    except:
        pass
    item._driver = driver
    if (driver is not None):
        bstack1lll11l11l1_opy_(item, report, summary, bstack1lll1l1ll1l_opy_)
    if (page is not None):
        bstack1lll11llll1_opy_(item, report, summary, bstack1lll1l1ll1l_opy_)
def bstack1lll11l11l1_opy_(item, report, summary, bstack1lll1l1ll1l_opy_):
    if report.when == bstack1l111l1_opy_ (u"ࠬࡹࡥࡵࡷࡳࠫᗗ") and report.skipped:
        bstack1llllll1ll1_opy_(report)
    if report.when in [bstack1l111l1_opy_ (u"ࠨࡳࡦࡶࡸࡴࠧᗘ"), bstack1l111l1_opy_ (u"ࠢࡵࡧࡤࡶࡩࡵࡷ࡯ࠤᗙ")]:
        return
    if not bstack11l11l1111_opy_():
        return
    try:
        if (str(bstack1lll1l1ll1l_opy_).lower() != bstack1l111l1_opy_ (u"ࠨࡶࡵࡹࡪ࠭ᗚ")):
            item._driver.execute_script(
                bstack1l111l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨ࡮ࡢ࡯ࡨࠦ࠿ࠦࠧᗛ") + json.dumps(
                    report.nodeid) + bstack1l111l1_opy_ (u"ࠪࢁࢂ࠭ᗜ"))
        os.environ[bstack1l111l1_opy_ (u"ࠫࡕ࡟ࡔࡆࡕࡗࡣ࡙ࡋࡓࡕࡡࡑࡅࡒࡋࠧᗝ")] = report.nodeid
    except Exception as e:
        summary.append(
            bstack1l111l1_opy_ (u"ࠧ࡝ࡁࡓࡐࡌࡒࡌࡀࠠࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡱࡦࡸ࡫ࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡱࡥࡲ࡫࠺ࠡࡽ࠳ࢁࠧᗞ").format(e)
        )
    passed = report.passed or report.skipped or (report.failed and hasattr(report, bstack1l111l1_opy_ (u"ࠨࡷࡢࡵࡻࡪࡦ࡯࡬ࠣᗟ")))
    bstack1l11lllll1_opy_ = bstack1l111l1_opy_ (u"ࠢࠣᗠ")
    bstack1llllll1ll1_opy_(report)
    if not passed:
        try:
            bstack1l11lllll1_opy_ = report.longrepr.reprcrash
        except Exception as e:
            summary.append(
                bstack1l111l1_opy_ (u"࡙ࠣࡄࡖࡓࡏࡎࡈ࠼ࠣࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡤࡦࡶࡨࡶࡲ࡯࡮ࡦࠢࡩࡥ࡮ࡲࡵࡳࡧࠣࡶࡪࡧࡳࡰࡰ࠽ࠤࢀ࠶ࡽࠣᗡ").format(e)
            )
        try:
            if (threading.current_thread().bstackTestErrorMessages == None):
                threading.current_thread().bstackTestErrorMessages = []
        except Exception as e:
            threading.current_thread().bstackTestErrorMessages = []
        threading.current_thread().bstackTestErrorMessages.append(str(bstack1l11lllll1_opy_))
    if not report.skipped:
        passed = report.passed or (report.failed and hasattr(report, bstack1l111l1_opy_ (u"ࠤࡺࡥࡸࡾࡦࡢ࡫࡯ࠦᗢ")))
        bstack1l11lllll1_opy_ = bstack1l111l1_opy_ (u"ࠥࠦᗣ")
        if not passed:
            try:
                bstack1l11lllll1_opy_ = report.longrepr.reprcrash
            except Exception as e:
                summary.append(
                    bstack1l111l1_opy_ (u"ࠦ࡜ࡇࡒࡏࡋࡑࡋ࠿ࠦࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡧࡩࡹ࡫ࡲ࡮࡫ࡱࡩࠥ࡬ࡡࡪ࡮ࡸࡶࡪࠦࡲࡦࡣࡶࡳࡳࡀࠠࡼ࠲ࢀࠦᗤ").format(e)
                )
            try:
                if (threading.current_thread().bstackTestErrorMessages == None):
                    threading.current_thread().bstackTestErrorMessages = []
            except Exception as e:
                threading.current_thread().bstackTestErrorMessages = []
            threading.current_thread().bstackTestErrorMessages.append(str(bstack1l11lllll1_opy_))
        try:
            if passed:
                item._driver.execute_script(
                    bstack1l111l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼ࡞ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠦࡦࡩࡴࡪࡱࡱࠦ࠿ࠦࠢࡢࡰࡱࡳࡹࡧࡴࡦࠤ࠯ࠤࡡࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁ࡜ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠨ࡬ࡦࡸࡨࡰࠧࡀࠠࠣ࡫ࡱࡪࡴࠨࠬࠡ࡞ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠣࡦࡤࡸࡦࠨ࠺ࠡࠩᗥ")
                    + json.dumps(bstack1l111l1_opy_ (u"ࠨࡰࡢࡵࡶࡩࡩࠧࠢᗦ"))
                    + bstack1l111l1_opy_ (u"ࠢ࡝ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࢀࡠࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡿࠥᗧ")
                )
            else:
                item._driver.execute_script(
                    bstack1l111l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࡡࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡥࡳࡴ࡯ࡵࡣࡷࡩࠧ࠲ࠠ࡝ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽ࡟ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠤ࡯ࡩࡻ࡫࡬ࠣ࠼ࠣࠦࡪࡸࡲࡰࡴࠥ࠰ࠥࡢࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠧࡪࡡࡵࡣࠥ࠾ࠥ࠭ᗨ")
                    + json.dumps(str(bstack1l11lllll1_opy_))
                    + bstack1l111l1_opy_ (u"ࠤ࡟ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࢂࡢࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࢁࠧᗩ")
                )
        except Exception as e:
            summary.append(bstack1l111l1_opy_ (u"࡛ࠥࡆࡘࡎࡊࡐࡊ࠾ࠥࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡣࡱࡲࡴࡺࡡࡵࡧ࠽ࠤࢀ࠶ࡽࠣᗪ").format(e))
def bstack1lll11l1lll_opy_(test_name, error_message):
    try:
        bstack1lll1l111ll_opy_ = []
        bstack1l1l11l11l_opy_ = os.environ.get(bstack1l111l1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡏࡎࡅࡇ࡛ࠫᗫ"), bstack1l111l1_opy_ (u"ࠬ࠶ࠧᗬ"))
        bstack1lllllllll_opy_ = {bstack1l111l1_opy_ (u"࠭࡮ࡢ࡯ࡨࠫᗭ"): test_name, bstack1l111l1_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭ᗮ"): error_message, bstack1l111l1_opy_ (u"ࠨ࡫ࡱࡨࡪࡾࠧᗯ"): bstack1l1l11l11l_opy_}
        bstack1lll11lllll_opy_ = os.path.join(tempfile.gettempdir(), bstack1l111l1_opy_ (u"ࠩࡳࡻࡤࡶࡹࡵࡧࡶࡸࡤ࡫ࡲࡳࡱࡵࡣࡱ࡯ࡳࡵ࠰࡭ࡷࡴࡴࠧᗰ"))
        if os.path.exists(bstack1lll11lllll_opy_):
            with open(bstack1lll11lllll_opy_) as f:
                bstack1lll1l111ll_opy_ = json.load(f)
        bstack1lll1l111ll_opy_.append(bstack1lllllllll_opy_)
        with open(bstack1lll11lllll_opy_, bstack1l111l1_opy_ (u"ࠪࡻࠬᗱ")) as f:
            json.dump(bstack1lll1l111ll_opy_, f)
    except Exception as e:
        logger.debug(bstack1l111l1_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡰࡦࡴࡶ࡭ࡸࡺࡩ࡯ࡩࠣࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠠࡱࡻࡷࡩࡸࡺࠠࡦࡴࡵࡳࡷࡹ࠺ࠡࠩᗲ") + str(e))
def bstack1lll11llll1_opy_(item, report, summary, bstack1lll1l1ll1l_opy_):
    if report.when in [bstack1l111l1_opy_ (u"ࠧࡹࡥࡵࡷࡳࠦᗳ"), bstack1l111l1_opy_ (u"ࠨࡴࡦࡣࡵࡨࡴࡽ࡮ࠣᗴ")]:
        return
    if (str(bstack1lll1l1ll1l_opy_).lower() != bstack1l111l1_opy_ (u"ࠧࡵࡴࡸࡩࠬᗵ")):
        bstack1lll11111l_opy_(item._page, report.nodeid)
    passed = report.passed or report.skipped or (report.failed and hasattr(report, bstack1l111l1_opy_ (u"ࠣࡹࡤࡷࡽ࡬ࡡࡪ࡮ࠥᗶ")))
    bstack1l11lllll1_opy_ = bstack1l111l1_opy_ (u"ࠤࠥᗷ")
    bstack1llllll1ll1_opy_(report)
    if not report.skipped:
        if not passed:
            try:
                bstack1l11lllll1_opy_ = report.longrepr.reprcrash
            except Exception as e:
                summary.append(
                    bstack1l111l1_opy_ (u"࡛ࠥࡆࡘࡎࡊࡐࡊ࠾ࠥࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡦࡨࡸࡪࡸ࡭ࡪࡰࡨࠤ࡫ࡧࡩ࡭ࡷࡵࡩࠥࡸࡥࡢࡵࡲࡲ࠿ࠦࡻ࠱ࡿࠥᗸ").format(e)
                )
        try:
            if passed:
                bstack1111l1lll_opy_(getattr(item, bstack1l111l1_opy_ (u"ࠫࡤࡶࡡࡨࡧࠪᗹ"), None), bstack1l111l1_opy_ (u"ࠧࡶࡡࡴࡵࡨࡨࠧᗺ"))
            else:
                error_message = bstack1l111l1_opy_ (u"࠭ࠧᗻ")
                if bstack1l11lllll1_opy_:
                    bstack11ll111ll_opy_(item._page, str(bstack1l11lllll1_opy_), bstack1l111l1_opy_ (u"ࠢࡦࡴࡵࡳࡷࠨᗼ"))
                    bstack1111l1lll_opy_(getattr(item, bstack1l111l1_opy_ (u"ࠨࡡࡳࡥ࡬࡫ࠧᗽ"), None), bstack1l111l1_opy_ (u"ࠤࡩࡥ࡮ࡲࡥࡥࠤᗾ"), str(bstack1l11lllll1_opy_))
                    error_message = str(bstack1l11lllll1_opy_)
                else:
                    bstack1111l1lll_opy_(getattr(item, bstack1l111l1_opy_ (u"ࠪࡣࡵࡧࡧࡦࠩᗿ"), None), bstack1l111l1_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࠦᘀ"))
                bstack1lll11l1lll_opy_(report.nodeid, error_message)
        except Exception as e:
            summary.append(bstack1l111l1_opy_ (u"ࠧ࡝ࡁࡓࡐࡌࡒࡌࡀࠠࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡹࡵࡪࡡࡵࡧࠣࡷࡪࡹࡳࡪࡱࡱࠤࡸࡺࡡࡵࡷࡶ࠾ࠥࢁ࠰ࡾࠤᘁ").format(e))
try:
    from typing import Generator
    import pytest_playwright.pytest_playwright as p
    @pytest.fixture
    def page(context: BrowserContext, request: pytest.FixtureRequest) -> Generator[Page, None, None]:
        page = context.new_page()
        request.node._page = page
        yield page
except:
    pass
def pytest_addoption(parser):
    parser.addoption(bstack1l111l1_opy_ (u"ࠨ࠭࠮ࡵ࡮࡭ࡵ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠥᘂ"), default=bstack1l111l1_opy_ (u"ࠢࡇࡣ࡯ࡷࡪࠨᘃ"), help=bstack1l111l1_opy_ (u"ࠣࡃࡸࡸࡴࡳࡡࡵ࡫ࡦࠤࡸ࡫ࡴࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡱࡥࡲ࡫ࠢᘄ"))
    parser.addoption(bstack1l111l1_opy_ (u"ࠤ࠰࠱ࡸࡱࡩࡱࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠣᘅ"), default=bstack1l111l1_opy_ (u"ࠥࡊࡦࡲࡳࡦࠤᘆ"), help=bstack1l111l1_opy_ (u"ࠦࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡩࠠࡴࡧࡷࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡴࡡ࡮ࡧࠥᘇ"))
    try:
        import pytest_selenium.pytest_selenium
    except:
        parser.addoption(bstack1l111l1_opy_ (u"ࠧ࠳࠭ࡥࡴ࡬ࡺࡪࡸࠢᘈ"), action=bstack1l111l1_opy_ (u"ࠨࡳࡵࡱࡵࡩࠧᘉ"), default=bstack1l111l1_opy_ (u"ࠢࡤࡪࡵࡳࡲ࡫ࠢᘊ"),
                         help=bstack1l111l1_opy_ (u"ࠣࡆࡵ࡭ࡻ࡫ࡲࠡࡶࡲࠤࡷࡻ࡮ࠡࡶࡨࡷࡹࡹࠢᘋ"))
def bstack1l1111l1l1_opy_(log):
    if not (log[bstack1l111l1_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪᘌ")] and log[bstack1l111l1_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫᘍ")].strip()):
        return
    active = bstack11llllll1l_opy_()
    log = {
        bstack1l111l1_opy_ (u"ࠫࡱ࡫ࡶࡦ࡮ࠪᘎ"): log[bstack1l111l1_opy_ (u"ࠬࡲࡥࡷࡧ࡯ࠫᘏ")],
        bstack1l111l1_opy_ (u"࠭ࡴࡪ࡯ࡨࡷࡹࡧ࡭ࡱࠩᘐ"): datetime.datetime.utcnow().isoformat() + bstack1l111l1_opy_ (u"࡛ࠧࠩᘑ"),
        bstack1l111l1_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩᘒ"): log[bstack1l111l1_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪᘓ")],
    }
    if active:
        if active[bstack1l111l1_opy_ (u"ࠪࡸࡾࡶࡥࠨᘔ")] == bstack1l111l1_opy_ (u"ࠫ࡭ࡵ࡯࡬ࠩᘕ"):
            log[bstack1l111l1_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬᘖ")] = active[bstack1l111l1_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ᘗ")]
        elif active[bstack1l111l1_opy_ (u"ࠧࡵࡻࡳࡩࠬᘘ")] == bstack1l111l1_opy_ (u"ࠨࡶࡨࡷࡹ࠭ᘙ"):
            log[bstack1l111l1_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩᘚ")] = active[bstack1l111l1_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪᘛ")]
    bstack1l1111l1l_opy_.bstack1lll1ll111_opy_([log])
def bstack11llllll1l_opy_():
    if len(store[bstack1l111l1_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤ࡮࡯ࡰ࡭ࡢࡹࡺ࡯ࡤࠨᘜ")]) > 0 and store[bstack1l111l1_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡨࡰࡱ࡮ࡣࡺࡻࡩࡥࠩᘝ")][-1]:
        return {
            bstack1l111l1_opy_ (u"࠭ࡴࡺࡲࡨࠫᘞ"): bstack1l111l1_opy_ (u"ࠧࡩࡱࡲ࡯ࠬᘟ"),
            bstack1l111l1_opy_ (u"ࠨࡪࡲࡳࡰࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨᘠ"): store[bstack1l111l1_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢ࡬ࡴࡵ࡫ࡠࡷࡸ࡭ࡩ࠭ᘡ")][-1]
        }
    if store.get(bstack1l111l1_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡࡸࡹ࡮ࡪࠧᘢ"), None):
        return {
            bstack1l111l1_opy_ (u"ࠫࡹࡿࡰࡦࠩᘣ"): bstack1l111l1_opy_ (u"ࠬࡺࡥࡴࡶࠪᘤ"),
            bstack1l111l1_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ᘥ"): store[bstack1l111l1_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡵࡶ࡫ࡧࠫᘦ")]
        }
    return None
bstack1l11111l11_opy_ = bstack1l11l11111_opy_(bstack1l1111l1l1_opy_)
def pytest_runtest_call(item):
    try:
        global CONFIG
        global bstack1lll1l1l11l_opy_
        item._1lll1l1llll_opy_ = True
        bstack11l1l11l1_opy_ = bstack1l1lll11l1_opy_.bstack1l1l111l_opy_(CONFIG, bstack11l11l111l_opy_(item.own_markers))
        item._a11y_test_case = bstack11l1l11l1_opy_
        if bstack1lll1l1l11l_opy_:
            driver = getattr(item, bstack1l111l1_opy_ (u"ࠨࡡࡧࡶ࡮ࡼࡥࡳࠩᘧ"), None)
            item._a11y_started = bstack1l1lll11l1_opy_.bstack11111ll1_opy_(driver, bstack11l1l11l1_opy_)
        if not bstack1l1111l1l_opy_.on() or bstack1lll11ll1ll_opy_ != bstack1l111l1_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩᘨ"):
            return
        global current_test_uuid, bstack1l11111l11_opy_
        bstack1l11111l11_opy_.start()
        bstack11lll1llll_opy_ = {
            bstack1l111l1_opy_ (u"ࠪࡹࡺ࡯ࡤࠨᘩ"): uuid4().__str__(),
            bstack1l111l1_opy_ (u"ࠫࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠨᘪ"): datetime.datetime.utcnow().isoformat() + bstack1l111l1_opy_ (u"ࠬࡠࠧᘫ")
        }
        current_test_uuid = bstack11lll1llll_opy_[bstack1l111l1_opy_ (u"࠭ࡵࡶ࡫ࡧࠫᘬ")]
        store[bstack1l111l1_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡵࡶ࡫ࡧࠫᘭ")] = bstack11lll1llll_opy_[bstack1l111l1_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭ᘮ")]
        threading.current_thread().current_test_uuid = current_test_uuid
        _1l11l111l1_opy_[item.nodeid] = {**_1l11l111l1_opy_[item.nodeid], **bstack11lll1llll_opy_}
        bstack1lll11l11ll_opy_(item, _1l11l111l1_opy_[item.nodeid], bstack1l111l1_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡖࡸࡦࡸࡴࡦࡦࠪᘯ"))
    except Exception as err:
        print(bstack1l111l1_opy_ (u"ࠪࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡳࡽࡹ࡫ࡳࡵࡡࡵࡹࡳࡺࡥࡴࡶࡢࡧࡦࡲ࡬࠻ࠢࡾࢁࠬᘰ"), str(err))
def pytest_runtest_setup(item):
    global bstack1lll1l1ll11_opy_
    threading.current_thread().percySessionName = item.nodeid
    if bstack111lllllll_opy_():
        atexit.register(bstack1l1lll111l_opy_)
        if not bstack1lll1l1ll11_opy_:
            try:
                bstack1lll1l1lll1_opy_ = [signal.SIGINT, signal.SIGTERM]
                if not bstack11l11111l1_opy_():
                    bstack1lll1l1lll1_opy_.extend([signal.SIGHUP, signal.SIGQUIT])
                for s in bstack1lll1l1lll1_opy_:
                    signal.signal(s, bstack1lll11l1l11_opy_)
                bstack1lll1l1ll11_opy_ = True
            except Exception as e:
                logger.debug(
                    bstack1l111l1_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡲࡦࡩ࡬ࡷࡹ࡫ࡲࠡࡵ࡬࡫ࡳࡧ࡬ࠡࡪࡤࡲࡩࡲࡥࡳࡵ࠽ࠤࠧᘱ") + str(e))
        try:
            item.config.hook.pytest_selenium_runtest_makereport = bstack1llllll1l11_opy_
        except Exception as err:
            threading.current_thread().testStatus = bstack1l111l1_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬᘲ")
    try:
        if not bstack1l1111l1l_opy_.on():
            return
        bstack1l11111l11_opy_.start()
        uuid = uuid4().__str__()
        bstack11lll1llll_opy_ = {
            bstack1l111l1_opy_ (u"࠭ࡵࡶ࡫ࡧࠫᘳ"): uuid,
            bstack1l111l1_opy_ (u"ࠧࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷࠫᘴ"): datetime.datetime.utcnow().isoformat() + bstack1l111l1_opy_ (u"ࠨ࡜ࠪᘵ"),
            bstack1l111l1_opy_ (u"ࠩࡷࡽࡵ࡫ࠧᘶ"): bstack1l111l1_opy_ (u"ࠪ࡬ࡴࡵ࡫ࠨᘷ"),
            bstack1l111l1_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡷࡽࡵ࡫ࠧᘸ"): bstack1l111l1_opy_ (u"ࠬࡈࡅࡇࡑࡕࡉࡤࡋࡁࡄࡊࠪᘹ"),
            bstack1l111l1_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡳࡧ࡭ࡦࠩᘺ"): bstack1l111l1_opy_ (u"ࠧࡴࡧࡷࡹࡵ࠭ᘻ")
        }
        threading.current_thread().current_hook_uuid = uuid
        threading.current_thread().current_test_item = item
        store[bstack1l111l1_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡷࡩࡸࡺ࡟ࡪࡶࡨࡱࠬᘼ")] = item
        store[bstack1l111l1_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢ࡬ࡴࡵ࡫ࡠࡷࡸ࡭ࡩ࠭ᘽ")] = [uuid]
        if not _1l11l111l1_opy_.get(item.nodeid, None):
            _1l11l111l1_opy_[item.nodeid] = {bstack1l111l1_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡴࠩᘾ"): [], bstack1l111l1_opy_ (u"ࠫ࡫࡯ࡸࡵࡷࡵࡩࡸ࠭ᘿ"): []}
        _1l11l111l1_opy_[item.nodeid][bstack1l111l1_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡶࠫᙀ")].append(bstack11lll1llll_opy_[bstack1l111l1_opy_ (u"࠭ࡵࡶ࡫ࡧࠫᙁ")])
        _1l11l111l1_opy_[item.nodeid + bstack1l111l1_opy_ (u"ࠧ࠮ࡵࡨࡸࡺࡶࠧᙂ")] = bstack11lll1llll_opy_
        bstack1lll1ll11ll_opy_(item, bstack11lll1llll_opy_, bstack1l111l1_opy_ (u"ࠨࡊࡲࡳࡰࡘࡵ࡯ࡕࡷࡥࡷࡺࡥࡥࠩᙃ"))
    except Exception as err:
        print(bstack1l111l1_opy_ (u"ࠩࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡲࡼࡸࡪࡹࡴࡠࡴࡸࡲࡹ࡫ࡳࡵࡡࡶࡩࡹࡻࡰ࠻ࠢࡾࢁࠬᙄ"), str(err))
def pytest_runtest_teardown(item):
    try:
        global bstack1l1lll111_opy_
        if CONFIG.get(bstack1l111l1_opy_ (u"ࠪࡴࡪࡸࡣࡺࠩᙅ"), False):
            if CONFIG.get(bstack1l111l1_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࡆࡥࡵࡺࡵࡳࡧࡐࡳࡩ࡫ࠧᙆ"), bstack1l111l1_opy_ (u"ࠧࡧࡵࡵࡱࠥᙇ")) == bstack1l111l1_opy_ (u"ࠨࡴࡦࡵࡷࡧࡦࡹࡥࠣᙈ"):
                bstack1lll1ll11l1_opy_ = bstack1ll1ll1l1_opy_(threading.current_thread(), bstack1l111l1_opy_ (u"ࠧࡱࡧࡵࡧࡾ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪᙉ"), None)
                bstack1ll111ll_opy_ = bstack1lll1ll11l1_opy_ + bstack1l111l1_opy_ (u"ࠣ࠯ࡷࡩࡸࡺࡣࡢࡵࡨࠦᙊ")
                driver = getattr(item, bstack1l111l1_opy_ (u"ࠩࡢࡨࡷ࡯ࡶࡦࡴࠪᙋ"), None)
                PercySDK.screenshot(driver, bstack1ll111ll_opy_)
        if getattr(item, bstack1l111l1_opy_ (u"ࠪࡣࡦ࠷࠱ࡺࡡࡶࡸࡦࡸࡴࡦࡦࠪᙌ"), False):
            bstack11llll11l_opy_.bstack1111l1ll1_opy_(getattr(item, bstack1l111l1_opy_ (u"ࠫࡤࡪࡲࡪࡸࡨࡶࠬᙍ"), None), bstack1l1lll111_opy_, logger, item)
        if not bstack1l1111l1l_opy_.on():
            return
        bstack11lll1llll_opy_ = {
            bstack1l111l1_opy_ (u"ࠬࡻࡵࡪࡦࠪᙎ"): uuid4().__str__(),
            bstack1l111l1_opy_ (u"࠭ࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠪᙏ"): datetime.datetime.utcnow().isoformat() + bstack1l111l1_opy_ (u"࡛ࠧࠩᙐ"),
            bstack1l111l1_opy_ (u"ࠨࡶࡼࡴࡪ࠭ᙑ"): bstack1l111l1_opy_ (u"ࠩ࡫ࡳࡴࡱࠧᙒ"),
            bstack1l111l1_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡶࡼࡴࡪ࠭ᙓ"): bstack1l111l1_opy_ (u"ࠫࡆࡌࡔࡆࡔࡢࡉࡆࡉࡈࠨᙔ"),
            bstack1l111l1_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡲࡦࡳࡥࠨᙕ"): bstack1l111l1_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࠨᙖ")
        }
        _1l11l111l1_opy_[item.nodeid + bstack1l111l1_opy_ (u"ࠧ࠮ࡶࡨࡥࡷࡪ࡯ࡸࡰࠪᙗ")] = bstack11lll1llll_opy_
        bstack1lll1ll11ll_opy_(item, bstack11lll1llll_opy_, bstack1l111l1_opy_ (u"ࠨࡊࡲࡳࡰࡘࡵ࡯ࡕࡷࡥࡷࡺࡥࡥࠩᙘ"))
    except Exception as err:
        print(bstack1l111l1_opy_ (u"ࠩࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡲࡼࡸࡪࡹࡴࡠࡴࡸࡲࡹ࡫ࡳࡵࡡࡷࡩࡦࡸࡤࡰࡹࡱ࠾ࠥࢁࡽࠨᙙ"), str(err))
@pytest.hookimpl(hookwrapper=True)
def pytest_fixture_setup(fixturedef, request):
    if not bstack1l1111l1l_opy_.on():
        yield
        return
    start_time = datetime.datetime.now()
    if bstack1llllll11ll_opy_(fixturedef.argname):
        store[bstack1l111l1_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡲࡵࡤࡶ࡮ࡨࡣ࡮ࡺࡥ࡮ࠩᙚ")] = request.node
    elif bstack1llllll111l_opy_(fixturedef.argname):
        store[bstack1l111l1_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡩ࡬ࡢࡵࡶࡣ࡮ࡺࡥ࡮ࠩᙛ")] = request.node
    outcome = yield
    try:
        fixture = {
            bstack1l111l1_opy_ (u"ࠬࡴࡡ࡮ࡧࠪᙜ"): fixturedef.argname,
            bstack1l111l1_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭ᙝ"): bstack11l11l1ll1_opy_(outcome),
            bstack1l111l1_opy_ (u"ࠧࡥࡷࡵࡥࡹ࡯࡯࡯ࠩᙞ"): (datetime.datetime.now() - start_time).total_seconds() * 1000
        }
        current_test_item = store[bstack1l111l1_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡷࡩࡸࡺ࡟ࡪࡶࡨࡱࠬᙟ")]
        if not _1l11l111l1_opy_.get(current_test_item.nodeid, None):
            _1l11l111l1_opy_[current_test_item.nodeid] = {bstack1l111l1_opy_ (u"ࠩࡩ࡭ࡽࡺࡵࡳࡧࡶࠫᙠ"): []}
        _1l11l111l1_opy_[current_test_item.nodeid][bstack1l111l1_opy_ (u"ࠪࡪ࡮ࡾࡴࡶࡴࡨࡷࠬᙡ")].append(fixture)
    except Exception as err:
        logger.debug(bstack1l111l1_opy_ (u"ࠫࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡴࡾࡺࡥࡴࡶࡢࡪ࡮ࡾࡴࡶࡴࡨࡣࡸ࡫ࡴࡶࡲ࠽ࠤࢀࢃࠧᙢ"), str(err))
if bstack1lll11l1l_opy_() and bstack1l1111l1l_opy_.on():
    def pytest_bdd_before_step(request, step):
        try:
            _1l11l111l1_opy_[request.node.nodeid][bstack1l111l1_opy_ (u"ࠬࡺࡥࡴࡶࡢࡨࡦࡺࡡࠨᙣ")].bstack1llll1l11ll_opy_(id(step))
        except Exception as err:
            print(bstack1l111l1_opy_ (u"࠭ࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡶࡹࡵࡧࡶࡸࡤࡨࡤࡥࡡࡥࡩ࡫ࡵࡲࡦࡡࡶࡸࡪࡶ࠺ࠡࡽࢀࠫᙤ"), str(err))
    def pytest_bdd_step_error(request, step, exception):
        try:
            _1l11l111l1_opy_[request.node.nodeid][bstack1l111l1_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣࠪᙥ")].bstack1l11111l1l_opy_(id(step), Result.failed(exception=exception))
        except Exception as err:
            print(bstack1l111l1_opy_ (u"ࠨࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡱࡻࡷࡩࡸࡺ࡟ࡣࡦࡧࡣࡸࡺࡥࡱࡡࡨࡶࡷࡵࡲ࠻ࠢࡾࢁࠬᙦ"), str(err))
    def pytest_bdd_after_step(request, step):
        try:
            bstack11llll1lll_opy_: bstack1l111l1l11_opy_ = _1l11l111l1_opy_[request.node.nodeid][bstack1l111l1_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡥࡣࡷࡥࠬᙧ")]
            bstack11llll1lll_opy_.bstack1l11111l1l_opy_(id(step), Result.passed())
        except Exception as err:
            print(bstack1l111l1_opy_ (u"ࠪࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡳࡽࡹ࡫ࡳࡵࡡࡥࡨࡩࡥࡳࡵࡧࡳࡣࡪࡸࡲࡰࡴ࠽ࠤࢀࢃࠧᙨ"), str(err))
    def pytest_bdd_before_scenario(request, feature, scenario):
        global bstack1lll11ll1ll_opy_
        try:
            if not bstack1l1111l1l_opy_.on() or bstack1lll11ll1ll_opy_ != bstack1l111l1_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷ࠱ࡧࡪࡤࠨᙩ"):
                return
            global bstack1l11111l11_opy_
            bstack1l11111l11_opy_.start()
            if not _1l11l111l1_opy_.get(request.node.nodeid, None):
                _1l11l111l1_opy_[request.node.nodeid] = {}
            bstack11llll1lll_opy_ = bstack1l111l1l11_opy_.bstack1llll1ll111_opy_(
                scenario, feature, request.node,
                name=bstack1llllll11l1_opy_(request.node, scenario),
                bstack11lllll1ll_opy_=bstack1lll11llll_opy_(),
                file_path=feature.filename,
                scope=[feature.name],
                framework=bstack1l111l1_opy_ (u"ࠬࡖࡹࡵࡧࡶࡸ࠲ࡩࡵࡤࡷࡰࡦࡪࡸࠧᙪ"),
                tags=bstack1lllllll11l_opy_(feature, scenario)
            )
            _1l11l111l1_opy_[request.node.nodeid][bstack1l111l1_opy_ (u"࠭ࡴࡦࡵࡷࡣࡩࡧࡴࡢࠩᙫ")] = bstack11llll1lll_opy_
            bstack1lll1l11l11_opy_(bstack11llll1lll_opy_.uuid)
            bstack1l1111l1l_opy_.bstack1l1111l111_opy_(bstack1l111l1_opy_ (u"ࠧࡕࡧࡶࡸࡗࡻ࡮ࡔࡶࡤࡶࡹ࡫ࡤࠨᙬ"), bstack11llll1lll_opy_)
        except Exception as err:
            print(bstack1l111l1_opy_ (u"ࠨࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡱࡻࡷࡩࡸࡺ࡟ࡣࡦࡧࡣࡧ࡫ࡦࡰࡴࡨࡣࡸࡩࡥ࡯ࡣࡵ࡭ࡴࡀࠠࡼࡿࠪ᙭"), str(err))
def bstack1lll1l11lll_opy_(bstack1lll11l1l1l_opy_):
    if bstack1lll11l1l1l_opy_ in store[bstack1l111l1_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢ࡬ࡴࡵ࡫ࡠࡷࡸ࡭ࡩ࠭᙮")]:
        store[bstack1l111l1_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣ࡭ࡵ࡯࡬ࡡࡸࡹ࡮ࡪࠧᙯ")].remove(bstack1lll11l1l1l_opy_)
def bstack1lll1l11l11_opy_(bstack1lll11ll111_opy_):
    store[bstack1l111l1_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢࡹࡺ࡯ࡤࠨᙰ")] = bstack1lll11ll111_opy_
    threading.current_thread().current_test_uuid = bstack1lll11ll111_opy_
@bstack1l1111l1l_opy_.bstack1llll1111l1_opy_
def bstack1lll1l1l1l1_opy_(item, call, report):
    global bstack1lll11ll1ll_opy_
    bstack1l11ll111l_opy_ = bstack1lll11llll_opy_()
    if hasattr(report, bstack1l111l1_opy_ (u"ࠬࡹࡴࡰࡲࠪᙱ")):
        bstack1l11ll111l_opy_ = bstack11l11l1l1l_opy_(report.stop)
    if hasattr(report, bstack1l111l1_opy_ (u"࠭ࡳࡵࡣࡵࡸࠬᙲ")):
        bstack1l11ll111l_opy_ = bstack11l11l1l1l_opy_(report.start)
    try:
        if getattr(report, bstack1l111l1_opy_ (u"ࠧࡸࡪࡨࡲࠬᙳ"), bstack1l111l1_opy_ (u"ࠨࠩᙴ")) == bstack1l111l1_opy_ (u"ࠩࡦࡥࡱࡲࠧᙵ"):
            bstack1l11111l11_opy_.reset()
        if getattr(report, bstack1l111l1_opy_ (u"ࠪࡻ࡭࡫࡮ࠨᙶ"), bstack1l111l1_opy_ (u"ࠫࠬᙷ")) == bstack1l111l1_opy_ (u"ࠬࡩࡡ࡭࡮ࠪᙸ"):
            if bstack1lll11ll1ll_opy_ == bstack1l111l1_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭ᙹ"):
                _1l11l111l1_opy_[item.nodeid][bstack1l111l1_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬᙺ")] = bstack1l11ll111l_opy_
                bstack1lll11l11ll_opy_(item, _1l11l111l1_opy_[item.nodeid], bstack1l111l1_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡈ࡬ࡲ࡮ࡹࡨࡦࡦࠪᙻ"), report, call)
                store[bstack1l111l1_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡸࡪࡹࡴࡠࡷࡸ࡭ࡩ࠭ᙼ")] = None
            elif bstack1lll11ll1ll_opy_ == bstack1l111l1_opy_ (u"ࠥࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠢᙽ"):
                bstack11llll1lll_opy_ = _1l11l111l1_opy_[item.nodeid][bstack1l111l1_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡧࡥࡹࡧࠧᙾ")]
                bstack11llll1lll_opy_.set(hooks=_1l11l111l1_opy_[item.nodeid].get(bstack1l111l1_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡶࠫᙿ"), []))
                exception, bstack11lll1ll1l_opy_ = None, None
                if call.excinfo:
                    exception = call.excinfo.value
                    bstack11lll1ll1l_opy_ = [call.excinfo.exconly(), getattr(report, bstack1l111l1_opy_ (u"࠭࡬ࡰࡰࡪࡶࡪࡶࡲࡵࡧࡻࡸࠬ "), bstack1l111l1_opy_ (u"ࠧࠨᚁ"))]
                bstack11llll1lll_opy_.stop(time=bstack1l11ll111l_opy_, result=Result(result=getattr(report, bstack1l111l1_opy_ (u"ࠨࡱࡸࡸࡨࡵ࡭ࡦࠩᚂ"), bstack1l111l1_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩᚃ")), exception=exception, bstack11lll1ll1l_opy_=bstack11lll1ll1l_opy_))
                bstack1l1111l1l_opy_.bstack1l1111l111_opy_(bstack1l111l1_opy_ (u"ࠪࡘࡪࡹࡴࡓࡷࡱࡊ࡮ࡴࡩࡴࡪࡨࡨࠬᚄ"), _1l11l111l1_opy_[item.nodeid][bstack1l111l1_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡧࡥࡹࡧࠧᚅ")])
        elif getattr(report, bstack1l111l1_opy_ (u"ࠬࡽࡨࡦࡰࠪᚆ"), bstack1l111l1_opy_ (u"࠭ࠧᚇ")) in [bstack1l111l1_opy_ (u"ࠧࡴࡧࡷࡹࡵ࠭ᚈ"), bstack1l111l1_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰࠪᚉ")]:
            bstack11lllllll1_opy_ = item.nodeid + bstack1l111l1_opy_ (u"ࠩ࠰ࠫᚊ") + getattr(report, bstack1l111l1_opy_ (u"ࠪࡻ࡭࡫࡮ࠨᚋ"), bstack1l111l1_opy_ (u"ࠫࠬᚌ"))
            if getattr(report, bstack1l111l1_opy_ (u"ࠬࡹ࡫ࡪࡲࡳࡩࡩ࠭ᚍ"), False):
                hook_type = bstack1l111l1_opy_ (u"࠭ࡂࡆࡈࡒࡖࡊࡥࡅࡂࡅࡋࠫᚎ") if getattr(report, bstack1l111l1_opy_ (u"ࠧࡸࡪࡨࡲࠬᚏ"), bstack1l111l1_opy_ (u"ࠨࠩᚐ")) == bstack1l111l1_opy_ (u"ࠩࡶࡩࡹࡻࡰࠨᚑ") else bstack1l111l1_opy_ (u"ࠪࡅࡋ࡚ࡅࡓࡡࡈࡅࡈࡎࠧᚒ")
                _1l11l111l1_opy_[bstack11lllllll1_opy_] = {
                    bstack1l111l1_opy_ (u"ࠫࡺࡻࡩࡥࠩᚓ"): uuid4().__str__(),
                    bstack1l111l1_opy_ (u"ࠬࡹࡴࡢࡴࡷࡩࡩࡥࡡࡵࠩᚔ"): bstack1l11ll111l_opy_,
                    bstack1l111l1_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡹࡿࡰࡦࠩᚕ"): hook_type
                }
            _1l11l111l1_opy_[bstack11lllllll1_opy_][bstack1l111l1_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬᚖ")] = bstack1l11ll111l_opy_
            bstack1lll1l11lll_opy_(_1l11l111l1_opy_[bstack11lllllll1_opy_][bstack1l111l1_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭ᚗ")])
            bstack1lll1ll11ll_opy_(item, _1l11l111l1_opy_[bstack11lllllll1_opy_], bstack1l111l1_opy_ (u"ࠩࡋࡳࡴࡱࡒࡶࡰࡉ࡭ࡳ࡯ࡳࡩࡧࡧࠫᚘ"), report, call)
            if getattr(report, bstack1l111l1_opy_ (u"ࠪࡻ࡭࡫࡮ࠨᚙ"), bstack1l111l1_opy_ (u"ࠫࠬᚚ")) == bstack1l111l1_opy_ (u"ࠬࡹࡥࡵࡷࡳࠫ᚛"):
                if getattr(report, bstack1l111l1_opy_ (u"࠭࡯ࡶࡶࡦࡳࡲ࡫ࠧ᚜"), bstack1l111l1_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧ᚝")) == bstack1l111l1_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨ᚞"):
                    bstack11lll1llll_opy_ = {
                        bstack1l111l1_opy_ (u"ࠩࡸࡹ࡮ࡪࠧ᚟"): uuid4().__str__(),
                        bstack1l111l1_opy_ (u"ࠪࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠧᚠ"): bstack1lll11llll_opy_(),
                        bstack1l111l1_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩᚡ"): bstack1lll11llll_opy_()
                    }
                    _1l11l111l1_opy_[item.nodeid] = {**_1l11l111l1_opy_[item.nodeid], **bstack11lll1llll_opy_}
                    bstack1lll11l11ll_opy_(item, _1l11l111l1_opy_[item.nodeid], bstack1l111l1_opy_ (u"࡚ࠬࡥࡴࡶࡕࡹࡳ࡙ࡴࡢࡴࡷࡩࡩ࠭ᚢ"))
                    bstack1lll11l11ll_opy_(item, _1l11l111l1_opy_[item.nodeid], bstack1l111l1_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡆࡪࡰ࡬ࡷ࡭࡫ࡤࠨᚣ"), report, call)
    except Exception as err:
        print(bstack1l111l1_opy_ (u"ࠧࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡨࡢࡰࡧࡰࡪࡥ࡯࠲࠳ࡼࡣࡹ࡫ࡳࡵࡡࡨࡺࡪࡴࡴ࠻ࠢࡾࢁࠬᚤ"), str(err))
def bstack1lll11lll11_opy_(test, bstack11lll1llll_opy_, result=None, call=None, bstack1lll1ll1l1_opy_=None, outcome=None):
    file_path = os.path.relpath(test.fspath.strpath, start=os.getcwd())
    bstack11llll1lll_opy_ = {
        bstack1l111l1_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭ᚥ"): bstack11lll1llll_opy_[bstack1l111l1_opy_ (u"ࠩࡸࡹ࡮ࡪࠧᚦ")],
        bstack1l111l1_opy_ (u"ࠪࡸࡾࡶࡥࠨᚧ"): bstack1l111l1_opy_ (u"ࠫࡹ࡫ࡳࡵࠩᚨ"),
        bstack1l111l1_opy_ (u"ࠬࡴࡡ࡮ࡧࠪᚩ"): test.name,
        bstack1l111l1_opy_ (u"࠭ࡢࡰࡦࡼࠫᚪ"): {
            bstack1l111l1_opy_ (u"ࠧ࡭ࡣࡱ࡫ࠬᚫ"): bstack1l111l1_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮ࠨᚬ"),
            bstack1l111l1_opy_ (u"ࠩࡦࡳࡩ࡫ࠧᚭ"): inspect.getsource(test.obj)
        },
        bstack1l111l1_opy_ (u"ࠪ࡭ࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧᚮ"): test.name,
        bstack1l111l1_opy_ (u"ࠫࡸࡩ࡯ࡱࡧࠪᚯ"): test.name,
        bstack1l111l1_opy_ (u"ࠬࡹࡣࡰࡲࡨࡷࠬᚰ"): bstack1l1111l1l_opy_.bstack11lll1l111_opy_(test),
        bstack1l111l1_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩᚱ"): file_path,
        bstack1l111l1_opy_ (u"ࠧ࡭ࡱࡦࡥࡹ࡯࡯࡯ࠩᚲ"): file_path,
        bstack1l111l1_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨᚳ"): bstack1l111l1_opy_ (u"ࠩࡳࡩࡳࡪࡩ࡯ࡩࠪᚴ"),
        bstack1l111l1_opy_ (u"ࠪࡺࡨࡥࡦࡪ࡮ࡨࡴࡦࡺࡨࠨᚵ"): file_path,
        bstack1l111l1_opy_ (u"ࠫࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠨᚶ"): bstack11lll1llll_opy_[bstack1l111l1_opy_ (u"ࠬࡹࡴࡢࡴࡷࡩࡩࡥࡡࡵࠩᚷ")],
        bstack1l111l1_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠩᚸ"): bstack1l111l1_opy_ (u"ࠧࡑࡻࡷࡩࡸࡺࠧᚹ"),
        bstack1l111l1_opy_ (u"ࠨࡥࡸࡷࡹࡵ࡭ࡓࡧࡵࡹࡳࡖࡡࡳࡣࡰࠫᚺ"): {
            bstack1l111l1_opy_ (u"ࠩࡵࡩࡷࡻ࡮ࡠࡰࡤࡱࡪ࠭ᚻ"): test.nodeid
        },
        bstack1l111l1_opy_ (u"ࠪࡸࡦ࡭ࡳࠨᚼ"): bstack11l11l111l_opy_(test.own_markers)
    }
    if bstack1lll1ll1l1_opy_ in [bstack1l111l1_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡘࡱࡩࡱࡲࡨࡨࠬᚽ"), bstack1l111l1_opy_ (u"࡚ࠬࡥࡴࡶࡕࡹࡳࡌࡩ࡯࡫ࡶ࡬ࡪࡪࠧᚾ")]:
        bstack11llll1lll_opy_[bstack1l111l1_opy_ (u"࠭࡭ࡦࡶࡤࠫᚿ")] = {
            bstack1l111l1_opy_ (u"ࠧࡧ࡫ࡻࡸࡺࡸࡥࡴࠩᛀ"): bstack11lll1llll_opy_.get(bstack1l111l1_opy_ (u"ࠨࡨ࡬ࡼࡹࡻࡲࡦࡵࠪᛁ"), [])
        }
    if bstack1lll1ll1l1_opy_ == bstack1l111l1_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡖ࡯࡮ࡶࡰࡦࡦࠪᛂ"):
        bstack11llll1lll_opy_[bstack1l111l1_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪᛃ")] = bstack1l111l1_opy_ (u"ࠫࡸࡱࡩࡱࡲࡨࡨࠬᛄ")
        bstack11llll1lll_opy_[bstack1l111l1_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡶࠫᛅ")] = bstack11lll1llll_opy_[bstack1l111l1_opy_ (u"࠭ࡨࡰࡱ࡮ࡷࠬᛆ")]
        bstack11llll1lll_opy_[bstack1l111l1_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬᛇ")] = bstack11lll1llll_opy_[bstack1l111l1_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭ᛈ")]
    if result:
        bstack11llll1lll_opy_[bstack1l111l1_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩᛉ")] = result.outcome
        bstack11llll1lll_opy_[bstack1l111l1_opy_ (u"ࠪࡨࡺࡸࡡࡵ࡫ࡲࡲࡤ࡯࡮ࡠ࡯ࡶࠫᛊ")] = result.duration * 1000
        bstack11llll1lll_opy_[bstack1l111l1_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩᛋ")] = bstack11lll1llll_opy_[bstack1l111l1_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪᛌ")]
        if result.failed:
            bstack11llll1lll_opy_[bstack1l111l1_opy_ (u"࠭ࡦࡢ࡫࡯ࡹࡷ࡫࡟ࡵࡻࡳࡩࠬᛍ")] = bstack1l1111l1l_opy_.bstack11ll1l1l11_opy_(call.excinfo.typename)
            bstack11llll1lll_opy_[bstack1l111l1_opy_ (u"ࠧࡧࡣ࡬ࡰࡺࡸࡥࠨᛎ")] = bstack1l1111l1l_opy_.bstack1llll111111_opy_(call.excinfo, result)
        bstack11llll1lll_opy_[bstack1l111l1_opy_ (u"ࠨࡪࡲࡳࡰࡹࠧᛏ")] = bstack11lll1llll_opy_[bstack1l111l1_opy_ (u"ࠩ࡫ࡳࡴࡱࡳࠨᛐ")]
    if outcome:
        bstack11llll1lll_opy_[bstack1l111l1_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪᛑ")] = bstack11l11l1ll1_opy_(outcome)
        bstack11llll1lll_opy_[bstack1l111l1_opy_ (u"ࠫࡩࡻࡲࡢࡶ࡬ࡳࡳࡥࡩ࡯ࡡࡰࡷࠬᛒ")] = 0
        bstack11llll1lll_opy_[bstack1l111l1_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪᛓ")] = bstack11lll1llll_opy_[bstack1l111l1_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫᛔ")]
        if bstack11llll1lll_opy_[bstack1l111l1_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧᛕ")] == bstack1l111l1_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨᛖ"):
            bstack11llll1lll_opy_[bstack1l111l1_opy_ (u"ࠩࡩࡥ࡮ࡲࡵࡳࡧࡢࡸࡾࡶࡥࠨᛗ")] = bstack1l111l1_opy_ (u"࡙ࠪࡳ࡮ࡡ࡯ࡦ࡯ࡩࡩࡋࡲࡳࡱࡵࠫᛘ")  # bstack1lll11ll1l1_opy_
            bstack11llll1lll_opy_[bstack1l111l1_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡷࡵࡩࠬᛙ")] = [{bstack1l111l1_opy_ (u"ࠬࡨࡡࡤ࡭ࡷࡶࡦࡩࡥࠨᛚ"): [bstack1l111l1_opy_ (u"࠭ࡳࡰ࡯ࡨࠤࡪࡸࡲࡰࡴࠪᛛ")]}]
        bstack11llll1lll_opy_[bstack1l111l1_opy_ (u"ࠧࡩࡱࡲ࡯ࡸ࠭ᛜ")] = bstack11lll1llll_opy_[bstack1l111l1_opy_ (u"ࠨࡪࡲࡳࡰࡹࠧᛝ")]
    return bstack11llll1lll_opy_
def bstack1lll1l11ll1_opy_(test, bstack11lllll111_opy_, bstack1lll1ll1l1_opy_, result, call, outcome, bstack1lll1l1111l_opy_):
    file_path = os.path.relpath(test.fspath.strpath, start=os.getcwd())
    hook_type = bstack11lllll111_opy_[bstack1l111l1_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡵࡻࡳࡩࠬᛞ")]
    hook_name = bstack11lllll111_opy_[bstack1l111l1_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡰࡤࡱࡪ࠭ᛟ")]
    hook_data = {
        bstack1l111l1_opy_ (u"ࠫࡺࡻࡩࡥࠩᛠ"): bstack11lllll111_opy_[bstack1l111l1_opy_ (u"ࠬࡻࡵࡪࡦࠪᛡ")],
        bstack1l111l1_opy_ (u"࠭ࡴࡺࡲࡨࠫᛢ"): bstack1l111l1_opy_ (u"ࠧࡩࡱࡲ࡯ࠬᛣ"),
        bstack1l111l1_opy_ (u"ࠨࡰࡤࡱࡪ࠭ᛤ"): bstack1l111l1_opy_ (u"ࠩࡾࢁࠬᛥ").format(bstack1llllll1l1l_opy_(hook_name)),
        bstack1l111l1_opy_ (u"ࠪࡦࡴࡪࡹࠨᛦ"): {
            bstack1l111l1_opy_ (u"ࠫࡱࡧ࡮ࡨࠩᛧ"): bstack1l111l1_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲࠬᛨ"),
            bstack1l111l1_opy_ (u"࠭ࡣࡰࡦࡨࠫᛩ"): None
        },
        bstack1l111l1_opy_ (u"ࠧࡴࡥࡲࡴࡪ࠭ᛪ"): test.name,
        bstack1l111l1_opy_ (u"ࠨࡵࡦࡳࡵ࡫ࡳࠨ᛫"): bstack1l1111l1l_opy_.bstack11lll1l111_opy_(test, hook_name),
        bstack1l111l1_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬ᛬"): file_path,
        bstack1l111l1_opy_ (u"ࠪࡰࡴࡩࡡࡵ࡫ࡲࡲࠬ᛭"): file_path,
        bstack1l111l1_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫᛮ"): bstack1l111l1_opy_ (u"ࠬࡶࡥ࡯ࡦ࡬ࡲ࡬࠭ᛯ"),
        bstack1l111l1_opy_ (u"࠭ࡶࡤࡡࡩ࡭ࡱ࡫ࡰࡢࡶ࡫ࠫᛰ"): file_path,
        bstack1l111l1_opy_ (u"ࠧࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷࠫᛱ"): bstack11lllll111_opy_[bstack1l111l1_opy_ (u"ࠨࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠬᛲ")],
        bstack1l111l1_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠬᛳ"): bstack1l111l1_opy_ (u"ࠪࡔࡾࡺࡥࡴࡶ࠰ࡧࡺࡩࡵ࡮ࡤࡨࡶࠬᛴ") if bstack1lll11ll1ll_opy_ == bstack1l111l1_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷ࠱ࡧࡪࡤࠨᛵ") else bstack1l111l1_opy_ (u"ࠬࡖࡹࡵࡧࡶࡸࠬᛶ"),
        bstack1l111l1_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡹࡿࡰࡦࠩᛷ"): hook_type
    }
    bstack1lll1l1l1ll_opy_ = bstack1l11111lll_opy_(_1l11l111l1_opy_.get(test.nodeid, None))
    if bstack1lll1l1l1ll_opy_:
        hook_data[bstack1l111l1_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡ࡬ࡨࠬᛸ")] = bstack1lll1l1l1ll_opy_
    if result:
        hook_data[bstack1l111l1_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨ᛹")] = result.outcome
        hook_data[bstack1l111l1_opy_ (u"ࠩࡧࡹࡷࡧࡴࡪࡱࡱࡣ࡮ࡴ࡟࡮ࡵࠪ᛺")] = result.duration * 1000
        hook_data[bstack1l111l1_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨ᛻")] = bstack11lllll111_opy_[bstack1l111l1_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩ᛼")]
        if result.failed:
            hook_data[bstack1l111l1_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡸࡶࡪࡥࡴࡺࡲࡨࠫ᛽")] = bstack1l1111l1l_opy_.bstack11ll1l1l11_opy_(call.excinfo.typename)
            hook_data[bstack1l111l1_opy_ (u"࠭ࡦࡢ࡫࡯ࡹࡷ࡫ࠧ᛾")] = bstack1l1111l1l_opy_.bstack1llll111111_opy_(call.excinfo, result)
    if outcome:
        hook_data[bstack1l111l1_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧ᛿")] = bstack11l11l1ll1_opy_(outcome)
        hook_data[bstack1l111l1_opy_ (u"ࠨࡦࡸࡶࡦࡺࡩࡰࡰࡢ࡭ࡳࡥ࡭ࡴࠩᜀ")] = 100
        hook_data[bstack1l111l1_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧᜁ")] = bstack11lllll111_opy_[bstack1l111l1_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨᜂ")]
        if hook_data[bstack1l111l1_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫᜃ")] == bstack1l111l1_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬᜄ"):
            hook_data[bstack1l111l1_opy_ (u"࠭ࡦࡢ࡫࡯ࡹࡷ࡫࡟ࡵࡻࡳࡩࠬᜅ")] = bstack1l111l1_opy_ (u"ࠧࡖࡰ࡫ࡥࡳࡪ࡬ࡦࡦࡈࡶࡷࡵࡲࠨᜆ")  # bstack1lll11ll1l1_opy_
            hook_data[bstack1l111l1_opy_ (u"ࠨࡨࡤ࡭ࡱࡻࡲࡦࠩᜇ")] = [{bstack1l111l1_opy_ (u"ࠩࡥࡥࡨࡱࡴࡳࡣࡦࡩࠬᜈ"): [bstack1l111l1_opy_ (u"ࠪࡷࡴࡳࡥࠡࡧࡵࡶࡴࡸࠧᜉ")]}]
    if bstack1lll1l1111l_opy_:
        hook_data[bstack1l111l1_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫᜊ")] = bstack1lll1l1111l_opy_.result
        hook_data[bstack1l111l1_opy_ (u"ࠬࡪࡵࡳࡣࡷ࡭ࡴࡴ࡟ࡪࡰࡢࡱࡸ࠭ᜋ")] = bstack11l1111ll1_opy_(bstack11lllll111_opy_[bstack1l111l1_opy_ (u"࠭ࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠪᜌ")], bstack11lllll111_opy_[bstack1l111l1_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬᜍ")])
        hook_data[bstack1l111l1_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭ᜎ")] = bstack11lllll111_opy_[bstack1l111l1_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧᜏ")]
        if hook_data[bstack1l111l1_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪᜐ")] == bstack1l111l1_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫᜑ"):
            hook_data[bstack1l111l1_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡸࡶࡪࡥࡴࡺࡲࡨࠫᜒ")] = bstack1l1111l1l_opy_.bstack11ll1l1l11_opy_(bstack1lll1l1111l_opy_.exception_type)
            hook_data[bstack1l111l1_opy_ (u"࠭ࡦࡢ࡫࡯ࡹࡷ࡫ࠧᜓ")] = [{bstack1l111l1_opy_ (u"ࠧࡣࡣࡦ࡯ࡹࡸࡡࡤࡧ᜔ࠪ"): bstack11l11l11ll_opy_(bstack1lll1l1111l_opy_.exception)}]
    return hook_data
def bstack1lll11l11ll_opy_(test, bstack11lll1llll_opy_, bstack1lll1ll1l1_opy_, result=None, call=None, outcome=None):
    bstack11llll1lll_opy_ = bstack1lll11lll11_opy_(test, bstack11lll1llll_opy_, result, call, bstack1lll1ll1l1_opy_, outcome)
    driver = getattr(test, bstack1l111l1_opy_ (u"ࠨࡡࡧࡶ࡮ࡼࡥࡳ᜕ࠩ"), None)
    if bstack1lll1ll1l1_opy_ == bstack1l111l1_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡖࡸࡦࡸࡴࡦࡦࠪ᜖") and driver:
        bstack11llll1lll_opy_[bstack1l111l1_opy_ (u"ࠪ࡭ࡳࡺࡥࡨࡴࡤࡸ࡮ࡵ࡮ࡴࠩ᜗")] = bstack1l1111l1l_opy_.bstack1l111lll1l_opy_(driver)
    if bstack1lll1ll1l1_opy_ == bstack1l111l1_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡘࡱࡩࡱࡲࡨࡨࠬ᜘"):
        bstack1lll1ll1l1_opy_ = bstack1l111l1_opy_ (u"࡚ࠬࡥࡴࡶࡕࡹࡳࡌࡩ࡯࡫ࡶ࡬ࡪࡪࠧ᜙")
    bstack1l1111ll11_opy_ = {
        bstack1l111l1_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡺࡹࡱࡧࠪ᜚"): bstack1lll1ll1l1_opy_,
        bstack1l111l1_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࠩ᜛"): bstack11llll1lll_opy_
    }
    bstack1l1111l1l_opy_.bstack11llll1l1l_opy_(bstack1l1111ll11_opy_)
def bstack1lll1ll11ll_opy_(test, bstack11lll1llll_opy_, bstack1lll1ll1l1_opy_, result=None, call=None, outcome=None, bstack1lll1l1111l_opy_=None):
    hook_data = bstack1lll1l11ll1_opy_(test, bstack11lll1llll_opy_, bstack1lll1ll1l1_opy_, result, call, outcome, bstack1lll1l1111l_opy_)
    bstack1l1111ll11_opy_ = {
        bstack1l111l1_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡵࡻࡳࡩࠬ᜜"): bstack1lll1ll1l1_opy_,
        bstack1l111l1_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡳࡷࡱࠫ᜝"): hook_data
    }
    bstack1l1111l1l_opy_.bstack11llll1l1l_opy_(bstack1l1111ll11_opy_)
def bstack1l11111lll_opy_(bstack11lll1llll_opy_):
    if not bstack11lll1llll_opy_:
        return None
    if bstack11lll1llll_opy_.get(bstack1l111l1_opy_ (u"ࠪࡸࡪࡹࡴࡠࡦࡤࡸࡦ࠭᜞"), None):
        return getattr(bstack11lll1llll_opy_[bstack1l111l1_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡧࡥࡹࡧࠧᜟ")], bstack1l111l1_opy_ (u"ࠬࡻࡵࡪࡦࠪᜠ"), None)
    return bstack11lll1llll_opy_.get(bstack1l111l1_opy_ (u"࠭ࡵࡶ࡫ࡧࠫᜡ"), None)
@pytest.fixture(autouse=True)
def second_fixture(caplog, request):
    yield
    try:
        if not bstack1l1111l1l_opy_.on():
            return
        places = [bstack1l111l1_opy_ (u"ࠧࡴࡧࡷࡹࡵ࠭ᜢ"), bstack1l111l1_opy_ (u"ࠨࡥࡤࡰࡱ࠭ᜣ"), bstack1l111l1_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࠫᜤ")]
        bstack11llll1111_opy_ = []
        for bstack1lll1l1l111_opy_ in places:
            records = caplog.get_records(bstack1lll1l1l111_opy_)
            bstack1lll1l11l1l_opy_ = bstack1l111l1_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪᜥ") if bstack1lll1l1l111_opy_ == bstack1l111l1_opy_ (u"ࠫࡨࡧ࡬࡭ࠩᜦ") else bstack1l111l1_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬᜧ")
            bstack1lll11ll11l_opy_ = request.node.nodeid + (bstack1l111l1_opy_ (u"࠭ࠧᜨ") if bstack1lll1l1l111_opy_ == bstack1l111l1_opy_ (u"ࠧࡤࡣ࡯ࡰࠬᜩ") else bstack1l111l1_opy_ (u"ࠨ࠯ࠪᜪ") + bstack1lll1l1l111_opy_)
            bstack1lll11ll111_opy_ = bstack1l11111lll_opy_(_1l11l111l1_opy_.get(bstack1lll11ll11l_opy_, None))
            if not bstack1lll11ll111_opy_:
                continue
            for record in records:
                if bstack11l111ll11_opy_(record.message):
                    continue
                bstack11llll1111_opy_.append({
                    bstack1l111l1_opy_ (u"ࠩࡷ࡭ࡲ࡫ࡳࡵࡣࡰࡴࠬᜫ"): datetime.datetime.utcfromtimestamp(record.created).isoformat() + bstack1l111l1_opy_ (u"ࠪ࡞ࠬᜬ"),
                    bstack1l111l1_opy_ (u"ࠫࡱ࡫ࡶࡦ࡮ࠪᜭ"): record.levelname,
                    bstack1l111l1_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭ᜮ"): record.message,
                    bstack1lll1l11l1l_opy_: bstack1lll11ll111_opy_
                })
        if len(bstack11llll1111_opy_) > 0:
            bstack1l1111l1l_opy_.bstack1lll1ll111_opy_(bstack11llll1111_opy_)
    except Exception as err:
        print(bstack1l111l1_opy_ (u"࠭ࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡹࡥࡤࡱࡱࡨࡤ࡬ࡩࡹࡶࡸࡶࡪࡀࠠࡼࡿࠪᜯ"), str(err))
def bstack1ll1ll11_opy_(sequence, driver_command, response=None, driver = None, args = None):
    global bstack1lll1l11l_opy_
    bstack11ll1l1l_opy_ = bstack1ll1ll1l1_opy_(threading.current_thread(), bstack1l111l1_opy_ (u"ࠧࡪࡵࡄ࠵࠶ࡿࡔࡦࡵࡷࠫᜰ"), None) and bstack1ll1ll1l1_opy_(
            threading.current_thread(), bstack1l111l1_opy_ (u"ࠨࡣ࠴࠵ࡾࡖ࡬ࡢࡶࡩࡳࡷࡳࠧᜱ"), None)
    bstack1ll1l1ll1_opy_ = getattr(driver, bstack1l111l1_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡃ࠴࠵ࡾ࡙ࡨࡰࡷ࡯ࡨࡘࡩࡡ࡯ࠩᜲ"), None) != None and getattr(driver, bstack1l111l1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡄ࠵࠶ࡿࡓࡩࡱࡸࡰࡩ࡙ࡣࡢࡰࠪᜳ"), None) == True
    if sequence == bstack1l111l1_opy_ (u"ࠫࡧ࡫ࡦࡰࡴࡨ᜴ࠫ") and driver != None:
      if not bstack1lll1l11l_opy_ and bstack11l11l1111_opy_() and bstack1l111l1_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ᜵") in CONFIG and CONFIG[bstack1l111l1_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭᜶")] == True and bstack1lll1l1l1_opy_.bstack1l1l1ll1ll_opy_(driver_command) and (bstack1ll1l1ll1_opy_ or bstack11ll1l1l_opy_) and not bstack1ll11ll11l_opy_(args):
        try:
          bstack1lll1l11l_opy_ = True
          logger.debug(bstack1l111l1_opy_ (u"ࠧࡑࡧࡵࡪࡴࡸ࡭ࡪࡰࡪࠤࡸࡩࡡ࡯ࠢࡩࡳࡷࠦࡻࡾࠩ᜷").format(driver_command))
          logger.debug(perform_scan(driver, driver_command=driver_command))
        except Exception as err:
          logger.debug(bstack1l111l1_opy_ (u"ࠨࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡵ࡫ࡲࡧࡱࡵࡱࠥࡹࡣࡢࡰࠣࡿࢂ࠭᜸").format(str(err)))
        bstack1lll1l11l_opy_ = False
    if sequence == bstack1l111l1_opy_ (u"ࠩࡤࡪࡹ࡫ࡲࠨ᜹"):
        if driver_command == bstack1l111l1_opy_ (u"ࠪࡷࡨࡸࡥࡦࡰࡶ࡬ࡴࡺࠧ᜺"):
            bstack1l1111l1l_opy_.bstack1ll1l1l1l1_opy_({
                bstack1l111l1_opy_ (u"ࠫ࡮ࡳࡡࡨࡧࠪ᜻"): response[bstack1l111l1_opy_ (u"ࠬࡼࡡ࡭ࡷࡨࠫ᜼")],
                bstack1l111l1_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭᜽"): store[bstack1l111l1_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡵࡶ࡫ࡧࠫ᜾")]
            })
def bstack1l1lll111l_opy_():
    global bstack11lll1l1_opy_
    bstack1ll111l1l1_opy_.bstack11l11l11_opy_()
    logging.shutdown()
    bstack1l1111l1l_opy_.bstack1l1111l11l_opy_()
    for driver in bstack11lll1l1_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
def bstack1lll11l1l11_opy_(*args):
    global bstack11lll1l1_opy_
    bstack1l1111l1l_opy_.bstack1l1111l11l_opy_()
    for driver in bstack11lll1l1_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
def bstack1l1l1l11l1_opy_(self, *args, **kwargs):
    bstack1l111ll1_opy_ = bstack1lllll111_opy_(self, *args, **kwargs)
    bstack1l1111l1l_opy_.bstack11lll111l_opy_(self)
    return bstack1l111ll1_opy_
def bstack1ll111llll_opy_(framework_name):
    global bstack11l1l11ll_opy_
    global bstack1ll1l111l_opy_
    bstack11l1l11ll_opy_ = framework_name
    logger.info(bstack1ll11l1ll1_opy_.format(bstack11l1l11ll_opy_.split(bstack1l111l1_opy_ (u"ࠨ࠯ࠪ᜿"))[0]))
    try:
        from selenium import webdriver
        from selenium.webdriver.common.service import Service
        from selenium.webdriver.remote.webdriver import WebDriver
        if bstack11l11l1111_opy_():
            Service.start = bstack1l11llll1_opy_
            Service.stop = bstack1l1l11ll1_opy_
            webdriver.Remote.__init__ = bstack1111l1111_opy_
            webdriver.Remote.get = bstack1lllll1l1_opy_
            if not isinstance(os.getenv(bstack1l111l1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒ࡜ࡘࡊ࡙ࡔࡠࡒࡄࡖࡆࡒࡌࡆࡎࠪᝀ")), str):
                return
            WebDriver.close = bstack111l1ll1l_opy_
            WebDriver.quit = bstack1ll1l1111_opy_
            WebDriver.getAccessibilityResults = getAccessibilityResults
            WebDriver.get_accessibility_results = getAccessibilityResults
            WebDriver.getAccessibilityResultsSummary = getAccessibilityResultsSummary
            WebDriver.get_accessibility_results_summary = getAccessibilityResultsSummary
            WebDriver.performScan = perform_scan
            WebDriver.perform_scan = perform_scan
        if not bstack11l11l1111_opy_() and bstack1l1111l1l_opy_.on():
            webdriver.Remote.__init__ = bstack1l1l1l11l1_opy_
        bstack1ll1l111l_opy_ = True
    except Exception as e:
        pass
    bstack1lll1ll11_opy_()
    if os.environ.get(bstack1l111l1_opy_ (u"ࠪࡗࡊࡒࡅࡏࡋࡘࡑࡤࡕࡒࡠࡒࡏࡅ࡞࡝ࡒࡊࡉࡋࡘࡤࡏࡎࡔࡖࡄࡐࡑࡋࡄࠨᝁ")):
        bstack1ll1l111l_opy_ = eval(os.environ.get(bstack1l111l1_opy_ (u"ࠫࡘࡋࡌࡆࡐࡌ࡙ࡒࡥࡏࡓࡡࡓࡐࡆ࡟ࡗࡓࡋࡊࡌ࡙ࡥࡉࡏࡕࡗࡅࡑࡒࡅࡅࠩᝂ")))
    if not bstack1ll1l111l_opy_:
        bstack111l11l1l_opy_(bstack1l111l1_opy_ (u"ࠧࡖࡡࡤ࡭ࡤ࡫ࡪࡹࠠ࡯ࡱࡷࠤ࡮ࡴࡳࡵࡣ࡯ࡰࡪࡪࠢᝃ"), bstack1llll11ll_opy_)
    if bstack1l1l1lll1_opy_():
        try:
            from selenium.webdriver.remote.remote_connection import RemoteConnection
            RemoteConnection._get_proxy_url = bstack1l1lll1111_opy_
        except Exception as e:
            logger.error(bstack1l1ll11111_opy_.format(str(e)))
    if bstack1l111l1_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭ᝄ") in str(framework_name).lower():
        if not bstack11l11l1111_opy_():
            return
        try:
            from pytest_selenium import pytest_selenium
            from _pytest.config import Config
            pytest_selenium.pytest_report_header = bstack1lll1l1ll1_opy_
            from pytest_selenium.drivers import browserstack
            browserstack.pytest_selenium_runtest_makereport = bstack1ll11l11l_opy_
            Config.getoption = bstack111l111l_opy_
        except Exception as e:
            pass
        try:
            from pytest_bdd import reporting
            reporting.runtest_makereport = bstack111l11ll_opy_
        except Exception as e:
            pass
def bstack1ll1l1111_opy_(self):
    global bstack11l1l11ll_opy_
    global bstack1lll1ll1_opy_
    global bstack1l11ll1ll_opy_
    try:
        if bstack1l111l1_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧᝅ") in bstack11l1l11ll_opy_ and self.session_id != None and bstack1ll1ll1l1_opy_(threading.current_thread(), bstack1l111l1_opy_ (u"ࠨࡶࡨࡷࡹ࡙ࡴࡢࡶࡸࡷࠬᝆ"), bstack1l111l1_opy_ (u"ࠩࠪᝇ")) != bstack1l111l1_opy_ (u"ࠪࡷࡰ࡯ࡰࡱࡧࡧࠫᝈ"):
            bstack1l1l111lll_opy_ = bstack1l111l1_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫᝉ") if len(threading.current_thread().bstackTestErrorMessages) == 0 else bstack1l111l1_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬᝊ")
            bstack1l1l111l1_opy_(logger, True)
            if self != None:
                bstack11l11111l_opy_(self, bstack1l1l111lll_opy_, bstack1l111l1_opy_ (u"࠭ࠬࠡࠩᝋ").join(threading.current_thread().bstackTestErrorMessages))
        item = store.get(bstack1l111l1_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡩࡵࡧࡰࠫᝌ"), None)
        if item is not None and bstack1lll1l1l11l_opy_:
            bstack11llll11l_opy_.bstack1111l1ll1_opy_(self, bstack1l1lll111_opy_, logger, item)
        threading.current_thread().testStatus = bstack1l111l1_opy_ (u"ࠨࠩᝍ")
    except Exception as e:
        logger.debug(bstack1l111l1_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡࡹ࡫࡭ࡱ࡫ࠠ࡮ࡣࡵ࡯࡮ࡴࡧࠡࡵࡷࡥࡹࡻࡳ࠻ࠢࠥᝎ") + str(e))
    bstack1l11ll1ll_opy_(self)
    self.session_id = None
def bstack1111l1111_opy_(self, command_executor,
             desired_capabilities=None, browser_profile=None, proxy=None,
             keep_alive=True, file_detector=None, options=None):
    global CONFIG
    global bstack1lll1ll1_opy_
    global bstack111lll1l_opy_
    global bstack1ll1l11lll_opy_
    global bstack11l1l11ll_opy_
    global bstack1lllll111_opy_
    global bstack11lll1l1_opy_
    global bstack1l1l11111_opy_
    global bstack1l1l11l111_opy_
    global bstack1lll1l1l11l_opy_
    global bstack1l1lll111_opy_
    CONFIG[bstack1l111l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡕࡇࡏࠬᝏ")] = str(bstack11l1l11ll_opy_) + str(__version__)
    command_executor = bstack11ll1l1l1_opy_(bstack1l1l11111_opy_)
    logger.debug(bstack1lll1111ll_opy_.format(command_executor))
    proxy = bstack1l1lll11ll_opy_(CONFIG, proxy)
    bstack1l1l11l11l_opy_ = 0
    try:
        if bstack1ll1l11lll_opy_ is True:
            bstack1l1l11l11l_opy_ = int(os.environ.get(bstack1l111l1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡏࡎࡅࡇ࡛ࠫᝐ")))
    except:
        bstack1l1l11l11l_opy_ = 0
    bstack1l1ll111_opy_ = bstack111ll1l1l_opy_(CONFIG, bstack1l1l11l11l_opy_)
    logger.debug(bstack11lll1111_opy_.format(str(bstack1l1ll111_opy_)))
    bstack1l1lll111_opy_ = CONFIG.get(bstack1l111l1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨᝑ"))[bstack1l1l11l11l_opy_]
    if bstack1l111l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪᝒ") in CONFIG and CONFIG[bstack1l111l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫᝓ")]:
        bstack111ll1111_opy_(bstack1l1ll111_opy_, bstack1l1l11l111_opy_)
    if desired_capabilities:
        bstack1l1111lll_opy_ = bstack11l1ll1l1_opy_(desired_capabilities)
        bstack1l1111lll_opy_[bstack1l111l1_opy_ (u"ࠨࡷࡶࡩ࡜࠹ࡃࠨ᝔")] = bstack111l11l1_opy_(CONFIG)
        bstack1ll11111ll_opy_ = bstack111ll1l1l_opy_(bstack1l1111lll_opy_)
        if bstack1ll11111ll_opy_:
            bstack1l1ll111_opy_ = update(bstack1ll11111ll_opy_, bstack1l1ll111_opy_)
        desired_capabilities = None
    if options:
        bstack1l11l1llll_opy_(options, bstack1l1ll111_opy_)
    if not options:
        options = bstack1111l11l_opy_(bstack1l1ll111_opy_)
    if bstack1l1lll11l1_opy_.bstack1lllll1ll_opy_(CONFIG, bstack1l1l11l11l_opy_) and bstack1l1lll11l1_opy_.bstack1lllll1l11_opy_(bstack1l1ll111_opy_, options):
        bstack1lll1l1l11l_opy_ = True
        bstack1l1lll11l1_opy_.set_capabilities(bstack1l1ll111_opy_, CONFIG)
    if proxy and bstack1l1ll11lll_opy_() >= version.parse(bstack1l111l1_opy_ (u"ࠩ࠷࠲࠶࠶࠮࠱ࠩ᝕")):
        options.proxy(proxy)
    if options and bstack1l1ll11lll_opy_() >= version.parse(bstack1l111l1_opy_ (u"ࠪ࠷࠳࠾࠮࠱ࠩ᝖")):
        desired_capabilities = None
    if (
            not options and not desired_capabilities
    ) or (
            bstack1l1ll11lll_opy_() < version.parse(bstack1l111l1_opy_ (u"ࠫ࠸࠴࠸࠯࠲ࠪ᝗")) and not desired_capabilities
    ):
        desired_capabilities = {}
        desired_capabilities.update(bstack1l1ll111_opy_)
    logger.info(bstack1l1ll1l1ll_opy_)
    if bstack1l1ll11lll_opy_() >= version.parse(bstack1l111l1_opy_ (u"ࠬ࠺࠮࠲࠲࠱࠴ࠬ᝘")):
        bstack1lllll111_opy_(self, command_executor=command_executor,
                  options=options, keep_alive=keep_alive, file_detector=file_detector)
    elif bstack1l1ll11lll_opy_() >= version.parse(bstack1l111l1_opy_ (u"࠭࠳࠯࠺࠱࠴ࠬ᝙")):
        bstack1lllll111_opy_(self, command_executor=command_executor,
                  desired_capabilities=desired_capabilities, options=options,
                  browser_profile=browser_profile, proxy=proxy,
                  keep_alive=keep_alive, file_detector=file_detector)
    elif bstack1l1ll11lll_opy_() >= version.parse(bstack1l111l1_opy_ (u"ࠧ࠳࠰࠸࠷࠳࠶ࠧ᝚")):
        bstack1lllll111_opy_(self, command_executor=command_executor,
                  desired_capabilities=desired_capabilities,
                  browser_profile=browser_profile, proxy=proxy,
                  keep_alive=keep_alive, file_detector=file_detector)
    else:
        bstack1lllll111_opy_(self, command_executor=command_executor,
                  desired_capabilities=desired_capabilities,
                  browser_profile=browser_profile, proxy=proxy,
                  keep_alive=keep_alive)
    try:
        bstack1llll11l11_opy_ = bstack1l111l1_opy_ (u"ࠨࠩ᝛")
        if bstack1l1ll11lll_opy_() >= version.parse(bstack1l111l1_opy_ (u"ࠩ࠷࠲࠵࠴࠰ࡣ࠳ࠪ᝜")):
            bstack1llll11l11_opy_ = self.caps.get(bstack1l111l1_opy_ (u"ࠥࡳࡵࡺࡩ࡮ࡣ࡯ࡌࡺࡨࡕࡳ࡮ࠥ᝝"))
        else:
            bstack1llll11l11_opy_ = self.capabilities.get(bstack1l111l1_opy_ (u"ࠦࡴࡶࡴࡪ࡯ࡤࡰࡍࡻࡢࡖࡴ࡯ࠦ᝞"))
        if bstack1llll11l11_opy_:
            bstack1lll11l111_opy_(bstack1llll11l11_opy_)
            if bstack1l1ll11lll_opy_() <= version.parse(bstack1l111l1_opy_ (u"ࠬ࠹࠮࠲࠵࠱࠴ࠬ᝟")):
                self.command_executor._url = bstack1l111l1_opy_ (u"ࠨࡨࡵࡶࡳ࠾࠴࠵ࠢᝠ") + bstack1l1l11111_opy_ + bstack1l111l1_opy_ (u"ࠢ࠻࠺࠳࠳ࡼࡪ࠯ࡩࡷࡥࠦᝡ")
            else:
                self.command_executor._url = bstack1l111l1_opy_ (u"ࠣࡪࡷࡸࡵࡹ࠺࠰࠱ࠥᝢ") + bstack1llll11l11_opy_ + bstack1l111l1_opy_ (u"ࠤ࠲ࡻࡩ࠵ࡨࡶࡤࠥᝣ")
            logger.debug(bstack1ll11l111l_opy_.format(bstack1llll11l11_opy_))
        else:
            logger.debug(bstack1l11ll11l1_opy_.format(bstack1l111l1_opy_ (u"ࠥࡓࡵࡺࡩ࡮ࡣ࡯ࠤࡍࡻࡢࠡࡰࡲࡸࠥ࡬࡯ࡶࡰࡧࠦᝤ")))
    except Exception as e:
        logger.debug(bstack1l11ll11l1_opy_.format(e))
    bstack1lll1ll1_opy_ = self.session_id
    if bstack1l111l1_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫᝥ") in bstack11l1l11ll_opy_:
        threading.current_thread().bstackSessionId = self.session_id
        threading.current_thread().bstackSessionDriver = self
        threading.current_thread().bstackTestErrorMessages = []
        item = store.get(bstack1l111l1_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣ࡮ࡺࡥ࡮ࠩᝦ"), None)
        if item:
            bstack1lll11lll1l_opy_ = getattr(item, bstack1l111l1_opy_ (u"࠭࡟ࡵࡧࡶࡸࡤࡩࡡࡴࡧࡢࡷࡹࡧࡲࡵࡧࡧࠫᝧ"), False)
            if not getattr(item, bstack1l111l1_opy_ (u"ࠧࡠࡦࡵ࡭ࡻ࡫ࡲࠨᝨ"), None) and bstack1lll11lll1l_opy_:
                setattr(store[bstack1l111l1_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡷࡩࡸࡺ࡟ࡪࡶࡨࡱࠬᝩ")], bstack1l111l1_opy_ (u"ࠩࡢࡨࡷ࡯ࡶࡦࡴࠪᝪ"), self)
        bstack1l1111l1l_opy_.bstack11lll111l_opy_(self)
    bstack11lll1l1_opy_.append(self)
    if bstack1l111l1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ᝫ") in CONFIG and bstack1l111l1_opy_ (u"ࠫࡸ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩᝬ") in CONFIG[bstack1l111l1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ᝭")][bstack1l1l11l11l_opy_]:
        bstack111lll1l_opy_ = CONFIG[bstack1l111l1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩᝮ")][bstack1l1l11l11l_opy_][bstack1l111l1_opy_ (u"ࠧࡴࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬᝯ")]
    logger.debug(bstack11l111l1_opy_.format(bstack1lll1ll1_opy_))
def bstack1lllll1l1_opy_(self, url):
    global bstack1lll11ll_opy_
    global CONFIG
    try:
        bstack11lllll11_opy_(url, CONFIG, logger)
    except Exception as err:
        logger.debug(bstack1ll11ll11_opy_.format(str(err)))
    try:
        bstack1lll11ll_opy_(self, url)
    except Exception as e:
        try:
            bstack1111lll1_opy_ = str(e)
            if any(err_msg in bstack1111lll1_opy_ for err_msg in bstack1ll11l111_opy_):
                bstack11lllll11_opy_(url, CONFIG, logger, True)
        except Exception as err:
            logger.debug(bstack1ll11ll11_opy_.format(str(err)))
        raise e
def bstack1l1l1l1lll_opy_(item, when):
    global bstack111l111ll_opy_
    try:
        bstack111l111ll_opy_(item, when)
    except Exception as e:
        pass
def bstack111l11ll_opy_(item, call, rep):
    global bstack1l11l1l11l_opy_
    global bstack11lll1l1_opy_
    name = bstack1l111l1_opy_ (u"ࠨࠩᝰ")
    try:
        if rep.when == bstack1l111l1_opy_ (u"ࠩࡦࡥࡱࡲࠧ᝱"):
            bstack1lll1ll1_opy_ = threading.current_thread().bstackSessionId
            bstack1lll1l1ll1l_opy_ = item.config.getoption(bstack1l111l1_opy_ (u"ࠪࡷࡰ࡯ࡰࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬᝲ"))
            try:
                if (str(bstack1lll1l1ll1l_opy_).lower() != bstack1l111l1_opy_ (u"ࠫࡹࡸࡵࡦࠩᝳ")):
                    name = str(rep.nodeid)
                    bstack1ll111l1l_opy_ = bstack1ll11111l1_opy_(bstack1l111l1_opy_ (u"ࠬࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭᝴"), name, bstack1l111l1_opy_ (u"࠭ࠧ᝵"), bstack1l111l1_opy_ (u"ࠧࠨ᝶"), bstack1l111l1_opy_ (u"ࠨࠩ᝷"), bstack1l111l1_opy_ (u"ࠩࠪ᝸"))
                    os.environ[bstack1l111l1_opy_ (u"ࠪࡔ࡞࡚ࡅࡔࡖࡢࡘࡊ࡙ࡔࡠࡐࡄࡑࡊ࠭᝹")] = name
                    for driver in bstack11lll1l1_opy_:
                        if bstack1lll1ll1_opy_ == driver.session_id:
                            driver.execute_script(bstack1ll111l1l_opy_)
            except Exception as e:
                logger.debug(bstack1l111l1_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡳࡦࡶࡷ࡭ࡳ࡭ࠠࡴࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠥ࡬࡯ࡳࠢࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩࠦࡳࡦࡵࡶ࡭ࡴࡴ࠺ࠡࡽࢀࠫ᝺").format(str(e)))
            try:
                bstack11ll1l111_opy_(rep.outcome.lower())
                if rep.outcome.lower() != bstack1l111l1_opy_ (u"ࠬࡹ࡫ࡪࡲࡳࡩࡩ࠭᝻"):
                    status = bstack1l111l1_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭᝼") if rep.outcome.lower() == bstack1l111l1_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧ᝽") else bstack1l111l1_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨ᝾")
                    reason = bstack1l111l1_opy_ (u"ࠩࠪ᝿")
                    if status == bstack1l111l1_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪក"):
                        reason = rep.longrepr.reprcrash.message
                        if (not threading.current_thread().bstackTestErrorMessages):
                            threading.current_thread().bstackTestErrorMessages = []
                        threading.current_thread().bstackTestErrorMessages.append(reason)
                    level = bstack1l111l1_opy_ (u"ࠫ࡮ࡴࡦࡰࠩខ") if status == bstack1l111l1_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬគ") else bstack1l111l1_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬឃ")
                    data = name + bstack1l111l1_opy_ (u"ࠧࠡࡲࡤࡷࡸ࡫ࡤࠢࠩង") if status == bstack1l111l1_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨច") else name + bstack1l111l1_opy_ (u"ࠩࠣࡪࡦ࡯࡬ࡦࡦࠤࠤࠬឆ") + reason
                    bstack1l1ll1l11l_opy_ = bstack1ll11111l1_opy_(bstack1l111l1_opy_ (u"ࠪࡥࡳࡴ࡯ࡵࡣࡷࡩࠬជ"), bstack1l111l1_opy_ (u"ࠫࠬឈ"), bstack1l111l1_opy_ (u"ࠬ࠭ញ"), bstack1l111l1_opy_ (u"࠭ࠧដ"), level, data)
                    for driver in bstack11lll1l1_opy_:
                        if bstack1lll1ll1_opy_ == driver.session_id:
                            driver.execute_script(bstack1l1ll1l11l_opy_)
            except Exception as e:
                logger.debug(bstack1l111l1_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡶࡩࡹࡺࡩ࡯ࡩࠣࡷࡪࡹࡳࡪࡱࡱࠤࡨࡵ࡮ࡵࡧࡻࡸࠥ࡬࡯ࡳࠢࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩࠦࡳࡦࡵࡶ࡭ࡴࡴ࠺ࠡࡽࢀࠫឋ").format(str(e)))
    except Exception as e:
        logger.debug(bstack1l111l1_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣ࡫ࡪࡺࡴࡪࡰࡪࠤࡸࡺࡡࡵࡧࠣ࡭ࡳࠦࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠣࡸࡪࡹࡴࠡࡵࡷࡥࡹࡻࡳ࠻ࠢࡾࢁࠬឌ").format(str(e)))
    bstack1l11l1l11l_opy_(item, call, rep)
notset = Notset()
def bstack111l111l_opy_(self, name: str, default=notset, skip: bool = False):
    global bstack1ll111ll11_opy_
    if str(name).lower() == bstack1l111l1_opy_ (u"ࠩࡧࡶ࡮ࡼࡥࡳࠩឍ"):
        return bstack1l111l1_opy_ (u"ࠥࡆࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࠤណ")
    else:
        return bstack1ll111ll11_opy_(self, name, default, skip)
def bstack1l1lll1111_opy_(self):
    global CONFIG
    global bstack11111lll1_opy_
    try:
        proxy = bstack1l11l1ll1l_opy_(CONFIG)
        if proxy:
            if proxy.endswith(bstack1l111l1_opy_ (u"ࠫ࠳ࡶࡡࡤࠩត")):
                proxies = bstack11l1l1111_opy_(proxy, bstack11ll1l1l1_opy_())
                if len(proxies) > 0:
                    protocol, bstack1ll11llll_opy_ = proxies.popitem()
                    if bstack1l111l1_opy_ (u"ࠧࡀ࠯࠰ࠤថ") in bstack1ll11llll_opy_:
                        return bstack1ll11llll_opy_
                    else:
                        return bstack1l111l1_opy_ (u"ࠨࡨࡵࡶࡳ࠾࠴࠵ࠢទ") + bstack1ll11llll_opy_
            else:
                return proxy
    except Exception as e:
        logger.error(bstack1l111l1_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡶࡩࡹࡺࡩ࡯ࡩࠣࡴࡷࡵࡸࡺࠢࡸࡶࡱࠦ࠺ࠡࡽࢀࠦធ").format(str(e)))
    return bstack11111lll1_opy_(self)
def bstack1l1l1lll1_opy_():
    return (bstack1l111l1_opy_ (u"ࠨࡪࡷࡸࡵࡖࡲࡰࡺࡼࠫន") in CONFIG or bstack1l111l1_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࡑࡴࡲࡼࡾ࠭ប") in CONFIG) and bstack1l1111l11_opy_() and bstack1l1ll11lll_opy_() >= version.parse(
        bstack1l1l1l1l1l_opy_)
def bstack1l111llll_opy_(self,
               executablePath=None,
               channel=None,
               args=None,
               ignoreDefaultArgs=None,
               handleSIGINT=None,
               handleSIGTERM=None,
               handleSIGHUP=None,
               timeout=None,
               env=None,
               headless=None,
               devtools=None,
               proxy=None,
               downloadsPath=None,
               slowMo=None,
               tracesDir=None,
               chromiumSandbox=None,
               firefoxUserPrefs=None
               ):
    global CONFIG
    global bstack111lll1l_opy_
    global bstack1ll1l11lll_opy_
    global bstack11l1l11ll_opy_
    CONFIG[bstack1l111l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡕࡇࡏࠬផ")] = str(bstack11l1l11ll_opy_) + str(__version__)
    bstack1l1l11l11l_opy_ = 0
    try:
        if bstack1ll1l11lll_opy_ is True:
            bstack1l1l11l11l_opy_ = int(os.environ.get(bstack1l111l1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡏࡎࡅࡇ࡛ࠫព")))
    except:
        bstack1l1l11l11l_opy_ = 0
    CONFIG[bstack1l111l1_opy_ (u"ࠧ࡯ࡳࡑ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠦភ")] = True
    bstack1l1ll111_opy_ = bstack111ll1l1l_opy_(CONFIG, bstack1l1l11l11l_opy_)
    logger.debug(bstack11lll1111_opy_.format(str(bstack1l1ll111_opy_)))
    if CONFIG.get(bstack1l111l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪម")):
        bstack111ll1111_opy_(bstack1l1ll111_opy_, bstack1l1l11l111_opy_)
    if bstack1l111l1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪយ") in CONFIG and bstack1l111l1_opy_ (u"ࠨࡵࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭រ") in CONFIG[bstack1l111l1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬល")][bstack1l1l11l11l_opy_]:
        bstack111lll1l_opy_ = CONFIG[bstack1l111l1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭វ")][bstack1l1l11l11l_opy_][bstack1l111l1_opy_ (u"ࠫࡸ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩឝ")]
    import urllib
    import json
    bstack1ll11lll1_opy_ = bstack1l111l1_opy_ (u"ࠬࡽࡳࡴ࠼࠲࠳ࡨࡪࡰ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰ࠳ࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࡀࡥࡤࡴࡸࡃࠧឞ") + urllib.parse.quote(json.dumps(bstack1l1ll111_opy_))
    browser = self.connect(bstack1ll11lll1_opy_)
    return browser
def bstack1lll1ll11_opy_():
    global bstack1ll1l111l_opy_
    try:
        from playwright._impl._browser_type import BrowserType
        BrowserType.launch = bstack1l111llll_opy_
        bstack1ll1l111l_opy_ = True
    except Exception as e:
        pass
def bstack1lll1l11111_opy_():
    global CONFIG
    global bstack1l1llll1l1_opy_
    global bstack1l1l11111_opy_
    global bstack1l1l11l111_opy_
    global bstack1ll1l11lll_opy_
    global bstack1llll11ll1_opy_
    CONFIG = json.loads(os.environ.get(bstack1l111l1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡉࡏࡏࡈࡌࡋࠬស")))
    bstack1l1llll1l1_opy_ = eval(os.environ.get(bstack1l111l1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡉࡔࡡࡄࡔࡕࡥࡁࡖࡖࡒࡑࡆ࡚ࡅࠨហ")))
    bstack1l1l11111_opy_ = os.environ.get(bstack1l111l1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡉࡗࡅࡣ࡚ࡘࡌࠨឡ"))
    bstack1lll1l11ll_opy_(CONFIG, bstack1l1llll1l1_opy_)
    bstack1llll11ll1_opy_ = bstack1ll111l1l1_opy_.bstack1ll1ll1ll1_opy_(CONFIG, bstack1llll11ll1_opy_)
    global bstack1lllll111_opy_
    global bstack1l11ll1ll_opy_
    global bstack11lll11ll_opy_
    global bstack1llll1llll_opy_
    global bstack1l11l1111_opy_
    global bstack1l1l1ll1_opy_
    global bstack1111ll1ll_opy_
    global bstack1lll11ll_opy_
    global bstack11111lll1_opy_
    global bstack1ll111ll11_opy_
    global bstack111l111ll_opy_
    global bstack1l11l1l11l_opy_
    try:
        from selenium import webdriver
        from selenium.webdriver.remote.webdriver import WebDriver
        bstack1lllll111_opy_ = webdriver.Remote.__init__
        bstack1l11ll1ll_opy_ = WebDriver.quit
        bstack1111ll1ll_opy_ = WebDriver.close
        bstack1lll11ll_opy_ = WebDriver.get
    except Exception as e:
        pass
    if (bstack1l111l1_opy_ (u"ࠩ࡫ࡸࡹࡶࡐࡳࡱࡻࡽࠬអ") in CONFIG or bstack1l111l1_opy_ (u"ࠪ࡬ࡹࡺࡰࡴࡒࡵࡳࡽࡿࠧឣ") in CONFIG) and bstack1l1111l11_opy_():
        if bstack1l1ll11lll_opy_() < version.parse(bstack1l1l1l1l1l_opy_):
            logger.error(bstack1l11l11l1_opy_.format(bstack1l1ll11lll_opy_()))
        else:
            try:
                from selenium.webdriver.remote.remote_connection import RemoteConnection
                bstack11111lll1_opy_ = RemoteConnection._get_proxy_url
            except Exception as e:
                logger.error(bstack1l1ll11111_opy_.format(str(e)))
    try:
        from _pytest.config import Config
        bstack1ll111ll11_opy_ = Config.getoption
        from _pytest import runner
        bstack111l111ll_opy_ = runner._update_current_test_var
    except Exception as e:
        logger.warn(e, bstack111llllll_opy_)
    try:
        from pytest_bdd import reporting
        bstack1l11l1l11l_opy_ = reporting.runtest_makereport
    except Exception as e:
        logger.debug(bstack1l111l1_opy_ (u"ࠫࡕࡲࡥࡢࡵࡨࠤ࡮ࡴࡳࡵࡣ࡯ࡰࠥࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠢࡷࡳࠥࡸࡵ࡯ࠢࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩࠦࡴࡦࡵࡷࡷࠬឤ"))
    bstack1l1l11l111_opy_ = CONFIG.get(bstack1l111l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩឥ"), {}).get(bstack1l111l1_opy_ (u"࠭࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨឦ"))
    bstack1ll1l11lll_opy_ = True
    bstack1ll111llll_opy_(bstack1ll1ll11ll_opy_)
if (bstack111lllllll_opy_()):
    bstack1lll1l11111_opy_()
@bstack1l1111lll1_opy_(class_method=False)
def bstack1lll1ll111l_opy_(hook_name, event, bstack1lll1ll1l11_opy_=None):
    if hook_name not in [bstack1l111l1_opy_ (u"ࠧࡴࡧࡷࡹࡵࡥࡦࡶࡰࡦࡸ࡮ࡵ࡮ࠨឧ"), bstack1l111l1_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡪࡺࡴࡣࡵ࡫ࡲࡲࠬឨ"), bstack1l111l1_opy_ (u"ࠩࡶࡩࡹࡻࡰࡠ࡯ࡲࡨࡺࡲࡥࠨឩ"), bstack1l111l1_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࡤࡳ࡯ࡥࡷ࡯ࡩࠬឪ"), bstack1l111l1_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࡢࡧࡱࡧࡳࡴࠩឫ"), bstack1l111l1_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴ࡟ࡤ࡮ࡤࡷࡸ࠭ឬ"), bstack1l111l1_opy_ (u"࠭ࡳࡦࡶࡸࡴࡤࡳࡥࡵࡪࡲࡨࠬឭ"), bstack1l111l1_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡰࡩࡹ࡮࡯ࡥࠩឮ")]:
        return
    node = store[bstack1l111l1_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡷࡩࡸࡺ࡟ࡪࡶࡨࡱࠬឯ")]
    if hook_name in [bstack1l111l1_opy_ (u"ࠩࡶࡩࡹࡻࡰࡠ࡯ࡲࡨࡺࡲࡥࠨឰ"), bstack1l111l1_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࡤࡳ࡯ࡥࡷ࡯ࡩࠬឱ")]:
        node = store[bstack1l111l1_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡳ࡯ࡥࡷ࡯ࡩࡤ࡯ࡴࡦ࡯ࠪឲ")]
    elif hook_name in [bstack1l111l1_opy_ (u"ࠬࡹࡥࡵࡷࡳࡣࡨࡲࡡࡴࡵࠪឳ"), bstack1l111l1_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࡠࡥ࡯ࡥࡸࡹࠧ឴")]:
        node = store[bstack1l111l1_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡥ࡯ࡥࡸࡹ࡟ࡪࡶࡨࡱࠬ឵")]
    if event == bstack1l111l1_opy_ (u"ࠨࡤࡨࡪࡴࡸࡥࠨា"):
        hook_type = bstack1lllllll1ll_opy_(hook_name)
        uuid = uuid4().__str__()
        bstack11lllll111_opy_ = {
            bstack1l111l1_opy_ (u"ࠩࡸࡹ࡮ࡪࠧិ"): uuid,
            bstack1l111l1_opy_ (u"ࠪࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠧី"): bstack1lll11llll_opy_(),
            bstack1l111l1_opy_ (u"ࠫࡹࡿࡰࡦࠩឹ"): bstack1l111l1_opy_ (u"ࠬ࡮࡯ࡰ࡭ࠪឺ"),
            bstack1l111l1_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡹࡿࡰࡦࠩុ"): hook_type,
            bstack1l111l1_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡴࡡ࡮ࡧࠪូ"): hook_name
        }
        store[bstack1l111l1_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡ࡫ࡳࡴࡱ࡟ࡶࡷ࡬ࡨࠬួ")].append(uuid)
        bstack1lll1ll1111_opy_ = node.nodeid
        if hook_type == bstack1l111l1_opy_ (u"ࠩࡅࡉࡋࡕࡒࡆࡡࡈࡅࡈࡎࠧើ"):
            if not _1l11l111l1_opy_.get(bstack1lll1ll1111_opy_, None):
                _1l11l111l1_opy_[bstack1lll1ll1111_opy_] = {bstack1l111l1_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡴࠩឿ"): []}
            _1l11l111l1_opy_[bstack1lll1ll1111_opy_][bstack1l111l1_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡵࠪៀ")].append(bstack11lllll111_opy_[bstack1l111l1_opy_ (u"ࠬࡻࡵࡪࡦࠪេ")])
        _1l11l111l1_opy_[bstack1lll1ll1111_opy_ + bstack1l111l1_opy_ (u"࠭࠭ࠨែ") + hook_name] = bstack11lllll111_opy_
        bstack1lll1ll11ll_opy_(node, bstack11lllll111_opy_, bstack1l111l1_opy_ (u"ࠧࡉࡱࡲ࡯ࡗࡻ࡮ࡔࡶࡤࡶࡹ࡫ࡤࠨៃ"))
    elif event == bstack1l111l1_opy_ (u"ࠨࡣࡩࡸࡪࡸࠧោ"):
        bstack11lllllll1_opy_ = node.nodeid + bstack1l111l1_opy_ (u"ࠩ࠰ࠫៅ") + hook_name
        _1l11l111l1_opy_[bstack11lllllll1_opy_][bstack1l111l1_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨំ")] = bstack1lll11llll_opy_()
        bstack1lll1l11lll_opy_(_1l11l111l1_opy_[bstack11lllllll1_opy_][bstack1l111l1_opy_ (u"ࠫࡺࡻࡩࡥࠩះ")])
        bstack1lll1ll11ll_opy_(node, _1l11l111l1_opy_[bstack11lllllll1_opy_], bstack1l111l1_opy_ (u"ࠬࡎ࡯ࡰ࡭ࡕࡹࡳࡌࡩ࡯࡫ࡶ࡬ࡪࡪࠧៈ"), bstack1lll1l1111l_opy_=bstack1lll1ll1l11_opy_)
def bstack1lll11l1ll1_opy_():
    global bstack1lll11ll1ll_opy_
    if bstack1lll11l1l_opy_():
        bstack1lll11ll1ll_opy_ = bstack1l111l1_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠪ៉")
    else:
        bstack1lll11ll1ll_opy_ = bstack1l111l1_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧ៊")
@bstack1l1111l1l_opy_.bstack1llll1111l1_opy_
def bstack1lll1l111l1_opy_():
    bstack1lll11l1ll1_opy_()
    if bstack1l1111l11_opy_():
        bstack1l1l1111l_opy_(bstack1ll1ll11_opy_)
    bstack111ll1111l_opy_ = bstack111ll1l1l1_opy_(bstack1lll1ll111l_opy_)
bstack1lll1l111l1_opy_()