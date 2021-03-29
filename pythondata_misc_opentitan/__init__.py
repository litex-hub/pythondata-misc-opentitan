import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5618"
version_tuple = (0, 0, 5618)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5618")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5523"
data_version_tuple = (0, 0, 5523)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5523")
except ImportError:
    pass
data_git_hash = "e051f4c7c73ee5de7e3f8cd0ddb40a6368b2cb7c"
data_git_describe = "v0.0-5523-ge051f4c7c"
data_git_msg = """\
commit e051f4c7c73ee5de7e3f8cd0ddb40a6368b2cb7c
Author: Cindy Chen <chencindy@google.com>
Date:   Tue Mar 23 17:08:15 2021 -0700

    [formal/conn] Support connectivity test locally
    
    This PR adds basic configs to run connecivity test locally.
    This is the first step to support running connecivity test using dvsim.
    The reason we are adding this local option is because we can temporarily
    using this script to run with GUI.
    
    Next PR will support running the connectivity test on dvsim.
    
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
