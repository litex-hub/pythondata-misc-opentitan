import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5821"
version_tuple = (0, 0, 5821)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5821")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5726"
data_version_tuple = (0, 0, 5726)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5726")
except ImportError:
    pass
data_git_hash = "085e2fbc092b63104842f1fec0541cb48e795125"
data_git_describe = "v0.0-5726-g085e2fbc0"
data_git_msg = """\
commit 085e2fbc092b63104842f1fec0541cb48e795125
Author: Weicai Yang <weicai@google.com>
Date:   Fri Apr 9 18:03:59 2021 -0700

    [dv] Fix tl_error failure
    
    Thanks @cindychip for finding this failure
    
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
