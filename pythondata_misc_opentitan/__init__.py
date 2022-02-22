import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10473"
version_tuple = (0, 0, 10473)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10473")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10347"
data_version_tuple = (0, 0, 10347)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10347")
except ImportError:
    pass
data_git_hash = "7d1bf1e3cb81ac75ea0a966d0178064b1b6d2c12"
data_git_describe = "v0.0-10347-g7d1bf1e3c"
data_git_msg = """\
commit 7d1bf1e3cb81ac75ea0a966d0178064b1b6d2c12
Author: Weicai Yang <weicai@google.com>
Date:   Thu Feb 17 15:13:47 2022 -0800

    [sramd/dv] Enable sec_cm test for sram
    
    Add additional checks
     - Check alert and `status.init_error` is set.
     -  After injecting faults, reading any address should return 0. #10909
    
    Signed-off-by: Weicai Yang <weicai@google.com>

"""

# Tool version info
tool_version_str = "0.0.post126"
tool_version_tuple = (0, 0, 126)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post126")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
