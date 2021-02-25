import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5140"
version_tuple = (0, 0, 5140)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5140")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5049"
data_version_tuple = (0, 0, 5049)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5049")
except ImportError:
    pass
data_git_hash = "6c46103d956da7583c77440009501a1974d24927"
data_git_describe = "v0.0-5049-g6c46103d9"
data_git_msg = """\
commit 6c46103d956da7583c77440009501a1974d24927
Author: Cindy Chen <chencindy@google.com>
Date:   Tue Feb 23 11:38:03 2021 -0800

    [dv/otp_ctrl] non-sticky interrupt check
    
    This PR enables interrupt check in scb according to the updates in PR
    To avoid scb doing cycle accurate prediction, this PR also adds a delay
    if lc_prog error is found, then we will wait one clock cycle to check
    interrupts.
    
    Signed-off-by: Cindy Chen <chencindy@google.com>

"""

# Tool version info
tool_version_str = "0.0.post91"
tool_version_tuple = (0, 0, 91)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post91")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
