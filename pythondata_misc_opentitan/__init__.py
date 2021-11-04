import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8582"
version_tuple = (0, 0, 8582)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8582")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8470"
data_version_tuple = (0, 0, 8470)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8470")
except ImportError:
    pass
data_git_hash = "4607d1c63afab73e716671f129c32bf98e69ff9a"
data_git_describe = "v0.0-8470-g4607d1c63"
data_git_msg = """\
commit 4607d1c63afab73e716671f129c32bf98e69ff9a
Author: Weicai Yang <weicai@google.com>
Date:   Tue Nov 2 16:31:23 2021 -0700

    [dv] Fix rstmgr intg test
    
    1. Added super.post_apply_reset as Cindy did in #8997
    2. Added associated err_code for intg error in cfg
    
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
