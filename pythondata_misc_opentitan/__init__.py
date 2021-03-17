import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5415"
version_tuple = (0, 0, 5415)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5415")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5320"
data_version_tuple = (0, 0, 5320)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5320")
except ImportError:
    pass
data_git_hash = "3c32208530d35cd7ee4eb620fbd9ba7fbc2639b7"
data_git_describe = "v0.0-5320-g3c3220853"
data_git_msg = """\
commit 3c32208530d35cd7ee4eb620fbd9ba7fbc2639b7
Author: Cindy Chen <chencindy@google.com>
Date:   Tue Mar 16 15:47:44 2021 -0700

    [dv/common] Fix regression warnings
    
    This PR fixes two warnings in regression:
    1. Add a void cast when using predict function
    2. Correct apply_reset input name in otp_ctrl dv
    
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
