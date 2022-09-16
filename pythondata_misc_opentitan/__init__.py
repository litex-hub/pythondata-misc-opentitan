import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14258"
version_tuple = (0, 0, 14258)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14258")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14116"
data_version_tuple = (0, 0, 14116)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14116")
except ImportError:
    pass
data_git_hash = "80e3a6cb0ab922adb51cf7ccabeebd64394d74e2"
data_git_describe = "v0.0-14116-g80e3a6cb0a"
data_git_msg = """\
commit 80e3a6cb0ab922adb51cf7ccabeebd64394d74e2
Author: Jon Flatley <jflat@google.com>
Date:   Wed Sep 14 12:02:23 2022 -0400

    [opentitanlib] Add alert_handler_reg tests
    
    Signed-off-by: Jon Flatley <jflat@google.com>

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
