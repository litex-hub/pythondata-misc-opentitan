import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8613"
version_tuple = (0, 0, 8613)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8613")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8501"
data_version_tuple = (0, 0, 8501)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8501")
except ImportError:
    pass
data_git_hash = "fbf2edc1dadaabd93df8c84e9748e0f524dd2326"
data_git_describe = "v0.0-8501-gfbf2edc1d"
data_git_msg = """\
commit fbf2edc1dadaabd93df8c84e9748e0f524dd2326
Author: Weicai Yang <weicai@google.com>
Date:   Mon Sep 27 15:31:08 2021 -0700

    [dv] Test security countermeasures
    
    Only support testing prim_count and enable this test in keymgr
    
    Also reduce timeout for spinwait of op_status in keymgr
    
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
