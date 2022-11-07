import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15286"
version_tuple = (0, 0, 15286)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15286")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post15144"
data_version_tuple = (0, 0, 15144)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post15144")
except ImportError:
    pass
data_git_hash = "b0e0bf8b8a3429fdc7e6dbce1eb7f216fa2c0b87"
data_git_describe = "v0.0-15144-gb0e0bf8b8a"
data_git_msg = """\
commit b0e0bf8b8a3429fdc7e6dbce1eb7f216fa2c0b87
Author: Jon Flatley <jflat@google.com>
Date:   Tue Nov 1 16:24:20 2022 -0400

    [bazel] Add rule for OTP alert_hander digests
    
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
