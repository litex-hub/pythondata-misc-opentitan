import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9841"
version_tuple = (0, 0, 9841)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9841")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9719"
data_version_tuple = (0, 0, 9719)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9719")
except ImportError:
    pass
data_git_hash = "48f64de05bb50cb37bf2f69a2d33d86fa3de0ddb"
data_git_describe = "v0.0-9719-g48f64de05"
data_git_msg = """\
commit 48f64de05bb50cb37bf2f69a2d33d86fa3de0ddb
Author: Jon Flatley <jflat@google.com>
Date:   Thu Jan 6 09:53:40 2022 -0500

    [opentitanlib] Add OTP hex file generation.
    
    Signed-off-by: Jon Flatley <jflat@google.com>

"""

# Tool version info
tool_version_str = "0.0.post122"
tool_version_tuple = (0, 0, 122)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post122")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
