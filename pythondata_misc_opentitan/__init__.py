import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8711"
version_tuple = (0, 0, 8711)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8711")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8599"
data_version_tuple = (0, 0, 8599)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8599")
except ImportError:
    pass
data_git_hash = "12810ea9f4a1a9cc5b1d0c1b9fce7ef4d8df4bef"
data_git_describe = "v0.0-8599-g12810ea9f"
data_git_msg = """\
commit 12810ea9f4a1a9cc5b1d0c1b9fce7ef4d8df4bef
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Thu Nov 11 16:56:37 2021 -0800

    [dv/alert] Fix alert init
    
    Before alert_init finish, there might be another reset happen.
    Previous code only handled the monitor part, this PR fixes the driver
    part as well.
    This PR also create a separate thread for alert_init from reset_thread.
    
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
