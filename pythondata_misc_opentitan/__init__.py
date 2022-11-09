import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15353"
version_tuple = (0, 0, 15353)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15353")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post15211"
data_version_tuple = (0, 0, 15211)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post15211")
except ImportError:
    pass
data_git_hash = "a0da3fcc689d6d26859858e84d33ae32f32cd756"
data_git_describe = "v0.0-15211-ga0da3fcc68"
data_git_msg = """\
commit a0da3fcc689d6d26859858e84d33ae32f32cd756
Author: Miles Dai <milesdai@google.com>
Date:   Tue Nov 8 15:43:58 2022 -0500

    [otp] Create a STANDARD_OTP_OVERLAYS list for E2E testing
    
    Signed-off-by: Miles Dai <milesdai@google.com>
    Signed-off-by: Alphan Ulusoy <alphan@google.com>

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
