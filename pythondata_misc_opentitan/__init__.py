import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10024"
version_tuple = (0, 0, 10024)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10024")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9900"
data_version_tuple = (0, 0, 9900)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9900")
except ImportError:
    pass
data_git_hash = "09eb5512f3ac7c17f48eaa6abfe89ba5e5ac8dee"
data_git_describe = "v0.0-9900-g09eb5512f"
data_git_msg = """\
commit 09eb5512f3ac7c17f48eaa6abfe89ba5e5ac8dee
Author: Weicai Yang <weicai@google.com>
Date:   Tue Feb 1 14:19:14 2022 -0800

    [keymgr/dv] Several DV updates for recent design changes
    
    several fixes for recent design changes
    1. add covergroup for control_shadowed
    2. fix start bit predict
    3. change to use csr_wr for start reg
    4. fix shadow reg test. When storage error occurs on control_shadowed,
       we can't issue operation as the reg is locked
    5. fix keymgr_direct_to_disabled_vseq. need to program start CSRs
    Signed-off-by: Weicai Yang <weicai@google.com>

"""

# Tool version info
tool_version_str = "0.0.post124"
tool_version_tuple = (0, 0, 124)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post124")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
