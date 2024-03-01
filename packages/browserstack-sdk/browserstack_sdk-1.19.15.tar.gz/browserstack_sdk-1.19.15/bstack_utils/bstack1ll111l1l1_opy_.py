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
import sys
import logging
import tarfile
import io
import os
import requests
import re
from requests_toolbelt.multipart.encoder import MultipartEncoder
from bstack_utils.constants import bstack11l1l11l1l_opy_
import tempfile
import json
bstack111l1l1111_opy_ = os.path.join(tempfile.gettempdir(), bstack1l111l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡩ࡫ࡢࡶࡩ࠱ࡰࡴ࡭ࠧጷ"))
def get_logger(name=__name__, level=None):
  logger = logging.getLogger(name)
  if level:
    logging.basicConfig(
      level=level,
      format=bstack1l111l1_opy_ (u"࠭࡜࡯ࠧࠫࡥࡸࡩࡴࡪ࡯ࡨ࠭ࡸ࡛ࠦࠦࠪࡱࡥࡲ࡫ࠩࡴ࡟࡞ࠩ࠭ࡲࡥࡷࡧ࡯ࡲࡦࡳࡥࠪࡵࡠࠤ࠲ࠦࠥࠩ࡯ࡨࡷࡸࡧࡧࡦࠫࡶࠫጸ"),
      datefmt=bstack1l111l1_opy_ (u"ࠧࠦࡊ࠽ࠩࡒࡀࠥࡔࠩጹ"),
      stream=sys.stdout
    )
  return logger
def bstack111l1l111l_opy_():
  global bstack111l1l1111_opy_
  if os.path.exists(bstack111l1l1111_opy_):
    os.remove(bstack111l1l1111_opy_)
def bstack11l11l11_opy_():
  for handler in logging.getLogger().handlers:
    logging.getLogger().removeHandler(handler)
def bstack1ll1ll1ll1_opy_(config, log_level):
  bstack111l1ll111_opy_ = log_level
  if bstack1l111l1_opy_ (u"ࠨ࡮ࡲ࡫ࡑ࡫ࡶࡦ࡮ࠪጺ") in config:
    bstack111l1ll111_opy_ = bstack11l1l11l1l_opy_[config[bstack1l111l1_opy_ (u"ࠩ࡯ࡳ࡬ࡒࡥࡷࡧ࡯ࠫጻ")]]
  if config.get(bstack1l111l1_opy_ (u"ࠪࡨ࡮ࡹࡡࡣ࡮ࡨࡅࡺࡺ࡯ࡄࡣࡳࡸࡺࡸࡥࡍࡱࡪࡷࠬጼ"), False):
    logging.getLogger().setLevel(bstack111l1ll111_opy_)
    return bstack111l1ll111_opy_
  global bstack111l1l1111_opy_
  bstack11l11l11_opy_()
  bstack111l1l1l1l_opy_ = logging.Formatter(
    fmt=bstack1l111l1_opy_ (u"ࠫࡡࡴࠥࠩࡣࡶࡧࡹ࡯࡭ࡦࠫࡶࠤࡠࠫࠨ࡯ࡣࡰࡩ࠮ࡹ࡝࡜ࠧࠫࡰࡪࡼࡥ࡭ࡰࡤࡱࡪ࠯ࡳ࡞ࠢ࠰ࠤࠪ࠮࡭ࡦࡵࡶࡥ࡬࡫ࠩࡴࠩጽ"),
    datefmt=bstack1l111l1_opy_ (u"ࠬࠫࡈ࠻ࠧࡐ࠾࡙ࠪࠧጾ")
  )
  bstack111l11llll_opy_ = logging.StreamHandler(sys.stdout)
  file_handler = logging.FileHandler(bstack111l1l1111_opy_)
  file_handler.setFormatter(bstack111l1l1l1l_opy_)
  bstack111l11llll_opy_.setFormatter(bstack111l1l1l1l_opy_)
  file_handler.setLevel(logging.DEBUG)
  bstack111l11llll_opy_.setLevel(log_level)
  file_handler.addFilter(lambda r: r.name != bstack1l111l1_opy_ (u"࠭ࡳࡦ࡮ࡨࡲ࡮ࡻ࡭࠯ࡹࡨࡦࡩࡸࡩࡷࡧࡵ࠲ࡷ࡫࡭ࡰࡶࡨ࠲ࡷ࡫࡭ࡰࡶࡨࡣࡨࡵ࡮࡯ࡧࡦࡸ࡮ࡵ࡮ࠨጿ"))
  logging.getLogger().setLevel(logging.DEBUG)
  bstack111l11llll_opy_.setLevel(bstack111l1ll111_opy_)
  logging.getLogger().addHandler(bstack111l11llll_opy_)
  logging.getLogger().addHandler(file_handler)
  return bstack111l1ll111_opy_
def bstack111l1l1ll1_opy_(config):
  try:
    bstack111l1lll11_opy_ = set([
      bstack1l111l1_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩፀ"), bstack1l111l1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫፁ"), bstack1l111l1_opy_ (u"ࠩ࡫ࡸࡹࡶࡐࡳࡱࡻࡽࠬፂ"), bstack1l111l1_opy_ (u"ࠪ࡬ࡹࡺࡰࡴࡒࡵࡳࡽࡿࠧፃ"), bstack1l111l1_opy_ (u"ࠫࡨࡻࡳࡵࡱࡰ࡚ࡦࡸࡩࡢࡤ࡯ࡩࡸ࠭ፄ"),
      bstack1l111l1_opy_ (u"ࠬࡶࡲࡰࡺࡼ࡙ࡸ࡫ࡲࠨፅ"), bstack1l111l1_opy_ (u"࠭ࡰࡳࡱࡻࡽࡕࡧࡳࡴࠩፆ"), bstack1l111l1_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡖࡲࡰࡺࡼ࡙ࡸ࡫ࡲࠨፇ"), bstack1l111l1_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡐࡳࡱࡻࡽࡕࡧࡳࡴࠩፈ")
    ])
    bstack111l1l11l1_opy_ = bstack1l111l1_opy_ (u"ࠩࠪፉ")
    with open(bstack1l111l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡼࡱࡱ࠭ፊ")) as bstack111l1l1lll_opy_:
      bstack111l1ll1ll_opy_ = bstack111l1l1lll_opy_.read()
      bstack111l1l11l1_opy_ = re.sub(bstack1l111l1_opy_ (u"ࡶࠬࡤࠨ࡝ࡵ࠮࠭ࡄࠩ࠮ࠫࠦ࡟ࡲࠬፋ"), bstack1l111l1_opy_ (u"ࠬ࠭ፌ"), bstack111l1ll1ll_opy_, flags=re.M)
      bstack111l1l11l1_opy_ = re.sub(
        bstack1l111l1_opy_ (u"ࡸࠧ࡟ࠪ࡟ࡷ࠰࠯࠿ࠩࠩፍ") + bstack1l111l1_opy_ (u"ࠧࡽࠩፎ").join(bstack111l1lll11_opy_) + bstack1l111l1_opy_ (u"ࠨࠫ࠱࠮ࠩ࠭ፏ"),
        bstack1l111l1_opy_ (u"ࡴࠪࡠ࠷ࡀࠠ࡜ࡔࡈࡈࡆࡉࡔࡆࡆࡠࠫፐ"),
        bstack111l1l11l1_opy_, flags=re.M | re.I
      )
    def bstack111l1l11ll_opy_(dic):
      bstack111l1l1l11_opy_ = {}
      for key, value in dic.items():
        if key in bstack111l1lll11_opy_:
          bstack111l1l1l11_opy_[key] = bstack1l111l1_opy_ (u"ࠪ࡟ࡗࡋࡄࡂࡅࡗࡉࡉࡣࠧፑ")
        else:
          if isinstance(value, dict):
            bstack111l1l1l11_opy_[key] = bstack111l1l11ll_opy_(value)
          else:
            bstack111l1l1l11_opy_[key] = value
      return bstack111l1l1l11_opy_
    bstack111l1l1l11_opy_ = bstack111l1l11ll_opy_(config)
    return {
      bstack1l111l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡽࡲࡲࠧፒ"): bstack111l1l11l1_opy_,
      bstack1l111l1_opy_ (u"ࠬ࡬ࡩ࡯ࡣ࡯ࡧࡴࡴࡦࡪࡩ࠱࡮ࡸࡵ࡮ࠨፓ"): json.dumps(bstack111l1l1l11_opy_)
    }
  except Exception as e:
    return {}
def bstack1lll1ll111_opy_(config):
  global bstack111l1l1111_opy_
  try:
    if config.get(bstack1l111l1_opy_ (u"࠭ࡤࡪࡵࡤࡦࡱ࡫ࡁࡶࡶࡲࡇࡦࡶࡴࡶࡴࡨࡐࡴ࡭ࡳࠨፔ"), False):
      return
    uuid = os.getenv(bstack1l111l1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬፕ"))
    if not uuid or uuid == bstack1l111l1_opy_ (u"ࠨࡰࡸࡰࡱ࠭ፖ"):
      return
    bstack111l1ll11l_opy_ = [bstack1l111l1_opy_ (u"ࠩࡵࡩࡶࡻࡩࡳࡧࡰࡩࡳࡺࡳ࠯ࡶࡻࡸࠬፗ"), bstack1l111l1_opy_ (u"ࠪࡔ࡮ࡶࡦࡪ࡮ࡨࠫፘ"), bstack1l111l1_opy_ (u"ࠫࡵࡿࡰࡳࡱ࡭ࡩࡨࡺ࠮ࡵࡱࡰࡰࠬፙ"), bstack111l1l1111_opy_]
    bstack11l11l11_opy_()
    logging.shutdown()
    output_file = os.path.join(tempfile.gettempdir(), bstack1l111l1_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠲ࡲ࡯ࡨࡵ࠰ࠫፚ") + uuid + bstack1l111l1_opy_ (u"࠭࠮ࡵࡣࡵ࠲࡬ࢀࠧ፛"))
    with tarfile.open(output_file, bstack1l111l1_opy_ (u"ࠢࡸ࠼ࡪࡾࠧ፜")) as archive:
      for file in filter(lambda f: os.path.exists(f), bstack111l1ll11l_opy_):
        try:
          archive.add(file,  arcname=os.path.basename(file))
        except:
          pass
      for name, data in bstack111l1l1ll1_opy_(config).items():
        tarinfo = tarfile.TarInfo(name)
        bstack111l1ll1l1_opy_ = data.encode()
        tarinfo.size = len(bstack111l1ll1l1_opy_)
        archive.addfile(tarinfo, io.BytesIO(bstack111l1ll1l1_opy_))
    bstack1ll1l1l1l_opy_ = MultipartEncoder(
      fields= {
        bstack1l111l1_opy_ (u"ࠨࡦࡤࡸࡦ࠭፝"): (os.path.basename(output_file), open(os.path.abspath(output_file), bstack1l111l1_opy_ (u"ࠩࡵࡦࠬ፞")), bstack1l111l1_opy_ (u"ࠪࡥࡵࡶ࡬ࡪࡥࡤࡸ࡮ࡵ࡮࠰ࡺ࠰࡫ࡿ࡯ࡰࠨ፟")),
        bstack1l111l1_opy_ (u"ࠫࡨࡲࡩࡦࡰࡷࡆࡺ࡯࡬ࡥࡗࡸ࡭ࡩ࠭፠"): uuid
      }
    )
    response = requests.post(
      bstack1l111l1_opy_ (u"ࠧ࡮ࡴࡵࡲࡶ࠾࠴࠵ࡵࡱ࡮ࡲࡥࡩ࠳࡯ࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮࠱ࡦࡰ࡮࡫࡮ࡵ࠯࡯ࡳ࡬ࡹ࠯ࡶࡲ࡯ࡳࡦࡪࠢ፡"),
      data=bstack1ll1l1l1l_opy_,
      headers={bstack1l111l1_opy_ (u"࠭ࡃࡰࡰࡷࡩࡳࡺ࠭ࡕࡻࡳࡩࠬ።"): bstack1ll1l1l1l_opy_.content_type},
      auth=(config[bstack1l111l1_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩ፣")], config[bstack1l111l1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫ፤")])
    )
    os.remove(output_file)
    if response.status_code != 200:
      get_logger().debug(bstack1l111l1_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡࡷࡳࡰࡴࡧࡤࠡ࡮ࡲ࡫ࡸࡀࠠࠨ፥") + response.status_code)
  except Exception as e:
    get_logger().debug(bstack1l111l1_opy_ (u"ࠪࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡶࡩࡳࡪࡩ࡯ࡩࠣࡰࡴ࡭ࡳ࠻ࠩ፦") + str(e))
  finally:
    try:
      bstack111l1l111l_opy_()
    except:
      pass