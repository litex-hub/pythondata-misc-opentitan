import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5202"
version_tuple = (0, 0, 5202)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5202")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5111"
data_version_tuple = (0, 0, 5111)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5111")
except ImportError:
    pass
data_git_hash = "840b59a02e86a6421c6ceeddfa0bcddf1fdc2efa"
data_git_describe = "v0.0-5111-g840b59a02"
data_git_msg = """\
commit 840b59a02e86a6421c6ceeddfa0bcddf1fdc2efa
Author: Tung Hoang <hoang.tung@wdc.com>
Date:   Fri Feb 26 21:25:34 2021 -0800

    [i2c, dv] Update fifo_watermark and fifo_fall test
    
      - Update vseqs to address comments in PR #5379
    
    Signed-off-by: Tung Hoang <hoang.tung@wdc.com>

"""

# Tool version info
tool_version_str = "0.0.post91"
tool_version_tuple = (0, 0, 91)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post91")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
