import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15162"
version_tuple = (0, 0, 15162)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15162")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post15020"
data_version_tuple = (0, 0, 15020)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post15020")
except ImportError:
    pass
data_git_hash = "6c6fb3069aaa84d786a65d9fc2b03c0a46f7c53f"
data_git_describe = "v0.0-15020-g6c6fb3069a"
data_git_msg = """\
commit 6c6fb3069aaa84d786a65d9fc2b03c0a46f7c53f
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Tue Nov 1 23:15:34 2022 -0700

    [dv/edn] Add an assertion to check EDN data stable
    
    This PR adds an assertion in EDN design code to ensure that EDN output
    data stays stable (once valid), until next EDN request.
    
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
