import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11010"
version_tuple = (0, 0, 11010)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11010")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10884"
data_version_tuple = (0, 0, 10884)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10884")
except ImportError:
    pass
data_git_hash = "e7306345946a94e958735f1c307bb482b45cd135"
data_git_describe = "v0.0-10884-ge73063459"
data_git_msg = """\
commit e7306345946a94e958735f1c307bb482b45cd135
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Fri Mar 18 15:34:34 2022 -0700

    [dv/otp] Add assertion for otp_alert_o
    
    This PR adds an assertion for open source OTP output otp_alert_o.
    This should be tied to 2'b01 in open source.
    This PR also fixes some small spacing syntax.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

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
