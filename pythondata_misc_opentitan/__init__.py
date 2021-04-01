import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5673"
version_tuple = (0, 0, 5673)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5673")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5578"
data_version_tuple = (0, 0, 5578)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5578")
except ImportError:
    pass
data_git_hash = "4653df9a423b5c13ea33da5bd0d50a756aee9667"
data_git_describe = "v0.0-5578-g4653df9a4"
data_git_msg = """\
commit 4653df9a423b5c13ea33da5bd0d50a756aee9667
Author: Cindy Chen <chencindy@google.com>
Date:   Thu Apr 1 11:21:27 2021 -0700

    [fpv] Fix connectivity script folder name
    
    This PR fixes connectivity script folder name.
    Also small fix on auto-exit in gui mode.
    
    Signed-off-by: Cindy Chen <chencindy@google.com>

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
