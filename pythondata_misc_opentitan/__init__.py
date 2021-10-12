import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8221"
version_tuple = (0, 0, 8221)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8221")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8109"
data_version_tuple = (0, 0, 8109)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8109")
except ImportError:
    pass
data_git_hash = "ea0407514aef8b9fb6efe8b16330b32c6df05372"
data_git_describe = "v0.0-8109-gea0407514"
data_git_msg = """\
commit ea0407514aef8b9fb6efe8b16330b32c6df05372
Author: Michael Schaffner <msf@google.com>
Date:   Mon Oct 11 11:22:00 2021 -0700

    [lc_ctrl] Convert mutex into mubi8 type
    
    Signed-off-by: Michael Schaffner <msf@google.com>

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
