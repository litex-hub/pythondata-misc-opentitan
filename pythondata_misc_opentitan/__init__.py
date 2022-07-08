import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12980"
version_tuple = (0, 0, 12980)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12980")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12838"
data_version_tuple = (0, 0, 12838)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12838")
except ImportError:
    pass
data_git_hash = "03a7e9bc90c991374be15a59ea561004e1e55212"
data_git_describe = "v0.0-12838-g03a7e9bc90"
data_git_msg = """\
commit 03a7e9bc90c991374be15a59ea561004e1e55212
Author: Cindy Chen <chencindy@google.com>
Date:   Fri Jul 8 10:23:09 2022 -0700

    [dv/otp_ctrl] Move stress_all sequence to a separate function
    
    This PR moves the stress_all sequence to a separate function to make it
    easier to override in close source env.
    
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
