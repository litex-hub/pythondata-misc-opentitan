import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14225"
version_tuple = (0, 0, 14225)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14225")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14083"
data_version_tuple = (0, 0, 14083)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14083")
except ImportError:
    pass
data_git_hash = "7d941705c42a8bec8f360f5468dd08e28a07d740"
data_git_describe = "v0.0-14083-g7d941705c4"
data_git_msg = """\
commit 7d941705c42a8bec8f360f5468dd08e28a07d740
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Wed Sep 14 12:43:56 2022 -0700

    [dv/kmac] support entropy request reg
    
    This PR supports entropy_req reg to request entropy.
    
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
