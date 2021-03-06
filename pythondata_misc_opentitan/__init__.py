import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5267"
version_tuple = (0, 0, 5267)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5267")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5172"
data_version_tuple = (0, 0, 5172)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5172")
except ImportError:
    pass
data_git_hash = "3508ebd7f522ac4caba28327a874b66af7ca5c0c"
data_git_describe = "v0.0-5172-g3508ebd7f"
data_git_msg = """\
commit 3508ebd7f522ac4caba28327a874b66af7ca5c0c
Author: Weicai Yang <weicai@google.com>
Date:   Fri Mar 5 14:07:27 2021 -0800

    [dv] only read mem which is written with full word data
    
    workaround for #5262
    Also change num_access to only count read access
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
