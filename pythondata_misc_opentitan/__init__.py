import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5841"
version_tuple = (0, 0, 5841)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5841")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5746"
data_version_tuple = (0, 0, 5746)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5746")
except ImportError:
    pass
data_git_hash = "fa3103653c863c1bd43b71cb69852d31c03f3bcf"
data_git_describe = "v0.0-5746-gfa3103653"
data_git_msg = """\
commit fa3103653c863c1bd43b71cb69852d31c03f3bcf
Author: Cindy Chen <chencindy@google.com>
Date:   Fri Apr 9 10:33:38 2021 -0700

    [dv/otp_ctrl] Add more sequence to stress_all test
    
    This PR adds all sequences to stress_all test.
    And a few updates:
    1. SCB when read back secret, needs to descramble it first
    2. Change post_start from apply_reset to dut_init so it can be used in
    stress_all sequence
    3. Force to have a reset at the end of each sequence.
    
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
