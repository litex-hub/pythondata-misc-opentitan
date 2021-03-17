import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5444"
version_tuple = (0, 0, 5444)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5444")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5349"
data_version_tuple = (0, 0, 5349)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5349")
except ImportError:
    pass
data_git_hash = "a4e2d7f2e1d7d76455558187a7792fa9176f6ee4"
data_git_describe = "v0.0-5349-ga4e2d7f2e"
data_git_msg = """\
commit a4e2d7f2e1d7d76455558187a7792fa9176f6ee4
Author: Timothy Chen <timothytim@google.com>
Date:   Thu Mar 11 22:34:21 2021 -0800

    [keymgr] Actually increase salt / sw binding sizes
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
