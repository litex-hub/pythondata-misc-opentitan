import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5619"
version_tuple = (0, 0, 5619)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5619")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5524"
data_version_tuple = (0, 0, 5524)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5524")
except ImportError:
    pass
data_git_hash = "3800c6dc1f36b4134bc2b3a9eb0a90889e980f9c"
data_git_describe = "v0.0-5524-g3800c6dc1"
data_git_msg = """\
commit 3800c6dc1f36b4134bc2b3a9eb0a90889e980f9c
Author: Cindy Chen <chencindy@google.com>
Date:   Mon Mar 29 15:00:04 2021 -0700

    [dv/otp] fix number of edn required for sram
    
    The num of EDN required for SRAM should be 12 instead of 10.
    
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
