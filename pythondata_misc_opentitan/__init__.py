import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8284"
version_tuple = (0, 0, 8284)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8284")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8172"
data_version_tuple = (0, 0, 8172)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8172")
except ImportError:
    pass
data_git_hash = "37162df4922631a361f17a5f88a9b0b9b194a81e"
data_git_describe = "v0.0-8172-g37162df49"
data_git_msg = """\
commit 37162df4922631a361f17a5f88a9b0b9b194a81e
Author: Weicai Yang <weicai@google.com>
Date:   Thu Oct 14 14:20:32 2021 -0700

    Fix CI failure
    
    Looks like we didn't check CI result before merging #8672
    Signed-off-by: Weicai Yang <weicai@google.com>

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
