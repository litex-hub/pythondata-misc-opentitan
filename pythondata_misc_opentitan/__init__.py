import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10629"
version_tuple = (0, 0, 10629)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10629")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10503"
data_version_tuple = (0, 0, 10503)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10503")
except ImportError:
    pass
data_git_hash = "9bd33908d2e9fda9977257151eaa3e048566797e"
data_git_describe = "v0.0-10503-g9bd33908d"
data_git_msg = """\
commit 9bd33908d2e9fda9977257151eaa3e048566797e
Author: Timothy Chen <timothytim@google.com>
Date:   Fri Feb 25 13:46:26 2022 -0800

    [rstmgr] unr related clean-up
    
    - fixes #11121
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
