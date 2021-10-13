import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8236"
version_tuple = (0, 0, 8236)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8236")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8124"
data_version_tuple = (0, 0, 8124)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8124")
except ImportError:
    pass
data_git_hash = "52512e8023f26a6ee65661641c47e3fd33b1949f"
data_git_describe = "v0.0-8124-g52512e802"
data_git_msg = """\
commit 52512e8023f26a6ee65661641c47e3fd33b1949f
Author: {Pascal Nasahl} <nasahl@google.com>
Date:   Mon Oct 11 17:33:38 2021 +0000

    [aes/pre_syn] Added missing keymgr_pkg file for Yosys synthesis
    
    Signed-off-by: {Pascal Nasahl} <nasahl@google.com>

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
