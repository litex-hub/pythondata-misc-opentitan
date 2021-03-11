import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5350"
version_tuple = (0, 0, 5350)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5350")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5255"
data_version_tuple = (0, 0, 5255)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5255")
except ImportError:
    pass
data_git_hash = "ee80c35e1cfb3a175bee2d60b4d2691176cf2e2d"
data_git_describe = "v0.0-5255-gee80c35e1"
data_git_msg = """\
commit ee80c35e1cfb3a175bee2d60b4d2691176cf2e2d
Author: Cindy Chen <chencindy@google.com>
Date:   Tue Mar 9 15:43:23 2021 -0800

    [dv/otp_ctrl] support err_code checking
    
    This PR adds support for err_code register checking
    
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
