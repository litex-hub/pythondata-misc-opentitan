import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13105"
version_tuple = (0, 0, 13105)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13105")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12963"
data_version_tuple = (0, 0, 12963)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12963")
except ImportError:
    pass
data_git_hash = "4c81f2388c931e88ee17f53353c2bf566637d9dd"
data_git_describe = "v0.0-12963-g4c81f2388c"
data_git_msg = """\
commit 4c81f2388c931e88ee17f53353c2bf566637d9dd
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Thu Jul 14 15:18:24 2022 -0700

    [dv/cip_base] Add checking in stress_all_with_rand_reset seq
    
    This PR adds a checking after reset is issued to check if there are
    still any outstanding csr items. If so, the following csr checks or
    sequences are unlikely to pass due to the hanging outstanding item.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post142"
tool_version_tuple = (0, 0, 142)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post142")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
