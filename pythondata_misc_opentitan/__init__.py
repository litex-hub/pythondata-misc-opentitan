import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5503"
version_tuple = (0, 0, 5503)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5503")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5408"
data_version_tuple = (0, 0, 5408)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5408")
except ImportError:
    pass
data_git_hash = "a560a2cedf0b77c94648076578e9954bd8847c00"
data_git_describe = "v0.0-5408-ga560a2ced"
data_git_msg = """\
commit a560a2cedf0b77c94648076578e9954bd8847c00
Author: Weicai Yang <weicai@google.com>
Date:   Fri Mar 19 14:49:38 2021 -0700

    [dv] Fix mem test hang
    
    Recently I updated to count N access of read for mem test, but read only
    occurs after at least a mem address is written. If reset occurs before any write,
    it will forever sending read access, which creates a deadloop
    
    Signed-off-by: Weicai Yang <weicai@google.com>

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
