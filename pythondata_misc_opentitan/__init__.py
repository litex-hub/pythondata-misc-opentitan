import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5017"
version_tuple = (0, 0, 5017)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5017")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post4926"
data_version_tuple = (0, 0, 4926)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post4926")
except ImportError:
    pass
data_git_hash = "0e451f07798d7fc09a94bf95565158fffd539a34"
data_git_describe = "v0.0-4926-g0e451f077"
data_git_msg = """\
commit 0e451f07798d7fc09a94bf95565158fffd539a34
Author: Cindy Chen <chencindy@google.com>
Date:   Fri Feb 12 19:02:09 2021 -0800

    [dv/otp_ctrl] Add lc_prog interface to otp_ctrl_if
    
    This PR adds lc_prog interface to otp_ctrl_if in order to:
    1. Add assertions to ensure if lc_program request is set, either
    otp_idle_o will be reset to 0, or lc_prog has error
    2. Add a clock cycle delay to lc_prog_req for later use in scb
    
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
