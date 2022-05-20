import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12266"
version_tuple = (0, 0, 12266)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12266")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12138"
data_version_tuple = (0, 0, 12138)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12138")
except ImportError:
    pass
data_git_hash = "a5093e820b4aeca7a6985430434356334d220f6d"
data_git_describe = "v0.0-12138-ga5093e820"
data_git_msg = """\
commit a5093e820b4aeca7a6985430434356334d220f6d
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Fri May 20 10:22:56 2022 -0700

    [dv/lc_ctrl] temp remove lc_ctrl stress_all_with_rand_reset test
    
    This PR temp removes a test to unblock nightly regression hanging issue.
    An issue is filed to re-enable this test: #12807
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post128"
tool_version_tuple = (0, 0, 128)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post128")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
