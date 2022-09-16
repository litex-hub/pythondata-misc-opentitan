import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14265"
version_tuple = (0, 0, 14265)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14265")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14123"
data_version_tuple = (0, 0, 14123)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14123")
except ImportError:
    pass
data_git_hash = "6ea75e8c34dcb115edc51747255ff386ab7df2a1"
data_git_describe = "v0.0-14123-g6ea75e8c34"
data_git_msg = """\
commit 6ea75e8c34dcb115edc51747255ff386ab7df2a1
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Thu Sep 15 10:31:37 2022 -0700

    [dv/kmac] Add scb checkings for entropy
    
    Upon entropy request or hash_cnt reaches threshold, we expect to see an
    entropy fetch.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post142"
tool_version_tuple = (0, 0, 142)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post142")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
