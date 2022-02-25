import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10536"
version_tuple = (0, 0, 10536)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10536")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10410"
data_version_tuple = (0, 0, 10410)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10410")
except ImportError:
    pass
data_git_hash = "27b4f9065fdfb60079b0ad0ddb26a81020d5593e"
data_git_describe = "v0.0-10410-g27b4f9065"
data_git_msg = """\
commit 27b4f9065fdfb60079b0ad0ddb26a81020d5593e
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Thu Feb 24 13:47:42 2022 -0800

    [dv/otp] fix memory access error
    
    This PR fixes OTP memory access error. OTP has to override
    `is_tl_mem_access_allowed` because in two other cases we will see a
    d_error in memory access:
    1). Memory read access is locked because the `read_lock` register is
      set.
    2). Memory read access is locked because read has ECC uncorrectble
      error.
    To make sure these two errors are reflected in `exp_d_error`, I added
    another output `customized_err`
    
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
