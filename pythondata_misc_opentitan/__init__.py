import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8919"
version_tuple = (0, 0, 8919)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8919")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8807"
data_version_tuple = (0, 0, 8807)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8807")
except ImportError:
    pass
data_git_hash = "bca0862cc61c3f7f50782d76b9f16809cb2e0d74"
data_git_describe = "v0.0-8807-gbca0862cc"
data_git_msg = """\
commit bca0862cc61c3f7f50782d76b9f16809cb2e0d74
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Tue Nov 30 14:17:52 2021 -0800

    [dv/otp_ctrl] Fix otp regression failure
    
    Fix otp_ctrl's regression failure on otp_init_test.
    We inject ECC uncorrectable error on vendor_test_partition.
    In design, this ECC uncorrectable error won't trigger alert.
    This PR aligns the behavior on DV side.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
