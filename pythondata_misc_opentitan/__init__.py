import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8949"
version_tuple = (0, 0, 8949)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8949")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8837"
data_version_tuple = (0, 0, 8837)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8837")
except ImportError:
    pass
data_git_hash = "9aeaac797a34043b2a04424f3128d3dc02e75c4c"
data_git_describe = "v0.0-8837-g9aeaac797"
data_git_msg = """\
commit 9aeaac797a34043b2a04424f3128d3dc02e75c4c
Author: Michael Schaffner <msf@opentitan.org>
Date:   Wed Dec 1 16:58:58 2021 -0800

    [alert_handler] Minor lint fix
    
    Signed-off-by: Michael Schaffner <msf@opentitan.org>

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
