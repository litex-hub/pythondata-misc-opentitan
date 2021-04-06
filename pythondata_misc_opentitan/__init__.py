import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5719"
version_tuple = (0, 0, 5719)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5719")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5624"
data_version_tuple = (0, 0, 5624)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5624")
except ImportError:
    pass
data_git_hash = "070d956d1d5191074df7e8815f300e9ff0267adc"
data_git_describe = "v0.0-5624-g070d956d1"
data_git_msg = """\
commit 070d956d1d5191074df7e8815f300e9ff0267adc
Author: Cindy Chen <chencindy@google.com>
Date:   Mon Apr 5 11:50:29 2021 -0700

    [dv/otp_ctrl] Add macro failure to otp init test
    
    The otp_init_fail can also be triggered by ECC failure.
    ECC correctable failure will pass OTP init with an error.
    ECC uncorrectable failure will fail OTP init with an alert.
    
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
