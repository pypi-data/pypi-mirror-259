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
import os
import signal
import sys
import yaml
import requests
import logging
import threading
import socket
import datetime
import string
import random
import json
import collections.abc
import re
import multiprocessing
import traceback
import copy
import tempfile
from packaging import version
from browserstack.local import Local
from urllib.parse import urlparse
from dotenv import load_dotenv
from bstack_utils.constants import *
from bstack_utils.percy import *
from browserstack_sdk.bstack1l11111ll_opy_ import *
from bstack_utils.percy_sdk import PercySDK
from bstack_utils.bstack11lll1ll1_opy_ import bstack1ll1l11111_opy_
import time
import requests
def bstack1l11ll1l11_opy_():
  global CONFIG
  headers = {
        bstack1l111l1_opy_ (u"ࠪࡇࡴࡴࡴࡦࡰࡷ࠱ࡹࡿࡰࡦࠩࡶ"): bstack1l111l1_opy_ (u"ࠫࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱࡭ࡷࡴࡴࠧࡷ"),
      }
  proxies = bstack1l1ll1ll_opy_(CONFIG, bstack11l111l11_opy_)
  try:
    response = requests.get(bstack11l111l11_opy_, headers=headers, proxies=proxies, timeout=5)
    if response.json():
      bstack1l11llll_opy_ = response.json()[bstack1l111l1_opy_ (u"ࠬ࡮ࡵࡣࡵࠪࡸ")]
      logger.debug(bstack111lll1l1_opy_.format(response.json()))
      return bstack1l11llll_opy_
    else:
      logger.debug(bstack1llll1l1ll_opy_.format(bstack1l111l1_opy_ (u"ࠨࡒࡦࡵࡳࡳࡳࡹࡥࠡࡌࡖࡓࡓࠦࡰࡢࡴࡶࡩࠥ࡫ࡲࡳࡱࡵࠤࠧࡹ")))
  except Exception as e:
    logger.debug(bstack1llll1l1ll_opy_.format(e))
def bstack1ll11lll11_opy_(hub_url):
  global CONFIG
  url = bstack1l111l1_opy_ (u"ࠢࡩࡶࡷࡴࡸࡀ࠯࠰ࠤࡺ")+  hub_url + bstack1l111l1_opy_ (u"ࠣ࠱ࡦ࡬ࡪࡩ࡫ࠣࡻ")
  headers = {
        bstack1l111l1_opy_ (u"ࠩࡆࡳࡳࡺࡥ࡯ࡶ࠰ࡸࡾࡶࡥࠨࡼ"): bstack1l111l1_opy_ (u"ࠪࡥࡵࡶ࡬ࡪࡥࡤࡸ࡮ࡵ࡮࠰࡬ࡶࡳࡳ࠭ࡽ"),
      }
  proxies = bstack1l1ll1ll_opy_(CONFIG, url)
  try:
    start_time = time.perf_counter()
    requests.get(url, headers=headers, proxies=proxies, timeout=5)
    latency = time.perf_counter() - start_time
    logger.debug(bstack11lll1ll_opy_.format(hub_url, latency))
    return dict(hub_url=hub_url, latency=latency)
  except Exception as e:
    logger.debug(bstack111ll1lll_opy_.format(hub_url, e))
def bstack11l11ll1l_opy_():
  try:
    global bstack1l1l11111_opy_
    bstack1l11llll_opy_ = bstack1l11ll1l11_opy_()
    bstack1l11ll1ll1_opy_ = []
    results = []
    for bstack1ll11l1111_opy_ in bstack1l11llll_opy_:
      bstack1l11ll1ll1_opy_.append(bstack1l1l11ll11_opy_(target=bstack1ll11lll11_opy_,args=(bstack1ll11l1111_opy_,)))
    for t in bstack1l11ll1ll1_opy_:
      t.start()
    for t in bstack1l11ll1ll1_opy_:
      results.append(t.join())
    bstack1l11lll1ll_opy_ = {}
    for item in results:
      hub_url = item[bstack1l111l1_opy_ (u"ࠫ࡭ࡻࡢࡠࡷࡵࡰࠬࡾ")]
      latency = item[bstack1l111l1_opy_ (u"ࠬࡲࡡࡵࡧࡱࡧࡾ࠭ࡿ")]
      bstack1l11lll1ll_opy_[hub_url] = latency
    bstack1ll1l1l11_opy_ = min(bstack1l11lll1ll_opy_, key= lambda x: bstack1l11lll1ll_opy_[x])
    bstack1l1l11111_opy_ = bstack1ll1l1l11_opy_
    logger.debug(bstack111ll11ll_opy_.format(bstack1ll1l1l11_opy_))
  except Exception as e:
    logger.debug(bstack111llll1l_opy_.format(e))
from bstack_utils.messages import *
from bstack_utils import bstack1ll111l1l1_opy_
from bstack_utils.config import Config
from bstack_utils.helper import bstack1llll1lll1_opy_, bstack1ll1llll1_opy_, bstack1l1ll1l1l_opy_, bstack1ll1ll1l1_opy_, bstack1ll1l1ll1l_opy_, \
  Notset, bstack111l11l1_opy_, \
  bstack11lllllll_opy_, bstack1lll1lll11_opy_, bstack1111l1l1_opy_, bstack11111l11l_opy_, bstack1lll11l1l_opy_, bstack1l1111l11_opy_, \
  bstack1l1lll1lll_opy_, \
  bstack1l1l1l11l_opy_, bstack1l1l11llll_opy_, bstack1lll11l111_opy_, bstack1ll1lll1l_opy_, \
  bstack1l1l111l1_opy_, bstack111111111_opy_, bstack1l1l1ll111_opy_
from bstack_utils.bstack1l11l1lll1_opy_ import bstack1111ll1l_opy_
from bstack_utils.bstack111ll111l_opy_ import bstack1l1l1111l_opy_
from bstack_utils.bstack1l1llll11l_opy_ import bstack11l11111l_opy_, bstack1111l1lll_opy_
from bstack_utils.bstack11ll11l11_opy_ import bstack1l1111l1l_opy_
from bstack_utils.bstack1lll1l1l1_opy_ import bstack1lll1l1l1_opy_
from bstack_utils.proxy import bstack11l1l1111_opy_, bstack1l1ll1ll_opy_, bstack1l11l1ll1l_opy_, bstack1l1ll1lll1_opy_
import bstack_utils.bstack1lll11l11l_opy_ as bstack1l1lll11l1_opy_
from browserstack_sdk.bstack11l1ll11_opy_ import *
from browserstack_sdk.bstack1llll1111_opy_ import *
from bstack_utils.bstack111l1lll_opy_ import bstack11ll1l111_opy_
bstack1lll11lll_opy_ = bstack1l111l1_opy_ (u"࠭ࠠࠡ࠱࠭ࠤࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽ࠡࠬ࠲ࡠࡳࠦࠠࡪࡨࠫࡴࡦ࡭ࡥࠡ࠿ࡀࡁࠥࡼ࡯ࡪࡦࠣ࠴࠮ࠦࡻ࡝ࡰࠣࠤࠥࡺࡲࡺࡽ࡟ࡲࠥࡩ࡯࡯ࡵࡷࠤ࡫ࡹࠠ࠾ࠢࡵࡩࡶࡻࡩࡳࡧࠫࡠࠬ࡬ࡳ࡝ࠩࠬ࠿ࡡࡴࠠࠡࠢࠣࠤ࡫ࡹ࠮ࡢࡲࡳࡩࡳࡪࡆࡪ࡮ࡨࡗࡾࡴࡣࠩࡤࡶࡸࡦࡩ࡫ࡠࡲࡤࡸ࡭࠲ࠠࡋࡕࡒࡒ࠳ࡹࡴࡳ࡫ࡱ࡫࡮࡬ࡹࠩࡲࡢ࡭ࡳࡪࡥࡹࠫࠣ࠯ࠥࠨ࠺ࠣࠢ࠮ࠤࡏ࡙ࡏࡏ࠰ࡶࡸࡷ࡯࡮ࡨ࡫ࡩࡽ࠭ࡐࡓࡐࡐ࠱ࡴࡦࡸࡳࡦࠪࠫࡥࡼࡧࡩࡵࠢࡱࡩࡼࡖࡡࡨࡧ࠵࠲ࡪࡼࡡ࡭ࡷࡤࡸࡪ࠮ࠢࠩࠫࠣࡁࡃࠦࡻࡾࠤ࠯ࠤࡡ࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡧࡦࡶࡖࡩࡸࡹࡩࡰࡰࡇࡩࡹࡧࡩ࡭ࡵࠥࢁࡡ࠭ࠩࠪࠫ࡞ࠦ࡭ࡧࡳࡩࡧࡧࡣ࡮ࡪࠢ࡞ࠫࠣ࠯ࠥࠨࠬ࡝࡞ࡱࠦ࠮ࡢ࡮ࠡࠢࠣࠤࢂࡩࡡࡵࡥ࡫ࠬࡪࡾࠩࡼ࡞ࡱࠤࠥࠦࠠࡾ࡞ࡱࠤࠥࢃ࡜࡯ࠢࠣ࠳࠯ࠦ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࠣ࠮࠴࠭ࢀ")
bstack1l11l111_opy_ = bstack1l111l1_opy_ (u"ࠧ࡝ࡰ࠲࠮ࠥࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾ࠢ࠭࠳ࡡࡴࡣࡰࡰࡶࡸࠥࡨࡳࡵࡣࡦ࡯ࡤࡶࡡࡵࡪࠣࡁࠥࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹ࡟ࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸ࠱ࡰࡪࡴࡧࡵࡪࠣ࠱ࠥ࠹࡝࡝ࡰࡦࡳࡳࡹࡴࠡࡤࡶࡸࡦࡩ࡫ࡠࡥࡤࡴࡸࠦ࠽ࠡࡲࡵࡳࡨ࡫ࡳࡴ࠰ࡤࡶ࡬ࡼ࡛ࡱࡴࡲࡧࡪࡹࡳ࠯ࡣࡵ࡫ࡻ࠴࡬ࡦࡰࡪࡸ࡭ࠦ࠭ࠡ࠳ࡠࡠࡳࡩ࡯࡯ࡵࡷࠤࡵࡥࡩ࡯ࡦࡨࡼࠥࡃࠠࡱࡴࡲࡧࡪࡹࡳ࠯ࡣࡵ࡫ࡻࡡࡰࡳࡱࡦࡩࡸࡹ࠮ࡢࡴࡪࡺ࠳ࡲࡥ࡯ࡩࡷ࡬ࠥ࠳ࠠ࠳࡟࡟ࡲࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸࠣࡁࠥࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹ࠲ࡸࡲࡩࡤࡧࠫ࠴࠱ࠦࡰࡳࡱࡦࡩࡸࡹ࠮ࡢࡴࡪࡺ࠳ࡲࡥ࡯ࡩࡷ࡬ࠥ࠳ࠠ࠴ࠫ࡟ࡲࡨࡵ࡮ࡴࡶࠣ࡭ࡲࡶ࡯ࡳࡶࡢࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺ࠴ࡠࡤࡶࡸࡦࡩ࡫ࠡ࠿ࠣࡶࡪࡷࡵࡪࡴࡨࠬࠧࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠤࠬ࠿ࡡࡴࡩ࡮ࡲࡲࡶࡹࡥࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶ࠷ࡣࡧࡹࡴࡢࡥ࡮࠲ࡨ࡮ࡲࡰ࡯࡬ࡹࡲ࠴࡬ࡢࡷࡱࡧ࡭ࠦ࠽ࠡࡣࡶࡽࡳࡩࠠࠩ࡮ࡤࡹࡳࡩࡨࡐࡲࡷ࡭ࡴࡴࡳࠪࠢࡀࡂࠥࢁ࡜࡯࡮ࡨࡸࠥࡩࡡࡱࡵ࠾ࡠࡳࡺࡲࡺࠢࡾࡠࡳࡩࡡࡱࡵࠣࡁࠥࡐࡓࡐࡐ࠱ࡴࡦࡸࡳࡦࠪࡥࡷࡹࡧࡣ࡬ࡡࡦࡥࡵࡹࠩ࡝ࡰࠣࠤࢂࠦࡣࡢࡶࡦ࡬࠭࡫ࡸࠪࠢࡾࡠࡳࠦࠠࠡࠢࢀࡠࡳࠦࠠࡳࡧࡷࡹࡷࡴࠠࡢࡹࡤ࡭ࡹࠦࡩ࡮ࡲࡲࡶࡹࡥࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶ࠷ࡣࡧࡹࡴࡢࡥ࡮࠲ࡨ࡮ࡲࡰ࡯࡬ࡹࡲ࠴ࡣࡰࡰࡱࡩࡨࡺࠨࡼ࡞ࡱࠤࠥࠦࠠࡸࡵࡈࡲࡩࡶ࡯ࡪࡰࡷ࠾ࠥࡦࡷࡴࡵ࠽࠳࠴ࡩࡤࡱ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱ࠴ࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࡁࡦࡥࡵࡹ࠽ࠥࡽࡨࡲࡨࡵࡤࡦࡗࡕࡍࡈࡵ࡭ࡱࡱࡱࡩࡳࡺࠨࡋࡕࡒࡒ࠳ࡹࡴࡳ࡫ࡱ࡫࡮࡬ࡹࠩࡥࡤࡴࡸ࠯ࠩࡾࡢ࠯ࡠࡳࠦࠠࠡࠢ࠱࠲࠳ࡲࡡࡶࡰࡦ࡬ࡔࡶࡴࡪࡱࡱࡷࡡࡴࠠࠡࡿࠬࡠࡳࢃ࡜࡯࠱࠭ࠤࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽ࠡࠬ࠲ࡠࡳ࠭ࢁ")
from ._version import __version__
bstack1l11lll111_opy_ = None
CONFIG = {}
bstack1111lllll_opy_ = {}
bstack1lll11ll11_opy_ = {}
bstack1lll1ll1_opy_ = None
bstack1ll1l1l11l_opy_ = None
bstack111lll1l_opy_ = None
bstack1llll1ll1_opy_ = -1
bstack1111lll1l_opy_ = 0
bstack1llll11ll1_opy_ = bstack1l1llll1l_opy_
bstack1ll1111ll1_opy_ = 1
bstack1ll1l11lll_opy_ = False
bstack1lll1l1111_opy_ = False
bstack11l1l11ll_opy_ = bstack1l111l1_opy_ (u"ࠨࠩࢂ")
bstack1l1l11l111_opy_ = bstack1l111l1_opy_ (u"ࠩࠪࢃ")
bstack1l1llll1l1_opy_ = False
bstack1lll1l1lll_opy_ = True
bstack11ll1lll_opy_ = bstack1l111l1_opy_ (u"ࠪࠫࢄ")
bstack11lll1l1_opy_ = []
bstack1l1l11111_opy_ = bstack1l111l1_opy_ (u"ࠫࠬࢅ")
bstack1ll1l111l_opy_ = False
bstack1ll11l1lll_opy_ = None
bstack1l1l11l1_opy_ = None
bstack1l11ll1111_opy_ = None
bstack11l11l1l_opy_ = -1
bstack1ll1l1lll1_opy_ = os.path.join(os.path.expanduser(bstack1l111l1_opy_ (u"ࠬࢄࠧࢆ")), bstack1l111l1_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭ࢇ"), bstack1l111l1_opy_ (u"ࠧ࠯ࡴࡲࡦࡴࡺ࠭ࡳࡧࡳࡳࡷࡺ࠭ࡩࡧ࡯ࡴࡪࡸ࠮࡫ࡵࡲࡲࠬ࢈"))
bstack1l11lllll_opy_ = 0
bstack11l1111l_opy_ = []
bstack1lll1lll1_opy_ = []
bstack1lllll1ll1_opy_ = []
bstack1l111lll1_opy_ = []
bstack1lll1ll1l_opy_ = bstack1l111l1_opy_ (u"ࠨࠩࢉ")
bstack11lll111_opy_ = bstack1l111l1_opy_ (u"ࠩࠪࢊ")
bstack111lll11l_opy_ = False
bstack1l1l1l1ll1_opy_ = False
bstack1l1lll111_opy_ = {}
bstack1lllll111_opy_ = None
bstack1l11ll1ll_opy_ = None
bstack1ll1111lll_opy_ = None
bstack1l111l1l_opy_ = None
bstack1111llll1_opy_ = None
bstack1l1ll1ll11_opy_ = None
bstack11lll11ll_opy_ = None
bstack1llll1llll_opy_ = None
bstack1ll1111ll_opy_ = None
bstack1l11l1111_opy_ = None
bstack1l1l1ll1_opy_ = None
bstack11111lll1_opy_ = None
bstack1111ll1ll_opy_ = None
bstack1lll11ll_opy_ = None
bstack11111ll1l_opy_ = None
bstack1ll111ll11_opy_ = None
bstack111l111ll_opy_ = None
bstack1l1ll11l11_opy_ = None
bstack1l11l1l11l_opy_ = None
bstack111lll11_opy_ = None
bstack1llll11111_opy_ = None
bstack1lll1l11l_opy_ = False
bstack1lll1llll1_opy_ = bstack1l111l1_opy_ (u"ࠥࠦࢋ")
logger = bstack1ll111l1l1_opy_.get_logger(__name__, bstack1llll11ll1_opy_)
bstack11111111_opy_ = Config.bstack1ll1l11ll_opy_()
percy = bstack1l1l11111l_opy_()
bstack1ll1l1111l_opy_ = bstack1ll1l11111_opy_()
def bstack1lll111ll1_opy_():
  global CONFIG
  global bstack111lll11l_opy_
  global bstack11111111_opy_
  bstack111111l1_opy_ = bstack1lllllll11_opy_(CONFIG)
  if (bstack1l111l1_opy_ (u"ࠫࡸࡱࡩࡱࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭ࢌ") in bstack111111l1_opy_ and str(bstack111111l1_opy_[bstack1l111l1_opy_ (u"ࠬࡹ࡫ࡪࡲࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧࢍ")]).lower() == bstack1l111l1_opy_ (u"࠭ࡴࡳࡷࡨࠫࢎ")):
    bstack111lll11l_opy_ = True
  bstack11111111_opy_.bstack1l1l1lllll_opy_(bstack111111l1_opy_.get(bstack1l111l1_opy_ (u"ࠧࡴ࡭࡬ࡴࡘ࡫ࡳࡴ࡫ࡲࡲࡘࡺࡡࡵࡷࡶࠫ࢏"), False))
def bstack111l1111l_opy_():
  from appium.version import version as appium_version
  return version.parse(appium_version)
def bstack1l1ll11lll_opy_():
  from selenium import webdriver
  return version.parse(webdriver.__version__)
def bstack1l1lllll1l_opy_():
  args = sys.argv
  for i in range(len(args)):
    if bstack1l111l1_opy_ (u"ࠣ࠯࠰ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡥࡲࡲ࡫࡯ࡧࡧ࡫࡯ࡩࠧ࢐") == args[i].lower() or bstack1l111l1_opy_ (u"ࠤ࠰࠱ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡴࡦࡪࡩࠥ࢑") == args[i].lower():
      path = args[i + 1]
      sys.argv.remove(args[i])
      sys.argv.remove(path)
      global bstack11ll1lll_opy_
      bstack11ll1lll_opy_ += bstack1l111l1_opy_ (u"ࠪ࠱࠲ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡇࡴࡴࡦࡪࡩࡉ࡭ࡱ࡫ࠠࠨ࢒") + path
      return path
  return None
bstack1lll111l_opy_ = re.compile(bstack1l111l1_opy_ (u"ࡶࠧ࠴ࠪࡀ࡞ࠧࡿ࠭࠴ࠪࡀࠫࢀ࠲࠯ࡅࠢ࢓"))
def bstack111l11lll_opy_(loader, node):
  value = loader.construct_scalar(node)
  for group in bstack1lll111l_opy_.findall(value):
    if group is not None and os.environ.get(group) is not None:
      value = value.replace(bstack1l111l1_opy_ (u"ࠧࠪࡻࠣ࢔") + group + bstack1l111l1_opy_ (u"ࠨࡽࠣ࢕"), os.environ.get(group))
  return value
def bstack1l1l11l1l1_opy_():
  bstack1ll1ll1ll_opy_ = bstack1l1lllll1l_opy_()
  if bstack1ll1ll1ll_opy_ and os.path.exists(os.path.abspath(bstack1ll1ll1ll_opy_)):
    fileName = bstack1ll1ll1ll_opy_
  if bstack1l111l1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡃࡐࡐࡉࡍࡌࡥࡆࡊࡎࡈࠫ࢖") in os.environ and os.path.exists(
          os.path.abspath(os.environ[bstack1l111l1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡄࡑࡑࡊࡎࡍ࡟ࡇࡋࡏࡉࠬࢗ")])) and not bstack1l111l1_opy_ (u"ࠩࡩ࡭ࡱ࡫ࡎࡢ࡯ࡨࠫ࢘") in locals():
    fileName = os.environ[bstack1l111l1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡆࡓࡓࡌࡉࡈࡡࡉࡍࡑࡋ࢙ࠧ")]
  if bstack1l111l1_opy_ (u"ࠫ࡫࡯࡬ࡦࡐࡤࡱࡪ࢚࠭") in locals():
    bstack1ll11l1_opy_ = os.path.abspath(fileName)
  else:
    bstack1ll11l1_opy_ = bstack1l111l1_opy_ (u"࢛ࠬ࠭")
  bstack11l1ll1l_opy_ = os.getcwd()
  bstack111l1l11l_opy_ = bstack1l111l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡿ࡭࡭ࠩ࢜")
  bstack111l1ll1_opy_ = bstack1l111l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡹࡢ࡯࡯ࠫ࢝")
  while (not os.path.exists(bstack1ll11l1_opy_)) and bstack11l1ll1l_opy_ != bstack1l111l1_opy_ (u"ࠣࠤ࢞"):
    bstack1ll11l1_opy_ = os.path.join(bstack11l1ll1l_opy_, bstack111l1l11l_opy_)
    if not os.path.exists(bstack1ll11l1_opy_):
      bstack1ll11l1_opy_ = os.path.join(bstack11l1ll1l_opy_, bstack111l1ll1_opy_)
    if bstack11l1ll1l_opy_ != os.path.dirname(bstack11l1ll1l_opy_):
      bstack11l1ll1l_opy_ = os.path.dirname(bstack11l1ll1l_opy_)
    else:
      bstack11l1ll1l_opy_ = bstack1l111l1_opy_ (u"ࠤࠥ࢟")
  if not os.path.exists(bstack1ll11l1_opy_):
    bstack11lll1l11_opy_(
      bstack1lll111lll_opy_.format(os.getcwd()))
  try:
    with open(bstack1ll11l1_opy_, bstack1l111l1_opy_ (u"ࠪࡶࠬࢠ")) as stream:
      yaml.add_implicit_resolver(bstack1l111l1_opy_ (u"ࠦࠦࡶࡡࡵࡪࡨࡼࠧࢡ"), bstack1lll111l_opy_)
      yaml.add_constructor(bstack1l111l1_opy_ (u"ࠧࠧࡰࡢࡶ࡫ࡩࡽࠨࢢ"), bstack111l11lll_opy_)
      config = yaml.load(stream, yaml.FullLoader)
      return config
  except:
    with open(bstack1ll11l1_opy_, bstack1l111l1_opy_ (u"࠭ࡲࠨࢣ")) as stream:
      try:
        config = yaml.safe_load(stream)
        return config
      except yaml.YAMLError as exc:
        bstack11lll1l11_opy_(bstack11ll1l1ll_opy_.format(str(exc)))
def bstack111l111l1_opy_(config):
  bstack111111l1l_opy_ = bstack11111lll_opy_(config)
  for option in list(bstack111111l1l_opy_):
    if option.lower() in bstack1ll1lll1l1_opy_ and option != bstack1ll1lll1l1_opy_[option.lower()]:
      bstack111111l1l_opy_[bstack1ll1lll1l1_opy_[option.lower()]] = bstack111111l1l_opy_[option]
      del bstack111111l1l_opy_[option]
  return config
def bstack111llll11_opy_():
  global bstack1lll11ll11_opy_
  for key, bstack1llll1l111_opy_ in bstack1ll111l1ll_opy_.items():
    if isinstance(bstack1llll1l111_opy_, list):
      for var in bstack1llll1l111_opy_:
        if var in os.environ and os.environ[var] and str(os.environ[var]).strip():
          bstack1lll11ll11_opy_[key] = os.environ[var]
          break
    elif bstack1llll1l111_opy_ in os.environ and os.environ[bstack1llll1l111_opy_] and str(os.environ[bstack1llll1l111_opy_]).strip():
      bstack1lll11ll11_opy_[key] = os.environ[bstack1llll1l111_opy_]
  if bstack1l111l1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡌࡐࡅࡄࡐࡤࡏࡄࡆࡐࡗࡍࡋࡏࡅࡓࠩࢤ") in os.environ:
    bstack1lll11ll11_opy_[bstack1l111l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬࢥ")] = {}
    bstack1lll11ll11_opy_[bstack1l111l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ࢦ")][bstack1l111l1_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬࢧ")] = os.environ[bstack1l111l1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡐࡔࡉࡁࡍࡡࡌࡈࡊࡔࡔࡊࡈࡌࡉࡗ࠭ࢨ")]
def bstack1ll1111l_opy_():
  global bstack1111lllll_opy_
  global bstack11ll1lll_opy_
  for idx, val in enumerate(sys.argv):
    if idx < len(sys.argv) and bstack1l111l1_opy_ (u"ࠬ࠳࠭ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨࢩ").lower() == val.lower():
      bstack1111lllll_opy_[bstack1l111l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪࢪ")] = {}
      bstack1111lllll_opy_[bstack1l111l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫࢫ")][bstack1l111l1_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪࢬ")] = sys.argv[idx + 1]
      del sys.argv[idx:idx + 2]
      break
  for key, bstack1llll1l1l1_opy_ in bstack1ll1lll11_opy_.items():
    if isinstance(bstack1llll1l1l1_opy_, list):
      for idx, val in enumerate(sys.argv):
        for var in bstack1llll1l1l1_opy_:
          if idx < len(sys.argv) and bstack1l111l1_opy_ (u"ࠩ࠰࠱ࠬࢭ") + var.lower() == val.lower() and not key in bstack1111lllll_opy_:
            bstack1111lllll_opy_[key] = sys.argv[idx + 1]
            bstack11ll1lll_opy_ += bstack1l111l1_opy_ (u"ࠪࠤ࠲࠳ࠧࢮ") + var + bstack1l111l1_opy_ (u"ࠫࠥ࠭ࢯ") + sys.argv[idx + 1]
            del sys.argv[idx:idx + 2]
            break
    else:
      for idx, val in enumerate(sys.argv):
        if idx < len(sys.argv) and bstack1l111l1_opy_ (u"ࠬ࠳࠭ࠨࢰ") + bstack1llll1l1l1_opy_.lower() == val.lower() and not key in bstack1111lllll_opy_:
          bstack1111lllll_opy_[key] = sys.argv[idx + 1]
          bstack11ll1lll_opy_ += bstack1l111l1_opy_ (u"࠭ࠠ࠮࠯ࠪࢱ") + bstack1llll1l1l1_opy_ + bstack1l111l1_opy_ (u"ࠧࠡࠩࢲ") + sys.argv[idx + 1]
          del sys.argv[idx:idx + 2]
def bstack11l1ll1l1_opy_(config):
  bstack1lll1111_opy_ = config.keys()
  for bstack1ll1l111_opy_, bstack111ll11l1_opy_ in bstack11l1111ll_opy_.items():
    if bstack111ll11l1_opy_ in bstack1lll1111_opy_:
      config[bstack1ll1l111_opy_] = config[bstack111ll11l1_opy_]
      del config[bstack111ll11l1_opy_]
  for bstack1ll1l111_opy_, bstack111ll11l1_opy_ in bstack1ll11111_opy_.items():
    if isinstance(bstack111ll11l1_opy_, list):
      for bstack111lllll1_opy_ in bstack111ll11l1_opy_:
        if bstack111lllll1_opy_ in bstack1lll1111_opy_:
          config[bstack1ll1l111_opy_] = config[bstack111lllll1_opy_]
          del config[bstack111lllll1_opy_]
          break
    elif bstack111ll11l1_opy_ in bstack1lll1111_opy_:
      config[bstack1ll1l111_opy_] = config[bstack111ll11l1_opy_]
      del config[bstack111ll11l1_opy_]
  for bstack111lllll1_opy_ in list(config):
    for bstack11ll11l1_opy_ in bstack1l1ll11ll1_opy_:
      if bstack111lllll1_opy_.lower() == bstack11ll11l1_opy_.lower() and bstack111lllll1_opy_ != bstack11ll11l1_opy_:
        config[bstack11ll11l1_opy_] = config[bstack111lllll1_opy_]
        del config[bstack111lllll1_opy_]
  bstack1llllll1l_opy_ = []
  if bstack1l111l1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫࢳ") in config:
    bstack1llllll1l_opy_ = config[bstack1l111l1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬࢴ")]
  for platform in bstack1llllll1l_opy_:
    for bstack111lllll1_opy_ in list(platform):
      for bstack11ll11l1_opy_ in bstack1l1ll11ll1_opy_:
        if bstack111lllll1_opy_.lower() == bstack11ll11l1_opy_.lower() and bstack111lllll1_opy_ != bstack11ll11l1_opy_:
          platform[bstack11ll11l1_opy_] = platform[bstack111lllll1_opy_]
          del platform[bstack111lllll1_opy_]
  for bstack1ll1l111_opy_, bstack111ll11l1_opy_ in bstack1ll11111_opy_.items():
    for platform in bstack1llllll1l_opy_:
      if isinstance(bstack111ll11l1_opy_, list):
        for bstack111lllll1_opy_ in bstack111ll11l1_opy_:
          if bstack111lllll1_opy_ in platform:
            platform[bstack1ll1l111_opy_] = platform[bstack111lllll1_opy_]
            del platform[bstack111lllll1_opy_]
            break
      elif bstack111ll11l1_opy_ in platform:
        platform[bstack1ll1l111_opy_] = platform[bstack111ll11l1_opy_]
        del platform[bstack111ll11l1_opy_]
  for bstack1111l11l1_opy_ in bstack1l1llll111_opy_:
    if bstack1111l11l1_opy_ in config:
      if not bstack1l1llll111_opy_[bstack1111l11l1_opy_] in config:
        config[bstack1l1llll111_opy_[bstack1111l11l1_opy_]] = {}
      config[bstack1l1llll111_opy_[bstack1111l11l1_opy_]].update(config[bstack1111l11l1_opy_])
      del config[bstack1111l11l1_opy_]
  for platform in bstack1llllll1l_opy_:
    for bstack1111l11l1_opy_ in bstack1l1llll111_opy_:
      if bstack1111l11l1_opy_ in list(platform):
        if not bstack1l1llll111_opy_[bstack1111l11l1_opy_] in platform:
          platform[bstack1l1llll111_opy_[bstack1111l11l1_opy_]] = {}
        platform[bstack1l1llll111_opy_[bstack1111l11l1_opy_]].update(platform[bstack1111l11l1_opy_])
        del platform[bstack1111l11l1_opy_]
  config = bstack111l111l1_opy_(config)
  return config
def bstack1lll111l11_opy_(config):
  global bstack1l1l11l111_opy_
  if bstack1l111l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧࢵ") in config and str(config[bstack1l111l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨࢶ")]).lower() != bstack1l111l1_opy_ (u"ࠬ࡬ࡡ࡭ࡵࡨࠫࢷ"):
    if not bstack1l111l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪࢸ") in config:
      config[bstack1l111l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫࢹ")] = {}
    if not bstack1l111l1_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪࢺ") in config[bstack1l111l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ࢻ")]:
      bstack1lll11llll_opy_ = datetime.datetime.now()
      bstack11l11l1ll_opy_ = bstack1lll11llll_opy_.strftime(bstack1l111l1_opy_ (u"ࠪࠩࡩࡥࠥࡣࡡࠨࡌࠪࡓࠧࢼ"))
      hostname = socket.gethostname()
      bstack1ll111lll_opy_ = bstack1l111l1_opy_ (u"ࠫࠬࢽ").join(random.choices(string.ascii_lowercase + string.digits, k=4))
      identifier = bstack1l111l1_opy_ (u"ࠬࢁࡽࡠࡽࢀࡣࢀࢃࠧࢾ").format(bstack11l11l1ll_opy_, hostname, bstack1ll111lll_opy_)
      config[bstack1l111l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪࢿ")][bstack1l111l1_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩࣀ")] = identifier
    bstack1l1l11l111_opy_ = config[bstack1l111l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬࣁ")][bstack1l111l1_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫࣂ")]
  return config
def bstack1ll111l1_opy_():
  bstack11l1ll1ll_opy_ =  bstack11111l11l_opy_()[bstack1l111l1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠩࣃ")]
  return bstack11l1ll1ll_opy_ if bstack11l1ll1ll_opy_ else -1
def bstack11ll11111_opy_(bstack11l1ll1ll_opy_):
  global CONFIG
  if not bstack1l111l1_opy_ (u"ࠫࠩࢁࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࢂ࠭ࣄ") in CONFIG[bstack1l111l1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧࣅ")]:
    return
  CONFIG[bstack1l111l1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨࣆ")] = CONFIG[bstack1l111l1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩࣇ")].replace(
    bstack1l111l1_opy_ (u"ࠨࠦࡾࡆ࡚ࡏࡌࡅࡡࡑ࡙ࡒࡈࡅࡓࡿࠪࣈ"),
    str(bstack11l1ll1ll_opy_)
  )
def bstack1llllllll1_opy_():
  global CONFIG
  if not bstack1l111l1_opy_ (u"ࠩࠧࡿࡉࡇࡔࡆࡡࡗࡍࡒࡋࡽࠨࣉ") in CONFIG[bstack1l111l1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ࣊")]:
    return
  bstack1lll11llll_opy_ = datetime.datetime.now()
  bstack11l11l1ll_opy_ = bstack1lll11llll_opy_.strftime(bstack1l111l1_opy_ (u"ࠫࠪࡪ࠭ࠦࡤ࠰ࠩࡍࡀࠥࡎࠩ࣋"))
  CONFIG[bstack1l111l1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ࣌")] = CONFIG[bstack1l111l1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ࣍")].replace(
    bstack1l111l1_opy_ (u"ࠧࠥࡽࡇࡅ࡙ࡋ࡟ࡕࡋࡐࡉࢂ࠭࣎"),
    bstack11l11l1ll_opy_
  )
def bstack1llll11lll_opy_():
  global CONFIG
  if bstack1l111l1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴ࣏ࠪ") in CONFIG and not bool(CONFIG[bstack1l111l1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵ࣐ࠫ")]):
    del CONFIG[bstack1l111l1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶ࣑ࠬ")]
    return
  if not bstack1l111l1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࣒࠭") in CONFIG:
    CONFIG[bstack1l111l1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸ࣓ࠧ")] = bstack1l111l1_opy_ (u"࠭ࠣࠥࡽࡅ࡙ࡎࡒࡄࡠࡐࡘࡑࡇࡋࡒࡾࠩࣔ")
  if bstack1l111l1_opy_ (u"ࠧࠥࡽࡇࡅ࡙ࡋ࡟ࡕࡋࡐࡉࢂ࠭ࣕ") in CONFIG[bstack1l111l1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪࣖ")]:
    bstack1llllllll1_opy_()
    os.environ[bstack1l111l1_opy_ (u"ࠩࡅࡗ࡙ࡇࡃࡌࡡࡆࡓࡒࡈࡉࡏࡇࡇࡣࡇ࡛ࡉࡍࡆࡢࡍࡉ࠭ࣗ")] = CONFIG[bstack1l111l1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬࣘ")]
  if not bstack1l111l1_opy_ (u"ࠫࠩࢁࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࢂ࠭ࣙ") in CONFIG[bstack1l111l1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧࣚ")]:
    return
  bstack11l1ll1ll_opy_ = bstack1l111l1_opy_ (u"࠭ࠧࣛ")
  bstack1l111ll11_opy_ = bstack1ll111l1_opy_()
  if bstack1l111ll11_opy_ != -1:
    bstack11l1ll1ll_opy_ = bstack1l111l1_opy_ (u"ࠧࡄࡋࠣࠫࣜ") + str(bstack1l111ll11_opy_)
  if bstack11l1ll1ll_opy_ == bstack1l111l1_opy_ (u"ࠨࠩࣝ"):
    bstack1lllll11l1_opy_ = bstack1l1l11lll_opy_(CONFIG[bstack1l111l1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬࣞ")])
    if bstack1lllll11l1_opy_ != -1:
      bstack11l1ll1ll_opy_ = str(bstack1lllll11l1_opy_)
  if bstack11l1ll1ll_opy_:
    bstack11ll11111_opy_(bstack11l1ll1ll_opy_)
    os.environ[bstack1l111l1_opy_ (u"ࠪࡆࡘ࡚ࡁࡄࡍࡢࡇࡔࡓࡂࡊࡐࡈࡈࡤࡈࡕࡊࡎࡇࡣࡎࡊࠧࣟ")] = CONFIG[bstack1l111l1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭࣠")]
def bstack1l1l11ll_opy_(bstack1ll1ll1l1l_opy_, bstack1ll1l1ll_opy_, path):
  bstack111lll111_opy_ = {
    bstack1l111l1_opy_ (u"ࠬ࡯ࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ࣡"): bstack1ll1l1ll_opy_
  }
  if os.path.exists(path):
    bstack111l11ll1_opy_ = json.load(open(path, bstack1l111l1_opy_ (u"࠭ࡲࡣࠩ࣢")))
  else:
    bstack111l11ll1_opy_ = {}
  bstack111l11ll1_opy_[bstack1ll1ll1l1l_opy_] = bstack111lll111_opy_
  with open(path, bstack1l111l1_opy_ (u"ࠢࡸࣣ࠭ࠥ")) as outfile:
    json.dump(bstack111l11ll1_opy_, outfile)
def bstack1l1l11lll_opy_(bstack1ll1ll1l1l_opy_):
  bstack1ll1ll1l1l_opy_ = str(bstack1ll1ll1l1l_opy_)
  bstack11l111111_opy_ = os.path.join(os.path.expanduser(bstack1l111l1_opy_ (u"ࠨࢀࠪࣤ")), bstack1l111l1_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩࣥ"))
  try:
    if not os.path.exists(bstack11l111111_opy_):
      os.makedirs(bstack11l111111_opy_)
    file_path = os.path.join(os.path.expanduser(bstack1l111l1_opy_ (u"ࠪࢂࣦࠬ")), bstack1l111l1_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫࣧ"), bstack1l111l1_opy_ (u"ࠬ࠴ࡢࡶ࡫࡯ࡨ࠲ࡴࡡ࡮ࡧ࠰ࡧࡦࡩࡨࡦ࠰࡭ࡷࡴࡴࠧࣨ"))
    if not os.path.isfile(file_path):
      with open(file_path, bstack1l111l1_opy_ (u"࠭ࡷࠨࣩ")):
        pass
      with open(file_path, bstack1l111l1_opy_ (u"ࠢࡸ࠭ࠥ࣪")) as outfile:
        json.dump({}, outfile)
    with open(file_path, bstack1l111l1_opy_ (u"ࠨࡴࠪ࣫")) as bstack11ll1ll11_opy_:
      bstack11l11lll1_opy_ = json.load(bstack11ll1ll11_opy_)
    if bstack1ll1ll1l1l_opy_ in bstack11l11lll1_opy_:
      bstack11l11l111_opy_ = bstack11l11lll1_opy_[bstack1ll1ll1l1l_opy_][bstack1l111l1_opy_ (u"ࠩ࡬ࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭࣬")]
      bstack1lll1l11_opy_ = int(bstack11l11l111_opy_) + 1
      bstack1l1l11ll_opy_(bstack1ll1ll1l1l_opy_, bstack1lll1l11_opy_, file_path)
      return bstack1lll1l11_opy_
    else:
      bstack1l1l11ll_opy_(bstack1ll1ll1l1l_opy_, 1, file_path)
      return 1
  except Exception as e:
    logger.warn(bstack1l1111ll1_opy_.format(str(e)))
    return -1
def bstack1l111l1ll_opy_(config):
  if not config[bstack1l111l1_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩ࣭ࠬ")] or not config[bstack1l111l1_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿ࣮ࠧ")]:
    return True
  else:
    return False
def bstack1ll11lllll_opy_(config, index=0):
  global bstack1l1llll1l1_opy_
  bstack1ll1l11l1_opy_ = {}
  caps = bstack1l1llll1ll_opy_ + bstack1l1lll1l11_opy_
  if bstack1l1llll1l1_opy_:
    caps += bstack11ll1l11l_opy_
  for key in config:
    if key in caps + [bstack1l111l1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ࣯")]:
      continue
    bstack1ll1l11l1_opy_[key] = config[key]
  if bstack1l111l1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࣰࠩ") in config:
    for bstack1llll1ll_opy_ in config[bstack1l111l1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࣱࠪ")][index]:
      if bstack1llll1ll_opy_ in caps + [bstack1l111l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪࣲ࠭"), bstack1l111l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪࣳ")]:
        continue
      bstack1ll1l11l1_opy_[bstack1llll1ll_opy_] = config[bstack1l111l1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ࣴ")][index][bstack1llll1ll_opy_]
  bstack1ll1l11l1_opy_[bstack1l111l1_opy_ (u"ࠫ࡭ࡵࡳࡵࡐࡤࡱࡪ࠭ࣵ")] = socket.gethostname()
  if bstack1l111l1_opy_ (u"ࠬࡼࡥࡳࡵ࡬ࡳࡳࣶ࠭") in bstack1ll1l11l1_opy_:
    del (bstack1ll1l11l1_opy_[bstack1l111l1_opy_ (u"࠭ࡶࡦࡴࡶ࡭ࡴࡴࠧࣷ")])
  return bstack1ll1l11l1_opy_
def bstack1l1ll11l_opy_(config):
  global bstack1l1llll1l1_opy_
  bstack1l11ll11ll_opy_ = {}
  caps = bstack1l1lll1l11_opy_
  if bstack1l1llll1l1_opy_:
    caps += bstack11ll1l11l_opy_
  for key in caps:
    if key in config:
      bstack1l11ll11ll_opy_[key] = config[key]
  return bstack1l11ll11ll_opy_
def bstack11l111ll_opy_(bstack1ll1l11l1_opy_, bstack1l11ll11ll_opy_):
  bstack1l1ll1111l_opy_ = {}
  for key in bstack1ll1l11l1_opy_.keys():
    if key in bstack11l1111ll_opy_:
      bstack1l1ll1111l_opy_[bstack11l1111ll_opy_[key]] = bstack1ll1l11l1_opy_[key]
    else:
      bstack1l1ll1111l_opy_[key] = bstack1ll1l11l1_opy_[key]
  for key in bstack1l11ll11ll_opy_:
    if key in bstack11l1111ll_opy_:
      bstack1l1ll1111l_opy_[bstack11l1111ll_opy_[key]] = bstack1l11ll11ll_opy_[key]
    else:
      bstack1l1ll1111l_opy_[key] = bstack1l11ll11ll_opy_[key]
  return bstack1l1ll1111l_opy_
def bstack111ll1l1l_opy_(config, index=0):
  global bstack1l1llll1l1_opy_
  caps = {}
  config = copy.deepcopy(config)
  bstack1l1lll11l_opy_ = bstack1llll1lll1_opy_(bstack1l11ll1lll_opy_, config, logger)
  bstack1l11ll11ll_opy_ = bstack1l1ll11l_opy_(config)
  bstack1llll11l1l_opy_ = bstack1l1lll1l11_opy_
  bstack1llll11l1l_opy_ += bstack1lll1111l_opy_
  bstack1l11ll11ll_opy_ = update(bstack1l11ll11ll_opy_, bstack1l1lll11l_opy_)
  if bstack1l1llll1l1_opy_:
    bstack1llll11l1l_opy_ += bstack11ll1l11l_opy_
  if bstack1l111l1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪࣸ") in config:
    if bstack1l111l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪࣹ࠭") in config[bstack1l111l1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࣺࠬ")][index]:
      caps[bstack1l111l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨࣻ")] = config[bstack1l111l1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧࣼ")][index][bstack1l111l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪࣽ")]
    if bstack1l111l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧࣾ") in config[bstack1l111l1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪࣿ")][index]:
      caps[bstack1l111l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩऀ")] = str(config[bstack1l111l1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬँ")][index][bstack1l111l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫं")])
    bstack1l1ll111l1_opy_ = bstack1llll1lll1_opy_(bstack1l11ll1lll_opy_, config[bstack1l111l1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧः")][index], logger)
    bstack1llll11l1l_opy_ += list(bstack1l1ll111l1_opy_.keys())
    for bstack11l11111_opy_ in bstack1llll11l1l_opy_:
      if bstack11l11111_opy_ in config[bstack1l111l1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨऄ")][index]:
        if bstack11l11111_opy_ == bstack1l111l1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠨअ"):
          try:
            bstack1l1ll111l1_opy_[bstack11l11111_opy_] = str(config[bstack1l111l1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪआ")][index][bstack11l11111_opy_] * 1.0)
          except:
            bstack1l1ll111l1_opy_[bstack11l11111_opy_] = str(config[bstack1l111l1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫइ")][index][bstack11l11111_opy_])
        else:
          bstack1l1ll111l1_opy_[bstack11l11111_opy_] = config[bstack1l111l1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬई")][index][bstack11l11111_opy_]
        del (config[bstack1l111l1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭उ")][index][bstack11l11111_opy_])
    bstack1l11ll11ll_opy_ = update(bstack1l11ll11ll_opy_, bstack1l1ll111l1_opy_)
  bstack1ll1l11l1_opy_ = bstack1ll11lllll_opy_(config, index)
  for bstack111lllll1_opy_ in bstack1l1lll1l11_opy_ + [bstack1l111l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩऊ"), bstack1l111l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ऋ")] + list(bstack1l1lll11l_opy_.keys()):
    if bstack111lllll1_opy_ in bstack1ll1l11l1_opy_:
      bstack1l11ll11ll_opy_[bstack111lllll1_opy_] = bstack1ll1l11l1_opy_[bstack111lllll1_opy_]
      del (bstack1ll1l11l1_opy_[bstack111lllll1_opy_])
  if bstack111l11l1_opy_(config):
    bstack1ll1l11l1_opy_[bstack1l111l1_opy_ (u"࠭ࡵࡴࡧ࡚࠷ࡈ࠭ऌ")] = True
    caps.update(bstack1l11ll11ll_opy_)
    caps[bstack1l111l1_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨऍ")] = bstack1ll1l11l1_opy_
  else:
    bstack1ll1l11l1_opy_[bstack1l111l1_opy_ (u"ࠨࡷࡶࡩ࡜࠹ࡃࠨऎ")] = False
    caps.update(bstack11l111ll_opy_(bstack1ll1l11l1_opy_, bstack1l11ll11ll_opy_))
    if bstack1l111l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧए") in caps:
      caps[bstack1l111l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࠫऐ")] = caps[bstack1l111l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩऑ")]
      del (caps[bstack1l111l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪऒ")])
    if bstack1l111l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧओ") in caps:
      caps[bstack1l111l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡠࡸࡨࡶࡸ࡯࡯࡯ࠩऔ")] = caps[bstack1l111l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩक")]
      del (caps[bstack1l111l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪख")])
  return caps
def bstack11ll1l1l1_opy_():
  global bstack1l1l11111_opy_
  if bstack1l1ll11lll_opy_() <= version.parse(bstack1l111l1_opy_ (u"ࠪ࠷࠳࠷࠳࠯࠲ࠪग")):
    if bstack1l1l11111_opy_ != bstack1l111l1_opy_ (u"ࠫࠬघ"):
      return bstack1l111l1_opy_ (u"ࠧ࡮ࡴࡵࡲ࠽࠳࠴ࠨङ") + bstack1l1l11111_opy_ + bstack1l111l1_opy_ (u"ࠨ࠺࠹࠲࠲ࡻࡩ࠵ࡨࡶࡤࠥच")
    return bstack1111l1l11_opy_
  if bstack1l1l11111_opy_ != bstack1l111l1_opy_ (u"ࠧࠨछ"):
    return bstack1l111l1_opy_ (u"ࠣࡪࡷࡸࡵࡹ࠺࠰࠱ࠥज") + bstack1l1l11111_opy_ + bstack1l111l1_opy_ (u"ࠤ࠲ࡻࡩ࠵ࡨࡶࡤࠥझ")
  return bstack1l11l1ll_opy_
def bstack1lllll1l1l_opy_(options):
  return hasattr(options, bstack1l111l1_opy_ (u"ࠪࡷࡪࡺ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶࡼࠫञ"))
def update(d, u):
  for k, v in u.items():
    if isinstance(v, collections.abc.Mapping):
      d[k] = update(d.get(k, {}), v)
    else:
      if isinstance(v, list):
        d[k] = d.get(k, []) + v
      else:
        d[k] = v
  return d
def bstack11l1l1l1_opy_(options, bstack111111l11_opy_):
  for bstack1llll111l_opy_ in bstack111111l11_opy_:
    if bstack1llll111l_opy_ in [bstack1l111l1_opy_ (u"ࠫࡦࡸࡧࡴࠩट"), bstack1l111l1_opy_ (u"ࠬ࡫ࡸࡵࡧࡱࡷ࡮ࡵ࡮ࡴࠩठ")]:
      continue
    if bstack1llll111l_opy_ in options._experimental_options:
      options._experimental_options[bstack1llll111l_opy_] = update(options._experimental_options[bstack1llll111l_opy_],
                                                         bstack111111l11_opy_[bstack1llll111l_opy_])
    else:
      options.add_experimental_option(bstack1llll111l_opy_, bstack111111l11_opy_[bstack1llll111l_opy_])
  if bstack1l111l1_opy_ (u"࠭ࡡࡳࡩࡶࠫड") in bstack111111l11_opy_:
    for arg in bstack111111l11_opy_[bstack1l111l1_opy_ (u"ࠧࡢࡴࡪࡷࠬढ")]:
      options.add_argument(arg)
    del (bstack111111l11_opy_[bstack1l111l1_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭ण")])
  if bstack1l111l1_opy_ (u"ࠩࡨࡼࡹ࡫࡮ࡴ࡫ࡲࡲࡸ࠭त") in bstack111111l11_opy_:
    for ext in bstack111111l11_opy_[bstack1l111l1_opy_ (u"ࠪࡩࡽࡺࡥ࡯ࡵ࡬ࡳࡳࡹࠧथ")]:
      options.add_extension(ext)
    del (bstack111111l11_opy_[bstack1l111l1_opy_ (u"ࠫࡪࡾࡴࡦࡰࡶ࡭ࡴࡴࡳࠨद")])
def bstack1l1l11l1l_opy_(options, bstack11ll1l11_opy_):
  if bstack1l111l1_opy_ (u"ࠬࡶࡲࡦࡨࡶࠫध") in bstack11ll1l11_opy_:
    for bstack1l1ll1l11_opy_ in bstack11ll1l11_opy_[bstack1l111l1_opy_ (u"࠭ࡰࡳࡧࡩࡷࠬन")]:
      if bstack1l1ll1l11_opy_ in options._preferences:
        options._preferences[bstack1l1ll1l11_opy_] = update(options._preferences[bstack1l1ll1l11_opy_], bstack11ll1l11_opy_[bstack1l111l1_opy_ (u"ࠧࡱࡴࡨࡪࡸ࠭ऩ")][bstack1l1ll1l11_opy_])
      else:
        options.set_preference(bstack1l1ll1l11_opy_, bstack11ll1l11_opy_[bstack1l111l1_opy_ (u"ࠨࡲࡵࡩ࡫ࡹࠧप")][bstack1l1ll1l11_opy_])
  if bstack1l111l1_opy_ (u"ࠩࡤࡶ࡬ࡹࠧफ") in bstack11ll1l11_opy_:
    for arg in bstack11ll1l11_opy_[bstack1l111l1_opy_ (u"ࠪࡥࡷ࡭ࡳࠨब")]:
      options.add_argument(arg)
def bstack1l1l1l1111_opy_(options, bstack1l1lll1ll1_opy_):
  if bstack1l111l1_opy_ (u"ࠫࡼ࡫ࡢࡷ࡫ࡨࡻࠬभ") in bstack1l1lll1ll1_opy_:
    options.use_webview(bool(bstack1l1lll1ll1_opy_[bstack1l111l1_opy_ (u"ࠬࡽࡥࡣࡸ࡬ࡩࡼ࠭म")]))
  bstack11l1l1l1_opy_(options, bstack1l1lll1ll1_opy_)
def bstack11l1lll11_opy_(options, bstack1l111l111_opy_):
  for bstack1ll1lll1ll_opy_ in bstack1l111l111_opy_:
    if bstack1ll1lll1ll_opy_ in [bstack1l111l1_opy_ (u"࠭ࡴࡦࡥ࡫ࡲࡴࡲ࡯ࡨࡻࡓࡶࡪࡼࡩࡦࡹࠪय"), bstack1l111l1_opy_ (u"ࠧࡢࡴࡪࡷࠬर")]:
      continue
    options.set_capability(bstack1ll1lll1ll_opy_, bstack1l111l111_opy_[bstack1ll1lll1ll_opy_])
  if bstack1l111l1_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭ऱ") in bstack1l111l111_opy_:
    for arg in bstack1l111l111_opy_[bstack1l111l1_opy_ (u"ࠩࡤࡶ࡬ࡹࠧल")]:
      options.add_argument(arg)
  if bstack1l111l1_opy_ (u"ࠪࡸࡪࡩࡨ࡯ࡱ࡯ࡳ࡬ࡿࡐࡳࡧࡹ࡭ࡪࡽࠧळ") in bstack1l111l111_opy_:
    options.bstack1llllllll_opy_(bool(bstack1l111l111_opy_[bstack1l111l1_opy_ (u"ࠫࡹ࡫ࡣࡩࡰࡲࡰࡴ࡭ࡹࡑࡴࡨࡺ࡮࡫ࡷࠨऴ")]))
def bstack1111l111l_opy_(options, bstack1lll1lllll_opy_):
  for bstack1llll1l11_opy_ in bstack1lll1lllll_opy_:
    if bstack1llll1l11_opy_ in [bstack1l111l1_opy_ (u"ࠬࡧࡤࡥ࡫ࡷ࡭ࡴࡴࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩव"), bstack1l111l1_opy_ (u"࠭ࡡࡳࡩࡶࠫश")]:
      continue
    options._options[bstack1llll1l11_opy_] = bstack1lll1lllll_opy_[bstack1llll1l11_opy_]
  if bstack1l111l1_opy_ (u"ࠧࡢࡦࡧ࡭ࡹ࡯࡯࡯ࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫष") in bstack1lll1lllll_opy_:
    for bstack1l111l1l1_opy_ in bstack1lll1lllll_opy_[bstack1l111l1_opy_ (u"ࠨࡣࡧࡨ࡮ࡺࡩࡰࡰࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬस")]:
      options.bstack1l1l1llll1_opy_(
        bstack1l111l1l1_opy_, bstack1lll1lllll_opy_[bstack1l111l1_opy_ (u"ࠩࡤࡨࡩ࡯ࡴࡪࡱࡱࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ह")][bstack1l111l1l1_opy_])
  if bstack1l111l1_opy_ (u"ࠪࡥࡷ࡭ࡳࠨऺ") in bstack1lll1lllll_opy_:
    for arg in bstack1lll1lllll_opy_[bstack1l111l1_opy_ (u"ࠫࡦࡸࡧࡴࠩऻ")]:
      options.add_argument(arg)
def bstack11111l1l1_opy_(options, caps):
  if not hasattr(options, bstack1l111l1_opy_ (u"ࠬࡑࡅ़࡚ࠩ")):
    return
  if options.KEY == bstack1l111l1_opy_ (u"࠭ࡧࡰࡱࡪ࠾ࡨ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠫऽ") and options.KEY in caps:
    bstack11l1l1l1_opy_(options, caps[bstack1l111l1_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬा")])
  elif options.KEY == bstack1l111l1_opy_ (u"ࠨ࡯ࡲࡾ࠿࡬ࡩࡳࡧࡩࡳࡽࡕࡰࡵ࡫ࡲࡲࡸ࠭ि") and options.KEY in caps:
    bstack1l1l11l1l_opy_(options, caps[bstack1l111l1_opy_ (u"ࠩࡰࡳࡿࡀࡦࡪࡴࡨࡪࡴࡾࡏࡱࡶ࡬ࡳࡳࡹࠧी")])
  elif options.KEY == bstack1l111l1_opy_ (u"ࠪࡷࡦ࡬ࡡࡳ࡫࠱ࡳࡵࡺࡩࡰࡰࡶࠫु") and options.KEY in caps:
    bstack11l1lll11_opy_(options, caps[bstack1l111l1_opy_ (u"ࠫࡸࡧࡦࡢࡴ࡬࠲ࡴࡶࡴࡪࡱࡱࡷࠬू")])
  elif options.KEY == bstack1l111l1_opy_ (u"ࠬࡳࡳ࠻ࡧࡧ࡫ࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭ृ") and options.KEY in caps:
    bstack1l1l1l1111_opy_(options, caps[bstack1l111l1_opy_ (u"࠭࡭ࡴ࠼ࡨࡨ࡬࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧॄ")])
  elif options.KEY == bstack1l111l1_opy_ (u"ࠧࡴࡧ࠽࡭ࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭ॅ") and options.KEY in caps:
    bstack1111l111l_opy_(options, caps[bstack1l111l1_opy_ (u"ࠨࡵࡨ࠾࡮࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧॆ")])
def bstack1111l11l_opy_(caps):
  global bstack1l1llll1l1_opy_
  if isinstance(os.environ.get(bstack1l111l1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡋࡖࡣࡆࡖࡐࡠࡃࡘࡘࡔࡓࡁࡕࡇࠪे")), str):
    bstack1l1llll1l1_opy_ = eval(os.getenv(bstack1l111l1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡌࡗࡤࡇࡐࡑࡡࡄ࡙࡙ࡕࡍࡂࡖࡈࠫै")))
  if bstack1l1llll1l1_opy_:
    if bstack111l1111l_opy_() < version.parse(bstack1l111l1_opy_ (u"ࠫ࠷࠴࠳࠯࠲ࠪॉ")):
      return None
    else:
      from appium.options.common.base import AppiumOptions
      options = AppiumOptions().load_capabilities(caps)
      return options
  else:
    browser = bstack1l111l1_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࠬॊ")
    if bstack1l111l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫो") in caps:
      browser = caps[bstack1l111l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬौ")]
    elif bstack1l111l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳ्ࠩ") in caps:
      browser = caps[bstack1l111l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࠪॎ")]
    browser = str(browser).lower()
    if browser == bstack1l111l1_opy_ (u"ࠪ࡭ࡵ࡮࡯࡯ࡧࠪॏ") or browser == bstack1l111l1_opy_ (u"ࠫ࡮ࡶࡡࡥࠩॐ"):
      browser = bstack1l111l1_opy_ (u"ࠬࡹࡡࡧࡣࡵ࡭ࠬ॑")
    if browser == bstack1l111l1_opy_ (u"࠭ࡳࡢ࡯ࡶࡹࡳ࡭॒ࠧ"):
      browser = bstack1l111l1_opy_ (u"ࠧࡤࡪࡵࡳࡲ࡫ࠧ॓")
    if browser not in [bstack1l111l1_opy_ (u"ࠨࡥ࡫ࡶࡴࡳࡥࠨ॔"), bstack1l111l1_opy_ (u"ࠩࡨࡨ࡬࡫ࠧॕ"), bstack1l111l1_opy_ (u"ࠪ࡭ࡪ࠭ॖ"), bstack1l111l1_opy_ (u"ࠫࡸࡧࡦࡢࡴ࡬ࠫॗ"), bstack1l111l1_opy_ (u"ࠬ࡬ࡩࡳࡧࡩࡳࡽ࠭क़")]:
      return None
    try:
      package = bstack1l111l1_opy_ (u"࠭ࡳࡦ࡮ࡨࡲ࡮ࡻ࡭࠯ࡹࡨࡦࡩࡸࡩࡷࡧࡵ࠲ࢀࢃ࠮ࡰࡲࡷ࡭ࡴࡴࡳࠨख़").format(browser)
      name = bstack1l111l1_opy_ (u"ࠧࡐࡲࡷ࡭ࡴࡴࡳࠨग़")
      browser_options = getattr(__import__(package, fromlist=[name]), name)
      options = browser_options()
      if not bstack1lllll1l1l_opy_(options):
        return None
      for bstack111lllll1_opy_ in caps.keys():
        options.set_capability(bstack111lllll1_opy_, caps[bstack111lllll1_opy_])
      bstack11111l1l1_opy_(options, caps)
      return options
    except Exception as e:
      logger.debug(str(e))
      return None
def bstack1l11l1llll_opy_(options, bstack1l1ll111_opy_):
  if not bstack1lllll1l1l_opy_(options):
    return
  for bstack111lllll1_opy_ in bstack1l1ll111_opy_.keys():
    if bstack111lllll1_opy_ in bstack1lll1111l_opy_:
      continue
    if bstack111lllll1_opy_ in options._caps and type(options._caps[bstack111lllll1_opy_]) in [dict, list]:
      options._caps[bstack111lllll1_opy_] = update(options._caps[bstack111lllll1_opy_], bstack1l1ll111_opy_[bstack111lllll1_opy_])
    else:
      options.set_capability(bstack111lllll1_opy_, bstack1l1ll111_opy_[bstack111lllll1_opy_])
  bstack11111l1l1_opy_(options, bstack1l1ll111_opy_)
  if bstack1l111l1_opy_ (u"ࠨ࡯ࡲࡾ࠿ࡪࡥࡣࡷࡪ࡫ࡪࡸࡁࡥࡦࡵࡩࡸࡹࠧज़") in options._caps:
    if options._caps[bstack1l111l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧड़")] and options._caps[bstack1l111l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨढ़")].lower() != bstack1l111l1_opy_ (u"ࠫ࡫࡯ࡲࡦࡨࡲࡼࠬफ़"):
      del options._caps[bstack1l111l1_opy_ (u"ࠬࡳ࡯ࡻ࠼ࡧࡩࡧࡻࡧࡨࡧࡵࡅࡩࡪࡲࡦࡵࡶࠫय़")]
def bstack1ll1l1ll11_opy_(proxy_config):
  if bstack1l111l1_opy_ (u"࠭ࡨࡵࡶࡳࡷࡕࡸ࡯ࡹࡻࠪॠ") in proxy_config:
    proxy_config[bstack1l111l1_opy_ (u"ࠧࡴࡵ࡯ࡔࡷࡵࡸࡺࠩॡ")] = proxy_config[bstack1l111l1_opy_ (u"ࠨࡪࡷࡸࡵࡹࡐࡳࡱࡻࡽࠬॢ")]
    del (proxy_config[bstack1l111l1_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࡑࡴࡲࡼࡾ࠭ॣ")])
  if bstack1l111l1_opy_ (u"ࠪࡴࡷࡵࡸࡺࡖࡼࡴࡪ࠭।") in proxy_config and proxy_config[bstack1l111l1_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡗࡽࡵ࡫ࠧ॥")].lower() != bstack1l111l1_opy_ (u"ࠬࡪࡩࡳࡧࡦࡸࠬ०"):
    proxy_config[bstack1l111l1_opy_ (u"࠭ࡰࡳࡱࡻࡽ࡙ࡿࡰࡦࠩ१")] = bstack1l111l1_opy_ (u"ࠧ࡮ࡣࡱࡹࡦࡲࠧ२")
  if bstack1l111l1_opy_ (u"ࠨࡲࡵࡳࡽࡿࡁࡶࡶࡲࡧࡴࡴࡦࡪࡩࡘࡶࡱ࠭३") in proxy_config:
    proxy_config[bstack1l111l1_opy_ (u"ࠩࡳࡶࡴࡾࡹࡕࡻࡳࡩࠬ४")] = bstack1l111l1_opy_ (u"ࠪࡴࡦࡩࠧ५")
  return proxy_config
def bstack1l1lll11ll_opy_(config, proxy):
  from selenium.webdriver.common.proxy import Proxy
  if not bstack1l111l1_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࠪ६") in config:
    return proxy
  config[bstack1l111l1_opy_ (u"ࠬࡶࡲࡰࡺࡼࠫ७")] = bstack1ll1l1ll11_opy_(config[bstack1l111l1_opy_ (u"࠭ࡰࡳࡱࡻࡽࠬ८")])
  if proxy == None:
    proxy = Proxy(config[bstack1l111l1_opy_ (u"ࠧࡱࡴࡲࡼࡾ࠭९")])
  return proxy
def bstack1l1lll1111_opy_(self):
  global CONFIG
  global bstack11111lll1_opy_
  try:
    proxy = bstack1l11l1ll1l_opy_(CONFIG)
    if proxy:
      if proxy.endswith(bstack1l111l1_opy_ (u"ࠨ࠰ࡳࡥࡨ࠭॰")):
        proxies = bstack11l1l1111_opy_(proxy, bstack11ll1l1l1_opy_())
        if len(proxies) > 0:
          protocol, bstack1ll11llll_opy_ = proxies.popitem()
          if bstack1l111l1_opy_ (u"ࠤ࠽࠳࠴ࠨॱ") in bstack1ll11llll_opy_:
            return bstack1ll11llll_opy_
          else:
            return bstack1l111l1_opy_ (u"ࠥ࡬ࡹࡺࡰ࠻࠱࠲ࠦॲ") + bstack1ll11llll_opy_
      else:
        return proxy
  except Exception as e:
    logger.error(bstack1l111l1_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡳࡦࡶࡷ࡭ࡳ࡭ࠠࡱࡴࡲࡼࡾࠦࡵࡳ࡮ࠣ࠾ࠥࢁࡽࠣॳ").format(str(e)))
  return bstack11111lll1_opy_(self)
def bstack1l1l1lll1_opy_():
  global CONFIG
  return bstack1l1ll1lll1_opy_(CONFIG) and bstack1l1111l11_opy_() and bstack1l1ll11lll_opy_() >= version.parse(bstack1l1l1l1l1l_opy_)
def bstack1lll111l1_opy_():
  global CONFIG
  return (bstack1l111l1_opy_ (u"ࠬ࡮ࡴࡵࡲࡓࡶࡴࡾࡹࠨॴ") in CONFIG or bstack1l111l1_opy_ (u"࠭ࡨࡵࡶࡳࡷࡕࡸ࡯ࡹࡻࠪॵ") in CONFIG) and bstack1l1lll1lll_opy_()
def bstack11111lll_opy_(config):
  bstack111111l1l_opy_ = {}
  if bstack1l111l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫॶ") in config:
    bstack111111l1l_opy_ = config[bstack1l111l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬॷ")]
  if bstack1l111l1_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨॸ") in config:
    bstack111111l1l_opy_ = config[bstack1l111l1_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩॹ")]
  proxy = bstack1l11l1ll1l_opy_(config)
  if proxy:
    if proxy.endswith(bstack1l111l1_opy_ (u"ࠫ࠳ࡶࡡࡤࠩॺ")) and os.path.isfile(proxy):
      bstack111111l1l_opy_[bstack1l111l1_opy_ (u"ࠬ࠳ࡰࡢࡥ࠰ࡪ࡮ࡲࡥࠨॻ")] = proxy
    else:
      parsed_url = None
      if proxy.endswith(bstack1l111l1_opy_ (u"࠭࠮ࡱࡣࡦࠫॼ")):
        proxies = bstack1l1ll1ll_opy_(config, bstack11ll1l1l1_opy_())
        if len(proxies) > 0:
          protocol, bstack1ll11llll_opy_ = proxies.popitem()
          if bstack1l111l1_opy_ (u"ࠢ࠻࠱࠲ࠦॽ") in bstack1ll11llll_opy_:
            parsed_url = urlparse(bstack1ll11llll_opy_)
          else:
            parsed_url = urlparse(protocol + bstack1l111l1_opy_ (u"ࠣ࠼࠲࠳ࠧॾ") + bstack1ll11llll_opy_)
      else:
        parsed_url = urlparse(proxy)
      if parsed_url and parsed_url.hostname: bstack111111l1l_opy_[bstack1l111l1_opy_ (u"ࠩࡳࡶࡴࡾࡹࡉࡱࡶࡸࠬॿ")] = str(parsed_url.hostname)
      if parsed_url and parsed_url.port: bstack111111l1l_opy_[bstack1l111l1_opy_ (u"ࠪࡴࡷࡵࡸࡺࡒࡲࡶࡹ࠭ঀ")] = str(parsed_url.port)
      if parsed_url and parsed_url.username: bstack111111l1l_opy_[bstack1l111l1_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡘࡷࡪࡸࠧঁ")] = str(parsed_url.username)
      if parsed_url and parsed_url.password: bstack111111l1l_opy_[bstack1l111l1_opy_ (u"ࠬࡶࡲࡰࡺࡼࡔࡦࡹࡳࠨং")] = str(parsed_url.password)
  return bstack111111l1l_opy_
def bstack1lllllll11_opy_(config):
  if bstack1l111l1_opy_ (u"࠭ࡴࡦࡵࡷࡇࡴࡴࡴࡦࡺࡷࡓࡵࡺࡩࡰࡰࡶࠫঃ") in config:
    return config[bstack1l111l1_opy_ (u"ࠧࡵࡧࡶࡸࡈࡵ࡮ࡵࡧࡻࡸࡔࡶࡴࡪࡱࡱࡷࠬ঄")]
  return {}
def bstack111ll1111_opy_(caps):
  global bstack1l1l11l111_opy_
  if bstack1l111l1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩঅ") in caps:
    caps[bstack1l111l1_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪআ")][bstack1l111l1_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࠩই")] = True
    if bstack1l1l11l111_opy_:
      caps[bstack1l111l1_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬঈ")][bstack1l111l1_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧউ")] = bstack1l1l11l111_opy_
  else:
    caps[bstack1l111l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡲ࡯ࡤࡣ࡯ࠫঊ")] = True
    if bstack1l1l11l111_opy_:
      caps[bstack1l111l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨঋ")] = bstack1l1l11l111_opy_
def bstack1l1l1111_opy_():
  global CONFIG
  if bstack1l111l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬঌ") in CONFIG and bstack1l1l1ll111_opy_(CONFIG[bstack1l111l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭঍")]):
    bstack111111l1l_opy_ = bstack11111lll_opy_(CONFIG)
    bstack1ll11ll111_opy_(CONFIG[bstack1l111l1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭঎")], bstack111111l1l_opy_)
def bstack1ll11ll111_opy_(key, bstack111111l1l_opy_):
  global bstack1l11lll111_opy_
  logger.info(bstack1l11ll111_opy_)
  try:
    bstack1l11lll111_opy_ = Local()
    bstack1ll1lllll1_opy_ = {bstack1l111l1_opy_ (u"ࠫࡰ࡫ࡹࠨএ"): key}
    bstack1ll1lllll1_opy_.update(bstack111111l1l_opy_)
    logger.debug(bstack1lllll111l_opy_.format(str(bstack1ll1lllll1_opy_)))
    bstack1l11lll111_opy_.start(**bstack1ll1lllll1_opy_)
    if bstack1l11lll111_opy_.isRunning():
      logger.info(bstack1lll1111l1_opy_)
  except Exception as e:
    bstack11lll1l11_opy_(bstack111l1ll11_opy_.format(str(e)))
def bstack1llll1lll_opy_():
  global bstack1l11lll111_opy_
  if bstack1l11lll111_opy_.isRunning():
    logger.info(bstack11ll11ll1_opy_)
    bstack1l11lll111_opy_.stop()
  bstack1l11lll111_opy_ = None
def bstack1l1llll1_opy_(bstack1l11l1lll_opy_=[]):
  global CONFIG
  bstack11ll1111l_opy_ = []
  bstack1llllll11l_opy_ = [bstack1l111l1_opy_ (u"ࠬࡵࡳࠨঐ"), bstack1l111l1_opy_ (u"࠭࡯ࡴࡘࡨࡶࡸ࡯࡯࡯ࠩ঑"), bstack1l111l1_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࡎࡢ࡯ࡨࠫ঒"), bstack1l111l1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯࡙ࡩࡷࡹࡩࡰࡰࠪও"), bstack1l111l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧঔ"), bstack1l111l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫক")]
  try:
    for err in bstack1l11l1lll_opy_:
      bstack1l1l1l1l11_opy_ = {}
      for k in bstack1llllll11l_opy_:
        val = CONFIG[bstack1l111l1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧখ")][int(err[bstack1l111l1_opy_ (u"ࠬ࡯࡮ࡥࡧࡻࠫগ")])].get(k)
        if val:
          bstack1l1l1l1l11_opy_[k] = val
      if(err[bstack1l111l1_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬঘ")] != bstack1l111l1_opy_ (u"ࠧࠨঙ")):
        bstack1l1l1l1l11_opy_[bstack1l111l1_opy_ (u"ࠨࡶࡨࡷࡹࡹࠧচ")] = {
          err[bstack1l111l1_opy_ (u"ࠩࡱࡥࡲ࡫ࠧছ")]: err[bstack1l111l1_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩজ")]
        }
        bstack11ll1111l_opy_.append(bstack1l1l1l1l11_opy_)
  except Exception as e:
    logger.debug(bstack1l111l1_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡦࡰࡴࡰࡥࡹࡺࡩ࡯ࡩࠣࡨࡦࡺࡡࠡࡨࡲࡶࠥ࡫ࡶࡦࡰࡷ࠾ࠥ࠭ঝ") + str(e))
  finally:
    return bstack11ll1111l_opy_
def bstack11llllll_opy_(file_name):
  bstack11ll1lll1_opy_ = []
  try:
    bstack1lll1l11l1_opy_ = os.path.join(tempfile.gettempdir(), file_name)
    if os.path.exists(bstack1lll1l11l1_opy_):
      with open(bstack1lll1l11l1_opy_) as f:
        bstack1l1ll11ll_opy_ = json.load(f)
        bstack11ll1lll1_opy_ = bstack1l1ll11ll_opy_
      os.remove(bstack1lll1l11l1_opy_)
    return bstack11ll1lll1_opy_
  except Exception as e:
    logger.debug(bstack1l111l1_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡧ࡫ࡱࡨ࡮ࡴࡧࠡࡧࡵࡶࡴࡸࠠ࡭࡫ࡶࡸ࠿ࠦࠧঞ") + str(e))
def bstack1l1lll111l_opy_():
  global bstack1lll1llll1_opy_
  global bstack11lll1l1_opy_
  global bstack11l1111l_opy_
  global bstack1lll1lll1_opy_
  global bstack1lllll1ll1_opy_
  global bstack11lll111_opy_
  global CONFIG
  percy.shutdown()
  bstack11l1l11l_opy_ = os.environ.get(bstack1l111l1_opy_ (u"࠭ࡆࡓࡃࡐࡉ࡜ࡕࡒࡌࡡࡘࡗࡊࡊࠧট"))
  if bstack11l1l11l_opy_ in [bstack1l111l1_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭ঠ"), bstack1l111l1_opy_ (u"ࠨࡲࡤࡦࡴࡺࠧড")]:
    bstack111111ll_opy_()
  if bstack1lll1llll1_opy_:
    logger.warning(bstack1l1ll111l_opy_.format(str(bstack1lll1llll1_opy_)))
  else:
    try:
      bstack111l11ll1_opy_ = bstack11lllllll_opy_(bstack1l111l1_opy_ (u"ࠩ࠱ࡦࡸࡺࡡࡤ࡭࠰ࡧࡴࡴࡦࡪࡩ࠱࡮ࡸࡵ࡮ࠨঢ"), logger)
      if bstack111l11ll1_opy_.get(bstack1l111l1_opy_ (u"ࠪࡲࡺࡪࡧࡦࡡ࡯ࡳࡨࡧ࡬ࠨণ")) and bstack111l11ll1_opy_.get(bstack1l111l1_opy_ (u"ࠫࡳࡻࡤࡨࡧࡢࡰࡴࡩࡡ࡭ࠩত")).get(bstack1l111l1_opy_ (u"ࠬ࡮࡯ࡴࡶࡱࡥࡲ࡫ࠧথ")):
        logger.warning(bstack1l1ll111l_opy_.format(str(bstack111l11ll1_opy_[bstack1l111l1_opy_ (u"࠭࡮ࡶࡦࡪࡩࡤࡲ࡯ࡤࡣ࡯ࠫদ")][bstack1l111l1_opy_ (u"ࠧࡩࡱࡶࡸࡳࡧ࡭ࡦࠩধ")])))
    except Exception as e:
      logger.error(e)
  logger.info(bstack1ll11llll1_opy_)
  global bstack1l11lll111_opy_
  if bstack1l11lll111_opy_:
    bstack1llll1lll_opy_()
  try:
    for driver in bstack11lll1l1_opy_:
      driver.quit()
  except Exception as e:
    pass
  logger.info(bstack1lll1lll_opy_)
  if bstack11lll111_opy_ == bstack1l111l1_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧন"):
    bstack1lllll1ll1_opy_ = bstack11llllll_opy_(bstack1l111l1_opy_ (u"ࠩࡵࡳࡧࡵࡴࡠࡧࡵࡶࡴࡸ࡟࡭࡫ࡶࡸ࠳ࡰࡳࡰࡰࠪ঩"))
  if bstack11lll111_opy_ == bstack1l111l1_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪপ") and len(bstack1lll1lll1_opy_) == 0:
    bstack1lll1lll1_opy_ = bstack11llllll_opy_(bstack1l111l1_opy_ (u"ࠫࡵࡽ࡟ࡱࡻࡷࡩࡸࡺ࡟ࡦࡴࡵࡳࡷࡥ࡬ࡪࡵࡷ࠲࡯ࡹ࡯࡯ࠩফ"))
    if len(bstack1lll1lll1_opy_) == 0:
      bstack1lll1lll1_opy_ = bstack11llllll_opy_(bstack1l111l1_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࡤࡶࡰࡱࡡࡨࡶࡷࡵࡲࡠ࡮࡬ࡷࡹ࠴ࡪࡴࡱࡱࠫব"))
  bstack1l1l11lll1_opy_ = bstack1l111l1_opy_ (u"࠭ࠧভ")
  if len(bstack11l1111l_opy_) > 0:
    bstack1l1l11lll1_opy_ = bstack1l1llll1_opy_(bstack11l1111l_opy_)
  elif len(bstack1lll1lll1_opy_) > 0:
    bstack1l1l11lll1_opy_ = bstack1l1llll1_opy_(bstack1lll1lll1_opy_)
  elif len(bstack1lllll1ll1_opy_) > 0:
    bstack1l1l11lll1_opy_ = bstack1l1llll1_opy_(bstack1lllll1ll1_opy_)
  elif len(bstack1l111lll1_opy_) > 0:
    bstack1l1l11lll1_opy_ = bstack1l1llll1_opy_(bstack1l111lll1_opy_)
  if bool(bstack1l1l11lll1_opy_):
    bstack1l11lll11l_opy_(bstack1l1l11lll1_opy_)
  else:
    bstack1l11lll11l_opy_()
  bstack1lll1lll11_opy_(bstack1lll1lll1l_opy_, logger)
  bstack1ll111l1l1_opy_.bstack1lll1ll111_opy_(CONFIG)
def bstack1l1l1l1l_opy_(self, *args):
  logger.error(bstack11l1ll111_opy_)
  bstack1l1lll111l_opy_()
  sys.exit(1)
def bstack11lll1l11_opy_(err):
  logger.critical(bstack1ll1111l1_opy_.format(str(err)))
  bstack1l11lll11l_opy_(bstack1ll1111l1_opy_.format(str(err)), True)
  atexit.unregister(bstack1l1lll111l_opy_)
  bstack111111ll_opy_()
  sys.exit(1)
def bstack111l11l1l_opy_(error, message):
  logger.critical(str(error))
  logger.critical(message)
  bstack1l11lll11l_opy_(message, True)
  atexit.unregister(bstack1l1lll111l_opy_)
  bstack111111ll_opy_()
  sys.exit(1)
def bstack1ll1llll1l_opy_():
  global CONFIG
  global bstack1111lllll_opy_
  global bstack1lll11ll11_opy_
  global bstack1lll1l1lll_opy_
  CONFIG = bstack1l1l11l1l1_opy_()
  load_dotenv(CONFIG.get(bstack1l111l1_opy_ (u"ࠧࡦࡰࡹࡊ࡮ࡲࡥࠨম")))
  bstack111llll11_opy_()
  bstack1ll1111l_opy_()
  CONFIG = bstack11l1ll1l1_opy_(CONFIG)
  update(CONFIG, bstack1lll11ll11_opy_)
  update(CONFIG, bstack1111lllll_opy_)
  CONFIG = bstack1lll111l11_opy_(CONFIG)
  bstack1lll1l1lll_opy_ = bstack1ll1l1ll1l_opy_(CONFIG)
  bstack11111111_opy_.bstack111ll1ll_opy_(bstack1l111l1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡠࡵࡨࡷࡸ࡯࡯࡯ࠩয"), bstack1lll1l1lll_opy_)
  if (bstack1l111l1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬর") in CONFIG and bstack1l111l1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭঱") in bstack1111lllll_opy_) or (
          bstack1l111l1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧল") in CONFIG and bstack1l111l1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨ঳") not in bstack1lll11ll11_opy_):
    if os.getenv(bstack1l111l1_opy_ (u"࠭ࡂࡔࡖࡄࡇࡐࡥࡃࡐࡏࡅࡍࡓࡋࡄࡠࡄࡘࡍࡑࡊ࡟ࡊࡆࠪ঴")):
      CONFIG[bstack1l111l1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ঵")] = os.getenv(bstack1l111l1_opy_ (u"ࠨࡄࡖࡘࡆࡉࡋࡠࡅࡒࡑࡇࡏࡎࡆࡆࡢࡆ࡚ࡏࡌࡅࡡࡌࡈࠬশ"))
    else:
      bstack1llll11lll_opy_()
  elif (bstack1l111l1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬষ") not in CONFIG and bstack1l111l1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬস") in CONFIG) or (
          bstack1l111l1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧহ") in bstack1lll11ll11_opy_ and bstack1l111l1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨ঺") not in bstack1111lllll_opy_):
    del (CONFIG[bstack1l111l1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ঻")])
  if bstack1l111l1ll_opy_(CONFIG):
    bstack11lll1l11_opy_(bstack111ll1ll1_opy_)
  bstack11ll11ll_opy_()
  bstack1111l111_opy_()
  if bstack1l1llll1l1_opy_:
    CONFIG[bstack1l111l1_opy_ (u"ࠧࡢࡲࡳ়ࠫ")] = bstack1lll1ll1ll_opy_(CONFIG)
    logger.info(bstack1ll1ll1l_opy_.format(CONFIG[bstack1l111l1_opy_ (u"ࠨࡣࡳࡴࠬঽ")]))
  if not bstack1lll1l1lll_opy_:
    CONFIG[bstack1l111l1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬা")] = [{}]
def bstack1lll1l11ll_opy_(config, bstack1ll1llll11_opy_):
  global CONFIG
  global bstack1l1llll1l1_opy_
  CONFIG = config
  bstack1l1llll1l1_opy_ = bstack1ll1llll11_opy_
def bstack1111l111_opy_():
  global CONFIG
  global bstack1l1llll1l1_opy_
  if bstack1l111l1_opy_ (u"ࠪࡥࡵࡶࠧি") in CONFIG:
    try:
      from appium import version
    except Exception as e:
      bstack111l11l1l_opy_(e, bstack111ll1l1_opy_)
    bstack1l1llll1l1_opy_ = True
    bstack11111111_opy_.bstack111ll1ll_opy_(bstack1l111l1_opy_ (u"ࠫࡦࡶࡰࡠࡣࡸࡸࡴࡳࡡࡵࡧࠪী"), True)
def bstack1lll1ll1ll_opy_(config):
  bstack1l1llllll1_opy_ = bstack1l111l1_opy_ (u"ࠬ࠭ু")
  app = config[bstack1l111l1_opy_ (u"࠭ࡡࡱࡲࠪূ")]
  if isinstance(app, str):
    if os.path.splitext(app)[1] in bstack1ll1111111_opy_:
      if os.path.exists(app):
        bstack1l1llllll1_opy_ = bstack11111111l_opy_(config, app)
      elif bstack1l1ll1l1_opy_(app):
        bstack1l1llllll1_opy_ = app
      else:
        bstack11lll1l11_opy_(bstack1llll111_opy_.format(app))
    else:
      if bstack1l1ll1l1_opy_(app):
        bstack1l1llllll1_opy_ = app
      elif os.path.exists(app):
        bstack1l1llllll1_opy_ = bstack11111111l_opy_(app)
      else:
        bstack11lll1l11_opy_(bstack1l1ll1llll_opy_)
  else:
    if len(app) > 2:
      bstack11lll1l11_opy_(bstack1lll11111_opy_)
    elif len(app) == 2:
      if bstack1l111l1_opy_ (u"ࠧࡱࡣࡷ࡬ࠬৃ") in app and bstack1l111l1_opy_ (u"ࠨࡥࡸࡷࡹࡵ࡭ࡠ࡫ࡧࠫৄ") in app:
        if os.path.exists(app[bstack1l111l1_opy_ (u"ࠩࡳࡥࡹ࡮ࠧ৅")]):
          bstack1l1llllll1_opy_ = bstack11111111l_opy_(config, app[bstack1l111l1_opy_ (u"ࠪࡴࡦࡺࡨࠨ৆")], app[bstack1l111l1_opy_ (u"ࠫࡨࡻࡳࡵࡱࡰࡣ࡮ࡪࠧে")])
        else:
          bstack11lll1l11_opy_(bstack1llll111_opy_.format(app))
      else:
        bstack11lll1l11_opy_(bstack1lll11111_opy_)
    else:
      for key in app:
        if key in bstack111l11l11_opy_:
          if key == bstack1l111l1_opy_ (u"ࠬࡶࡡࡵࡪࠪৈ"):
            if os.path.exists(app[key]):
              bstack1l1llllll1_opy_ = bstack11111111l_opy_(config, app[key])
            else:
              bstack11lll1l11_opy_(bstack1llll111_opy_.format(app))
          else:
            bstack1l1llllll1_opy_ = app[key]
        else:
          bstack11lll1l11_opy_(bstack1l1l1l1l1_opy_)
  return bstack1l1llllll1_opy_
def bstack1l1ll1l1_opy_(bstack1l1llllll1_opy_):
  import re
  bstack111l1l1l_opy_ = re.compile(bstack1l111l1_opy_ (u"ࡸࠢ࡟࡝ࡤ࠱ࡿࡇ࡛࠭࠲࠰࠽ࡡࡥ࠮࡝࠯ࡠ࠮ࠩࠨ৉"))
  bstack1l1l111111_opy_ = re.compile(bstack1l111l1_opy_ (u"ࡲࠣࡠ࡞ࡥ࠲ࢀࡁ࠮࡜࠳࠱࠾ࡢ࡟࠯࡞࠰ࡡ࠯࠵࡛ࡢ࠯ࡽࡅ࠲ࡠ࠰࠮࠻࡟ࡣ࠳ࡢ࠭࡞ࠬࠧࠦ৊"))
  if bstack1l111l1_opy_ (u"ࠨࡤࡶ࠾࠴࠵ࠧো") in bstack1l1llllll1_opy_ or re.fullmatch(bstack111l1l1l_opy_, bstack1l1llllll1_opy_) or re.fullmatch(bstack1l1l111111_opy_, bstack1l1llllll1_opy_):
    return True
  else:
    return False
def bstack11111111l_opy_(config, path, bstack1l11ll1l1_opy_=None):
  import requests
  from requests_toolbelt.multipart.encoder import MultipartEncoder
  import hashlib
  md5_hash = hashlib.md5(open(os.path.abspath(path), bstack1l111l1_opy_ (u"ࠩࡵࡦࠬৌ")).read()).hexdigest()
  bstack1lll11l11_opy_ = bstack11111ll11_opy_(md5_hash)
  bstack1l1llllll1_opy_ = None
  if bstack1lll11l11_opy_:
    logger.info(bstack1l111111l_opy_.format(bstack1lll11l11_opy_, md5_hash))
    return bstack1lll11l11_opy_
  bstack1ll1l1l1l_opy_ = MultipartEncoder(
    fields={
      bstack1l111l1_opy_ (u"ࠪࡪ࡮ࡲࡥࠨ্"): (os.path.basename(path), open(os.path.abspath(path), bstack1l111l1_opy_ (u"ࠫࡷࡨࠧৎ")), bstack1l111l1_opy_ (u"ࠬࡺࡥࡹࡶ࠲ࡴࡱࡧࡩ࡯ࠩ৏")),
      bstack1l111l1_opy_ (u"࠭ࡣࡶࡵࡷࡳࡲࡥࡩࡥࠩ৐"): bstack1l11ll1l1_opy_
    }
  )
  response = requests.post(bstack1ll1l1lll_opy_, data=bstack1ll1l1l1l_opy_,
                           headers={bstack1l111l1_opy_ (u"ࠧࡄࡱࡱࡸࡪࡴࡴ࠮ࡖࡼࡴࡪ࠭৑"): bstack1ll1l1l1l_opy_.content_type},
                           auth=(config[bstack1l111l1_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪ৒")], config[bstack1l111l1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬ৓")]))
  try:
    res = json.loads(response.text)
    bstack1l1llllll1_opy_ = res[bstack1l111l1_opy_ (u"ࠪࡥࡵࡶ࡟ࡶࡴ࡯ࠫ৔")]
    logger.info(bstack1l1l1l11ll_opy_.format(bstack1l1llllll1_opy_))
    bstack1lll1ll11l_opy_(md5_hash, bstack1l1llllll1_opy_)
  except ValueError as err:
    bstack11lll1l11_opy_(bstack11l1l1ll_opy_.format(str(err)))
  return bstack1l1llllll1_opy_
def bstack11ll11ll_opy_():
  global CONFIG
  global bstack1ll1111ll1_opy_
  bstack1111111ll_opy_ = 0
  bstack11llll11_opy_ = 1
  if bstack1l111l1_opy_ (u"ࠫࡵࡧࡲࡢ࡮࡯ࡩࡱࡹࡐࡦࡴࡓࡰࡦࡺࡦࡰࡴࡰࠫ৕") in CONFIG:
    bstack11llll11_opy_ = CONFIG[bstack1l111l1_opy_ (u"ࠬࡶࡡࡳࡣ࡯ࡰࡪࡲࡳࡑࡧࡵࡔࡱࡧࡴࡧࡱࡵࡱࠬ৖")]
  if bstack1l111l1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩৗ") in CONFIG:
    bstack1111111ll_opy_ = len(CONFIG[bstack1l111l1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ৘")])
  bstack1ll1111ll1_opy_ = int(bstack11llll11_opy_) * int(bstack1111111ll_opy_)
def bstack11111ll11_opy_(md5_hash):
  bstack1l11lll1l_opy_ = os.path.join(os.path.expanduser(bstack1l111l1_opy_ (u"ࠨࢀࠪ৙")), bstack1l111l1_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩ৚"), bstack1l111l1_opy_ (u"ࠪࡥࡵࡶࡕࡱ࡮ࡲࡥࡩࡓࡄ࠶ࡊࡤࡷ࡭࠴ࡪࡴࡱࡱࠫ৛"))
  if os.path.exists(bstack1l11lll1l_opy_):
    bstack1llllll11_opy_ = json.load(open(bstack1l11lll1l_opy_, bstack1l111l1_opy_ (u"ࠫࡷࡨࠧড়")))
    if md5_hash in bstack1llllll11_opy_:
      bstack1l11l1l1l1_opy_ = bstack1llllll11_opy_[md5_hash]
      bstack1l11ll111l_opy_ = datetime.datetime.now()
      bstack1ll111ll1l_opy_ = datetime.datetime.strptime(bstack1l11l1l1l1_opy_[bstack1l111l1_opy_ (u"ࠬࡺࡩ࡮ࡧࡶࡸࡦࡳࡰࠨঢ়")], bstack1l111l1_opy_ (u"࠭ࠥࡥ࠱ࠨࡱ࠴࡙ࠫࠡࠧࡋ࠾ࠪࡓ࠺ࠦࡕࠪ৞"))
      if (bstack1l11ll111l_opy_ - bstack1ll111ll1l_opy_).days > 30:
        return None
      elif version.parse(str(__version__)) > version.parse(bstack1l11l1l1l1_opy_[bstack1l111l1_opy_ (u"ࠧࡴࡦ࡮ࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬয়")]):
        return None
      return bstack1l11l1l1l1_opy_[bstack1l111l1_opy_ (u"ࠨ࡫ࡧࠫৠ")]
  else:
    return None
def bstack1lll1ll11l_opy_(md5_hash, bstack1l1llllll1_opy_):
  bstack11l111111_opy_ = os.path.join(os.path.expanduser(bstack1l111l1_opy_ (u"ࠩࢁࠫৡ")), bstack1l111l1_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪৢ"))
  if not os.path.exists(bstack11l111111_opy_):
    os.makedirs(bstack11l111111_opy_)
  bstack1l11lll1l_opy_ = os.path.join(os.path.expanduser(bstack1l111l1_opy_ (u"ࠫࢃ࠭ৣ")), bstack1l111l1_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬ৤"), bstack1l111l1_opy_ (u"࠭ࡡࡱࡲࡘࡴࡱࡵࡡࡥࡏࡇ࠹ࡍࡧࡳࡩ࠰࡭ࡷࡴࡴࠧ৥"))
  bstack1llllll1l1_opy_ = {
    bstack1l111l1_opy_ (u"ࠧࡪࡦࠪ০"): bstack1l1llllll1_opy_,
    bstack1l111l1_opy_ (u"ࠨࡶ࡬ࡱࡪࡹࡴࡢ࡯ࡳࠫ১"): datetime.datetime.strftime(datetime.datetime.now(), bstack1l111l1_opy_ (u"ࠩࠨࡨ࠴ࠫ࡭࠰ࠧ࡜ࠤࠪࡎ࠺ࠦࡏ࠽ࠩࡘ࠭২")),
    bstack1l111l1_opy_ (u"ࠪࡷࡩࡱ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨ৩"): str(__version__)
  }
  if os.path.exists(bstack1l11lll1l_opy_):
    bstack1llllll11_opy_ = json.load(open(bstack1l11lll1l_opy_, bstack1l111l1_opy_ (u"ࠫࡷࡨࠧ৪")))
  else:
    bstack1llllll11_opy_ = {}
  bstack1llllll11_opy_[md5_hash] = bstack1llllll1l1_opy_
  with open(bstack1l11lll1l_opy_, bstack1l111l1_opy_ (u"ࠧࡽࠫࠣ৫")) as outfile:
    json.dump(bstack1llllll11_opy_, outfile)
def bstack1l11llll1_opy_(self):
  return
def bstack1l1l11ll1_opy_(self):
  return
def bstack111l1ll1l_opy_(self):
  global bstack1111ll1ll_opy_
  bstack1111ll1ll_opy_(self)
def bstack111llll1_opy_():
  global bstack1l11ll1111_opy_
  bstack1l11ll1111_opy_ = True
def bstack1ll1l1111_opy_(self):
  global bstack11l1l11ll_opy_
  global bstack1lll1ll1_opy_
  global bstack1l11ll1ll_opy_
  try:
    if bstack1l111l1_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭৬") in bstack11l1l11ll_opy_ and self.session_id != None and bstack1ll1ll1l1_opy_(threading.current_thread(), bstack1l111l1_opy_ (u"ࠧࡵࡧࡶࡸࡘࡺࡡࡵࡷࡶࠫ৭"), bstack1l111l1_opy_ (u"ࠨࠩ৮")) != bstack1l111l1_opy_ (u"ࠩࡶ࡯࡮ࡶࡰࡦࡦࠪ৯"):
      bstack1l1l111lll_opy_ = bstack1l111l1_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪৰ") if len(threading.current_thread().bstackTestErrorMessages) == 0 else bstack1l111l1_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫৱ")
      if bstack1l1l111lll_opy_ == bstack1l111l1_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬ৲"):
        bstack1l1l111l1_opy_(logger)
      if self != None:
        bstack11l11111l_opy_(self, bstack1l1l111lll_opy_, bstack1l111l1_opy_ (u"࠭ࠬࠡࠩ৳").join(threading.current_thread().bstackTestErrorMessages))
    threading.current_thread().testStatus = bstack1l111l1_opy_ (u"ࠧࠨ৴")
    if bstack1l111l1_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨ৵") in bstack11l1l11ll_opy_ and getattr(threading.current_thread(), bstack1l111l1_opy_ (u"ࠩࡤ࠵࠶ࡿࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨ৶"), None):
      bstack11llll11l_opy_.bstack1111l1ll1_opy_(self, bstack1l1lll111_opy_, logger, wait=True)
  except Exception as e:
    logger.debug(bstack1l111l1_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡺ࡬࡮ࡲࡥࠡ࡯ࡤࡶࡰ࡯࡮ࡨࠢࡶࡸࡦࡺࡵࡴ࠼ࠣࠦ৷") + str(e))
  bstack1l11ll1ll_opy_(self)
  self.session_id = None
def bstack1l1l1l11l1_opy_(self, command_executor=bstack1l111l1_opy_ (u"ࠦ࡭ࡺࡴࡱ࠼࠲࠳࠶࠸࠷࠯࠲࠱࠴࠳࠷࠺࠵࠶࠷࠸ࠧ৸"), *args, **kwargs):
  bstack1l111ll1_opy_ = bstack1lllll111_opy_(self, command_executor, *args, **kwargs)
  try:
    logger.debug(bstack1l111l1_opy_ (u"ࠬࡉ࡯࡮࡯ࡤࡲࡩࠦࡅࡹࡧࡦࡹࡹࡵࡲࠡࡹ࡫ࡩࡳࠦࡂࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢ࡬ࡷࠥ࡬ࡡ࡭ࡵࡨࠤ࠲ࠦࡻࡾࠩ৹").format(str(command_executor)))
    logger.debug(bstack1l111l1_opy_ (u"࠭ࡈࡶࡤ࡙ࠣࡗࡒࠠࡪࡵࠣ࠱ࠥࢁࡽࠨ৺").format(str(command_executor._url)))
    from selenium.webdriver.remote.remote_connection import RemoteConnection
    if isinstance(command_executor, RemoteConnection) and bstack1l111l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯ࠪ৻") in command_executor._url:
      bstack11111111_opy_.bstack111ll1ll_opy_(bstack1l111l1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡠࡵࡨࡷࡸ࡯࡯࡯ࠩৼ"), True)
  except:
    pass
  if (isinstance(command_executor, str) and bstack1l111l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱࠬ৽") in command_executor):
    bstack11111111_opy_.bstack111ll1ll_opy_(bstack1l111l1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡢࡷࡪࡹࡳࡪࡱࡱࠫ৾"), True)
  threading.current_thread().bstackSessionDriver = self
  bstack1l1111l1l_opy_.bstack11lll111l_opy_(self)
  return bstack1l111ll1_opy_
def bstack1ll11ll11l_opy_(args):
  return bstack1l111l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶࠬ৿") in str(args)
def bstack1llll1l1l_opy_(self, driver_command, *args, **kwargs):
  global bstack111lll11_opy_
  global bstack1lll1l11l_opy_
  bstack11ll1l1l_opy_ = bstack1ll1ll1l1_opy_(threading.current_thread(), bstack1l111l1_opy_ (u"ࠬ࡯ࡳࡂ࠳࠴ࡽ࡙࡫ࡳࡵࠩ਀"), None) and bstack1ll1ll1l1_opy_(
          threading.current_thread(), bstack1l111l1_opy_ (u"࠭ࡡ࠲࠳ࡼࡔࡱࡧࡴࡧࡱࡵࡱࠬਁ"), None)
  bstack1ll1l1ll1_opy_ = getattr(self, bstack1l111l1_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡁ࠲࠳ࡼࡗ࡭ࡵࡵ࡭ࡦࡖࡧࡦࡴࠧਂ"), None) != None and getattr(self, bstack1l111l1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡂ࠳࠴ࡽࡘ࡮࡯ࡶ࡮ࡧࡗࡨࡧ࡮ࠨਃ"), None) == True
  if not bstack1lll1l11l_opy_ and bstack1lll1l1lll_opy_ and bstack1l111l1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩ਄") in CONFIG and CONFIG[bstack1l111l1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪਅ")] == True and bstack1lll1l1l1_opy_.bstack1l1l1ll1ll_opy_(driver_command) and (bstack1ll1l1ll1_opy_ or bstack11ll1l1l_opy_) and not bstack1ll11ll11l_opy_(args):
    try:
      bstack1lll1l11l_opy_ = True
      logger.debug(bstack1l111l1_opy_ (u"ࠫࡕ࡫ࡲࡧࡱࡵࡱ࡮ࡴࡧࠡࡵࡦࡥࡳࠦࡦࡰࡴࠣࡿࢂ࠭ਆ").format(driver_command))
      logger.debug(perform_scan(self, driver_command=driver_command))
    except Exception as err:
      logger.debug(bstack1l111l1_opy_ (u"ࠬࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡲࡨࡶ࡫ࡵࡲ࡮ࠢࡶࡧࡦࡴࠠࡼࡿࠪਇ").format(str(err)))
    bstack1lll1l11l_opy_ = False
  response = bstack111lll11_opy_(self, driver_command, *args, **kwargs)
  if bstack1l111l1_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬਈ") in str(bstack11l1l11ll_opy_).lower() and bstack1l1111l1l_opy_.on():
    try:
      if driver_command == bstack1l111l1_opy_ (u"ࠧࡴࡥࡵࡩࡪࡴࡳࡩࡱࡷࠫਉ"):
        bstack1l1111l1l_opy_.bstack1ll1l1l1l1_opy_({
            bstack1l111l1_opy_ (u"ࠨ࡫ࡰࡥ࡬࡫ࠧਊ"): response[bstack1l111l1_opy_ (u"ࠩࡹࡥࡱࡻࡥࠨ਋")],
            bstack1l111l1_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪ਌"): bstack1l1111l1l_opy_.current_test_uuid() if bstack1l1111l1l_opy_.current_test_uuid() else bstack1l1111l1l_opy_.current_hook_uuid()
        })
    except:
      pass
  return response
def bstack1111l1111_opy_(self, command_executor,
             desired_capabilities=None, browser_profile=None, proxy=None,
             keep_alive=True, file_detector=None, options=None):
  global CONFIG
  global bstack1lll1ll1_opy_
  global bstack1llll1ll1_opy_
  global bstack111lll1l_opy_
  global bstack1ll1l11lll_opy_
  global bstack1lll1l1111_opy_
  global bstack11l1l11ll_opy_
  global bstack1lllll111_opy_
  global bstack11lll1l1_opy_
  global bstack11l11l1l_opy_
  global bstack1l1lll111_opy_
  CONFIG[bstack1l111l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡖࡈࡐ࠭਍")] = str(bstack11l1l11ll_opy_) + str(__version__)
  command_executor = bstack11ll1l1l1_opy_()
  logger.debug(bstack1lll1111ll_opy_.format(command_executor))
  proxy = bstack1l1lll11ll_opy_(CONFIG, proxy)
  bstack1l1l11l11l_opy_ = 0 if bstack1llll1ll1_opy_ < 0 else bstack1llll1ll1_opy_
  try:
    if bstack1ll1l11lll_opy_ is True:
      bstack1l1l11l11l_opy_ = int(multiprocessing.current_process().name)
    elif bstack1lll1l1111_opy_ is True:
      bstack1l1l11l11l_opy_ = int(threading.current_thread().name)
  except:
    bstack1l1l11l11l_opy_ = 0
  bstack1l1ll111_opy_ = bstack111ll1l1l_opy_(CONFIG, bstack1l1l11l11l_opy_)
  logger.debug(bstack11lll1111_opy_.format(str(bstack1l1ll111_opy_)))
  if bstack1l111l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩ਎") in CONFIG and bstack1l1l1ll111_opy_(CONFIG[bstack1l111l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪਏ")]):
    bstack111ll1111_opy_(bstack1l1ll111_opy_)
  if desired_capabilities:
    bstack1l1111lll_opy_ = bstack11l1ll1l1_opy_(desired_capabilities)
    bstack1l1111lll_opy_[bstack1l111l1_opy_ (u"ࠧࡶࡵࡨ࡛࠸ࡉࠧਐ")] = bstack111l11l1_opy_(CONFIG)
    bstack1ll11111ll_opy_ = bstack111ll1l1l_opy_(bstack1l1111lll_opy_)
    if bstack1ll11111ll_opy_:
      bstack1l1ll111_opy_ = update(bstack1ll11111ll_opy_, bstack1l1ll111_opy_)
    desired_capabilities = None
  if options:
    bstack1l11l1llll_opy_(options, bstack1l1ll111_opy_)
  if not options:
    options = bstack1111l11l_opy_(bstack1l1ll111_opy_)
  bstack1l1lll111_opy_ = CONFIG.get(bstack1l111l1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ਑"))[bstack1l1l11l11l_opy_]
  if bstack1l1lll11l1_opy_.bstack1lllll1ll_opy_(CONFIG, bstack1l1l11l11l_opy_) and bstack1l1lll11l1_opy_.bstack1lllll1l11_opy_(bstack1l1ll111_opy_, options):
    threading.current_thread().a11yPlatform = True
    bstack1l1lll11l1_opy_.set_capabilities(bstack1l1ll111_opy_, CONFIG)
  if proxy and bstack1l1ll11lll_opy_() >= version.parse(bstack1l111l1_opy_ (u"ࠩ࠷࠲࠶࠶࠮࠱ࠩ਒")):
    options.proxy(proxy)
  if options and bstack1l1ll11lll_opy_() >= version.parse(bstack1l111l1_opy_ (u"ࠪ࠷࠳࠾࠮࠱ࠩਓ")):
    desired_capabilities = None
  if (
          not options and not desired_capabilities
  ) or (
          bstack1l1ll11lll_opy_() < version.parse(bstack1l111l1_opy_ (u"ࠫ࠸࠴࠸࠯࠲ࠪਔ")) and not desired_capabilities
  ):
    desired_capabilities = {}
    desired_capabilities.update(bstack1l1ll111_opy_)
  logger.info(bstack1l1ll1l1ll_opy_)
  if bstack1l1ll11lll_opy_() >= version.parse(bstack1l111l1_opy_ (u"ࠬ࠺࠮࠲࠲࠱࠴ࠬਕ")):
    bstack1lllll111_opy_(self, command_executor=command_executor,
              options=options, keep_alive=keep_alive, file_detector=file_detector)
  elif bstack1l1ll11lll_opy_() >= version.parse(bstack1l111l1_opy_ (u"࠭࠳࠯࠺࠱࠴ࠬਖ")):
    bstack1lllll111_opy_(self, command_executor=command_executor,
              desired_capabilities=desired_capabilities, options=options,
              browser_profile=browser_profile, proxy=proxy,
              keep_alive=keep_alive, file_detector=file_detector)
  elif bstack1l1ll11lll_opy_() >= version.parse(bstack1l111l1_opy_ (u"ࠧ࠳࠰࠸࠷࠳࠶ࠧਗ")):
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
    bstack1llll11l11_opy_ = bstack1l111l1_opy_ (u"ࠨࠩਘ")
    if bstack1l1ll11lll_opy_() >= version.parse(bstack1l111l1_opy_ (u"ࠩ࠷࠲࠵࠴࠰ࡣ࠳ࠪਙ")):
      bstack1llll11l11_opy_ = self.caps.get(bstack1l111l1_opy_ (u"ࠥࡳࡵࡺࡩ࡮ࡣ࡯ࡌࡺࡨࡕࡳ࡮ࠥਚ"))
    else:
      bstack1llll11l11_opy_ = self.capabilities.get(bstack1l111l1_opy_ (u"ࠦࡴࡶࡴࡪ࡯ࡤࡰࡍࡻࡢࡖࡴ࡯ࠦਛ"))
    if bstack1llll11l11_opy_:
      bstack1lll11l111_opy_(bstack1llll11l11_opy_)
      if bstack1l1ll11lll_opy_() <= version.parse(bstack1l111l1_opy_ (u"ࠬ࠹࠮࠲࠵࠱࠴ࠬਜ")):
        self.command_executor._url = bstack1l111l1_opy_ (u"ࠨࡨࡵࡶࡳ࠾࠴࠵ࠢਝ") + bstack1l1l11111_opy_ + bstack1l111l1_opy_ (u"ࠢ࠻࠺࠳࠳ࡼࡪ࠯ࡩࡷࡥࠦਞ")
      else:
        self.command_executor._url = bstack1l111l1_opy_ (u"ࠣࡪࡷࡸࡵࡹ࠺࠰࠱ࠥਟ") + bstack1llll11l11_opy_ + bstack1l111l1_opy_ (u"ࠤ࠲ࡻࡩ࠵ࡨࡶࡤࠥਠ")
      logger.debug(bstack1ll11l111l_opy_.format(bstack1llll11l11_opy_))
    else:
      logger.debug(bstack1l11ll11l1_opy_.format(bstack1l111l1_opy_ (u"ࠥࡓࡵࡺࡩ࡮ࡣ࡯ࠤࡍࡻࡢࠡࡰࡲࡸࠥ࡬࡯ࡶࡰࡧࠦਡ")))
  except Exception as e:
    logger.debug(bstack1l11ll11l1_opy_.format(e))
  if bstack1l111l1_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪਢ") in bstack11l1l11ll_opy_:
    bstack1l1l111ll1_opy_(bstack1llll1ll1_opy_, bstack11l11l1l_opy_)
  bstack1lll1ll1_opy_ = self.session_id
  if bstack1l111l1_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬਣ") in bstack11l1l11ll_opy_ or bstack1l111l1_opy_ (u"࠭ࡢࡦࡪࡤࡺࡪ࠭ਤ") in bstack11l1l11ll_opy_ or bstack1l111l1_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭ਥ") in bstack11l1l11ll_opy_:
    threading.current_thread().bstackSessionId = self.session_id
    threading.current_thread().bstackSessionDriver = self
    threading.current_thread().bstackTestErrorMessages = []
    bstack1l1111l1l_opy_.bstack11lll111l_opy_(self)
  bstack11lll1l1_opy_.append(self)
  if bstack1l111l1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫਦ") in CONFIG and bstack1l111l1_opy_ (u"ࠩࡶࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧਧ") in CONFIG[bstack1l111l1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ਨ")][bstack1l1l11l11l_opy_]:
    bstack111lll1l_opy_ = CONFIG[bstack1l111l1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ਩")][bstack1l1l11l11l_opy_][bstack1l111l1_opy_ (u"ࠬࡹࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪਪ")]
  logger.debug(bstack11l111l1_opy_.format(bstack1lll1ll1_opy_))
try:
  try:
    import Browser
    from subprocess import Popen
    def bstack1l1lll1l1_opy_(self, args, bufsize=-1, executable=None,
              stdin=None, stdout=None, stderr=None,
              preexec_fn=None, close_fds=True,
              shell=False, cwd=None, env=None, universal_newlines=None,
              startupinfo=None, creationflags=0,
              restore_signals=True, start_new_session=False,
              pass_fds=(), *, user=None, group=None, extra_groups=None,
              encoding=None, errors=None, text=None, umask=-1, pipesize=-1):
      global CONFIG
      global bstack1ll1l111l_opy_
      if(bstack1l111l1_opy_ (u"ࠨࡩ࡯ࡦࡨࡼ࠳ࡰࡳࠣਫ") in args[1]):
        with open(os.path.join(os.path.expanduser(bstack1l111l1_opy_ (u"ࠧࡿࠩਬ")), bstack1l111l1_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨਭ"), bstack1l111l1_opy_ (u"ࠩ࠱ࡷࡪࡹࡳࡪࡱࡱ࡭ࡩࡹ࠮ࡵࡺࡷࠫਮ")), bstack1l111l1_opy_ (u"ࠪࡻࠬਯ")) as fp:
          fp.write(bstack1l111l1_opy_ (u"ࠦࠧਰ"))
        if(not os.path.exists(os.path.join(os.path.dirname(args[1]), bstack1l111l1_opy_ (u"ࠧ࡯࡮ࡥࡧࡻࡣࡧࡹࡴࡢࡥ࡮࠲࡯ࡹࠢ਱")))):
          with open(args[1], bstack1l111l1_opy_ (u"࠭ࡲࠨਲ")) as f:
            lines = f.readlines()
            index = next((i for i, line in enumerate(lines) if bstack1l111l1_opy_ (u"ࠧࡢࡵࡼࡲࡨࠦࡦࡶࡰࡦࡸ࡮ࡵ࡮ࠡࡡࡱࡩࡼࡖࡡࡨࡧࠫࡧࡴࡴࡴࡦࡺࡷ࠰ࠥࡶࡡࡨࡧࠣࡁࠥࡼ࡯ࡪࡦࠣ࠴࠮࠭ਲ਼") in line), None)
            if index is not None:
                lines.insert(index+2, bstack1lll11lll_opy_)
            lines.insert(1, bstack1l11l111_opy_)
            f.seek(0)
            with open(os.path.join(os.path.dirname(args[1]), bstack1l111l1_opy_ (u"ࠣ࡫ࡱࡨࡪࡾ࡟ࡣࡵࡷࡥࡨࡱ࠮࡫ࡵࠥ਴")), bstack1l111l1_opy_ (u"ࠩࡺࠫਵ")) as bstack1l11llll1l_opy_:
              bstack1l11llll1l_opy_.writelines(lines)
        CONFIG[bstack1l111l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡕࡇࡏࠬਸ਼")] = str(bstack11l1l11ll_opy_) + str(__version__)
        bstack1l1l11l11l_opy_ = 0 if bstack1llll1ll1_opy_ < 0 else bstack1llll1ll1_opy_
        try:
          if bstack1ll1l11lll_opy_ is True:
            bstack1l1l11l11l_opy_ = int(multiprocessing.current_process().name)
          elif bstack1lll1l1111_opy_ is True:
            bstack1l1l11l11l_opy_ = int(threading.current_thread().name)
        except:
          bstack1l1l11l11l_opy_ = 0
        CONFIG[bstack1l111l1_opy_ (u"ࠦࡺࡹࡥࡘ࠵ࡆࠦ਷")] = False
        CONFIG[bstack1l111l1_opy_ (u"ࠧ࡯ࡳࡑ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠦਸ")] = True
        bstack1l1ll111_opy_ = bstack111ll1l1l_opy_(CONFIG, bstack1l1l11l11l_opy_)
        logger.debug(bstack11lll1111_opy_.format(str(bstack1l1ll111_opy_)))
        if CONFIG.get(bstack1l111l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪਹ")):
          bstack111ll1111_opy_(bstack1l1ll111_opy_)
        if bstack1l111l1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ਺") in CONFIG and bstack1l111l1_opy_ (u"ࠨࡵࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭਻") in CONFIG[bstack1l111l1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷ਼ࠬ")][bstack1l1l11l11l_opy_]:
          bstack111lll1l_opy_ = CONFIG[bstack1l111l1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭਽")][bstack1l1l11l11l_opy_][bstack1l111l1_opy_ (u"ࠫࡸ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩਾ")]
        args.append(os.path.join(os.path.expanduser(bstack1l111l1_opy_ (u"ࠬࢄࠧਿ")), bstack1l111l1_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭ੀ"), bstack1l111l1_opy_ (u"ࠧ࠯ࡵࡨࡷࡸ࡯࡯࡯࡫ࡧࡷ࠳ࡺࡸࡵࠩੁ")))
        args.append(str(threading.get_ident()))
        args.append(json.dumps(bstack1l1ll111_opy_))
        args[1] = os.path.join(os.path.dirname(args[1]), bstack1l111l1_opy_ (u"ࠣ࡫ࡱࡨࡪࡾ࡟ࡣࡵࡷࡥࡨࡱ࠮࡫ࡵࠥੂ"))
      bstack1ll1l111l_opy_ = True
      return bstack11111ll1l_opy_(self, args, bufsize=bufsize, executable=executable,
                    stdin=stdin, stdout=stdout, stderr=stderr,
                    preexec_fn=preexec_fn, close_fds=close_fds,
                    shell=shell, cwd=cwd, env=env, universal_newlines=universal_newlines,
                    startupinfo=startupinfo, creationflags=creationflags,
                    restore_signals=restore_signals, start_new_session=start_new_session,
                    pass_fds=pass_fds, user=user, group=group, extra_groups=extra_groups,
                    encoding=encoding, errors=errors, text=text, umask=umask, pipesize=pipesize)
  except Exception as e:
    pass
  import playwright._impl._api_structures
  import playwright._impl._helper
  def bstack1l111llll_opy_(self,
        executablePath = None,
        channel = None,
        args = None,
        ignoreDefaultArgs = None,
        handleSIGINT = None,
        handleSIGTERM = None,
        handleSIGHUP = None,
        timeout = None,
        env = None,
        headless = None,
        devtools = None,
        proxy = None,
        downloadsPath = None,
        slowMo = None,
        tracesDir = None,
        chromiumSandbox = None,
        firefoxUserPrefs = None
        ):
    global CONFIG
    global bstack1llll1ll1_opy_
    global bstack111lll1l_opy_
    global bstack1ll1l11lll_opy_
    global bstack1lll1l1111_opy_
    global bstack11l1l11ll_opy_
    CONFIG[bstack1l111l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡔࡆࡎࠫ੃")] = str(bstack11l1l11ll_opy_) + str(__version__)
    bstack1l1l11l11l_opy_ = 0 if bstack1llll1ll1_opy_ < 0 else bstack1llll1ll1_opy_
    try:
      if bstack1ll1l11lll_opy_ is True:
        bstack1l1l11l11l_opy_ = int(multiprocessing.current_process().name)
      elif bstack1lll1l1111_opy_ is True:
        bstack1l1l11l11l_opy_ = int(threading.current_thread().name)
    except:
      bstack1l1l11l11l_opy_ = 0
    CONFIG[bstack1l111l1_opy_ (u"ࠥ࡭ࡸࡖ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠤ੄")] = True
    bstack1l1ll111_opy_ = bstack111ll1l1l_opy_(CONFIG, bstack1l1l11l11l_opy_)
    logger.debug(bstack11lll1111_opy_.format(str(bstack1l1ll111_opy_)))
    if CONFIG.get(bstack1l111l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨ੅")):
      bstack111ll1111_opy_(bstack1l1ll111_opy_)
    if bstack1l111l1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ੆") in CONFIG and bstack1l111l1_opy_ (u"࠭ࡳࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫੇ") in CONFIG[bstack1l111l1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪੈ")][bstack1l1l11l11l_opy_]:
      bstack111lll1l_opy_ = CONFIG[bstack1l111l1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ੉")][bstack1l1l11l11l_opy_][bstack1l111l1_opy_ (u"ࠩࡶࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧ੊")]
    import urllib
    import json
    bstack1ll11lll1_opy_ = bstack1l111l1_opy_ (u"ࠪࡻࡸࡹ࠺࠰࠱ࡦࡨࡵ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮࠱ࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࡅࡣࡢࡲࡶࡁࠬੋ") + urllib.parse.quote(json.dumps(bstack1l1ll111_opy_))
    browser = self.connect(bstack1ll11lll1_opy_)
    return browser
except Exception as e:
    pass
def bstack1lll1ll11_opy_():
    global bstack1ll1l111l_opy_
    try:
        from playwright._impl._browser_type import BrowserType
        BrowserType.launch = bstack1l111llll_opy_
        bstack1ll1l111l_opy_ = True
    except Exception as e:
        pass
    try:
      import Browser
      from subprocess import Popen
      Popen.__init__ = bstack1l1lll1l1_opy_
      bstack1ll1l111l_opy_ = True
    except Exception as e:
      pass
def bstack1lll11111l_opy_(context, bstack11l1lll1_opy_):
  try:
    context.page.evaluate(bstack1l111l1_opy_ (u"ࠦࡤࠦ࠽࠿ࠢࡾࢁࠧੌ"), bstack1l111l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪࠨࠬࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼࠤࡱࡥࡲ࡫ࠢ࠻੍ࠩ")+ json.dumps(bstack11l1lll1_opy_) + bstack1l111l1_opy_ (u"ࠨࡽࡾࠤ੎"))
  except Exception as e:
    logger.debug(bstack1l111l1_opy_ (u"ࠢࡦࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠣࡷࡪࡹࡳࡪࡱࡱࠤࡳࡧ࡭ࡦࠢࡾࢁࠧ੏"), e)
def bstack11ll111ll_opy_(context, message, level):
  try:
    context.page.evaluate(bstack1l111l1_opy_ (u"ࠣࡡࠣࡁࡃࠦࡻࡾࠤ੐"), bstack1l111l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡤࡲࡳࡵࡴࡢࡶࡨࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢࡥࡣࡷࡥࠧࡀࠧੑ") + json.dumps(message) + bstack1l111l1_opy_ (u"ࠪ࠰ࠧࡲࡥࡷࡧ࡯ࠦ࠿࠭੒") + json.dumps(level) + bstack1l111l1_opy_ (u"ࠫࢂࢃࠧ੓"))
  except Exception as e:
    logger.debug(bstack1l111l1_opy_ (u"ࠧ࡫ࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠡࡣࡱࡲࡴࡺࡡࡵ࡫ࡲࡲࠥࢁࡽࠣ੔"), e)
def bstack1lllll1l1_opy_(self, url):
  global bstack1lll11ll_opy_
  try:
    bstack11lllll11_opy_(url)
  except Exception as err:
    logger.debug(bstack1ll11ll11_opy_.format(str(err)))
  try:
    bstack1lll11ll_opy_(self, url)
  except Exception as e:
    try:
      bstack1111lll1_opy_ = str(e)
      if any(err_msg in bstack1111lll1_opy_ for err_msg in bstack1ll11l111_opy_):
        bstack11lllll11_opy_(url, True)
    except Exception as err:
      logger.debug(bstack1ll11ll11_opy_.format(str(err)))
    raise e
def bstack11111l111_opy_(self):
  global bstack1l1l11l1_opy_
  bstack1l1l11l1_opy_ = self
  return
def bstack1ll11ll1l_opy_(self):
  global bstack1ll11l1lll_opy_
  bstack1ll11l1lll_opy_ = self
  return
def bstack111l11111_opy_(test_name, bstack1l1l1111l1_opy_):
  global CONFIG
  if CONFIG.get(bstack1l111l1_opy_ (u"࠭ࡰࡦࡴࡦࡽࠬ੕"), False):
    bstack11lllll1_opy_ = os.path.relpath(bstack1l1l1111l1_opy_, start=os.getcwd())
    suite_name, _ = os.path.splitext(bstack11lllll1_opy_)
    bstack1l111l11_opy_ = suite_name + bstack1l111l1_opy_ (u"ࠢ࠮ࠤ੖") + test_name
    threading.current_thread().percySessionName = bstack1l111l11_opy_
def bstack1111ll11l_opy_(self, test, *args, **kwargs):
  global bstack1ll1111lll_opy_
  test_name = None
  bstack1l1l1111l1_opy_ = None
  if test:
    test_name = str(test.name)
    bstack1l1l1111l1_opy_ = str(test.source)
  bstack111l11111_opy_(test_name, bstack1l1l1111l1_opy_)
  bstack1ll1111lll_opy_(self, test, *args, **kwargs)
def bstack11111llll_opy_(driver, bstack1l111l11_opy_):
  if not bstack111lll11l_opy_ and bstack1l111l11_opy_:
      bstack1l11lll1l1_opy_ = {
          bstack1l111l1_opy_ (u"ࠨࡣࡦࡸ࡮ࡵ࡮ࠨ੗"): bstack1l111l1_opy_ (u"ࠩࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪ੘"),
          bstack1l111l1_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭ਖ਼"): {
              bstack1l111l1_opy_ (u"ࠫࡳࡧ࡭ࡦࠩਗ਼"): bstack1l111l11_opy_
          }
      }
      bstack1ll11lll_opy_ = bstack1l111l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࡿࠪਜ਼").format(json.dumps(bstack1l11lll1l1_opy_))
      driver.execute_script(bstack1ll11lll_opy_)
  if bstack1ll1l1l11l_opy_:
      bstack1111ll1l1_opy_ = {
          bstack1l111l1_opy_ (u"࠭ࡡࡤࡶ࡬ࡳࡳ࠭ੜ"): bstack1l111l1_opy_ (u"ࠧࡢࡰࡱࡳࡹࡧࡴࡦࠩ੝"),
          bstack1l111l1_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫਫ਼"): {
              bstack1l111l1_opy_ (u"ࠩࡧࡥࡹࡧࠧ੟"): bstack1l111l11_opy_ + bstack1l111l1_opy_ (u"ࠪࠤࡵࡧࡳࡴࡧࡧࠥࠬ੠"),
              bstack1l111l1_opy_ (u"ࠫࡱ࡫ࡶࡦ࡮ࠪ੡"): bstack1l111l1_opy_ (u"ࠬ࡯࡮ࡧࡱࠪ੢")
          }
      }
      if bstack1ll1l1l11l_opy_.status == bstack1l111l1_opy_ (u"࠭ࡐࡂࡕࡖࠫ੣"):
          bstack1llll1l11l_opy_ = bstack1l111l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࢁࠬ੤").format(json.dumps(bstack1111ll1l1_opy_))
          driver.execute_script(bstack1llll1l11l_opy_)
          bstack11l11111l_opy_(driver, bstack1l111l1_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨ੥"))
      elif bstack1ll1l1l11l_opy_.status == bstack1l111l1_opy_ (u"ࠩࡉࡅࡎࡒࠧ੦"):
          reason = bstack1l111l1_opy_ (u"ࠥࠦ੧")
          bstack1l111ll1l_opy_ = bstack1l111l11_opy_ + bstack1l111l1_opy_ (u"ࠫࠥ࡬ࡡࡪ࡮ࡨࡨࠬ੨")
          if bstack1ll1l1l11l_opy_.message:
              reason = str(bstack1ll1l1l11l_opy_.message)
              bstack1l111ll1l_opy_ = bstack1l111ll1l_opy_ + bstack1l111l1_opy_ (u"ࠬࠦࡷࡪࡶ࡫ࠤࡪࡸࡲࡰࡴ࠽ࠤࠬ੩") + reason
          bstack1111ll1l1_opy_[bstack1l111l1_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩ੪")] = {
              bstack1l111l1_opy_ (u"ࠧ࡭ࡧࡹࡩࡱ࠭੫"): bstack1l111l1_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧ੬"),
              bstack1l111l1_opy_ (u"ࠩࡧࡥࡹࡧࠧ੭"): bstack1l111ll1l_opy_
          }
          bstack1llll1l11l_opy_ = bstack1l111l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࡽࠨ੮").format(json.dumps(bstack1111ll1l1_opy_))
          driver.execute_script(bstack1llll1l11l_opy_)
          bstack11l11111l_opy_(driver, bstack1l111l1_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫ੯"), reason)
          bstack111111111_opy_(reason, str(bstack1ll1l1l11l_opy_), str(bstack1llll1ll1_opy_), logger)
def bstack1ll1111l1l_opy_(driver, test):
  if CONFIG.get(bstack1l111l1_opy_ (u"ࠬࡶࡥࡳࡥࡼࠫੰ"), False) and CONFIG.get(bstack1l111l1_opy_ (u"࠭ࡰࡦࡴࡦࡽࡈࡧࡰࡵࡷࡵࡩࡒࡵࡤࡦࠩੱ"), bstack1l111l1_opy_ (u"ࠢࡢࡷࡷࡳࠧੲ")) == bstack1l111l1_opy_ (u"ࠣࡶࡨࡷࡹࡩࡡࡴࡧࠥੳ"):
      bstack1ll111ll_opy_ = bstack1ll1ll1l1_opy_(threading.current_thread(), bstack1l111l1_opy_ (u"ࠩࡳࡩࡷࡩࡹࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬੴ"), None)
      bstack11l111ll1_opy_(driver, bstack1ll111ll_opy_)
  if bstack1ll1ll1l1_opy_(threading.current_thread(), bstack1l111l1_opy_ (u"ࠪ࡭ࡸࡇ࠱࠲ࡻࡗࡩࡸࡺࠧੵ"), None) and bstack1ll1ll1l1_opy_(
          threading.current_thread(), bstack1l111l1_opy_ (u"ࠫࡦ࠷࠱ࡺࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪ੶"), None):
      logger.info(bstack1l111l1_opy_ (u"ࠧࡇࡵࡵࡱࡰࡥࡹ࡫ࠠࡵࡧࡶࡸࠥࡩࡡࡴࡧࠣࡩࡽ࡫ࡣࡶࡶ࡬ࡳࡳࠦࡨࡢࡵࠣࡩࡳࡪࡥࡥ࠰ࠣࡔࡷࡵࡣࡦࡵࡶ࡭ࡳ࡭ࠠࡧࡱࡵࠤࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡹ࡫ࡳࡵ࡫ࡱ࡫ࠥ࡯ࡳࠡࡷࡱࡨࡪࡸࡷࡢࡻ࠱ࠤࠧ੷"))
      bstack1l1lll11l1_opy_.bstack11l1l111l_opy_(driver, class_name=test.parent.name, name=test.name, module_name=None,
                              path=test.source, bstack1ll111ll1_opy_=bstack1l1lll111_opy_)
def bstack1l11l1l1_opy_(test, bstack1l111l11_opy_):
    try:
      data = {}
      if test:
        data[bstack1l111l1_opy_ (u"࠭࡮ࡢ࡯ࡨࠫ੸")] = bstack1l111l11_opy_
      if bstack1ll1l1l11l_opy_:
        if bstack1ll1l1l11l_opy_.status == bstack1l111l1_opy_ (u"ࠧࡑࡃࡖࡗࠬ੹"):
          data[bstack1l111l1_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨ੺")] = bstack1l111l1_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩ੻")
        elif bstack1ll1l1l11l_opy_.status == bstack1l111l1_opy_ (u"ࠪࡊࡆࡏࡌࠨ੼"):
          data[bstack1l111l1_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫ੽")] = bstack1l111l1_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬ੾")
          if bstack1ll1l1l11l_opy_.message:
            data[bstack1l111l1_opy_ (u"࠭ࡲࡦࡣࡶࡳࡳ࠭੿")] = str(bstack1ll1l1l11l_opy_.message)
      user = CONFIG[bstack1l111l1_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩ઀")]
      key = CONFIG[bstack1l111l1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫઁ")]
      url = bstack1l111l1_opy_ (u"ࠩ࡫ࡸࡹࡶࡳ࠻࠱࠲ࡿࢂࡀࡻࡾࡂࡤࡴ࡮࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮࠱ࡤࡹࡹࡵ࡭ࡢࡶࡨ࠳ࡸ࡫ࡳࡴ࡫ࡲࡲࡸ࠵ࡻࡾ࠰࡭ࡷࡴࡴࠧં").format(user, key, bstack1lll1ll1_opy_)
      headers = {
        bstack1l111l1_opy_ (u"ࠪࡇࡴࡴࡴࡦࡰࡷ࠱ࡹࡿࡰࡦࠩઃ"): bstack1l111l1_opy_ (u"ࠫࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱࡭ࡷࡴࡴࠧ઄"),
      }
      if bool(data):
        requests.put(url, json=data, headers=headers)
    except Exception as e:
      logger.error(bstack1ll1ll111_opy_.format(str(e)))
def bstack1ll1l1l1ll_opy_(test, bstack1l111l11_opy_):
  global CONFIG
  global bstack1ll11l1lll_opy_
  global bstack1l1l11l1_opy_
  global bstack1lll1ll1_opy_
  global bstack1ll1l1l11l_opy_
  global bstack111lll1l_opy_
  global bstack1l111l1l_opy_
  global bstack1111llll1_opy_
  global bstack1l1ll1ll11_opy_
  global bstack1llll11111_opy_
  global bstack11lll1l1_opy_
  global bstack1l1lll111_opy_
  try:
    if not bstack1lll1ll1_opy_:
      with open(os.path.join(os.path.expanduser(bstack1l111l1_opy_ (u"ࠬࢄࠧઅ")), bstack1l111l1_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭આ"), bstack1l111l1_opy_ (u"ࠧ࠯ࡵࡨࡷࡸ࡯࡯࡯࡫ࡧࡷ࠳ࡺࡸࡵࠩઇ"))) as f:
        bstack1l11llllll_opy_ = json.loads(bstack1l111l1_opy_ (u"ࠣࡽࠥઈ") + f.read().strip() + bstack1l111l1_opy_ (u"ࠩࠥࡼࠧࡀࠠࠣࡻࠥࠫઉ") + bstack1l111l1_opy_ (u"ࠥࢁࠧઊ"))
        bstack1lll1ll1_opy_ = bstack1l11llllll_opy_[str(threading.get_ident())]
  except:
    pass
  if bstack11lll1l1_opy_:
    for driver in bstack11lll1l1_opy_:
      if bstack1lll1ll1_opy_ == driver.session_id:
        if test:
          bstack1ll1111l1l_opy_(driver, test)
        bstack11111llll_opy_(driver, bstack1l111l11_opy_)
  elif bstack1lll1ll1_opy_:
    bstack1l11l1l1_opy_(test, bstack1l111l11_opy_)
  if bstack1ll11l1lll_opy_:
    bstack1111llll1_opy_(bstack1ll11l1lll_opy_)
  if bstack1l1l11l1_opy_:
    bstack1l1ll1ll11_opy_(bstack1l1l11l1_opy_)
  if bstack1l11ll1111_opy_:
    bstack1llll11111_opy_()
def bstack11lll11l_opy_(self, test, *args, **kwargs):
  bstack1l111l11_opy_ = None
  if test:
    bstack1l111l11_opy_ = str(test.name)
  bstack1ll1l1l1ll_opy_(test, bstack1l111l11_opy_)
  bstack1l111l1l_opy_(self, test, *args, **kwargs)
def bstack1l1l1111ll_opy_(self, parent, test, skip_on_failure=None, rpa=False):
  global bstack11lll11ll_opy_
  global CONFIG
  global bstack11lll1l1_opy_
  global bstack1lll1ll1_opy_
  bstack1l1lllll1_opy_ = None
  try:
    if bstack1ll1ll1l1_opy_(threading.current_thread(), bstack1l111l1_opy_ (u"ࠫࡦ࠷࠱ࡺࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪઋ"), None):
      try:
        if not bstack1lll1ll1_opy_:
          with open(os.path.join(os.path.expanduser(bstack1l111l1_opy_ (u"ࠬࢄࠧઌ")), bstack1l111l1_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭ઍ"), bstack1l111l1_opy_ (u"ࠧ࠯ࡵࡨࡷࡸ࡯࡯࡯࡫ࡧࡷ࠳ࡺࡸࡵࠩ઎"))) as f:
            bstack1l11llllll_opy_ = json.loads(bstack1l111l1_opy_ (u"ࠣࡽࠥએ") + f.read().strip() + bstack1l111l1_opy_ (u"ࠩࠥࡼࠧࡀࠠࠣࡻࠥࠫઐ") + bstack1l111l1_opy_ (u"ࠥࢁࠧઑ"))
            bstack1lll1ll1_opy_ = bstack1l11llllll_opy_[str(threading.get_ident())]
      except:
        pass
      if bstack11lll1l1_opy_:
        for driver in bstack11lll1l1_opy_:
          if bstack1lll1ll1_opy_ == driver.session_id:
            bstack1l1lllll1_opy_ = driver
    bstack11l1l11l1_opy_ = bstack1l1lll11l1_opy_.bstack1l1l111l_opy_(CONFIG, test.tags)
    if bstack1l1lllll1_opy_:
      threading.current_thread().isA11yTest = bstack1l1lll11l1_opy_.bstack11111ll1_opy_(bstack1l1lllll1_opy_, bstack11l1l11l1_opy_)
    else:
      threading.current_thread().isA11yTest = bstack11l1l11l1_opy_
  except:
    pass
  bstack11lll11ll_opy_(self, parent, test, skip_on_failure=skip_on_failure, rpa=rpa)
  global bstack1ll1l1l11l_opy_
  bstack1ll1l1l11l_opy_ = self._test
def bstack111ll111_opy_():
  global bstack1ll1l1lll1_opy_
  try:
    if os.path.exists(bstack1ll1l1lll1_opy_):
      os.remove(bstack1ll1l1lll1_opy_)
  except Exception as e:
    logger.debug(bstack1l111l1_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡤࡦ࡮ࡨࡸ࡮ࡴࡧࠡࡴࡲࡦࡴࡺࠠࡳࡧࡳࡳࡷࡺࠠࡧ࡫࡯ࡩ࠿ࠦࠧ઒") + str(e))
def bstack1l1l1l111_opy_():
  global bstack1ll1l1lll1_opy_
  bstack111l11ll1_opy_ = {}
  try:
    if not os.path.isfile(bstack1ll1l1lll1_opy_):
      with open(bstack1ll1l1lll1_opy_, bstack1l111l1_opy_ (u"ࠬࡽࠧઓ")):
        pass
      with open(bstack1ll1l1lll1_opy_, bstack1l111l1_opy_ (u"ࠨࡷࠬࠤઔ")) as outfile:
        json.dump({}, outfile)
    if os.path.exists(bstack1ll1l1lll1_opy_):
      bstack111l11ll1_opy_ = json.load(open(bstack1ll1l1lll1_opy_, bstack1l111l1_opy_ (u"ࠧࡳࡤࠪક")))
  except Exception as e:
    logger.debug(bstack1l111l1_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡶࡪࡧࡤࡪࡰࡪࠤࡷࡵࡢࡰࡶࠣࡶࡪࡶ࡯ࡳࡶࠣࡪ࡮ࡲࡥ࠻ࠢࠪખ") + str(e))
  finally:
    return bstack111l11ll1_opy_
def bstack1l1l111ll1_opy_(platform_index, item_index):
  global bstack1ll1l1lll1_opy_
  try:
    bstack111l11ll1_opy_ = bstack1l1l1l111_opy_()
    bstack111l11ll1_opy_[item_index] = platform_index
    with open(bstack1ll1l1lll1_opy_, bstack1l111l1_opy_ (u"ࠤࡺ࠯ࠧગ")) as outfile:
      json.dump(bstack111l11ll1_opy_, outfile)
  except Exception as e:
    logger.debug(bstack1l111l1_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡽࡲࡪࡶ࡬ࡲ࡬ࠦࡴࡰࠢࡵࡳࡧࡵࡴࠡࡴࡨࡴࡴࡸࡴࠡࡨ࡬ࡰࡪࡀࠠࠨઘ") + str(e))
def bstack1l11llll11_opy_(bstack1l111lll_opy_):
  global CONFIG
  bstack1ll11111l_opy_ = bstack1l111l1_opy_ (u"ࠫࠬઙ")
  if not bstack1l111l1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨચ") in CONFIG:
    logger.info(bstack1l111l1_opy_ (u"࠭ࡎࡰࠢࡳࡰࡦࡺࡦࡰࡴࡰࡷࠥࡶࡡࡴࡵࡨࡨࠥࡻ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡩࡨࡲࡪࡸࡡࡵࡧࠣࡶࡪࡶ࡯ࡳࡶࠣࡪࡴࡸࠠࡓࡱࡥࡳࡹࠦࡲࡶࡰࠪછ"))
  try:
    platform = CONFIG[bstack1l111l1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪજ")][bstack1l111lll_opy_]
    if bstack1l111l1_opy_ (u"ࠨࡱࡶࠫઝ") in platform:
      bstack1ll11111l_opy_ += str(platform[bstack1l111l1_opy_ (u"ࠩࡲࡷࠬઞ")]) + bstack1l111l1_opy_ (u"ࠪ࠰ࠥ࠭ટ")
    if bstack1l111l1_opy_ (u"ࠫࡴࡹࡖࡦࡴࡶ࡭ࡴࡴࠧઠ") in platform:
      bstack1ll11111l_opy_ += str(platform[bstack1l111l1_opy_ (u"ࠬࡵࡳࡗࡧࡵࡷ࡮ࡵ࡮ࠨડ")]) + bstack1l111l1_opy_ (u"࠭ࠬࠡࠩઢ")
    if bstack1l111l1_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࡎࡢ࡯ࡨࠫણ") in platform:
      bstack1ll11111l_opy_ += str(platform[bstack1l111l1_opy_ (u"ࠨࡦࡨࡺ࡮ࡩࡥࡏࡣࡰࡩࠬત")]) + bstack1l111l1_opy_ (u"ࠩ࠯ࠤࠬથ")
    if bstack1l111l1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱ࡛࡫ࡲࡴ࡫ࡲࡲࠬદ") in platform:
      bstack1ll11111l_opy_ += str(platform[bstack1l111l1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ધ")]) + bstack1l111l1_opy_ (u"ࠬ࠲ࠠࠨન")
    if bstack1l111l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫ઩") in platform:
      bstack1ll11111l_opy_ += str(platform[bstack1l111l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬપ")]) + bstack1l111l1_opy_ (u"ࠨ࠮ࠣࠫફ")
    if bstack1l111l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪબ") in platform:
      bstack1ll11111l_opy_ += str(platform[bstack1l111l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫભ")]) + bstack1l111l1_opy_ (u"ࠫ࠱ࠦࠧમ")
  except Exception as e:
    logger.debug(bstack1l111l1_opy_ (u"࡙ࠬ࡯࡮ࡧࠣࡩࡷࡸ࡯ࡳࠢ࡬ࡲࠥ࡭ࡥ࡯ࡧࡵࡥࡹ࡯࡮ࡨࠢࡳࡰࡦࡺࡦࡰࡴࡰࠤࡸࡺࡲࡪࡰࡪࠤ࡫ࡵࡲࠡࡴࡨࡴࡴࡸࡴࠡࡩࡨࡲࡪࡸࡡࡵ࡫ࡲࡲࠬય") + str(e))
  finally:
    if bstack1ll11111l_opy_[len(bstack1ll11111l_opy_) - 2:] == bstack1l111l1_opy_ (u"࠭ࠬࠡࠩર"):
      bstack1ll11111l_opy_ = bstack1ll11111l_opy_[:-2]
    return bstack1ll11111l_opy_
def bstack1ll11l1l1l_opy_(path, bstack1ll11111l_opy_):
  try:
    import xml.etree.ElementTree as ET
    bstack1ll1llll_opy_ = ET.parse(path)
    bstack1l1llll11_opy_ = bstack1ll1llll_opy_.getroot()
    bstack1111111l_opy_ = None
    for suite in bstack1l1llll11_opy_.iter(bstack1l111l1_opy_ (u"ࠧࡴࡷ࡬ࡸࡪ࠭઱")):
      if bstack1l111l1_opy_ (u"ࠨࡵࡲࡹࡷࡩࡥࠨલ") in suite.attrib:
        suite.attrib[bstack1l111l1_opy_ (u"ࠩࡱࡥࡲ࡫ࠧળ")] += bstack1l111l1_opy_ (u"ࠪࠤࠬ઴") + bstack1ll11111l_opy_
        bstack1111111l_opy_ = suite
    bstack1ll11ll1_opy_ = None
    for robot in bstack1l1llll11_opy_.iter(bstack1l111l1_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪવ")):
      bstack1ll11ll1_opy_ = robot
    bstack1ll11ll1l1_opy_ = len(bstack1ll11ll1_opy_.findall(bstack1l111l1_opy_ (u"ࠬࡹࡵࡪࡶࡨࠫશ")))
    if bstack1ll11ll1l1_opy_ == 1:
      bstack1ll11ll1_opy_.remove(bstack1ll11ll1_opy_.findall(bstack1l111l1_opy_ (u"࠭ࡳࡶ࡫ࡷࡩࠬષ"))[0])
      bstack1lll11l1l1_opy_ = ET.Element(bstack1l111l1_opy_ (u"ࠧࡴࡷ࡬ࡸࡪ࠭સ"), attrib={bstack1l111l1_opy_ (u"ࠨࡰࡤࡱࡪ࠭હ"): bstack1l111l1_opy_ (u"ࠩࡖࡹ࡮ࡺࡥࡴࠩ઺"), bstack1l111l1_opy_ (u"ࠪ࡭ࡩ࠭઻"): bstack1l111l1_opy_ (u"ࠫࡸ࠶઼ࠧ")})
      bstack1ll11ll1_opy_.insert(1, bstack1lll11l1l1_opy_)
      bstack1llll1111l_opy_ = None
      for suite in bstack1ll11ll1_opy_.iter(bstack1l111l1_opy_ (u"ࠬࡹࡵࡪࡶࡨࠫઽ")):
        bstack1llll1111l_opy_ = suite
      bstack1llll1111l_opy_.append(bstack1111111l_opy_)
      bstack1l1l1ll11_opy_ = None
      for status in bstack1111111l_opy_.iter(bstack1l111l1_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭ા")):
        bstack1l1l1ll11_opy_ = status
      bstack1llll1111l_opy_.append(bstack1l1l1ll11_opy_)
    bstack1ll1llll_opy_.write(path)
  except Exception as e:
    logger.debug(bstack1l111l1_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡳࡥࡷࡹࡩ࡯ࡩࠣࡻ࡭࡯࡬ࡦࠢࡪࡩࡳ࡫ࡲࡢࡶ࡬ࡲ࡬ࠦࡲࡰࡤࡲࡸࠥࡸࡥࡱࡱࡵࡸࠬિ") + str(e))
def bstack1lllll11l_opy_(outs_dir, pabot_args, options, start_time_string, tests_root_name):
  global bstack1l1ll11l11_opy_
  global CONFIG
  if bstack1l111l1_opy_ (u"ࠣࡲࡼࡸ࡭ࡵ࡮ࡱࡣࡷ࡬ࠧી") in options:
    del options[bstack1l111l1_opy_ (u"ࠤࡳࡽࡹ࡮࡯࡯ࡲࡤࡸ࡭ࠨુ")]
  bstack111lll111_opy_ = bstack1l1l1l111_opy_()
  for bstack1l11ll11l_opy_ in bstack111lll111_opy_.keys():
    path = os.path.join(os.getcwd(), bstack1l111l1_opy_ (u"ࠪࡴࡦࡨ࡯ࡵࡡࡵࡩࡸࡻ࡬ࡵࡵࠪૂ"), str(bstack1l11ll11l_opy_), bstack1l111l1_opy_ (u"ࠫࡴࡻࡴࡱࡷࡷ࠲ࡽࡳ࡬ࠨૃ"))
    bstack1ll11l1l1l_opy_(path, bstack1l11llll11_opy_(bstack111lll111_opy_[bstack1l11ll11l_opy_]))
  bstack111ll111_opy_()
  return bstack1l1ll11l11_opy_(outs_dir, pabot_args, options, start_time_string, tests_root_name)
def bstack1111ll111_opy_(self, ff_profile_dir):
  global bstack1llll1llll_opy_
  if not ff_profile_dir:
    return None
  return bstack1llll1llll_opy_(self, ff_profile_dir)
def bstack1l1ll1111_opy_(datasources, opts_for_run, outs_dir, pabot_args, suite_group):
  from pabot.pabot import QueueItem
  global CONFIG
  global bstack1l1l11l111_opy_
  bstack1l1l1l1ll_opy_ = []
  if bstack1l111l1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨૄ") in CONFIG:
    bstack1l1l1l1ll_opy_ = CONFIG[bstack1l111l1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩૅ")]
  return [
    QueueItem(
      datasources,
      outs_dir,
      opts_for_run,
      suite,
      pabot_args[bstack1l111l1_opy_ (u"ࠢࡤࡱࡰࡱࡦࡴࡤࠣ૆")],
      pabot_args[bstack1l111l1_opy_ (u"ࠣࡸࡨࡶࡧࡵࡳࡦࠤે")],
      argfile,
      pabot_args.get(bstack1l111l1_opy_ (u"ࠤ࡫࡭ࡻ࡫ࠢૈ")),
      pabot_args[bstack1l111l1_opy_ (u"ࠥࡴࡷࡵࡣࡦࡵࡶࡩࡸࠨૉ")],
      platform[0],
      bstack1l1l11l111_opy_
    )
    for suite in suite_group
    for argfile in pabot_args[bstack1l111l1_opy_ (u"ࠦࡦࡸࡧࡶ࡯ࡨࡲࡹ࡬ࡩ࡭ࡧࡶࠦ૊")] or [(bstack1l111l1_opy_ (u"ࠧࠨો"), None)]
    for platform in enumerate(bstack1l1l1l1ll_opy_)
  ]
def bstack1ll1lll11l_opy_(self, datasources, outs_dir, options,
                        execution_item, command, verbose, argfile,
                        hive=None, processes=0, platform_index=0, bstack1ll11ll1ll_opy_=bstack1l111l1_opy_ (u"࠭ࠧૌ")):
  global bstack1l11l1111_opy_
  self.platform_index = platform_index
  self.bstack1ll111111_opy_ = bstack1ll11ll1ll_opy_
  bstack1l11l1111_opy_(self, datasources, outs_dir, options,
                      execution_item, command, verbose, argfile, hive, processes)
def bstack1l1lllll_opy_(caller_id, datasources, is_last, item, outs_dir):
  global bstack1l1l1ll1_opy_
  global bstack11ll1lll_opy_
  if not bstack1l111l1_opy_ (u"ࠧࡷࡣࡵ࡭ࡦࡨ࡬ࡦ્ࠩ") in item.options:
    item.options[bstack1l111l1_opy_ (u"ࠨࡸࡤࡶ࡮ࡧࡢ࡭ࡧࠪ૎")] = []
  for v in item.options[bstack1l111l1_opy_ (u"ࠩࡹࡥࡷ࡯ࡡࡣ࡮ࡨࠫ૏")]:
    if bstack1l111l1_opy_ (u"ࠪࡆࡘ࡚ࡁࡄࡍࡓࡐࡆ࡚ࡆࡐࡔࡐࡍࡓࡊࡅ࡙ࠩૐ") in v:
      item.options[bstack1l111l1_opy_ (u"ࠫࡻࡧࡲࡪࡣࡥࡰࡪ࠭૑")].remove(v)
    if bstack1l111l1_opy_ (u"ࠬࡈࡓࡕࡃࡆࡏࡈࡒࡉࡂࡔࡊࡗࠬ૒") in v:
      item.options[bstack1l111l1_opy_ (u"࠭ࡶࡢࡴ࡬ࡥࡧࡲࡥࠨ૓")].remove(v)
  item.options[bstack1l111l1_opy_ (u"ࠧࡷࡣࡵ࡭ࡦࡨ࡬ࡦࠩ૔")].insert(0, bstack1l111l1_opy_ (u"ࠨࡄࡖࡘࡆࡉࡋࡑࡎࡄࡘࡋࡕࡒࡎࡋࡑࡈࡊ࡞࠺ࡼࡿࠪ૕").format(item.platform_index))
  item.options[bstack1l111l1_opy_ (u"ࠩࡹࡥࡷ࡯ࡡࡣ࡮ࡨࠫ૖")].insert(0, bstack1l111l1_opy_ (u"ࠪࡆࡘ࡚ࡁࡄࡍࡇࡉࡋࡒࡏࡄࡃࡏࡍࡉࡋࡎࡕࡋࡉࡍࡊࡘ࠺ࡼࡿࠪ૗").format(item.bstack1ll111111_opy_))
  if bstack11ll1lll_opy_:
    item.options[bstack1l111l1_opy_ (u"ࠫࡻࡧࡲࡪࡣࡥࡰࡪ࠭૘")].insert(0, bstack1l111l1_opy_ (u"ࠬࡈࡓࡕࡃࡆࡏࡈࡒࡉࡂࡔࡊࡗ࠿ࢁࡽࠨ૙").format(bstack11ll1lll_opy_))
  return bstack1l1l1ll1_opy_(caller_id, datasources, is_last, item, outs_dir)
def bstack1lll1l111_opy_(command, item_index):
  if bstack11111111_opy_.get_property(bstack1l111l1_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡥࡳࡦࡵࡶ࡭ࡴࡴࠧ૚")):
    os.environ[bstack1l111l1_opy_ (u"ࠧࡄࡗࡕࡖࡊࡔࡔࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡈࡆ࡚ࡁࠨ૛")] = json.dumps(CONFIG[bstack1l111l1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ૜")][item_index % bstack1111lll1l_opy_])
  global bstack11ll1lll_opy_
  if bstack11ll1lll_opy_:
    command[0] = command[0].replace(bstack1l111l1_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨ૝"), bstack1l111l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠯ࡶࡨࡰࠦࡲࡰࡤࡲࡸ࠲࡯࡮ࡵࡧࡵࡲࡦࡲࠠ࠮࠯ࡥࡷࡹࡧࡣ࡬ࡡ࡬ࡸࡪࡳ࡟ࡪࡰࡧࡩࡽࠦࠧ૞") + str(
      item_index) + bstack1l111l1_opy_ (u"ࠫࠥ࠭૟") + bstack11ll1lll_opy_, 1)
  else:
    command[0] = command[0].replace(bstack1l111l1_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫૠ"),
                                    bstack1l111l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠲ࡹࡤ࡬ࠢࡵࡳࡧࡵࡴ࠮࡫ࡱࡸࡪࡸ࡮ࡢ࡮ࠣ࠱࠲ࡨࡳࡵࡣࡦ࡯ࡤ࡯ࡴࡦ࡯ࡢ࡭ࡳࡪࡥࡹࠢࠪૡ") + str(item_index), 1)
def bstack1ll111l11_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index):
  global bstack1ll1111ll_opy_
  bstack1lll1l111_opy_(command, item_index)
  return bstack1ll1111ll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index)
def bstack1l1l111l1l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir):
  global bstack1ll1111ll_opy_
  bstack1lll1l111_opy_(command, item_index)
  return bstack1ll1111ll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir)
def bstack1l11111l1_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout):
  global bstack1ll1111ll_opy_
  bstack1lll1l111_opy_(command, item_index)
  return bstack1ll1111ll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout)
def bstack1l1lll1l1l_opy_(self, runner, quiet=False, capture=True):
  global bstack1l1ll11l1l_opy_
  bstack1ll111l11l_opy_ = bstack1l1ll11l1l_opy_(self, runner, quiet=False, capture=True)
  if self.exception:
    if not hasattr(runner, bstack1l111l1_opy_ (u"ࠧࡦࡺࡦࡩࡵࡺࡩࡰࡰࡢࡥࡷࡸࠧૢ")):
      runner.exception_arr = []
    if not hasattr(runner, bstack1l111l1_opy_ (u"ࠨࡧࡻࡧࡤࡺࡲࡢࡥࡨࡦࡦࡩ࡫ࡠࡣࡵࡶࠬૣ")):
      runner.exc_traceback_arr = []
    runner.exception = self.exception
    runner.exc_traceback = self.exc_traceback
    runner.exception_arr.append(self.exception)
    runner.exc_traceback_arr.append(self.exc_traceback)
  return bstack1ll111l11l_opy_
def bstack1l1l1ll11l_opy_(self, name, context, *args):
  os.environ[bstack1l111l1_opy_ (u"ࠩࡆ࡙ࡗࡘࡅࡏࡖࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡊࡁࡕࡃࠪ૤")] = json.dumps(CONFIG[bstack1l111l1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭૥")][int(threading.current_thread()._name) % bstack1111lll1l_opy_])
  global bstack111l1l11_opy_
  if name == bstack1l111l1_opy_ (u"ࠫࡧ࡫ࡦࡰࡴࡨࡣ࡫࡫ࡡࡵࡷࡵࡩࠬ૦"):
    bstack111l1l11_opy_(self, name, context, *args)
    try:
      if not bstack111lll11l_opy_:
        bstack1l1lllll1_opy_ = threading.current_thread().bstackSessionDriver if bstack1l1lll11_opy_(bstack1l111l1_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡘ࡫ࡳࡴ࡫ࡲࡲࡉࡸࡩࡷࡧࡵࠫ૧")) else context.browser
        bstack11l1lll1_opy_ = str(self.feature.name)
        bstack1lll11111l_opy_(context, bstack11l1lll1_opy_)
        bstack1l1lllll1_opy_.execute_script(bstack1l111l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠢ࠭ࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽࠥࡲࡦࡳࡥࠣ࠼ࠣࠫ૨") + json.dumps(bstack11l1lll1_opy_) + bstack1l111l1_opy_ (u"ࠧࡾࡿࠪ૩"))
      self.driver_before_scenario = False
    except Exception as e:
      logger.debug(bstack1l111l1_opy_ (u"ࠨࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡸ࡫ࡴࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡱࡥࡲ࡫ࠠࡪࡰࠣࡦࡪ࡬࡯ࡳࡧࠣࡪࡪࡧࡴࡶࡴࡨ࠾ࠥࢁࡽࠨ૪").format(str(e)))
  elif name == bstack1l111l1_opy_ (u"ࠩࡥࡩ࡫ࡵࡲࡦࡡࡶࡧࡪࡴࡡࡳ࡫ࡲࠫ૫"):
    bstack111l1l11_opy_(self, name, context, *args)
    try:
      if not hasattr(self, bstack1l111l1_opy_ (u"ࠪࡨࡷ࡯ࡶࡦࡴࡢࡦࡪ࡬࡯ࡳࡧࡢࡷࡨ࡫࡮ࡢࡴ࡬ࡳࠬ૬")):
        self.driver_before_scenario = True
      if (not bstack111lll11l_opy_):
        scenario_name = args[0].name
        feature_name = bstack11l1lll1_opy_ = str(self.feature.name)
        bstack11l1lll1_opy_ = feature_name + bstack1l111l1_opy_ (u"ࠫࠥ࠳ࠠࠨ૭") + scenario_name
        bstack1l1lllll1_opy_ = threading.current_thread().bstackSessionDriver if bstack1l1lll11_opy_(bstack1l111l1_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡘ࡫ࡳࡴ࡫ࡲࡲࡉࡸࡩࡷࡧࡵࠫ૮")) else context.browser
        if self.driver_before_scenario:
          bstack1lll11111l_opy_(context, bstack11l1lll1_opy_)
          bstack1l1lllll1_opy_.execute_script(bstack1l111l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠢ࠭ࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽࠥࡲࡦࡳࡥࠣ࠼ࠣࠫ૯") + json.dumps(bstack11l1lll1_opy_) + bstack1l111l1_opy_ (u"ࠧࡾࡿࠪ૰"))
    except Exception as e:
      logger.debug(bstack1l111l1_opy_ (u"ࠨࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡸ࡫ࡴࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡱࡥࡲ࡫ࠠࡪࡰࠣࡦࡪ࡬࡯ࡳࡧࠣࡷࡨ࡫࡮ࡢࡴ࡬ࡳ࠿ࠦࡻࡾࠩ૱").format(str(e)))
  elif name == bstack1l111l1_opy_ (u"ࠩࡤࡪࡹ࡫ࡲࡠࡵࡦࡩࡳࡧࡲࡪࡱࠪ૲"):
    try:
      bstack1l111111_opy_ = args[0].status.name
      bstack1l1lllll1_opy_ = threading.current_thread().bstackSessionDriver if bstack1l111l1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡖࡩࡸࡹࡩࡰࡰࡇࡶ࡮ࡼࡥࡳࠩ૳") in threading.current_thread().__dict__.keys() else context.browser
      if str(bstack1l111111_opy_).lower() == bstack1l111l1_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫ૴"):
        bstack1l11lllll1_opy_ = bstack1l111l1_opy_ (u"ࠬ࠭૵")
        bstack1l11l1ll11_opy_ = bstack1l111l1_opy_ (u"࠭ࠧ૶")
        bstack1l11l11l_opy_ = bstack1l111l1_opy_ (u"ࠧࠨ૷")
        try:
          import traceback
          bstack1l11lllll1_opy_ = self.exception.__class__.__name__
          bstack1l11ll1l_opy_ = traceback.format_tb(self.exc_traceback)
          bstack1l11l1ll11_opy_ = bstack1l111l1_opy_ (u"ࠨࠢࠪ૸").join(bstack1l11ll1l_opy_)
          bstack1l11l11l_opy_ = bstack1l11ll1l_opy_[-1]
        except Exception as e:
          logger.debug(bstack111l1l111_opy_.format(str(e)))
        bstack1l11lllll1_opy_ += bstack1l11l11l_opy_
        bstack11ll111ll_opy_(context, json.dumps(str(args[0].name) + bstack1l111l1_opy_ (u"ࠤࠣ࠱ࠥࡌࡡࡪ࡮ࡨࡨࠦࡢ࡮ࠣૹ") + str(bstack1l11l1ll11_opy_)),
                            bstack1l111l1_opy_ (u"ࠥࡩࡷࡸ࡯ࡳࠤૺ"))
        if self.driver_before_scenario:
          bstack1111l1lll_opy_(getattr(context, bstack1l111l1_opy_ (u"ࠫࡵࡧࡧࡦࠩૻ"), None), bstack1l111l1_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡨࡨࠧૼ"), bstack1l11lllll1_opy_)
          bstack1l1lllll1_opy_.execute_script(bstack1l111l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡡ࡯ࡰࡲࡸࡦࡺࡥࠣ࠮ࠣࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢ࠻ࠢࡾࠦࡩࡧࡴࡢࠤ࠽ࠫ૽") + json.dumps(str(args[0].name) + bstack1l111l1_opy_ (u"ࠢࠡ࠯ࠣࡊࡦ࡯࡬ࡦࡦࠤࡠࡳࠨ૾") + str(bstack1l11l1ll11_opy_)) + bstack1l111l1_opy_ (u"ࠨ࠮ࠣࠦࡱ࡫ࡶࡦ࡮ࠥ࠾ࠥࠨࡥࡳࡴࡲࡶࠧࢃࡽࠨ૿"))
        if self.driver_before_scenario:
          bstack11l11111l_opy_(bstack1l1lllll1_opy_, bstack1l111l1_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩ଀"), bstack1l111l1_opy_ (u"ࠥࡗࡨ࡫࡮ࡢࡴ࡬ࡳࠥ࡬ࡡࡪ࡮ࡨࡨࠥࡽࡩࡵࡪ࠽ࠤࡡࡴࠢଁ") + str(bstack1l11lllll1_opy_))
      else:
        bstack11ll111ll_opy_(context, bstack1l111l1_opy_ (u"ࠦࡕࡧࡳࡴࡧࡧࠥࠧଂ"), bstack1l111l1_opy_ (u"ࠧ࡯࡮ࡧࡱࠥଃ"))
        if self.driver_before_scenario:
          bstack1111l1lll_opy_(getattr(context, bstack1l111l1_opy_ (u"࠭ࡰࡢࡩࡨࠫ଄"), None), bstack1l111l1_opy_ (u"ࠢࡱࡣࡶࡷࡪࡪࠢଅ"))
        bstack1l1lllll1_opy_.execute_script(bstack1l111l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡣࡱࡲࡴࡺࡡࡵࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨࡤࡢࡶࡤࠦ࠿࠭ଆ") + json.dumps(str(args[0].name) + bstack1l111l1_opy_ (u"ࠤࠣ࠱ࠥࡖࡡࡴࡵࡨࡨࠦࠨଇ")) + bstack1l111l1_opy_ (u"ࠪ࠰ࠥࠨ࡬ࡦࡸࡨࡰࠧࡀࠠࠣ࡫ࡱࡪࡴࠨࡽࡾࠩଈ"))
        if self.driver_before_scenario:
          bstack11l11111l_opy_(bstack1l1lllll1_opy_, bstack1l111l1_opy_ (u"ࠦࡵࡧࡳࡴࡧࡧࠦଉ"))
    except Exception as e:
      logger.debug(bstack1l111l1_opy_ (u"ࠬࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡ࡯ࡤࡶࡰࠦࡳࡦࡵࡶ࡭ࡴࡴࠠࡴࡶࡤࡸࡺࡹࠠࡪࡰࠣࡥ࡫ࡺࡥࡳࠢࡩࡩࡦࡺࡵࡳࡧ࠽ࠤࢀࢃࠧଊ").format(str(e)))
  elif name == bstack1l111l1_opy_ (u"࠭ࡡࡧࡶࡨࡶࡤ࡬ࡥࡢࡶࡸࡶࡪ࠭ଋ"):
    try:
      bstack1l1lllll1_opy_ = threading.current_thread().bstackSessionDriver if bstack1l1lll11_opy_(bstack1l111l1_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡓࡦࡵࡶ࡭ࡴࡴࡄࡳ࡫ࡹࡩࡷ࠭ଌ")) else context.browser
      if context.failed is True:
        bstack1l1ll1ll1l_opy_ = []
        bstack11ll11lll_opy_ = []
        bstack1llll11l1_opy_ = []
        bstack1l11l1ll1_opy_ = bstack1l111l1_opy_ (u"ࠨࠩ଍")
        try:
          import traceback
          for exc in self.exception_arr:
            bstack1l1ll1ll1l_opy_.append(exc.__class__.__name__)
          for exc_tb in self.exc_traceback_arr:
            bstack1l11ll1l_opy_ = traceback.format_tb(exc_tb)
            bstack1lllll1lll_opy_ = bstack1l111l1_opy_ (u"ࠩࠣࠫ଎").join(bstack1l11ll1l_opy_)
            bstack11ll11lll_opy_.append(bstack1lllll1lll_opy_)
            bstack1llll11l1_opy_.append(bstack1l11ll1l_opy_[-1])
        except Exception as e:
          logger.debug(bstack111l1l111_opy_.format(str(e)))
        bstack1l11lllll1_opy_ = bstack1l111l1_opy_ (u"ࠪࠫଏ")
        for i in range(len(bstack1l1ll1ll1l_opy_)):
          bstack1l11lllll1_opy_ += bstack1l1ll1ll1l_opy_[i] + bstack1llll11l1_opy_[i] + bstack1l111l1_opy_ (u"ࠫࡡࡴࠧଐ")
        bstack1l11l1ll1_opy_ = bstack1l111l1_opy_ (u"ࠬࠦࠧ଑").join(bstack11ll11lll_opy_)
        if not self.driver_before_scenario:
          bstack11ll111ll_opy_(context, bstack1l11l1ll1_opy_, bstack1l111l1_opy_ (u"ࠨࡥࡳࡴࡲࡶࠧ଒"))
          bstack1111l1lll_opy_(getattr(context, bstack1l111l1_opy_ (u"ࠧࡱࡣࡪࡩࠬଓ"), None), bstack1l111l1_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࠣଔ"), bstack1l11lllll1_opy_)
          bstack1l1lllll1_opy_.execute_script(bstack1l111l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡤࡲࡳࡵࡴࡢࡶࡨࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢࡥࡣࡷࡥࠧࡀࠧକ") + json.dumps(bstack1l11l1ll1_opy_) + bstack1l111l1_opy_ (u"ࠪ࠰ࠥࠨ࡬ࡦࡸࡨࡰࠧࡀࠠࠣࡧࡵࡶࡴࡸࠢࡾࡿࠪଖ"))
          bstack11l11111l_opy_(bstack1l1lllll1_opy_, bstack1l111l1_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࠦଗ"), bstack1l111l1_opy_ (u"࡙ࠧ࡯࡮ࡧࠣࡷࡨ࡫࡮ࡢࡴ࡬ࡳࡸࠦࡦࡢ࡫࡯ࡩࡩࡀࠠ࡝ࡰࠥଘ") + str(bstack1l11lllll1_opy_))
          bstack1lllllllll_opy_ = bstack1ll1lll1l_opy_(bstack1l11l1ll1_opy_, self.feature.name, logger)
          if (bstack1lllllllll_opy_ != None):
            bstack1l111lll1_opy_.append(bstack1lllllllll_opy_)
      else:
        if not self.driver_before_scenario:
          bstack11ll111ll_opy_(context, bstack1l111l1_opy_ (u"ࠨࡆࡦࡣࡷࡹࡷ࡫࠺ࠡࠤଙ") + str(self.feature.name) + bstack1l111l1_opy_ (u"ࠢࠡࡲࡤࡷࡸ࡫ࡤࠢࠤଚ"), bstack1l111l1_opy_ (u"ࠣ࡫ࡱࡪࡴࠨଛ"))
          bstack1111l1lll_opy_(getattr(context, bstack1l111l1_opy_ (u"ࠩࡳࡥ࡬࡫ࠧଜ"), None), bstack1l111l1_opy_ (u"ࠥࡴࡦࡹࡳࡦࡦࠥଝ"))
          bstack1l1lllll1_opy_.execute_script(bstack1l111l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡦࡴ࡮ࡰࡶࡤࡸࡪࠨࠬࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼࠤࡧࡥࡹࡧࠢ࠻ࠩଞ") + json.dumps(bstack1l111l1_opy_ (u"ࠧࡌࡥࡢࡶࡸࡶࡪࡀࠠࠣଟ") + str(self.feature.name) + bstack1l111l1_opy_ (u"ࠨࠠࡱࡣࡶࡷࡪࡪࠡࠣଠ")) + bstack1l111l1_opy_ (u"ࠧ࠭ࠢࠥࡰࡪࡼࡥ࡭ࠤ࠽ࠤࠧ࡯࡮ࡧࡱࠥࢁࢂ࠭ଡ"))
          bstack11l11111l_opy_(bstack1l1lllll1_opy_, bstack1l111l1_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨଢ"))
          bstack1lllllllll_opy_ = bstack1ll1lll1l_opy_(bstack1l11l1ll1_opy_, self.feature.name, logger)
          if (bstack1lllllllll_opy_ != None):
            bstack1l111lll1_opy_.append(bstack1lllllllll_opy_)
    except Exception as e:
      logger.debug(bstack1l111l1_opy_ (u"ࠩࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡳࡡࡳ࡭ࠣࡷࡪࡹࡳࡪࡱࡱࠤࡸࡺࡡࡵࡷࡶࠤ࡮ࡴࠠࡢࡨࡷࡩࡷࠦࡦࡦࡣࡷࡹࡷ࡫࠺ࠡࡽࢀࠫଣ").format(str(e)))
  else:
    bstack111l1l11_opy_(self, name, context, *args)
  if name in [bstack1l111l1_opy_ (u"ࠪࡥ࡫ࡺࡥࡳࡡࡩࡩࡦࡺࡵࡳࡧࠪତ"), bstack1l111l1_opy_ (u"ࠫࡦ࡬ࡴࡦࡴࡢࡷࡨ࡫࡮ࡢࡴ࡬ࡳࠬଥ")]:
    bstack111l1l11_opy_(self, name, context, *args)
    if (name == bstack1l111l1_opy_ (u"ࠬࡧࡦࡵࡧࡵࡣࡸࡩࡥ࡯ࡣࡵ࡭ࡴ࠭ଦ") and self.driver_before_scenario) or (
            name == bstack1l111l1_opy_ (u"࠭ࡡࡧࡶࡨࡶࡤ࡬ࡥࡢࡶࡸࡶࡪ࠭ଧ") and not self.driver_before_scenario):
      try:
        bstack1l1lllll1_opy_ = threading.current_thread().bstackSessionDriver if bstack1l1lll11_opy_(bstack1l111l1_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡓࡦࡵࡶ࡭ࡴࡴࡄࡳ࡫ࡹࡩࡷ࠭ନ")) else context.browser
        bstack1l1lllll1_opy_.quit()
      except Exception:
        pass
def bstack1lll1l1ll1_opy_(config, startdir):
  return bstack1l111l1_opy_ (u"ࠣࡦࡵ࡭ࡻ࡫ࡲ࠻ࠢࡾ࠴ࢂࠨ଩").format(bstack1l111l1_opy_ (u"ࠤࡅࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࠣପ"))
notset = Notset()
def bstack111l111l_opy_(self, name: str, default=notset, skip: bool = False):
  global bstack1ll111ll11_opy_
  if str(name).lower() == bstack1l111l1_opy_ (u"ࠪࡨࡷ࡯ࡶࡦࡴࠪଫ"):
    return bstack1l111l1_opy_ (u"ࠦࡇࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࠥବ")
  else:
    return bstack1ll111ll11_opy_(self, name, default, skip)
def bstack1l1l1l1lll_opy_(item, when):
  global bstack111l111ll_opy_
  try:
    bstack111l111ll_opy_(item, when)
  except Exception as e:
    pass
def bstack1ll11l11l_opy_():
  return
def bstack1ll11111l1_opy_(type, name, status, reason, bstack1llll1ll1l_opy_, bstack11ll111l_opy_):
  bstack1l11lll1l1_opy_ = {
    bstack1l111l1_opy_ (u"ࠬࡧࡣࡵ࡫ࡲࡲࠬଭ"): type,
    bstack1l111l1_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩମ"): {}
  }
  if type == bstack1l111l1_opy_ (u"ࠧࡢࡰࡱࡳࡹࡧࡴࡦࠩଯ"):
    bstack1l11lll1l1_opy_[bstack1l111l1_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫର")][bstack1l111l1_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨ଱")] = bstack1llll1ll1l_opy_
    bstack1l11lll1l1_opy_[bstack1l111l1_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭ଲ")][bstack1l111l1_opy_ (u"ࠫࡩࡧࡴࡢࠩଳ")] = json.dumps(str(bstack11ll111l_opy_))
  if type == bstack1l111l1_opy_ (u"ࠬࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭଴"):
    bstack1l11lll1l1_opy_[bstack1l111l1_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩଵ")][bstack1l111l1_opy_ (u"ࠧ࡯ࡣࡰࡩࠬଶ")] = name
  if type == bstack1l111l1_opy_ (u"ࠨࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡘࡺࡡࡵࡷࡶࠫଷ"):
    bstack1l11lll1l1_opy_[bstack1l111l1_opy_ (u"ࠩࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠬସ")][bstack1l111l1_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪହ")] = status
    if status == bstack1l111l1_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫ଺"):
      bstack1l11lll1l1_opy_[bstack1l111l1_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨ଻")][bstack1l111l1_opy_ (u"࠭ࡲࡦࡣࡶࡳࡳ଼࠭")] = json.dumps(str(reason))
  bstack1ll11lll_opy_ = bstack1l111l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࢁࠬଽ").format(json.dumps(bstack1l11lll1l1_opy_))
  return bstack1ll11lll_opy_
def bstack1ll1ll11_opy_(driver_command, response):
    if driver_command == bstack1l111l1_opy_ (u"ࠨࡵࡦࡶࡪ࡫࡮ࡴࡪࡲࡸࠬା"):
        bstack1l1111l1l_opy_.bstack1ll1l1l1l1_opy_({
            bstack1l111l1_opy_ (u"ࠩ࡬ࡱࡦ࡭ࡥࠨି"): response[bstack1l111l1_opy_ (u"ࠪࡺࡦࡲࡵࡦࠩୀ")],
            bstack1l111l1_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫୁ"): bstack1l1111l1l_opy_.current_test_uuid()
        })
def bstack111l11ll_opy_(item, call, rep):
  global bstack1l11l1l11l_opy_
  global bstack11lll1l1_opy_
  global bstack111lll11l_opy_
  name = bstack1l111l1_opy_ (u"ࠬ࠭ୂ")
  try:
    if rep.when == bstack1l111l1_opy_ (u"࠭ࡣࡢ࡮࡯ࠫୃ"):
      bstack1lll1ll1_opy_ = threading.current_thread().bstackSessionId
      try:
        if not bstack111lll11l_opy_:
          name = str(rep.nodeid)
          bstack1ll111l1l_opy_ = bstack1ll11111l1_opy_(bstack1l111l1_opy_ (u"ࠧࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨୄ"), name, bstack1l111l1_opy_ (u"ࠨࠩ୅"), bstack1l111l1_opy_ (u"ࠩࠪ୆"), bstack1l111l1_opy_ (u"ࠪࠫେ"), bstack1l111l1_opy_ (u"ࠫࠬୈ"))
          threading.current_thread().bstack1111llll_opy_ = name
          for driver in bstack11lll1l1_opy_:
            if bstack1lll1ll1_opy_ == driver.session_id:
              driver.execute_script(bstack1ll111l1l_opy_)
      except Exception as e:
        logger.debug(bstack1l111l1_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡴࡧࡷࡸ࡮ࡴࡧࠡࡵࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪࠦࡦࡰࡴࠣࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠠࡴࡧࡶࡷ࡮ࡵ࡮࠻ࠢࡾࢁࠬ୉").format(str(e)))
      try:
        bstack11ll1l111_opy_(rep.outcome.lower())
        if rep.outcome.lower() != bstack1l111l1_opy_ (u"࠭ࡳ࡬࡫ࡳࡴࡪࡪࠧ୊"):
          status = bstack1l111l1_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧୋ") if rep.outcome.lower() == bstack1l111l1_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨୌ") else bstack1l111l1_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥ୍ࠩ")
          reason = bstack1l111l1_opy_ (u"ࠪࠫ୎")
          if status == bstack1l111l1_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫ୏"):
            reason = rep.longrepr.reprcrash.message
            if (not threading.current_thread().bstackTestErrorMessages):
              threading.current_thread().bstackTestErrorMessages = []
            threading.current_thread().bstackTestErrorMessages.append(reason)
          level = bstack1l111l1_opy_ (u"ࠬ࡯࡮ࡧࡱࠪ୐") if status == bstack1l111l1_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭୑") else bstack1l111l1_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭୒")
          data = name + bstack1l111l1_opy_ (u"ࠨࠢࡳࡥࡸࡹࡥࡥࠣࠪ୓") if status == bstack1l111l1_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩ୔") else name + bstack1l111l1_opy_ (u"ࠪࠤ࡫ࡧࡩ࡭ࡧࡧࠥࠥ࠭୕") + reason
          bstack1l1ll1l11l_opy_ = bstack1ll11111l1_opy_(bstack1l111l1_opy_ (u"ࠫࡦࡴ࡮ࡰࡶࡤࡸࡪ࠭ୖ"), bstack1l111l1_opy_ (u"ࠬ࠭ୗ"), bstack1l111l1_opy_ (u"࠭ࠧ୘"), bstack1l111l1_opy_ (u"ࠧࠨ୙"), level, data)
          for driver in bstack11lll1l1_opy_:
            if bstack1lll1ll1_opy_ == driver.session_id:
              driver.execute_script(bstack1l1ll1l11l_opy_)
      except Exception as e:
        logger.debug(bstack1l111l1_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡷࡪࡺࡴࡪࡰࡪࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡩ࡯࡯ࡶࡨࡼࡹࠦࡦࡰࡴࠣࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠠࡴࡧࡶࡷ࡮ࡵ࡮࠻ࠢࡾࢁࠬ୚").format(str(e)))
  except Exception as e:
    logger.debug(bstack1l111l1_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤ࡬࡫ࡴࡵ࡫ࡱ࡫ࠥࡹࡴࡢࡶࡨࠤ࡮ࡴࠠࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠤࡹ࡫ࡳࡵࠢࡶࡸࡦࡺࡵࡴ࠼ࠣࡿࢂ࠭୛").format(str(e)))
  bstack1l11l1l11l_opy_(item, call, rep)
def bstack11l111ll1_opy_(driver, bstack1l1ll1ll1_opy_):
  PercySDK.screenshot(driver, bstack1l1ll1ll1_opy_)
def bstack11l1lllll_opy_(driver):
  if bstack1ll1l1111l_opy_.bstack1lll11ll1_opy_() is True or bstack1ll1l1111l_opy_.capturing() is True:
    return
  bstack1ll1l1111l_opy_.bstack1ll1l1l111_opy_()
  while not bstack1ll1l1111l_opy_.bstack1lll11ll1_opy_():
    bstack1l1l1ll1l_opy_ = bstack1ll1l1111l_opy_.bstack1ll1ll1l11_opy_()
    bstack11l111ll1_opy_(driver, bstack1l1l1ll1l_opy_)
  bstack1ll1l1111l_opy_.bstack1lll11l1ll_opy_()
def bstack1l11l1l1l_opy_(sequence, driver_command, response = None, bstack1lll11lll1_opy_ = None, args = None):
    try:
      if sequence != bstack1l111l1_opy_ (u"ࠪࡦࡪ࡬࡯ࡳࡧࠪଡ଼"):
        return
      if not CONFIG.get(bstack1l111l1_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࠪଢ଼"), False):
        return
      bstack1l1l1ll1l_opy_ = bstack1ll1ll1l1_opy_(threading.current_thread(), bstack1l111l1_opy_ (u"ࠬࡶࡥࡳࡥࡼࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨ୞"), None)
      for command in bstack111l1l1ll_opy_:
        if command == driver_command:
          for driver in bstack11lll1l1_opy_:
            bstack11l1lllll_opy_(driver)
      bstack1l1111ll_opy_ = CONFIG.get(bstack1l111l1_opy_ (u"࠭ࡰࡦࡴࡦࡽࡈࡧࡰࡵࡷࡵࡩࡒࡵࡤࡦࠩୟ"), bstack1l111l1_opy_ (u"ࠢࡢࡷࡷࡳࠧୠ"))
      if driver_command in bstack1lllll11ll_opy_[bstack1l1111ll_opy_]:
        bstack1ll1l1111l_opy_.bstack1lll1l1l11_opy_(bstack1l1l1ll1l_opy_, driver_command)
    except Exception as e:
      pass
def bstack1ll111llll_opy_(framework_name):
  global bstack11l1l11ll_opy_
  global bstack1ll1l111l_opy_
  global bstack1l1l1l1ll1_opy_
  bstack11l1l11ll_opy_ = framework_name
  logger.info(bstack1ll11l1ll1_opy_.format(bstack11l1l11ll_opy_.split(bstack1l111l1_opy_ (u"ࠨ࠯ࠪୡ"))[0]))
  try:
    from selenium import webdriver
    from selenium.webdriver.common.service import Service
    from selenium.webdriver.remote.webdriver import WebDriver
    if bstack1lll1l1lll_opy_:
      Service.start = bstack1l11llll1_opy_
      Service.stop = bstack1l1l11ll1_opy_
      webdriver.Remote.get = bstack1lllll1l1_opy_
      WebDriver.close = bstack111l1ll1l_opy_
      WebDriver.quit = bstack1ll1l1111_opy_
      webdriver.Remote.__init__ = bstack1111l1111_opy_
      WebDriver.getAccessibilityResults = getAccessibilityResults
      WebDriver.get_accessibility_results = getAccessibilityResults
      WebDriver.getAccessibilityResultsSummary = getAccessibilityResultsSummary
      WebDriver.get_accessibility_results_summary = getAccessibilityResultsSummary
      WebDriver.performScan = perform_scan
      WebDriver.perform_scan = perform_scan
    if not bstack1lll1l1lll_opy_ and bstack1l1111l1l_opy_.on():
      webdriver.Remote.__init__ = bstack1l1l1l11l1_opy_
    WebDriver.execute = bstack1llll1l1l_opy_
    bstack1ll1l111l_opy_ = True
  except Exception as e:
    pass
  try:
    if bstack1lll1l1lll_opy_:
      from QWeb.keywords import browser
      browser.close_browser = bstack111llll1_opy_
  except Exception as e:
    pass
  bstack1lll1ll11_opy_()
  if not bstack1ll1l111l_opy_:
    bstack111l11l1l_opy_(bstack1l111l1_opy_ (u"ࠤࡓࡥࡨࡱࡡࡨࡧࡶࠤࡳࡵࡴࠡ࡫ࡱࡷࡹࡧ࡬࡭ࡧࡧࠦୢ"), bstack1llll11ll_opy_)
  if bstack1l1l1lll1_opy_():
    try:
      from selenium.webdriver.remote.remote_connection import RemoteConnection
      RemoteConnection._get_proxy_url = bstack1l1lll1111_opy_
    except Exception as e:
      logger.error(bstack1l1ll11111_opy_.format(str(e)))
  if bstack1lll111l1_opy_():
    bstack1l1l1l11l_opy_(CONFIG, logger)
  if (bstack1l111l1_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩୣ") in str(framework_name).lower()):
    try:
      from robot import run_cli
      from robot.output import Output
      from robot.running.status import TestStatus
      from pabot.pabot import QueueItem
      from pabot import pabot
      try:
        if CONFIG.get(bstack1l111l1_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࠪ୤"), False):
          bstack1l1l1111l_opy_(bstack1l11l1l1l_opy_)
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCreator
        WebDriverCreator._get_ff_profile = bstack1111ll111_opy_
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCache
        WebDriverCache.close = bstack1ll11ll1l_opy_
      except Exception as e:
        logger.warn(bstack1lll111111_opy_ + str(e))
      try:
        from AppiumLibrary.utils.applicationcache import ApplicationCache
        ApplicationCache.close = bstack11111l111_opy_
      except Exception as e:
        logger.debug(bstack11l1llll_opy_ + str(e))
    except Exception as e:
      bstack111l11l1l_opy_(e, bstack1lll111111_opy_)
    Output.start_test = bstack1111ll11l_opy_
    Output.end_test = bstack11lll11l_opy_
    TestStatus.__init__ = bstack1l1l1111ll_opy_
    QueueItem.__init__ = bstack1ll1lll11l_opy_
    pabot._create_items = bstack1l1ll1111_opy_
    try:
      from pabot import __version__ as bstack11l11l1l1_opy_
      if version.parse(bstack11l11l1l1_opy_) >= version.parse(bstack1l111l1_opy_ (u"ࠬ࠸࠮࠲࠷࠱࠴ࠬ୥")):
        pabot._run = bstack1l11111l1_opy_
      elif version.parse(bstack11l11l1l1_opy_) >= version.parse(bstack1l111l1_opy_ (u"࠭࠲࠯࠳࠶࠲࠵࠭୦")):
        pabot._run = bstack1l1l111l1l_opy_
      else:
        pabot._run = bstack1ll111l11_opy_
    except Exception as e:
      pabot._run = bstack1ll111l11_opy_
    pabot._create_command_for_execution = bstack1l1lllll_opy_
    pabot._report_results = bstack1lllll11l_opy_
  if bstack1l111l1_opy_ (u"ࠧࡣࡧ࡫ࡥࡻ࡫ࠧ୧") in str(framework_name).lower():
    if not bstack1lll1l1lll_opy_:
      return
    try:
      from behave.runner import Runner
      from behave.model import Step
    except Exception as e:
      bstack111l11l1l_opy_(e, bstack1ll11l1l11_opy_)
    Runner.run_hook = bstack1l1l1ll11l_opy_
    Step.run = bstack1l1lll1l1l_opy_
  if bstack1l111l1_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨ୨") in str(framework_name).lower():
    if not bstack1lll1l1lll_opy_:
      return
    try:
      if CONFIG.get(bstack1l111l1_opy_ (u"ࠩࡳࡩࡷࡩࡹࠨ୩"), False):
          bstack1l1l1111l_opy_(bstack1l11l1l1l_opy_)
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
def bstack1lll1l1l_opy_():
  global CONFIG
  if bstack1l111l1_opy_ (u"ࠪࡴࡦࡸࡡ࡭࡮ࡨࡰࡸࡖࡥࡳࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪ୪") in CONFIG and int(CONFIG[bstack1l111l1_opy_ (u"ࠫࡵࡧࡲࡢ࡮࡯ࡩࡱࡹࡐࡦࡴࡓࡰࡦࡺࡦࡰࡴࡰࠫ୫")]) > 1:
    logger.warn(bstack11llllll1_opy_)
def bstack1lll11l1_opy_(arg, bstack11llll1ll_opy_, bstack11ll1lll1_opy_=None):
  global CONFIG
  global bstack1l1l11111_opy_
  global bstack1l1llll1l1_opy_
  global bstack1lll1l1lll_opy_
  global bstack11111111_opy_
  bstack11l1l11l_opy_ = bstack1l111l1_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬ୬")
  if bstack11llll1ll_opy_ and isinstance(bstack11llll1ll_opy_, str):
    bstack11llll1ll_opy_ = eval(bstack11llll1ll_opy_)
  CONFIG = bstack11llll1ll_opy_[bstack1l111l1_opy_ (u"࠭ࡃࡐࡐࡉࡍࡌ࠭୭")]
  bstack1l1l11111_opy_ = bstack11llll1ll_opy_[bstack1l111l1_opy_ (u"ࠧࡉࡗࡅࡣ࡚ࡘࡌࠨ୮")]
  bstack1l1llll1l1_opy_ = bstack11llll1ll_opy_[bstack1l111l1_opy_ (u"ࠨࡋࡖࡣࡆࡖࡐࡠࡃࡘࡘࡔࡓࡁࡕࡇࠪ୯")]
  bstack1lll1l1lll_opy_ = bstack11llll1ll_opy_[bstack1l111l1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡃࡘࡘࡔࡓࡁࡕࡋࡒࡒࠬ୰")]
  bstack11111111_opy_.bstack111ll1ll_opy_(bstack1l111l1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡢࡷࡪࡹࡳࡪࡱࡱࠫୱ"), bstack1lll1l1lll_opy_)
  os.environ[bstack1l111l1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡊࡗࡇࡍࡆ࡙ࡒࡖࡐ࠭୲")] = bstack11l1l11l_opy_
  os.environ[bstack1l111l1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡈࡕࡎࡇࡋࡊࠫ୳")] = json.dumps(CONFIG)
  os.environ[bstack1l111l1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡎࡕࡃࡡࡘࡖࡑ࠭୴")] = bstack1l1l11111_opy_
  os.environ[bstack1l111l1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡉࡔࡡࡄࡔࡕࡥࡁࡖࡖࡒࡑࡆ࡚ࡅࠨ୵")] = str(bstack1l1llll1l1_opy_)
  os.environ[bstack1l111l1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑ࡛ࡗࡉࡘ࡚࡟ࡑࡎࡘࡋࡎࡔࠧ୶")] = str(True)
  if bstack1111l1l1_opy_(arg, [bstack1l111l1_opy_ (u"ࠩ࠰ࡲࠬ୷"), bstack1l111l1_opy_ (u"ࠪ࠱࠲ࡴࡵ࡮ࡲࡵࡳࡨ࡫ࡳࡴࡧࡶࠫ୸")]) != -1:
    os.environ[bstack1l111l1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔ࡞࡚ࡅࡔࡖࡢࡔࡆࡘࡁࡍࡎࡈࡐࠬ୹")] = str(True)
  if len(sys.argv) <= 1:
    logger.critical(bstack1l1ll1l1l1_opy_)
    return
  bstack1llll1ll11_opy_()
  global bstack1ll1111ll1_opy_
  global bstack1llll1ll1_opy_
  global bstack1l1l11l111_opy_
  global bstack11ll1lll_opy_
  global bstack1lll1lll1_opy_
  global bstack1l1l1l1ll1_opy_
  global bstack1ll1l11lll_opy_
  arg.append(bstack1l111l1_opy_ (u"ࠧ࠳ࡗࠣ୺"))
  arg.append(bstack1l111l1_opy_ (u"ࠨࡩࡨࡰࡲࡶࡪࡀࡍࡰࡦࡸࡰࡪࠦࡡ࡭ࡴࡨࡥࡩࡿࠠࡪ࡯ࡳࡳࡷࡺࡥࡥ࠼ࡳࡽࡹ࡫ࡳࡵ࠰ࡓࡽࡹ࡫ࡳࡵ࡙ࡤࡶࡳ࡯࡮ࡨࠤ୻"))
  arg.append(bstack1l111l1_opy_ (u"ࠢ࠮࡙ࠥ୼"))
  arg.append(bstack1l111l1_opy_ (u"ࠣ࡫ࡪࡲࡴࡸࡥ࠻ࡖ࡫ࡩࠥ࡮࡯ࡰ࡭࡬ࡱࡵࡲࠢ୽"))
  global bstack1lllll111_opy_
  global bstack1l11ll1ll_opy_
  global bstack111lll11_opy_
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
    bstack111lll11_opy_ = WebDriver.execute
  except Exception as e:
    pass
  if bstack1l1ll1lll1_opy_(CONFIG) and bstack1l1111l11_opy_():
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
    logger.debug(bstack1l111l1_opy_ (u"ࠩࡓࡰࡪࡧࡳࡦࠢ࡬ࡲࡸࡺࡡ࡭࡮ࠣࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠠࡵࡱࠣࡶࡺࡴࠠࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠤࡹ࡫ࡳࡵࡵࠪ୾"))
  bstack1l1l11l111_opy_ = CONFIG.get(bstack1l111l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧ୿"), {}).get(bstack1l111l1_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭஀"))
  bstack1ll1l11lll_opy_ = True
  bstack1ll111llll_opy_(bstack1ll1ll11ll_opy_)
  os.environ[bstack1l111l1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡚࡙ࡅࡓࡐࡄࡑࡊ࠭஁")] = CONFIG[bstack1l111l1_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨஂ")]
  os.environ[bstack1l111l1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡁࡄࡅࡈࡗࡘࡥࡋࡆ࡛ࠪஃ")] = CONFIG[bstack1l111l1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫ஄")]
  os.environ[bstack1l111l1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡃࡘࡘࡔࡓࡁࡕࡋࡒࡒࠬஅ")] = bstack1lll1l1lll_opy_.__str__()
  from _pytest.config import main as bstack1ll1llllll_opy_
  bstack1l1l1llll_opy_ = bstack1ll1llllll_opy_(arg)
  bstack1ll1ll111l_opy_ = []
  if bstack1l111l1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡢࡩࡷࡸ࡯ࡳࡡ࡯࡭ࡸࡺࠧஆ") in multiprocessing.current_process().__dict__.keys():
    for bstack11ll1111_opy_ in multiprocessing.current_process().bstack_error_list:
      bstack1ll1ll111l_opy_.append(bstack11ll1111_opy_)
  try:
    bstack11l11llll_opy_ = (bstack1ll1ll111l_opy_, int(bstack1l1l1llll_opy_))
    bstack11ll1lll1_opy_.append(bstack11l11llll_opy_)
  except:
    bstack11ll1lll1_opy_.append((bstack1ll1ll111l_opy_, bstack1l1l1llll_opy_))
def bstack111ll1l11_opy_(arg):
  bstack1ll111llll_opy_(bstack1l1l1l11_opy_)
  os.environ[bstack1l111l1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡍࡘࡥࡁࡑࡒࡢࡅ࡚࡚ࡏࡎࡃࡗࡉࠬஇ")] = str(bstack1l1llll1l1_opy_)
  from behave.__main__ import main as bstack11l1l1ll1_opy_
  bstack11l1l1ll1_opy_(arg)
def bstack1l11l1l11_opy_():
  logger.info(bstack1llll11l_opy_)
  import argparse
  parser = argparse.ArgumentParser()
  parser.add_argument(bstack1l111l1_opy_ (u"ࠬࡹࡥࡵࡷࡳࠫஈ"), help=bstack1l111l1_opy_ (u"࠭ࡇࡦࡰࡨࡶࡦࡺࡥࠡࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠠࡤࡱࡱࡪ࡮࡭ࠧஉ"))
  parser.add_argument(bstack1l111l1_opy_ (u"ࠧ࠮ࡷࠪஊ"), bstack1l111l1_opy_ (u"ࠨ࠯࠰ࡹࡸ࡫ࡲ࡯ࡣࡰࡩࠬ஋"), help=bstack1l111l1_opy_ (u"ࠩ࡜ࡳࡺࡸࠠࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࠦࡵࡴࡧࡵࡲࡦࡳࡥࠨ஌"))
  parser.add_argument(bstack1l111l1_opy_ (u"ࠪ࠱ࡰ࠭஍"), bstack1l111l1_opy_ (u"ࠫ࠲࠳࡫ࡦࡻࠪஎ"), help=bstack1l111l1_opy_ (u"ࠬ࡟࡯ࡶࡴࠣࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠢࡤࡧࡨ࡫ࡳࡴࠢ࡮ࡩࡾ࠭ஏ"))
  parser.add_argument(bstack1l111l1_opy_ (u"࠭࠭ࡧࠩஐ"), bstack1l111l1_opy_ (u"ࠧ࠮࠯ࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠬ஑"), help=bstack1l111l1_opy_ (u"ࠨ࡛ࡲࡹࡷࠦࡴࡦࡵࡷࠤ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧஒ"))
  bstack1l1lllll11_opy_ = parser.parse_args()
  try:
    bstack1ll1111l11_opy_ = bstack1l111l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡩࡨࡲࡪࡸࡩࡤ࠰ࡼࡱࡱ࠴ࡳࡢ࡯ࡳࡰࡪ࠭ஓ")
    if bstack1l1lllll11_opy_.framework and bstack1l1lllll11_opy_.framework not in (bstack1l111l1_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰࠪஔ"), bstack1l111l1_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱ࠷ࠬக")):
      bstack1ll1111l11_opy_ = bstack1l111l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࠮ࡺ࡯࡯࠲ࡸࡧ࡭ࡱ࡮ࡨࠫ஖")
    bstack1ll1l11ll1_opy_ = os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack1ll1111l11_opy_)
    bstack1l111l11l_opy_ = open(bstack1ll1l11ll1_opy_, bstack1l111l1_opy_ (u"࠭ࡲࠨ஗"))
    bstack1lllllll1l_opy_ = bstack1l111l11l_opy_.read()
    bstack1l111l11l_opy_.close()
    if bstack1l1lllll11_opy_.username:
      bstack1lllllll1l_opy_ = bstack1lllllll1l_opy_.replace(bstack1l111l1_opy_ (u"࡚ࠧࡑࡘࡖࡤ࡛ࡓࡆࡔࡑࡅࡒࡋࠧ஘"), bstack1l1lllll11_opy_.username)
    if bstack1l1lllll11_opy_.key:
      bstack1lllllll1l_opy_ = bstack1lllllll1l_opy_.replace(bstack1l111l1_opy_ (u"ࠨ࡛ࡒ࡙ࡗࡥࡁࡄࡅࡈࡗࡘࡥࡋࡆ࡛ࠪங"), bstack1l1lllll11_opy_.key)
    if bstack1l1lllll11_opy_.framework:
      bstack1lllllll1l_opy_ = bstack1lllllll1l_opy_.replace(bstack1l111l1_opy_ (u"ࠩ࡜ࡓ࡚ࡘ࡟ࡇࡔࡄࡑࡊ࡝ࡏࡓࡍࠪச"), bstack1l1lllll11_opy_.framework)
    file_name = bstack1l111l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡼࡱࡱ࠭஛")
    file_path = os.path.abspath(file_name)
    bstack11l11lll_opy_ = open(file_path, bstack1l111l1_opy_ (u"ࠫࡼ࠭ஜ"))
    bstack11l11lll_opy_.write(bstack1lllllll1l_opy_)
    bstack11l11lll_opy_.close()
    logger.info(bstack11l11ll1_opy_)
    try:
      os.environ[bstack1l111l1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡋࡘࡁࡎࡇ࡚ࡓࡗࡑࠧ஝")] = bstack1l1lllll11_opy_.framework if bstack1l1lllll11_opy_.framework != None else bstack1l111l1_opy_ (u"ࠨࠢஞ")
      config = yaml.safe_load(bstack1lllllll1l_opy_)
      config[bstack1l111l1_opy_ (u"ࠧࡴࡱࡸࡶࡨ࡫ࠧட")] = bstack1l111l1_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮࠮ࡵࡨࡸࡺࡶࠧ஠")
      bstack1lllll1111_opy_(bstack1111111l1_opy_, config)
    except Exception as e:
      logger.debug(bstack11llll111_opy_.format(str(e)))
  except Exception as e:
    logger.error(bstack1l1ll111ll_opy_.format(str(e)))
def bstack1lllll1111_opy_(bstack1lll1ll1l1_opy_, config, bstack1lll1l111l_opy_={}):
  global bstack1lll1l1lll_opy_
  global bstack11lll111_opy_
  if not config:
    return
  bstack1111l11ll_opy_ = bstack1ll1l1llll_opy_ if not bstack1lll1l1lll_opy_ else (
    bstack1l11lll11_opy_ if bstack1l111l1_opy_ (u"ࠩࡤࡴࡵ࠭஡") in config else bstack1lll1l1ll_opy_)
  bstack111111lll_opy_ = False
  bstack1ll1ll1111_opy_ = False
  if bstack1lll1l1lll_opy_ is True:
      if bstack1l111l1_opy_ (u"ࠪࡥࡵࡶࠧ஢") in config:
          bstack111111lll_opy_ = True
      else:
          bstack1ll1ll1111_opy_ = True
  bstack1l1l111ll_opy_ = {
      bstack1l111l1_opy_ (u"ࠫࡴࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࠫண"): bstack1l1111l1l_opy_.bstack11l1llll1_opy_(),
      bstack1l111l1_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬத"): bstack1l1lll11l1_opy_.bstack1111l1ll_opy_(config),
      bstack1l111l1_opy_ (u"࠭ࡰࡦࡴࡦࡽࠬ஥"): config.get(bstack1l111l1_opy_ (u"ࠧࡱࡧࡵࡧࡾ࠭஦"), False),
      bstack1l111l1_opy_ (u"ࠨࡣࡸࡸࡴࡳࡡࡵࡧࠪ஧"): bstack1ll1ll1111_opy_,
      bstack1l111l1_opy_ (u"ࠩࡤࡴࡵࡥࡡࡶࡶࡲࡱࡦࡺࡥࠨந"): bstack111111lll_opy_
  }
  data = {
    bstack1l111l1_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬன"): config[bstack1l111l1_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ࠭ப")],
    bstack1l111l1_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨ஫"): config[bstack1l111l1_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩ஬")],
    bstack1l111l1_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡴࡺࡲࡨࠫ஭"): bstack1lll1ll1l1_opy_,
    bstack1l111l1_opy_ (u"ࠨࡦࡨࡸࡪࡩࡴࡦࡦࡉࡶࡦࡳࡥࡸࡱࡵ࡯ࠬம"): os.environ.get(bstack1l111l1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡈࡕࡅࡒࡋࡗࡐࡔࡎࠫய"), bstack11lll111_opy_),
    bstack1l111l1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡡ࡫ࡥࡸ࡮ࡥࡥࡡ࡬ࡨࠬர"): bstack1lll1ll1l_opy_,
    bstack1l111l1_opy_ (u"ࠫࡴࡶࡴࡪ࡯ࡤࡰࡤ࡮ࡵࡣࡡࡸࡶࡱ࠭ற"): bstack1l1l11llll_opy_(),
    bstack1l111l1_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡵࡸ࡯ࡱࡧࡵࡸ࡮࡫ࡳࠨல"): {
      bstack1l111l1_opy_ (u"࠭࡬ࡢࡰࡪࡹࡦ࡭ࡥࡠࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫள"): str(config[bstack1l111l1_opy_ (u"ࠧࡴࡱࡸࡶࡨ࡫ࠧழ")]) if bstack1l111l1_opy_ (u"ࠨࡵࡲࡹࡷࡩࡥࠨவ") in config else bstack1l111l1_opy_ (u"ࠤࡸࡲࡰࡴ࡯ࡸࡰࠥஶ"),
      bstack1l111l1_opy_ (u"ࠪࡰࡦࡴࡧࡶࡣࡪࡩ࡛࡫ࡲࡴ࡫ࡲࡲࠬஷ"): sys.version,
      bstack1l111l1_opy_ (u"ࠫࡷ࡫ࡦࡦࡴࡵࡩࡷ࠭ஸ"): bstack11lll1l1l_opy_(os.getenv(bstack1l111l1_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡋࡘࡁࡎࡇ࡚ࡓࡗࡑࠢஹ"), bstack1l111l1_opy_ (u"ࠨࠢ஺"))),
      bstack1l111l1_opy_ (u"ࠧ࡭ࡣࡱ࡫ࡺࡧࡧࡦࠩ஻"): bstack1l111l1_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮ࠨ஼"),
      bstack1l111l1_opy_ (u"ࠩࡳࡶࡴࡪࡵࡤࡶࠪ஽"): bstack1111l11ll_opy_,
      bstack1l111l1_opy_ (u"ࠪࡴࡷࡵࡤࡶࡥࡷࡣࡲࡧࡰࠨா"): bstack1l1l111ll_opy_,
      bstack1l111l1_opy_ (u"ࠫࡹ࡫ࡳࡵࡪࡸࡦࡤࡻࡵࡪࡦࠪி"): os.environ[bstack1l111l1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪீ")],
      bstack1l111l1_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡘࡨࡶࡸ࡯࡯࡯ࠩு"): bstack1111ll1l_opy_(os.environ.get(bstack1l111l1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡆࡓࡃࡐࡉ࡜ࡕࡒࡌࠩூ"), bstack11lll111_opy_)),
      bstack1l111l1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫ௃"): config[bstack1l111l1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬ௄")] if config[bstack1l111l1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭௅")] else bstack1l111l1_opy_ (u"ࠦࡺࡴ࡫࡯ࡱࡺࡲࠧெ"),
      bstack1l111l1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧே"): str(config[bstack1l111l1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨை")]) if bstack1l111l1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ௉") in config else bstack1l111l1_opy_ (u"ࠣࡷࡱ࡯ࡳࡵࡷ࡯ࠤொ"),
      bstack1l111l1_opy_ (u"ࠩࡲࡷࠬோ"): sys.platform,
      bstack1l111l1_opy_ (u"ࠪ࡬ࡴࡹࡴ࡯ࡣࡰࡩࠬௌ"): socket.gethostname()
    }
  }
  update(data[bstack1l111l1_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡴࡷࡵࡰࡦࡴࡷ࡭ࡪࡹ்ࠧ")], bstack1lll1l111l_opy_)
  try:
    response = bstack1ll1llll1_opy_(bstack1l111l1_opy_ (u"ࠬࡖࡏࡔࡖࠪ௎"), bstack1l1ll1l1l_opy_(bstack1ll1l111ll_opy_), data, {
      bstack1l111l1_opy_ (u"࠭ࡡࡶࡶ࡫ࠫ௏"): (config[bstack1l111l1_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩௐ")], config[bstack1l111l1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫ௑")])
    })
    if response:
      logger.debug(bstack11l1l111_opy_.format(bstack1lll1ll1l1_opy_, str(response.json())))
  except Exception as e:
    logger.debug(bstack1lllllll1_opy_.format(str(e)))
def bstack11lll1l1l_opy_(framework):
  return bstack1l111l1_opy_ (u"ࠤࡾࢁ࠲ࡶࡹࡵࡪࡲࡲࡦ࡭ࡥ࡯ࡶ࠲ࡿࢂࠨ௒").format(str(framework), __version__) if framework else bstack1l111l1_opy_ (u"ࠥࡴࡾࡺࡨࡰࡰࡤ࡫ࡪࡴࡴ࠰ࡽࢀࠦ௓").format(
    __version__)
def bstack1llll1ll11_opy_():
  global CONFIG
  global bstack1llll11ll1_opy_
  if bool(CONFIG):
    return
  try:
    bstack1ll1llll1l_opy_()
    logger.debug(bstack11lll11l1_opy_.format(str(CONFIG)))
    bstack1llll11ll1_opy_ = bstack1ll111l1l1_opy_.bstack1ll1ll1ll1_opy_(CONFIG, bstack1llll11ll1_opy_)
    bstack1lll111ll1_opy_()
  except Exception as e:
    logger.error(bstack1l111l1_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡴࡧࡷࡹࡵ࠲ࠠࡦࡴࡵࡳࡷࡀࠠࠣ௔") + str(e))
    sys.exit(1)
  sys.excepthook = bstack1ll1lllll_opy_
  atexit.register(bstack1l1lll111l_opy_)
  signal.signal(signal.SIGINT, bstack1l1l1l1l_opy_)
  signal.signal(signal.SIGTERM, bstack1l1l1l1l_opy_)
def bstack1ll1lllll_opy_(exctype, value, traceback):
  global bstack11lll1l1_opy_
  try:
    for driver in bstack11lll1l1_opy_:
      bstack11l11111l_opy_(driver, bstack1l111l1_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬ௕"), bstack1l111l1_opy_ (u"ࠨࡓࡦࡵࡶ࡭ࡴࡴࠠࡧࡣ࡬ࡰࡪࡪࠠࡸ࡫ࡷ࡬࠿ࠦ࡜࡯ࠤ௖") + str(value))
  except Exception:
    pass
  bstack1l11lll11l_opy_(value, True)
  sys.__excepthook__(exctype, value, traceback)
  sys.exit(1)
def bstack1l11lll11l_opy_(message=bstack1l111l1_opy_ (u"ࠧࠨௗ"), bstack1ll1l11l11_opy_ = False):
  global CONFIG
  bstack111111ll1_opy_ = bstack1l111l1_opy_ (u"ࠨࡩ࡯ࡳࡧࡧ࡬ࡆࡺࡦࡩࡵࡺࡩࡰࡰࠪ௘") if bstack1ll1l11l11_opy_ else bstack1l111l1_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨ௙")
  try:
    if message:
      bstack1lll1l111l_opy_ = {
        bstack111111ll1_opy_ : str(message)
      }
      bstack1lllll1111_opy_(bstack1l1lll1l_opy_, CONFIG, bstack1lll1l111l_opy_)
    else:
      bstack1lllll1111_opy_(bstack1l1lll1l_opy_, CONFIG)
  except Exception as e:
    logger.debug(bstack1ll1ll1lll_opy_.format(str(e)))
def bstack11l111l1l_opy_(bstack111l1llll_opy_, size):
  bstack1ll11l11_opy_ = []
  while len(bstack111l1llll_opy_) > size:
    bstack1ll1l11l_opy_ = bstack111l1llll_opy_[:size]
    bstack1ll11l11_opy_.append(bstack1ll1l11l_opy_)
    bstack111l1llll_opy_ = bstack111l1llll_opy_[size:]
  bstack1ll11l11_opy_.append(bstack111l1llll_opy_)
  return bstack1ll11l11_opy_
def bstack111lllll_opy_(args):
  if bstack1l111l1_opy_ (u"ࠪ࠱ࡲ࠭௚") in args and bstack1l111l1_opy_ (u"ࠫࡵࡪࡢࠨ௛") in args:
    return True
  return False
def run_on_browserstack(bstack1l11ll1l1l_opy_=None, bstack11ll1lll1_opy_=None, bstack1l1ll1lll_opy_=False):
  global CONFIG
  global bstack1l1l11111_opy_
  global bstack1l1llll1l1_opy_
  global bstack11lll111_opy_
  bstack11l1l11l_opy_ = bstack1l111l1_opy_ (u"ࠬ࠭௜")
  bstack1lll1lll11_opy_(bstack1lll1lll1l_opy_, logger)
  if bstack1l11ll1l1l_opy_ and isinstance(bstack1l11ll1l1l_opy_, str):
    bstack1l11ll1l1l_opy_ = eval(bstack1l11ll1l1l_opy_)
  if bstack1l11ll1l1l_opy_:
    CONFIG = bstack1l11ll1l1l_opy_[bstack1l111l1_opy_ (u"࠭ࡃࡐࡐࡉࡍࡌ࠭௝")]
    bstack1l1l11111_opy_ = bstack1l11ll1l1l_opy_[bstack1l111l1_opy_ (u"ࠧࡉࡗࡅࡣ࡚ࡘࡌࠨ௞")]
    bstack1l1llll1l1_opy_ = bstack1l11ll1l1l_opy_[bstack1l111l1_opy_ (u"ࠨࡋࡖࡣࡆࡖࡐࡠࡃࡘࡘࡔࡓࡁࡕࡇࠪ௟")]
    bstack11111111_opy_.bstack111ll1ll_opy_(bstack1l111l1_opy_ (u"ࠩࡌࡗࡤࡇࡐࡑࡡࡄ࡙࡙ࡕࡍࡂࡖࡈࠫ௠"), bstack1l1llll1l1_opy_)
    bstack11l1l11l_opy_ = bstack1l111l1_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰࠪ௡")
  if not bstack1l1ll1lll_opy_:
    if len(sys.argv) <= 1:
      logger.critical(bstack1l1ll1l1l1_opy_)
      return
    if sys.argv[1] == bstack1l111l1_opy_ (u"ࠫ࠲࠳ࡶࡦࡴࡶ࡭ࡴࡴࠧ௢") or sys.argv[1] == bstack1l111l1_opy_ (u"ࠬ࠳ࡶࠨ௣"):
      logger.info(bstack1l111l1_opy_ (u"࠭ࡂࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠥࡖࡹࡵࡪࡲࡲ࡙ࠥࡄࡌࠢࡹࡿࢂ࠭௤").format(__version__))
      return
    if sys.argv[1] == bstack1l111l1_opy_ (u"ࠧࡴࡧࡷࡹࡵ࠭௥"):
      bstack1l11l1l11_opy_()
      return
  args = sys.argv
  bstack1llll1ll11_opy_()
  global bstack1ll1111ll1_opy_
  global bstack1111lll1l_opy_
  global bstack1ll1l11lll_opy_
  global bstack1lll1l1111_opy_
  global bstack1llll1ll1_opy_
  global bstack1l1l11l111_opy_
  global bstack11ll1lll_opy_
  global bstack11l1111l_opy_
  global bstack1lll1lll1_opy_
  global bstack1l1l1l1ll1_opy_
  global bstack1l11lllll_opy_
  bstack1111lll1l_opy_ = len(CONFIG.get(bstack1l111l1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ௦"), []))
  if not bstack11l1l11l_opy_:
    if args[1] == bstack1l111l1_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯ࠩ௧") or args[1] == bstack1l111l1_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰ࠶ࠫ௨"):
      bstack11l1l11l_opy_ = bstack1l111l1_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱࠫ௩")
      args = args[2:]
    elif args[1] == bstack1l111l1_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫ௪"):
      bstack11l1l11l_opy_ = bstack1l111l1_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬ௫")
      args = args[2:]
    elif args[1] == bstack1l111l1_opy_ (u"ࠧࡱࡣࡥࡳࡹ࠭௬"):
      bstack11l1l11l_opy_ = bstack1l111l1_opy_ (u"ࠨࡲࡤࡦࡴࡺࠧ௭")
      args = args[2:]
    elif args[1] == bstack1l111l1_opy_ (u"ࠩࡵࡳࡧࡵࡴ࠮࡫ࡱࡸࡪࡸ࡮ࡢ࡮ࠪ௮"):
      bstack11l1l11l_opy_ = bstack1l111l1_opy_ (u"ࠪࡶࡴࡨ࡯ࡵ࠯࡬ࡲࡹ࡫ࡲ࡯ࡣ࡯ࠫ௯")
      args = args[2:]
    elif args[1] == bstack1l111l1_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫ௰"):
      bstack11l1l11l_opy_ = bstack1l111l1_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬ௱")
      args = args[2:]
    elif args[1] == bstack1l111l1_opy_ (u"࠭ࡢࡦࡪࡤࡺࡪ࠭௲"):
      bstack11l1l11l_opy_ = bstack1l111l1_opy_ (u"ࠧࡣࡧ࡫ࡥࡻ࡫ࠧ௳")
      args = args[2:]
    else:
      if not bstack1l111l1_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫ௴") in CONFIG or str(CONFIG[bstack1l111l1_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠬ௵")]).lower() in [bstack1l111l1_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰࠪ௶"), bstack1l111l1_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱ࠷ࠬ௷")]:
        bstack11l1l11l_opy_ = bstack1l111l1_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲࠬ௸")
        args = args[1:]
      elif str(CONFIG[bstack1l111l1_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠩ௹")]).lower() == bstack1l111l1_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭௺"):
        bstack11l1l11l_opy_ = bstack1l111l1_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧ௻")
        args = args[1:]
      elif str(CONFIG[bstack1l111l1_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠬ௼")]).lower() == bstack1l111l1_opy_ (u"ࠪࡴࡦࡨ࡯ࡵࠩ௽"):
        bstack11l1l11l_opy_ = bstack1l111l1_opy_ (u"ࠫࡵࡧࡢࡰࡶࠪ௾")
        args = args[1:]
      elif str(CONFIG[bstack1l111l1_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨ௿")]).lower() == bstack1l111l1_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭ఀ"):
        bstack11l1l11l_opy_ = bstack1l111l1_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧఁ")
        args = args[1:]
      elif str(CONFIG[bstack1l111l1_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫం")]).lower() == bstack1l111l1_opy_ (u"ࠩࡥࡩ࡭ࡧࡶࡦࠩః"):
        bstack11l1l11l_opy_ = bstack1l111l1_opy_ (u"ࠪࡦࡪ࡮ࡡࡷࡧࠪఄ")
        args = args[1:]
      else:
        os.environ[bstack1l111l1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡊࡗࡇࡍࡆ࡙ࡒࡖࡐ࠭అ")] = bstack11l1l11l_opy_
        bstack11lll1l11_opy_(bstack1ll1ll11l1_opy_)
  os.environ[bstack1l111l1_opy_ (u"ࠬࡌࡒࡂࡏࡈ࡛ࡔࡘࡋࡠࡗࡖࡉࡉ࠭ఆ")] = bstack11l1l11l_opy_
  bstack11lll111_opy_ = bstack11l1l11l_opy_
  global bstack11111ll1l_opy_
  if bstack1l11ll1l1l_opy_:
    try:
      os.environ[bstack1l111l1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡌࡒࡂࡏࡈ࡛ࡔࡘࡋࠨఇ")] = bstack11l1l11l_opy_
      bstack1lllll1111_opy_(bstack11111l11_opy_, CONFIG)
    except Exception as e:
      logger.debug(bstack1ll1ll1lll_opy_.format(str(e)))
  global bstack1lllll111_opy_
  global bstack1l11ll1ll_opy_
  global bstack1ll1111lll_opy_
  global bstack1l111l1l_opy_
  global bstack1l1ll1ll11_opy_
  global bstack1111llll1_opy_
  global bstack11lll11ll_opy_
  global bstack1llll1llll_opy_
  global bstack1ll1111ll_opy_
  global bstack1l11l1111_opy_
  global bstack1l1l1ll1_opy_
  global bstack1111ll1ll_opy_
  global bstack111l1l11_opy_
  global bstack1l1ll11l1l_opy_
  global bstack1lll11ll_opy_
  global bstack11111lll1_opy_
  global bstack1ll111ll11_opy_
  global bstack111l111ll_opy_
  global bstack1l1ll11l11_opy_
  global bstack1l11l1l11l_opy_
  global bstack111lll11_opy_
  try:
    from selenium import webdriver
    from selenium.webdriver.remote.webdriver import WebDriver
    bstack1lllll111_opy_ = webdriver.Remote.__init__
    bstack1l11ll1ll_opy_ = WebDriver.quit
    bstack1111ll1ll_opy_ = WebDriver.close
    bstack1lll11ll_opy_ = WebDriver.get
    bstack111lll11_opy_ = WebDriver.execute
  except Exception as e:
    pass
  try:
    import Browser
    from subprocess import Popen
    bstack11111ll1l_opy_ = Popen.__init__
  except Exception as e:
    pass
  try:
    global bstack1llll11111_opy_
    from QWeb.keywords import browser
    bstack1llll11111_opy_ = browser.close_browser
  except Exception as e:
    pass
  if bstack1l1ll1lll1_opy_(CONFIG) and bstack1l1111l11_opy_():
    if bstack1l1ll11lll_opy_() < version.parse(bstack1l1l1l1l1l_opy_):
      logger.error(bstack1l11l11l1_opy_.format(bstack1l1ll11lll_opy_()))
    else:
      try:
        from selenium.webdriver.remote.remote_connection import RemoteConnection
        bstack11111lll1_opy_ = RemoteConnection._get_proxy_url
      except Exception as e:
        logger.error(bstack1l1ll11111_opy_.format(str(e)))
  if not CONFIG.get(bstack1l111l1_opy_ (u"ࠧࡥ࡫ࡶࡥࡧࡲࡥࡂࡷࡷࡳࡈࡧࡰࡵࡷࡵࡩࡑࡵࡧࡴࠩఈ"), False) and not bstack1l11ll1l1l_opy_:
    logger.info(bstack1l1l1lll11_opy_)
  if bstack11l1l11l_opy_ != bstack1l111l1_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮ࠨఉ") or (bstack11l1l11l_opy_ == bstack1l111l1_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯ࠩఊ") and not bstack1l11ll1l1l_opy_):
    bstack11l11ll1l_opy_()
  if (bstack11l1l11l_opy_ in [bstack1l111l1_opy_ (u"ࠪࡴࡦࡨ࡯ࡵࠩఋ"), bstack1l111l1_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪఌ"), bstack1l111l1_opy_ (u"ࠬࡸ࡯ࡣࡱࡷ࠱࡮ࡴࡴࡦࡴࡱࡥࡱ࠭఍")]):
    try:
      from robot import run_cli
      from robot.output import Output
      from robot.running.status import TestStatus
      from pabot.pabot import QueueItem
      from pabot import pabot
      try:
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCreator
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCache
        WebDriverCreator._get_ff_profile = bstack1111ll111_opy_
        bstack1111llll1_opy_ = WebDriverCache.close
      except Exception as e:
        logger.warn(bstack1lll111111_opy_ + str(e))
      try:
        from AppiumLibrary.utils.applicationcache import ApplicationCache
        bstack1l1ll1ll11_opy_ = ApplicationCache.close
      except Exception as e:
        logger.debug(bstack11l1llll_opy_ + str(e))
    except Exception as e:
      bstack111l11l1l_opy_(e, bstack1lll111111_opy_)
    if bstack11l1l11l_opy_ != bstack1l111l1_opy_ (u"࠭ࡲࡰࡤࡲࡸ࠲࡯࡮ࡵࡧࡵࡲࡦࡲࠧఎ"):
      bstack111ll111_opy_()
    bstack1ll1111lll_opy_ = Output.start_test
    bstack1l111l1l_opy_ = Output.end_test
    bstack11lll11ll_opy_ = TestStatus.__init__
    bstack1ll1111ll_opy_ = pabot._run
    bstack1l11l1111_opy_ = QueueItem.__init__
    bstack1l1l1ll1_opy_ = pabot._create_command_for_execution
    bstack1l1ll11l11_opy_ = pabot._report_results
  if bstack11l1l11l_opy_ == bstack1l111l1_opy_ (u"ࠧࡣࡧ࡫ࡥࡻ࡫ࠧఏ"):
    try:
      from behave.runner import Runner
      from behave.model import Step
    except Exception as e:
      bstack111l11l1l_opy_(e, bstack1ll11l1l11_opy_)
    bstack111l1l11_opy_ = Runner.run_hook
    bstack1l1ll11l1l_opy_ = Step.run
  if bstack11l1l11l_opy_ == bstack1l111l1_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨఐ"):
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
      logger.debug(bstack1l111l1_opy_ (u"ࠩࡓࡰࡪࡧࡳࡦࠢ࡬ࡲࡸࡺࡡ࡭࡮ࠣࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠠࡵࡱࠣࡶࡺࡴࠠࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠤࡹ࡫ࡳࡵࡵࠪ఑"))
  try:
    framework_name = bstack1l111l1_opy_ (u"ࠪࡖࡴࡨ࡯ࡵࠩఒ") if bstack11l1l11l_opy_ in [bstack1l111l1_opy_ (u"ࠫࡵࡧࡢࡰࡶࠪఓ"), bstack1l111l1_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫఔ"), bstack1l111l1_opy_ (u"࠭ࡲࡰࡤࡲࡸ࠲࡯࡮ࡵࡧࡵࡲࡦࡲࠧక")] else bstack1l1ll11l1_opy_(bstack11l1l11l_opy_)
    bstack1l1111l1l_opy_.launch(CONFIG, {
      bstack1l111l1_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡲࡦࡳࡥࠨఖ"): bstack1l111l1_opy_ (u"ࠨࡽ࠳ࢁ࠲ࡩࡵࡤࡷࡰࡦࡪࡸࠧగ").format(framework_name) if bstack11l1l11l_opy_ == bstack1l111l1_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩఘ") and bstack1lll11l1l_opy_() else framework_name,
      bstack1l111l1_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡶࡦࡴࡶ࡭ࡴࡴࠧఙ"): bstack1111ll1l_opy_(framework_name),
      bstack1l111l1_opy_ (u"ࠫࡸࡪ࡫ࡠࡸࡨࡶࡸ࡯࡯࡯ࠩచ"): __version__,
      bstack1l111l1_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡷࡶࡩࡩ࠭ఛ"): bstack11l1l11l_opy_
    })
  except Exception as e:
    logger.debug(bstack1111lll11_opy_.format(bstack1l111l1_opy_ (u"࠭ࡏࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࠭జ"), str(e)))
  if bstack11l1l11l_opy_ in bstack11l11ll11_opy_:
    try:
      framework_name = bstack1l111l1_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭ఝ") if bstack11l1l11l_opy_ in [bstack1l111l1_opy_ (u"ࠨࡲࡤࡦࡴࡺࠧఞ"), bstack1l111l1_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨట")] else bstack11l1l11l_opy_
      if bstack1lll1l1lll_opy_ and bstack1l111l1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪఠ") in CONFIG and CONFIG[bstack1l111l1_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫడ")] == True:
        if bstack1l111l1_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡔࡶࡴࡪࡱࡱࡷࠬఢ") in CONFIG:
          os.environ[bstack1l111l1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡢࡅࡈࡉࡅࡔࡕࡌࡆࡎࡒࡉࡕ࡛ࡢࡇࡔࡔࡆࡊࡉࡘࡖࡆ࡚ࡉࡐࡐࡢ࡝ࡒࡒࠧణ")] = os.getenv(bstack1l111l1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡣࡆࡉࡃࡆࡕࡖࡍࡇࡏࡌࡊࡖ࡜ࡣࡈࡕࡎࡇࡋࡊ࡙ࡗࡇࡔࡊࡑࡑࡣ࡞ࡓࡌࠨత"), json.dumps(CONFIG[bstack1l111l1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳࠨథ")]))
          CONFIG[bstack1l111l1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩద")].pop(bstack1l111l1_opy_ (u"ࠪ࡭ࡳࡩ࡬ࡶࡦࡨࡘࡦ࡭ࡳࡊࡰࡗࡩࡸࡺࡩ࡯ࡩࡖࡧࡴࡶࡥࠨధ"), None)
          CONFIG[bstack1l111l1_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫన")].pop(bstack1l111l1_opy_ (u"ࠬ࡫ࡸࡤ࡮ࡸࡨࡪ࡚ࡡࡨࡵࡌࡲ࡙࡫ࡳࡵ࡫ࡱ࡫ࡘࡩ࡯ࡱࡧࠪ఩"), None)
        bstack1ll11l11ll_opy_, bstack1llllll111_opy_ = bstack1l1lll11l1_opy_.bstack1ll11l11l1_opy_(CONFIG, bstack11l1l11l_opy_, bstack1111ll1l_opy_(framework_name), str(bstack1l1ll11lll_opy_()))
        if not bstack1ll11l11ll_opy_ is None:
          os.environ[bstack1l111l1_opy_ (u"࠭ࡂࡔࡡࡄ࠵࠶࡟࡟ࡋ࡙ࡗࠫప")] = bstack1ll11l11ll_opy_
          os.environ[bstack1l111l1_opy_ (u"ࠧࡃࡕࡢࡅ࠶࠷࡙ࡠࡖࡈࡗ࡙ࡥࡒࡖࡐࡢࡍࡉ࠭ఫ")] = str(bstack1llllll111_opy_)
    except Exception as e:
      logger.debug(bstack1111lll11_opy_.format(bstack1l111l1_opy_ (u"ࠨࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨబ"), str(e)))
  if bstack11l1l11l_opy_ == bstack1l111l1_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯ࠩభ"):
    bstack1ll1l11lll_opy_ = True
    if bstack1l11ll1l1l_opy_ and bstack1l1ll1lll_opy_:
      bstack1l1l11l111_opy_ = CONFIG.get(bstack1l111l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧమ"), {}).get(bstack1l111l1_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭య"))
      bstack1ll111llll_opy_(bstack11l111lll_opy_)
    elif bstack1l11ll1l1l_opy_:
      bstack1l1l11l111_opy_ = CONFIG.get(bstack1l111l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩర"), {}).get(bstack1l111l1_opy_ (u"࠭࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨఱ"))
      global bstack11lll1l1_opy_
      try:
        if bstack111lllll_opy_(bstack1l11ll1l1l_opy_[bstack1l111l1_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪల")]) and multiprocessing.current_process().name == bstack1l111l1_opy_ (u"ࠨ࠲ࠪళ"):
          bstack1l11ll1l1l_opy_[bstack1l111l1_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬఴ")].remove(bstack1l111l1_opy_ (u"ࠪ࠱ࡲ࠭వ"))
          bstack1l11ll1l1l_opy_[bstack1l111l1_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧశ")].remove(bstack1l111l1_opy_ (u"ࠬࡶࡤࡣࠩష"))
          bstack1l11ll1l1l_opy_[bstack1l111l1_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩస")] = bstack1l11ll1l1l_opy_[bstack1l111l1_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪహ")][0]
          with open(bstack1l11ll1l1l_opy_[bstack1l111l1_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫ఺")], bstack1l111l1_opy_ (u"ࠩࡵࠫ఻")) as f:
            bstack1l1ll1l111_opy_ = f.read()
          bstack1llllll1ll_opy_ = bstack1l111l1_opy_ (u"ࠥࠦࠧ࡬ࡲࡰ࡯ࠣࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡶࡨࡰࠦࡩ࡮ࡲࡲࡶࡹࠦࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡯࡮ࡪࡶ࡬ࡥࡱ࡯ࡺࡦ࠽ࠣࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡ࡬ࡲ࡮ࡺࡩࡢ࡮࡬ࡾࡪ࠮ࡻࡾࠫ࠾ࠤ࡫ࡸ࡯࡮ࠢࡳࡨࡧࠦࡩ࡮ࡲࡲࡶࡹࠦࡐࡥࡤ࠾ࠤࡴ࡭࡟ࡥࡤࠣࡁࠥࡖࡤࡣ࠰ࡧࡳࡤࡨࡲࡦࡣ࡮࠿ࠏࡪࡥࡧࠢࡰࡳࡩࡥࡢࡳࡧࡤ࡯࠭ࡹࡥ࡭ࡨ࠯ࠤࡦࡸࡧ࠭ࠢࡷࡩࡲࡶ࡯ࡳࡣࡵࡽࠥࡃࠠ࠱ࠫ࠽ࠎࠥࠦࡴࡳࡻ࠽ࠎࠥࠦࠠࠡࡣࡵ࡫ࠥࡃࠠࡴࡶࡵࠬ࡮ࡴࡴࠩࡣࡵ࡫࠮࠱࠱࠱ࠫࠍࠤࠥ࡫ࡸࡤࡧࡳࡸࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡣࡶࠤࡪࡀࠊࠡࠢࠣࠤࡵࡧࡳࡴࠌࠣࠤࡴ࡭࡟ࡥࡤࠫࡷࡪࡲࡦ࠭ࡣࡵ࡫࠱ࡺࡥ࡮ࡲࡲࡶࡦࡸࡹࠪࠌࡓࡨࡧ࠴ࡤࡰࡡࡥࠤࡂࠦ࡭ࡰࡦࡢࡦࡷ࡫ࡡ࡬ࠌࡓࡨࡧ࠴ࡤࡰࡡࡥࡶࡪࡧ࡫ࠡ࠿ࠣࡱࡴࡪ࡟ࡣࡴࡨࡥࡰࠐࡐࡥࡤࠫ࠭࠳ࡹࡥࡵࡡࡷࡶࡦࡩࡥࠩࠫ࡟ࡲࠧࠨ఼ࠢ").format(str(bstack1l11ll1l1l_opy_))
          bstack1lll111ll_opy_ = bstack1llllll1ll_opy_ + bstack1l1ll1l111_opy_
          bstack11llll1l_opy_ = bstack1l11ll1l1l_opy_[bstack1l111l1_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧఽ")] + bstack1l111l1_opy_ (u"ࠬࡥࡢࡴࡶࡤࡧࡰࡥࡴࡦ࡯ࡳ࠲ࡵࡿࠧా")
          with open(bstack11llll1l_opy_, bstack1l111l1_opy_ (u"࠭ࡷࠨి")):
            pass
          with open(bstack11llll1l_opy_, bstack1l111l1_opy_ (u"ࠢࡸ࠭ࠥీ")) as f:
            f.write(bstack1lll111ll_opy_)
          import subprocess
          bstack1l11l11ll_opy_ = subprocess.run([bstack1l111l1_opy_ (u"ࠣࡲࡼࡸ࡭ࡵ࡮ࠣు"), bstack11llll1l_opy_])
          if os.path.exists(bstack11llll1l_opy_):
            os.unlink(bstack11llll1l_opy_)
          os._exit(bstack1l11l11ll_opy_.returncode)
        else:
          if bstack111lllll_opy_(bstack1l11ll1l1l_opy_[bstack1l111l1_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬూ")]):
            bstack1l11ll1l1l_opy_[bstack1l111l1_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭ృ")].remove(bstack1l111l1_opy_ (u"ࠫ࠲ࡳࠧౄ"))
            bstack1l11ll1l1l_opy_[bstack1l111l1_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨ౅")].remove(bstack1l111l1_opy_ (u"࠭ࡰࡥࡤࠪె"))
            bstack1l11ll1l1l_opy_[bstack1l111l1_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪే")] = bstack1l11ll1l1l_opy_[bstack1l111l1_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫై")][0]
          bstack1ll111llll_opy_(bstack11l111lll_opy_)
          sys.path.append(os.path.dirname(os.path.abspath(bstack1l11ll1l1l_opy_[bstack1l111l1_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬ౉")])))
          sys.argv = sys.argv[2:]
          mod_globals = globals()
          mod_globals[bstack1l111l1_opy_ (u"ࠪࡣࡤࡴࡡ࡮ࡧࡢࡣࠬొ")] = bstack1l111l1_opy_ (u"ࠫࡤࡥ࡭ࡢ࡫ࡱࡣࡤ࠭ో")
          mod_globals[bstack1l111l1_opy_ (u"ࠬࡥ࡟ࡧ࡫࡯ࡩࡤࡥࠧౌ")] = os.path.abspath(bstack1l11ll1l1l_opy_[bstack1l111l1_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦ్ࠩ")])
          exec(open(bstack1l11ll1l1l_opy_[bstack1l111l1_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪ౎")]).read(), mod_globals)
      except BaseException as e:
        try:
          traceback.print_exc()
          logger.error(bstack1l111l1_opy_ (u"ࠨࡅࡤࡹ࡬࡮ࡴࠡࡇࡻࡧࡪࡶࡴࡪࡱࡱ࠾ࠥࢁࡽࠨ౏").format(str(e)))
          for driver in bstack11lll1l1_opy_:
            bstack11ll1lll1_opy_.append({
              bstack1l111l1_opy_ (u"ࠩࡱࡥࡲ࡫ࠧ౐"): bstack1l11ll1l1l_opy_[bstack1l111l1_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭౑")],
              bstack1l111l1_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪ౒"): str(e),
              bstack1l111l1_opy_ (u"ࠬ࡯࡮ࡥࡧࡻࠫ౓"): multiprocessing.current_process().name
            })
            bstack11l11111l_opy_(driver, bstack1l111l1_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭౔"), bstack1l111l1_opy_ (u"ࠢࡔࡧࡶࡷ࡮ࡵ࡮ࠡࡨࡤ࡭ࡱ࡫ࡤࠡࡹ࡬ࡸ࡭ࡀࠠ࡝ࡰౕࠥ") + str(e))
        except Exception:
          pass
      finally:
        try:
          for driver in bstack11lll1l1_opy_:
            driver.quit()
        except Exception as e:
          pass
    else:
      percy.init(bstack1l1llll1l1_opy_, CONFIG, logger)
      bstack1l1l1111_opy_()
      bstack1lll1l1l_opy_()
      bstack11llll1ll_opy_ = {
        bstack1l111l1_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨౖࠫ"): args[0],
        bstack1l111l1_opy_ (u"ࠩࡆࡓࡓࡌࡉࡈࠩ౗"): CONFIG,
        bstack1l111l1_opy_ (u"ࠪࡌ࡚ࡈ࡟ࡖࡔࡏࠫౘ"): bstack1l1l11111_opy_,
        bstack1l111l1_opy_ (u"ࠫࡎ࡙࡟ࡂࡒࡓࡣࡆ࡛ࡔࡐࡏࡄࡘࡊ࠭ౙ"): bstack1l1llll1l1_opy_
      }
      percy.bstack1lll1llll_opy_()
      if bstack1l111l1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨౚ") in CONFIG:
        bstack1ll111111l_opy_ = []
        manager = multiprocessing.Manager()
        bstack1l1l11ll1l_opy_ = manager.list()
        if bstack111lllll_opy_(args):
          for index, platform in enumerate(CONFIG[bstack1l111l1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ౛")]):
            if index == 0:
              bstack11llll1ll_opy_[bstack1l111l1_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪ౜")] = args
            bstack1ll111111l_opy_.append(multiprocessing.Process(name=str(index),
                                                       target=run_on_browserstack,
                                                       args=(bstack11llll1ll_opy_, bstack1l1l11ll1l_opy_)))
        else:
          for index, platform in enumerate(CONFIG[bstack1l111l1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫౝ")]):
            bstack1ll111111l_opy_.append(multiprocessing.Process(name=str(index),
                                                       target=run_on_browserstack,
                                                       args=(bstack11llll1ll_opy_, bstack1l1l11ll1l_opy_)))
        for t in bstack1ll111111l_opy_:
          t.start()
        for t in bstack1ll111111l_opy_:
          t.join()
        bstack11l1111l_opy_ = list(bstack1l1l11ll1l_opy_)
      else:
        if bstack111lllll_opy_(args):
          bstack11llll1ll_opy_[bstack1l111l1_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬ౞")] = args
          test = multiprocessing.Process(name=str(0),
                                         target=run_on_browserstack, args=(bstack11llll1ll_opy_,))
          test.start()
          test.join()
        else:
          bstack1ll111llll_opy_(bstack11l111lll_opy_)
          sys.path.append(os.path.dirname(os.path.abspath(args[0])))
          mod_globals = globals()
          mod_globals[bstack1l111l1_opy_ (u"ࠪࡣࡤࡴࡡ࡮ࡧࡢࡣࠬ౟")] = bstack1l111l1_opy_ (u"ࠫࡤࡥ࡭ࡢ࡫ࡱࡣࡤ࠭ౠ")
          mod_globals[bstack1l111l1_opy_ (u"ࠬࡥ࡟ࡧ࡫࡯ࡩࡤࡥࠧౡ")] = os.path.abspath(args[0])
          sys.argv = sys.argv[2:]
          exec(open(args[0]).read(), mod_globals)
  elif bstack11l1l11l_opy_ == bstack1l111l1_opy_ (u"࠭ࡰࡢࡤࡲࡸࠬౢ") or bstack11l1l11l_opy_ == bstack1l111l1_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭ౣ"):
    percy.init(bstack1l1llll1l1_opy_, CONFIG, logger)
    percy.bstack1lll1llll_opy_()
    try:
      from pabot import pabot
    except Exception as e:
      bstack111l11l1l_opy_(e, bstack1lll111111_opy_)
    bstack1l1l1111_opy_()
    bstack1ll111llll_opy_(bstack1ll1l11l1l_opy_)
    if bstack1lll1l1lll_opy_ and bstack1l111l1_opy_ (u"ࠨ࠯࠰ࡴࡷࡵࡣࡦࡵࡶࡩࡸ࠭౤") in args:
      i = args.index(bstack1l111l1_opy_ (u"ࠩ࠰࠱ࡵࡸ࡯ࡤࡧࡶࡷࡪࡹࠧ౥"))
      args.pop(i)
      args.pop(i)
    if bstack1lll1l1lll_opy_:
      args.insert(0, str(bstack1ll1111ll1_opy_))
      args.insert(0, str(bstack1l111l1_opy_ (u"ࠪ࠱࠲ࡶࡲࡰࡥࡨࡷࡸ࡫ࡳࠨ౦")))
    if bstack1l1111l1l_opy_.on():
      try:
        from robot.run import USAGE
        from robot.utils import ArgumentParser
        from pabot.arguments import _parse_pabot_args
        bstack1lll11ll1l_opy_, pabot_args = _parse_pabot_args(args)
        opts, bstack1ll11l1l1_opy_ = ArgumentParser(
            USAGE,
            auto_pythonpath=False,
            auto_argumentfile=True,
            env_options=bstack1l111l1_opy_ (u"ࠦࡗࡕࡂࡐࡖࡢࡓࡕ࡚ࡉࡐࡐࡖࠦ౧"),
        ).parse_args(bstack1lll11ll1l_opy_)
        args.insert(args.index(bstack1ll11l1l1_opy_[0]), str(bstack1l111l1_opy_ (u"ࠬ࠳࠭࡭࡫ࡶࡸࡪࡴࡥࡳࠩ౨")))
        args.insert(args.index(bstack1ll11l1l1_opy_[0]), str(os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack1l111l1_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡥࡲࡰࡤࡲࡸࡤࡲࡩࡴࡶࡨࡲࡪࡸ࠮ࡱࡻࠪ౩"))))
        if bstack1l1l1ll111_opy_(os.environ.get(bstack1l111l1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡒࡆࡔࡘࡒࠬ౪"))) and str(os.environ.get(bstack1l111l1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡓࡇࡕ࡙ࡓࡥࡔࡆࡕࡗࡗࠬ౫"), bstack1l111l1_opy_ (u"ࠩࡱࡹࡱࡲࠧ౬"))) != bstack1l111l1_opy_ (u"ࠪࡲࡺࡲ࡬ࠨ౭"):
          for bstack1ll1ll11l_opy_ in bstack1ll11l1l1_opy_:
            args.remove(bstack1ll1ll11l_opy_)
          bstack1l1l1ll1l1_opy_ = os.environ.get(bstack1l111l1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡖࡊࡘࡕࡏࡡࡗࡉࡘ࡚ࡓࠨ౮")).split(bstack1l111l1_opy_ (u"ࠬ࠲ࠧ౯"))
          for bstack1ll111lll1_opy_ in bstack1l1l1ll1l1_opy_:
            args.append(bstack1ll111lll1_opy_)
      except Exception as e:
        logger.error(bstack1l111l1_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡽࡨࡪ࡮ࡨࠤࡦࡺࡴࡢࡥ࡫࡭ࡳ࡭ࠠ࡭࡫ࡶࡸࡪࡴࡥࡳࠢࡩࡳࡷࠦࡏࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࠴ࠠࡆࡴࡵࡳࡷࠦ࠭ࠡࠤ౰").format(e))
    pabot.main(args)
  elif bstack11l1l11l_opy_ == bstack1l111l1_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠳ࡩ࡯ࡶࡨࡶࡳࡧ࡬ࠨ౱"):
    try:
      from robot import run_cli
    except Exception as e:
      bstack111l11l1l_opy_(e, bstack1lll111111_opy_)
    for a in args:
      if bstack1l111l1_opy_ (u"ࠨࡄࡖࡘࡆࡉࡋࡑࡎࡄࡘࡋࡕࡒࡎࡋࡑࡈࡊ࡞ࠧ౲") in a:
        bstack1llll1ll1_opy_ = int(a.split(bstack1l111l1_opy_ (u"ࠩ࠽ࠫ౳"))[1])
      if bstack1l111l1_opy_ (u"ࠪࡆࡘ࡚ࡁࡄࡍࡇࡉࡋࡒࡏࡄࡃࡏࡍࡉࡋࡎࡕࡋࡉࡍࡊࡘࠧ౴") in a:
        bstack1l1l11l111_opy_ = str(a.split(bstack1l111l1_opy_ (u"ࠫ࠿࠭౵"))[1])
      if bstack1l111l1_opy_ (u"ࠬࡈࡓࡕࡃࡆࡏࡈࡒࡉࡂࡔࡊࡗࠬ౶") in a:
        bstack11ll1lll_opy_ = str(a.split(bstack1l111l1_opy_ (u"࠭࠺ࠨ౷"))[1])
    bstack1l1l111l11_opy_ = None
    if bstack1l111l1_opy_ (u"ࠧ࠮࠯ࡥࡷࡹࡧࡣ࡬ࡡ࡬ࡸࡪࡳ࡟ࡪࡰࡧࡩࡽ࠭౸") in args:
      i = args.index(bstack1l111l1_opy_ (u"ࠨ࠯࠰ࡦࡸࡺࡡࡤ࡭ࡢ࡭ࡹ࡫࡭ࡠ࡫ࡱࡨࡪࡾࠧ౹"))
      args.pop(i)
      bstack1l1l111l11_opy_ = args.pop(i)
    if bstack1l1l111l11_opy_ is not None:
      global bstack11l11l1l_opy_
      bstack11l11l1l_opy_ = bstack1l1l111l11_opy_
    bstack1ll111llll_opy_(bstack1ll1l11l1l_opy_)
    run_cli(args)
    if bstack1l111l1_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡡࡨࡶࡷࡵࡲࡠ࡮࡬ࡷࡹ࠭౺") in multiprocessing.current_process().__dict__.keys():
      for bstack11ll1111_opy_ in multiprocessing.current_process().bstack_error_list:
        bstack11ll1lll1_opy_.append(bstack11ll1111_opy_)
  elif bstack11l1l11l_opy_ == bstack1l111l1_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪ౻"):
    percy.init(bstack1l1llll1l1_opy_, CONFIG, logger)
    percy.bstack1lll1llll_opy_()
    bstack1111ll11_opy_ = bstack11llll11l_opy_(args, logger, CONFIG, bstack1lll1l1lll_opy_)
    bstack1111ll11_opy_.bstack11llll1l1_opy_()
    bstack1l1l1111_opy_()
    bstack1lll1l1111_opy_ = True
    bstack1l1l1l1ll1_opy_ = bstack1111ll11_opy_.bstack11111l1l_opy_()
    bstack1111ll11_opy_.bstack11llll1ll_opy_(bstack111lll11l_opy_)
    bstack1l1lll1ll_opy_ = bstack1111ll11_opy_.bstack1lllll11_opy_(bstack1lll11l1_opy_, {
      bstack1l111l1_opy_ (u"ࠫࡍ࡛ࡂࡠࡗࡕࡐࠬ౼"): bstack1l1l11111_opy_,
      bstack1l111l1_opy_ (u"ࠬࡏࡓࡠࡃࡓࡔࡤࡇࡕࡕࡑࡐࡅ࡙ࡋࠧ౽"): bstack1l1llll1l1_opy_,
      bstack1l111l1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡇࡕࡕࡑࡐࡅ࡙ࡏࡏࡏࠩ౾"): bstack1lll1l1lll_opy_
    })
    try:
      bstack1ll1ll111l_opy_, bstack11l1111l1_opy_ = map(list, zip(*bstack1l1lll1ll_opy_))
      bstack1lll1lll1_opy_ = bstack1ll1ll111l_opy_[0]
      for status_code in bstack11l1111l1_opy_:
        if status_code != 0:
          bstack1l11lllll_opy_ = status_code
          break
    except Exception as e:
      logger.debug(bstack1l111l1_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡷࡦࡼࡥࠡࡧࡵࡶࡴࡸࡳࠡࡣࡱࡨࠥࡹࡴࡢࡶࡸࡷࠥࡩ࡯ࡥࡧ࠱ࠤࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠ࠻ࠢࡾࢁࠧ౿").format(str(e)))
  elif bstack11l1l11l_opy_ == bstack1l111l1_opy_ (u"ࠨࡤࡨ࡬ࡦࡼࡥࠨಀ"):
    try:
      from behave.__main__ import main as bstack11l1l1ll1_opy_
      from behave.configuration import Configuration
    except Exception as e:
      bstack111l11l1l_opy_(e, bstack1ll11l1l11_opy_)
    bstack1l1l1111_opy_()
    bstack1lll1l1111_opy_ = True
    bstack1l1l11l11_opy_ = 1
    if bstack1l111l1_opy_ (u"ࠩࡳࡥࡷࡧ࡬࡭ࡧ࡯ࡷࡕ࡫ࡲࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩಁ") in CONFIG:
      bstack1l1l11l11_opy_ = CONFIG[bstack1l111l1_opy_ (u"ࠪࡴࡦࡸࡡ࡭࡮ࡨࡰࡸࡖࡥࡳࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪಂ")]
    bstack1lll111l1l_opy_ = int(bstack1l1l11l11_opy_) * int(len(CONFIG[bstack1l111l1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧಃ")]))
    config = Configuration(args)
    bstack1ll1lll1_opy_ = config.paths
    if len(bstack1ll1lll1_opy_) == 0:
      import glob
      pattern = bstack1l111l1_opy_ (u"ࠬ࠰ࠪ࠰ࠬ࠱ࡪࡪࡧࡴࡶࡴࡨࠫ಄")
      bstack1l1lllllll_opy_ = glob.glob(pattern, recursive=True)
      args.extend(bstack1l1lllllll_opy_)
      config = Configuration(args)
      bstack1ll1lll1_opy_ = config.paths
    bstack1l1111111_opy_ = [os.path.normpath(item) for item in bstack1ll1lll1_opy_]
    bstack1ll1l111l1_opy_ = [os.path.normpath(item) for item in args]
    bstack11ll1llll_opy_ = [item for item in bstack1ll1l111l1_opy_ if item not in bstack1l1111111_opy_]
    import platform as pf
    if pf.system().lower() == bstack1l111l1_opy_ (u"࠭ࡷࡪࡰࡧࡳࡼࡹࠧಅ"):
      from pathlib import PureWindowsPath, PurePosixPath
      bstack1l1111111_opy_ = [str(PurePosixPath(PureWindowsPath(bstack11l1l1l11_opy_)))
                    for bstack11l1l1l11_opy_ in bstack1l1111111_opy_]
    bstack111l1lll1_opy_ = []
    for spec in bstack1l1111111_opy_:
      bstack11ll11l1l_opy_ = []
      bstack11ll11l1l_opy_ += bstack11ll1llll_opy_
      bstack11ll11l1l_opy_.append(spec)
      bstack111l1lll1_opy_.append(bstack11ll11l1l_opy_)
    execution_items = []
    for bstack11ll11l1l_opy_ in bstack111l1lll1_opy_:
      for index, _ in enumerate(CONFIG[bstack1l111l1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪಆ")]):
        item = {}
        item[bstack1l111l1_opy_ (u"ࠨࡣࡵ࡫ࠬಇ")] = bstack1l111l1_opy_ (u"ࠩࠣࠫಈ").join(bstack11ll11l1l_opy_)
        item[bstack1l111l1_opy_ (u"ࠪ࡭ࡳࡪࡥࡹࠩಉ")] = index
        execution_items.append(item)
    bstack1ll1lll111_opy_ = bstack11l111l1l_opy_(execution_items, bstack1lll111l1l_opy_)
    for execution_item in bstack1ll1lll111_opy_:
      bstack1ll111111l_opy_ = []
      for item in execution_item:
        bstack1ll111111l_opy_.append(bstack1l1l11ll11_opy_(name=str(item[bstack1l111l1_opy_ (u"ࠫ࡮ࡴࡤࡦࡺࠪಊ")]),
                                             target=bstack111ll1l11_opy_,
                                             args=(item[bstack1l111l1_opy_ (u"ࠬࡧࡲࡨࠩಋ")],)))
      for t in bstack1ll111111l_opy_:
        t.start()
      for t in bstack1ll111111l_opy_:
        t.join()
  else:
    bstack11lll1l11_opy_(bstack1ll1ll11l1_opy_)
  if not bstack1l11ll1l1l_opy_:
    bstack111111ll_opy_()
  bstack1ll111l1l1_opy_.bstack11l11l11_opy_()
def browserstack_initialize(bstack1l1l1lll_opy_=None):
  run_on_browserstack(bstack1l1l1lll_opy_, None, True)
def bstack111111ll_opy_():
  global CONFIG
  global bstack11lll111_opy_
  global bstack1l11lllll_opy_
  bstack1l1111l1l_opy_.stop()
  bstack1l1111l1l_opy_.bstack11111l1ll_opy_()
  if bstack1l1lll11l1_opy_.bstack1111l1ll_opy_(CONFIG):
    bstack1l1lll11l1_opy_.bstack1l1l1l111l_opy_()
  [bstack1lll1l1l1l_opy_, bstack111ll11l_opy_] = bstack1ll11l1l_opy_()
  if bstack1lll1l1l1l_opy_ is not None and bstack1ll111l1_opy_() != -1:
    sessions = bstack11l11l11l_opy_(bstack1lll1l1l1l_opy_)
    bstack1llll111ll_opy_(sessions, bstack111ll11l_opy_)
  if bstack11lll111_opy_ == bstack1l111l1_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭ಌ") and bstack1l11lllll_opy_ != 0:
    sys.exit(bstack1l11lllll_opy_)
def bstack1l1ll11l1_opy_(bstack1111l1l1l_opy_):
  if bstack1111l1l1l_opy_:
    return bstack1111l1l1l_opy_.capitalize()
  else:
    return bstack1l111l1_opy_ (u"ࠧࠨ಍")
def bstack1llll111l1_opy_(bstack1ll11l1ll_opy_):
  if bstack1l111l1_opy_ (u"ࠨࡰࡤࡱࡪ࠭ಎ") in bstack1ll11l1ll_opy_ and bstack1ll11l1ll_opy_[bstack1l111l1_opy_ (u"ࠩࡱࡥࡲ࡫ࠧಏ")] != bstack1l111l1_opy_ (u"ࠪࠫಐ"):
    return bstack1ll11l1ll_opy_[bstack1l111l1_opy_ (u"ࠫࡳࡧ࡭ࡦࠩ಑")]
  else:
    bstack1l111l11_opy_ = bstack1l111l1_opy_ (u"ࠧࠨಒ")
    if bstack1l111l1_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪ࠭ಓ") in bstack1ll11l1ll_opy_ and bstack1ll11l1ll_opy_[bstack1l111l1_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࠧಔ")] != None:
      bstack1l111l11_opy_ += bstack1ll11l1ll_opy_[bstack1l111l1_opy_ (u"ࠨࡦࡨࡺ࡮ࡩࡥࠨಕ")] + bstack1l111l1_opy_ (u"ࠤ࠯ࠤࠧಖ")
      if bstack1ll11l1ll_opy_[bstack1l111l1_opy_ (u"ࠪࡳࡸ࠭ಗ")] == bstack1l111l1_opy_ (u"ࠦ࡮ࡵࡳࠣಘ"):
        bstack1l111l11_opy_ += bstack1l111l1_opy_ (u"ࠧ࡯ࡏࡔࠢࠥಙ")
      bstack1l111l11_opy_ += (bstack1ll11l1ll_opy_[bstack1l111l1_opy_ (u"࠭࡯ࡴࡡࡹࡩࡷࡹࡩࡰࡰࠪಚ")] or bstack1l111l1_opy_ (u"ࠧࠨಛ"))
      return bstack1l111l11_opy_
    else:
      bstack1l111l11_opy_ += bstack1l1ll11l1_opy_(bstack1ll11l1ll_opy_[bstack1l111l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࠩಜ")]) + bstack1l111l1_opy_ (u"ࠤࠣࠦಝ") + (
              bstack1ll11l1ll_opy_[bstack1l111l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬಞ")] or bstack1l111l1_opy_ (u"ࠫࠬಟ")) + bstack1l111l1_opy_ (u"ࠧ࠲ࠠࠣಠ")
      if bstack1ll11l1ll_opy_[bstack1l111l1_opy_ (u"࠭࡯ࡴࠩಡ")] == bstack1l111l1_opy_ (u"ࠢࡘ࡫ࡱࡨࡴࡽࡳࠣಢ"):
        bstack1l111l11_opy_ += bstack1l111l1_opy_ (u"࡙ࠣ࡬ࡲࠥࠨಣ")
      bstack1l111l11_opy_ += bstack1ll11l1ll_opy_[bstack1l111l1_opy_ (u"ࠩࡲࡷࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭ತ")] or bstack1l111l1_opy_ (u"ࠪࠫಥ")
      return bstack1l111l11_opy_
def bstack11l1ll11l_opy_(bstack11ll1ll1_opy_):
  if bstack11ll1ll1_opy_ == bstack1l111l1_opy_ (u"ࠦࡩࡵ࡮ࡦࠤದ"):
    return bstack1l111l1_opy_ (u"ࠬࡂࡴࡥࠢࡦࡰࡦࡹࡳ࠾ࠤࡥࡷࡹࡧࡣ࡬࠯ࡧࡥࡹࡧࠢࠡࡵࡷࡽࡱ࡫࠽ࠣࡥࡲࡰࡴࡸ࠺ࡨࡴࡨࡩࡳࡁࠢ࠿࠾ࡩࡳࡳࡺࠠࡤࡱ࡯ࡳࡷࡃࠢࡨࡴࡨࡩࡳࠨ࠾ࡄࡱࡰࡴࡱ࡫ࡴࡦࡦ࠿࠳࡫ࡵ࡮ࡵࡀ࠿࠳ࡹࡪ࠾ࠨಧ")
  elif bstack11ll1ll1_opy_ == bstack1l111l1_opy_ (u"ࠨࡦࡢ࡫࡯ࡩࡩࠨನ"):
    return bstack1l111l1_opy_ (u"ࠧ࠽ࡶࡧࠤࡨࡲࡡࡴࡵࡀࠦࡧࡹࡴࡢࡥ࡮࠱ࡩࡧࡴࡢࠤࠣࡷࡹࡿ࡬ࡦ࠿ࠥࡧࡴࡲ࡯ࡳ࠼ࡵࡩࡩࡁࠢ࠿࠾ࡩࡳࡳࡺࠠࡤࡱ࡯ࡳࡷࡃࠢࡳࡧࡧࠦࡃࡌࡡࡪ࡮ࡨࡨࡁ࠵ࡦࡰࡰࡷࡂࡁ࠵ࡴࡥࡀࠪ಩")
  elif bstack11ll1ll1_opy_ == bstack1l111l1_opy_ (u"ࠣࡲࡤࡷࡸ࡫ࡤࠣಪ"):
    return bstack1l111l1_opy_ (u"ࠩ࠿ࡸࡩࠦࡣ࡭ࡣࡶࡷࡂࠨࡢࡴࡶࡤࡧࡰ࠳ࡤࡢࡶࡤࠦࠥࡹࡴࡺ࡮ࡨࡁࠧࡩ࡯࡭ࡱࡵ࠾࡬ࡸࡥࡦࡰ࠾ࠦࡃࡂࡦࡰࡰࡷࠤࡨࡵ࡬ࡰࡴࡀࠦ࡬ࡸࡥࡦࡰࠥࡂࡕࡧࡳࡴࡧࡧࡀ࠴࡬࡯࡯ࡶࡁࡀ࠴ࡺࡤ࠿ࠩಫ")
  elif bstack11ll1ll1_opy_ == bstack1l111l1_opy_ (u"ࠥࡩࡷࡸ࡯ࡳࠤಬ"):
    return bstack1l111l1_opy_ (u"ࠫࡁࡺࡤࠡࡥ࡯ࡥࡸࡹ࠽ࠣࡤࡶࡸࡦࡩ࡫࠮ࡦࡤࡸࡦࠨࠠࡴࡶࡼࡰࡪࡃࠢࡤࡱ࡯ࡳࡷࡀࡲࡦࡦ࠾ࠦࡃࡂࡦࡰࡰࡷࠤࡨࡵ࡬ࡰࡴࡀࠦࡷ࡫ࡤࠣࡀࡈࡶࡷࡵࡲ࠽࠱ࡩࡳࡳࡺ࠾࠽࠱ࡷࡨࡃ࠭ಭ")
  elif bstack11ll1ll1_opy_ == bstack1l111l1_opy_ (u"ࠧࡺࡩ࡮ࡧࡲࡹࡹࠨಮ"):
    return bstack1l111l1_opy_ (u"࠭࠼ࡵࡦࠣࡧࡱࡧࡳࡴ࠿ࠥࡦࡸࡺࡡࡤ࡭࠰ࡨࡦࡺࡡࠣࠢࡶࡸࡾࡲࡥ࠾ࠤࡦࡳࡱࡵࡲ࠻ࠥࡨࡩࡦ࠹࠲࠷࠽ࠥࡂࡁ࡬࡯࡯ࡶࠣࡧࡴࡲ࡯ࡳ࠿ࠥࠧࡪ࡫ࡡ࠴࠴࠹ࠦࡃ࡚ࡩ࡮ࡧࡲࡹࡹࡂ࠯ࡧࡱࡱࡸࡃࡂ࠯ࡵࡦࡁࠫಯ")
  elif bstack11ll1ll1_opy_ == bstack1l111l1_opy_ (u"ࠢࡳࡷࡱࡲ࡮ࡴࡧࠣರ"):
    return bstack1l111l1_opy_ (u"ࠨ࠾ࡷࡨࠥࡩ࡬ࡢࡵࡶࡁࠧࡨࡳࡵࡣࡦ࡯࠲ࡪࡡࡵࡣࠥࠤࡸࡺࡹ࡭ࡧࡀࠦࡨࡵ࡬ࡰࡴ࠽ࡦࡱࡧࡣ࡬࠽ࠥࡂࡁ࡬࡯࡯ࡶࠣࡧࡴࡲ࡯ࡳ࠿ࠥࡦࡱࡧࡣ࡬ࠤࡁࡖࡺࡴ࡮ࡪࡰࡪࡀ࠴࡬࡯࡯ࡶࡁࡀ࠴ࡺࡤ࠿ࠩಱ")
  else:
    return bstack1l111l1_opy_ (u"ࠩ࠿ࡸࡩࠦࡡ࡭࡫ࡪࡲࡂࠨࡣࡦࡰࡷࡩࡷࠨࠠࡤ࡮ࡤࡷࡸࡃࠢࡣࡵࡷࡥࡨࡱ࠭ࡥࡣࡷࡥࠧࠦࡳࡵࡻ࡯ࡩࡂࠨࡣࡰ࡮ࡲࡶ࠿ࡨ࡬ࡢࡥ࡮࠿ࠧࡄ࠼ࡧࡱࡱࡸࠥࡩ࡯࡭ࡱࡵࡁࠧࡨ࡬ࡢࡥ࡮ࠦࡃ࠭ಲ") + bstack1l1ll11l1_opy_(
      bstack11ll1ll1_opy_) + bstack1l111l1_opy_ (u"ࠪࡀ࠴࡬࡯࡯ࡶࡁࡀ࠴ࡺࡤ࠿ࠩಳ")
def bstack1l11111l_opy_(session):
  return bstack1l111l1_opy_ (u"ࠫࡁࡺࡲࠡࡥ࡯ࡥࡸࡹ࠽ࠣࡤࡶࡸࡦࡩ࡫࠮ࡴࡲࡻࠧࡄ࠼ࡵࡦࠣࡧࡱࡧࡳࡴ࠿ࠥࡦࡸࡺࡡࡤ࡭࠰ࡨࡦࡺࡡࠡࡵࡨࡷࡸ࡯࡯࡯࠯ࡱࡥࡲ࡫ࠢ࠿࠾ࡤࠤ࡭ࡸࡥࡧ࠿ࠥࡿࢂࠨࠠࡵࡣࡵ࡫ࡪࡺ࠽ࠣࡡࡥࡰࡦࡴ࡫ࠣࡀࡾࢁࡁ࠵ࡡ࠿࠾࠲ࡸࡩࡄࡻࡾࡽࢀࡀࡹࡪࠠࡢ࡮࡬࡫ࡳࡃࠢࡤࡧࡱࡸࡪࡸࠢࠡࡥ࡯ࡥࡸࡹ࠽ࠣࡤࡶࡸࡦࡩ࡫࠮ࡦࡤࡸࡦࠨ࠾ࡼࡿ࠿࠳ࡹࡪ࠾࠽ࡶࡧࠤࡦࡲࡩࡨࡰࡀࠦࡨ࡫࡮ࡵࡧࡵࠦࠥࡩ࡬ࡢࡵࡶࡁࠧࡨࡳࡵࡣࡦ࡯࠲ࡪࡡࡵࡣࠥࡂࢀࢃ࠼࠰ࡶࡧࡂࡁࡺࡤࠡࡣ࡯࡭࡬ࡴ࠽ࠣࡥࡨࡲࡹ࡫ࡲࠣࠢࡦࡰࡦࡹࡳ࠾ࠤࡥࡷࡹࡧࡣ࡬࠯ࡧࡥࡹࡧࠢ࠿ࡽࢀࡀ࠴ࡺࡤ࠿࠾ࡷࡨࠥࡧ࡬ࡪࡩࡱࡁࠧࡩࡥ࡯ࡶࡨࡶࠧࠦࡣ࡭ࡣࡶࡷࡂࠨࡢࡴࡶࡤࡧࡰ࠳ࡤࡢࡶࡤࠦࡃࢁࡽ࠽࠱ࡷࡨࡃࡂ࠯ࡵࡴࡁࠫ಴").format(
    session[bstack1l111l1_opy_ (u"ࠬࡶࡵࡣ࡮࡬ࡧࡤࡻࡲ࡭ࠩವ")], bstack1llll111l1_opy_(session), bstack11l1ll11l_opy_(session[bstack1l111l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤࡹࡴࡢࡶࡸࡷࠬಶ")]),
    bstack11l1ll11l_opy_(session[bstack1l111l1_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧಷ")]),
    bstack1l1ll11l1_opy_(session[bstack1l111l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࠩಸ")] or session[bstack1l111l1_opy_ (u"ࠩࡧࡩࡻ࡯ࡣࡦࠩಹ")] or bstack1l111l1_opy_ (u"ࠪࠫ಺")) + bstack1l111l1_opy_ (u"ࠦࠥࠨ಻") + (session[bstack1l111l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡥࡶࡦࡴࡶ࡭ࡴࡴ಼ࠧ")] or bstack1l111l1_opy_ (u"࠭ࠧಽ")),
    session[bstack1l111l1_opy_ (u"ࠧࡰࡵࠪಾ")] + bstack1l111l1_opy_ (u"ࠣࠢࠥಿ") + session[bstack1l111l1_opy_ (u"ࠩࡲࡷࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭ೀ")], session[bstack1l111l1_opy_ (u"ࠪࡨࡺࡸࡡࡵ࡫ࡲࡲࠬು")] or bstack1l111l1_opy_ (u"ࠫࠬೂ"),
    session[bstack1l111l1_opy_ (u"ࠬࡩࡲࡦࡣࡷࡩࡩࡥࡡࡵࠩೃ")] if session[bstack1l111l1_opy_ (u"࠭ࡣࡳࡧࡤࡸࡪࡪ࡟ࡢࡶࠪೄ")] else bstack1l111l1_opy_ (u"ࠧࠨ೅"))
def bstack1llll111ll_opy_(sessions, bstack111ll11l_opy_):
  try:
    bstack111lll1ll_opy_ = bstack1l111l1_opy_ (u"ࠣࠤೆ")
    if not os.path.exists(bstack11lllll1l_opy_):
      os.mkdir(bstack11lllll1l_opy_)
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack1l111l1_opy_ (u"ࠩࡤࡷࡸ࡫ࡴࡴ࠱ࡵࡩࡵࡵࡲࡵ࠰࡫ࡸࡲࡲࠧೇ")), bstack1l111l1_opy_ (u"ࠪࡶࠬೈ")) as f:
      bstack111lll1ll_opy_ = f.read()
    bstack111lll1ll_opy_ = bstack111lll1ll_opy_.replace(bstack1l111l1_opy_ (u"ࠫࢀࠫࡒࡆࡕࡘࡐ࡙࡙࡟ࡄࡑࡘࡒ࡙ࠫࡽࠨ೉"), str(len(sessions)))
    bstack111lll1ll_opy_ = bstack111lll1ll_opy_.replace(bstack1l111l1_opy_ (u"ࠬࢁࠥࡃࡗࡌࡐࡉࡥࡕࡓࡎࠨࢁࠬೊ"), bstack111ll11l_opy_)
    bstack111lll1ll_opy_ = bstack111lll1ll_opy_.replace(bstack1l111l1_opy_ (u"࠭ࡻࠦࡄࡘࡍࡑࡊ࡟ࡏࡃࡐࡉࠪࢃࠧೋ"),
                                              sessions[0].get(bstack1l111l1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡥ࡮ࡢ࡯ࡨࠫೌ")) if sessions[0] else bstack1l111l1_opy_ (u"ࠨ್ࠩ"))
    with open(os.path.join(bstack11lllll1l_opy_, bstack1l111l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠮ࡴࡨࡴࡴࡸࡴ࠯ࡪࡷࡱࡱ࠭೎")), bstack1l111l1_opy_ (u"ࠪࡻࠬ೏")) as stream:
      stream.write(bstack111lll1ll_opy_.split(bstack1l111l1_opy_ (u"ࠫࢀࠫࡓࡆࡕࡖࡍࡔࡔࡓࡠࡆࡄࡘࡆࠫࡽࠨ೐"))[0])
      for session in sessions:
        stream.write(bstack1l11111l_opy_(session))
      stream.write(bstack111lll1ll_opy_.split(bstack1l111l1_opy_ (u"ࠬࢁࠥࡔࡇࡖࡗࡎࡕࡎࡔࡡࡇࡅ࡙ࡇࠥࡾࠩ೑"))[1])
    logger.info(bstack1l111l1_opy_ (u"࠭ࡇࡦࡰࡨࡶࡦࡺࡥࡥࠢࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠡࡤࡸ࡭ࡱࡪࠠࡢࡴࡷ࡭࡫ࡧࡣࡵࡵࠣࡥࡹࠦࡻࡾࠩ೒").format(bstack11lllll1l_opy_));
  except Exception as e:
    logger.debug(bstack1l1llllll_opy_.format(str(e)))
def bstack11l11l11l_opy_(bstack1lll1l1l1l_opy_):
  global CONFIG
  try:
    host = bstack1l111l1_opy_ (u"ࠧࡢࡲ࡬࠱ࡨࡲ࡯ࡶࡦࠪ೓") if bstack1l111l1_opy_ (u"ࠨࡣࡳࡴࠬ೔") in CONFIG else bstack1l111l1_opy_ (u"ࠩࡤࡴ࡮࠭ೕ")
    user = CONFIG[bstack1l111l1_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬೖ")]
    key = CONFIG[bstack1l111l1_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧ೗")]
    bstack111l1111_opy_ = bstack1l111l1_opy_ (u"ࠬࡧࡰࡱ࠯ࡤࡹࡹࡵ࡭ࡢࡶࡨࠫ೘") if bstack1l111l1_opy_ (u"࠭ࡡࡱࡲࠪ೙") in CONFIG else bstack1l111l1_opy_ (u"ࠧࡢࡷࡷࡳࡲࡧࡴࡦࠩ೚")
    url = bstack1l111l1_opy_ (u"ࠨࡪࡷࡸࡵࡹ࠺࠰࠱ࡾࢁ࠿ࢁࡽࡁࡽࢀ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳ࠯ࡼࡿ࠲ࡦࡺ࡯࡬ࡥࡵ࠲ࡿࢂ࠵ࡳࡦࡵࡶ࡭ࡴࡴࡳ࠯࡬ࡶࡳࡳ࠭೛").format(user, key, host, bstack111l1111_opy_,
                                                                                bstack1lll1l1l1l_opy_)
    headers = {
      bstack1l111l1_opy_ (u"ࠩࡆࡳࡳࡺࡥ࡯ࡶ࠰ࡸࡾࡶࡥࠨ೜"): bstack1l111l1_opy_ (u"ࠪࡥࡵࡶ࡬ࡪࡥࡤࡸ࡮ࡵ࡮࠰࡬ࡶࡳࡳ࠭ೝ"),
    }
    proxies = bstack1l1ll1ll_opy_(CONFIG, url)
    response = requests.get(url, headers=headers, proxies=proxies)
    if response.json():
      return list(map(lambda session: session[bstack1l111l1_opy_ (u"ࠫࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࡠࡵࡨࡷࡸ࡯࡯࡯ࠩೞ")], response.json()))
  except Exception as e:
    logger.debug(bstack1l11l1l1ll_opy_.format(str(e)))
def bstack1ll11l1l_opy_():
  global CONFIG
  global bstack1lll1ll1l_opy_
  try:
    if bstack1l111l1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨ೟") in CONFIG:
      host = bstack1l111l1_opy_ (u"࠭ࡡࡱ࡫࠰ࡧࡱࡵࡵࡥࠩೠ") if bstack1l111l1_opy_ (u"ࠧࡢࡲࡳࠫೡ") in CONFIG else bstack1l111l1_opy_ (u"ࠨࡣࡳ࡭ࠬೢ")
      user = CONFIG[bstack1l111l1_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫೣ")]
      key = CONFIG[bstack1l111l1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭೤")]
      bstack111l1111_opy_ = bstack1l111l1_opy_ (u"ࠫࡦࡶࡰ࠮ࡣࡸࡸࡴࡳࡡࡵࡧࠪ೥") if bstack1l111l1_opy_ (u"ࠬࡧࡰࡱࠩ೦") in CONFIG else bstack1l111l1_opy_ (u"࠭ࡡࡶࡶࡲࡱࡦࡺࡥࠨ೧")
      url = bstack1l111l1_opy_ (u"ࠧࡩࡶࡷࡴࡸࡀ࠯࠰ࡽࢀ࠾ࢀࢃࡀࡼࡿ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲ࠵ࡻࡾ࠱ࡥࡹ࡮ࡲࡤࡴ࠰࡭ࡷࡴࡴࠧ೨").format(user, key, host, bstack111l1111_opy_)
      headers = {
        bstack1l111l1_opy_ (u"ࠨࡅࡲࡲࡹ࡫࡮ࡵ࠯ࡷࡽࡵ࡫ࠧ೩"): bstack1l111l1_opy_ (u"ࠩࡤࡴࡵࡲࡩࡤࡣࡷ࡭ࡴࡴ࠯࡫ࡵࡲࡲࠬ೪"),
      }
      if bstack1l111l1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ೫") in CONFIG:
        params = {bstack1l111l1_opy_ (u"ࠫࡳࡧ࡭ࡦࠩ೬"): CONFIG[bstack1l111l1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨ೭")], bstack1l111l1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤ࡯ࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ೮"): CONFIG[bstack1l111l1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ೯")]}
      else:
        params = {bstack1l111l1_opy_ (u"ࠨࡰࡤࡱࡪ࠭೰"): CONFIG[bstack1l111l1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬೱ")]}
      proxies = bstack1l1ll1ll_opy_(CONFIG, url)
      response = requests.get(url, params=params, headers=headers, proxies=proxies)
      if response.json():
        bstack1llll1l1_opy_ = response.json()[0][bstack1l111l1_opy_ (u"ࠪࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ࡟ࡣࡷ࡬ࡰࡩ࠭ೲ")]
        if bstack1llll1l1_opy_:
          bstack111ll11l_opy_ = bstack1llll1l1_opy_[bstack1l111l1_opy_ (u"ࠫࡵࡻࡢ࡭࡫ࡦࡣࡺࡸ࡬ࠨೳ")].split(bstack1l111l1_opy_ (u"ࠬࡶࡵࡣ࡮࡬ࡧ࠲ࡨࡵࡪ࡮ࡧࠫ೴"))[0] + bstack1l111l1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡸ࠵ࠧ೵") + bstack1llll1l1_opy_[
            bstack1l111l1_opy_ (u"ࠧࡩࡣࡶ࡬ࡪࡪ࡟ࡪࡦࠪ೶")]
          logger.info(bstack1l1l1lll1l_opy_.format(bstack111ll11l_opy_))
          bstack1lll1ll1l_opy_ = bstack1llll1l1_opy_[bstack1l111l1_opy_ (u"ࠨࡪࡤࡷ࡭࡫ࡤࡠ࡫ࡧࠫ೷")]
          bstack1l1111l1_opy_ = CONFIG[bstack1l111l1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬ೸")]
          if bstack1l111l1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ೹") in CONFIG:
            bstack1l1111l1_opy_ += bstack1l111l1_opy_ (u"ࠫࠥ࠭೺") + CONFIG[bstack1l111l1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ೻")]
          if bstack1l1111l1_opy_ != bstack1llll1l1_opy_[bstack1l111l1_opy_ (u"࠭࡮ࡢ࡯ࡨࠫ೼")]:
            logger.debug(bstack1ll1l1l1_opy_.format(bstack1llll1l1_opy_[bstack1l111l1_opy_ (u"ࠧ࡯ࡣࡰࡩࠬ೽")], bstack1l1111l1_opy_))
          return [bstack1llll1l1_opy_[bstack1l111l1_opy_ (u"ࠨࡪࡤࡷ࡭࡫ࡤࡠ࡫ࡧࠫ೾")], bstack111ll11l_opy_]
    else:
      logger.warn(bstack111l1l1l1_opy_)
  except Exception as e:
    logger.debug(bstack1l11l111l_opy_.format(str(e)))
  return [None, None]
def bstack11lllll11_opy_(url, bstack11ll111l1_opy_=False):
  global CONFIG
  global bstack1lll1llll1_opy_
  if not bstack1lll1llll1_opy_:
    hostname = bstack11ll1ll1l_opy_(url)
    is_private = bstack11l1l1l1l_opy_(hostname)
    if (bstack1l111l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭೿") in CONFIG and not bstack1l1l1ll111_opy_(CONFIG[bstack1l111l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧഀ")])) and (is_private or bstack11ll111l1_opy_):
      bstack1lll1llll1_opy_ = hostname
def bstack11ll1ll1l_opy_(url):
  return urlparse(url).hostname
def bstack11l1l1l1l_opy_(hostname):
  for bstack1ll11lll1l_opy_ in bstack11l1lll1l_opy_:
    regex = re.compile(bstack1ll11lll1l_opy_)
    if regex.match(hostname):
      return True
  return False
def bstack1l1lll11_opy_(key_name):
  return True if key_name in threading.current_thread().__dict__.keys() else False
def getAccessibilityResults(driver):
  global CONFIG
  global bstack1llll1ll1_opy_
  bstack11lll1lll_opy_ = not (bstack1ll1ll1l1_opy_(threading.current_thread(), bstack1l111l1_opy_ (u"ࠫ࡮ࡹࡁ࠲࠳ࡼࡘࡪࡹࡴࠨഁ"), None) and bstack1ll1ll1l1_opy_(
          threading.current_thread(), bstack1l111l1_opy_ (u"ࠬࡧ࠱࠲ࡻࡓࡰࡦࡺࡦࡰࡴࡰࠫം"), None))
  bstack1ll111l111_opy_ = getattr(driver, bstack1l111l1_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡇ࠱࠲ࡻࡖ࡬ࡴࡻ࡬ࡥࡕࡦࡥࡳ࠭ഃ"), None) != True
  if not bstack1l1lll11l1_opy_.bstack1lllll1ll_opy_(CONFIG, bstack1llll1ll1_opy_) or (bstack1ll111l111_opy_ and bstack11lll1lll_opy_):
    logger.warning(bstack1l111l1_opy_ (u"ࠢࡏࡱࡷࠤࡦࡴࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤࡸ࡫ࡳࡴ࡫ࡲࡲ࠱ࠦࡣࡢࡰࡱࡳࡹࠦࡲࡦࡶࡵ࡭ࡪࡼࡥࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡴࡨࡷࡺࡲࡴࡴ࠰ࠥഄ"))
    return {}
  try:
    logger.debug(bstack1l111l1_opy_ (u"ࠨࡒࡨࡶ࡫ࡵࡲ࡮࡫ࡱ࡫ࠥࡹࡣࡢࡰࠣࡦࡪ࡬࡯ࡳࡧࠣ࡫ࡪࡺࡴࡪࡰࡪࠤࡷ࡫ࡳࡶ࡮ࡷࡷࠬഅ"))
    logger.debug(perform_scan(driver))
    results = driver.execute_async_script(bstack1lll1l1l1_opy_.bstack1l11ll11_opy_)
    return results
  except Exception:
    logger.error(bstack1l111l1_opy_ (u"ࠤࡑࡳࠥࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡸࡥࡴࡷ࡯ࡸࡸࠦࡷࡦࡴࡨࠤ࡫ࡵࡵ࡯ࡦ࠱ࠦആ"))
    return {}
def getAccessibilityResultsSummary(driver):
  global CONFIG
  global bstack1llll1ll1_opy_
  bstack11lll1lll_opy_ = not (bstack1ll1ll1l1_opy_(threading.current_thread(), bstack1l111l1_opy_ (u"ࠪ࡭ࡸࡇ࠱࠲ࡻࡗࡩࡸࡺࠧഇ"), None) and bstack1ll1ll1l1_opy_(
          threading.current_thread(), bstack1l111l1_opy_ (u"ࠫࡦ࠷࠱ࡺࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪഈ"), None))
  bstack1ll111l111_opy_ = getattr(driver, bstack1l111l1_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡆ࠷࠱ࡺࡕ࡫ࡳࡺࡲࡤࡔࡥࡤࡲࠬഉ"), None) != True
  if not bstack1l1lll11l1_opy_.bstack1lllll1ll_opy_(CONFIG, bstack1llll1ll1_opy_) or (bstack1ll111l111_opy_ and bstack11lll1lll_opy_):
    logger.warning(bstack1l111l1_opy_ (u"ࠨࡎࡰࡶࠣࡥࡳࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣࡷࡪࡹࡳࡪࡱࡱ࠰ࠥࡩࡡ࡯ࡰࡲࡸࠥࡸࡥࡵࡴ࡬ࡩࡻ࡫ࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡳࡧࡶࡹࡱࡺࡳࠡࡵࡸࡱࡲࡧࡲࡺ࠰ࠥഊ"))
    return {}
  try:
    logger.debug(bstack1l111l1_opy_ (u"ࠧࡑࡧࡵࡪࡴࡸ࡭ࡪࡰࡪࠤࡸࡩࡡ࡯ࠢࡥࡩ࡫ࡵࡲࡦࠢࡪࡩࡹࡺࡩ࡯ࡩࠣࡶࡪࡹࡵ࡭ࡶࡶࠤࡸࡻ࡭࡮ࡣࡵࡽࠬഋ"))
    logger.debug(perform_scan(driver))
    bstack1l1l11l1ll_opy_ = driver.execute_async_script(bstack1lll1l1l1_opy_.bstack1l11lll1_opy_)
    return bstack1l1l11l1ll_opy_
  except Exception:
    logger.error(bstack1l111l1_opy_ (u"ࠣࡐࡲࠤࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡸࡻ࡭࡮ࡣࡵࡽࠥࡽࡡࡴࠢࡩࡳࡺࡴࡤ࠯ࠤഌ"))
    return {}
def perform_scan(driver, *args, **kwargs):
  global CONFIG
  global bstack1llll1ll1_opy_
  bstack11lll1lll_opy_ = not (bstack1ll1ll1l1_opy_(threading.current_thread(), bstack1l111l1_opy_ (u"ࠩ࡬ࡷࡆ࠷࠱ࡺࡖࡨࡷࡹ࠭഍"), None) and bstack1ll1ll1l1_opy_(
          threading.current_thread(), bstack1l111l1_opy_ (u"ࠪࡥ࠶࠷ࡹࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩഎ"), None))
  bstack1ll111l111_opy_ = getattr(driver, bstack1l111l1_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡅ࠶࠷ࡹࡔࡪࡲࡹࡱࡪࡓࡤࡣࡱࠫഏ"), None) != True
  if not bstack1l1lll11l1_opy_.bstack1lllll1ll_opy_(CONFIG, bstack1llll1ll1_opy_) or (bstack1ll111l111_opy_ and bstack11lll1lll_opy_):
    logger.warning(bstack1l111l1_opy_ (u"ࠧࡔ࡯ࡵࠢࡤࡲࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡶࡩࡸࡹࡩࡰࡰ࠯ࠤࡨࡧ࡮࡯ࡱࡷࠤࡷࡻ࡮ࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡵࡦࡥࡳ࠴ࠢഐ"))
    return {}
  try:
    bstack11l1l1lll_opy_ = driver.execute_async_script(bstack1lll1l1l1_opy_.perform_scan, {bstack1l111l1_opy_ (u"࠭࡭ࡦࡶ࡫ࡳࡩ࠭഑"): kwargs.get(bstack1l111l1_opy_ (u"ࠧࡥࡴ࡬ࡺࡪࡸ࡟ࡤࡱࡰࡱࡦࡴࡤࠨഒ"), None) or bstack1l111l1_opy_ (u"ࠨࠩഓ")})
    return bstack11l1l1lll_opy_
  except Exception:
    logger.error(bstack1l111l1_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡸࡵ࡯ࠢࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡶࡧࡦࡴ࠮ࠣഔ"))
    return {}