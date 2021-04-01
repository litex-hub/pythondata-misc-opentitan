import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5659"
version_tuple = (0, 0, 5659)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5659")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5564"
data_version_tuple = (0, 0, 5564)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5564")
except ImportError:
    pass
data_git_hash = "51761ca5e5f714e621d3ca58902e3e4512c387a7"
data_git_describe = "v0.0-5564-g51761ca5e"
data_git_msg = """\
commit 51761ca5e5f714e621d3ca58902e3e4512c387a7
Author: Cindy Chen <chencindy@google.com>
Date:   Tue Mar 30 17:39:19 2021 -0700

    [otp_ctrl/rtl] Fix otp_ctrl consistency check false alert
    
    Solve issue #5870
    
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
