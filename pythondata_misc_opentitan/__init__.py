import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8842"
version_tuple = (0, 0, 8842)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8842")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8730"
data_version_tuple = (0, 0, 8730)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8730")
except ImportError:
    pass
data_git_hash = "1b1ac41011c16cfe29aef49e47ac3ea22c808e36"
data_git_describe = "v0.0-8730-g1b1ac4101"
data_git_msg = """\
commit 1b1ac41011c16cfe29aef49e47ac3ea22c808e36
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Mon Nov 22 17:20:48 2021 -0800

    [dv/chip_lc_trans] Fix small typos in lc_transition_test
    
    This PR fixes two small typos:
    1). The test_exit_token is in secret0 not secret9 partition.
    2). Avoid extra apply_reset and otp_backdoor_write.
    
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
