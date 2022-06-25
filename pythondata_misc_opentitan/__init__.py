import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12851"
version_tuple = (0, 0, 12851)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12851")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12709"
data_version_tuple = (0, 0, 12709)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12709")
except ImportError:
    pass
data_git_hash = "e80d18267b548cb2e803fa57abde1e0a71872d56"
data_git_describe = "v0.0-12709-ge80d18267b"
data_git_msg = """\
commit e80d18267b548cb2e803fa57abde1e0a71872d56
Author: Cindy Chen <chencindy@google.com>
Date:   Fri Jun 24 17:39:03 2022 -0700

    [formal/conn] Fix bbox command
    
    Fix script issue that causes the weekly connectivity test to fail.
    
    Signed-off-by: Cindy Chen <chencindy@google.com>

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
