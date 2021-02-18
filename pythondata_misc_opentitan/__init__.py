import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5037"
version_tuple = (0, 0, 5037)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5037")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post4946"
data_version_tuple = (0, 0, 4946)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post4946")
except ImportError:
    pass
data_git_hash = "52a50550a38178ed255942f88b0cb437d7e6ab80"
data_git_describe = "v0.0-4946-g52a50550a"
data_git_msg = """\
commit 52a50550a38178ed255942f88b0cb437d7e6ab80
Author: Weicai Yang <weicai@google.com>
Date:   Tue Feb 16 10:59:44 2021 -0800

    [keymgr/dv] update scb to remove non-block assignment
    
    address #5159
    
    Signed-off-by: Weicai Yang <weicai@google.com>

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
