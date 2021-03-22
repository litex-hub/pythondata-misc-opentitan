import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5514"
version_tuple = (0, 0, 5514)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5514")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5419"
data_version_tuple = (0, 0, 5419)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5419")
except ImportError:
    pass
data_git_hash = "1cbcce42ed2a2583eccb96c64df78468f40b0c40"
data_git_describe = "v0.0-5419-g1cbcce42e"
data_git_msg = """\
commit 1cbcce42ed2a2583eccb96c64df78468f40b0c40
Author: Cindy Chen <chencindy@google.com>
Date:   Thu Mar 18 19:38:03 2021 -0700

    [dv/otp_ctrl] test_access sequence
    
    This PR adds a test_access sequence to access otp_ctrl's test_access.
    For open-sourced testbench, this is a dummy check to ensure the
    connection is correct. The real output should be checked in
    proprietary env.
    
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
