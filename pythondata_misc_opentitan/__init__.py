import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14482"
version_tuple = (0, 0, 14482)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14482")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14340"
data_version_tuple = (0, 0, 14340)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14340")
except ImportError:
    pass
data_git_hash = "c9f6c6e93c8f10904df3bf253a3206753e26b9be"
data_git_describe = "v0.0-14340-gc9f6c6e93c"
data_git_msg = """\
commit c9f6c6e93c8f10904df3bf253a3206753e26b9be
Author: Michael Schaffner <msf@google.com>
Date:   Fri Sep 23 16:30:34 2022 +0200

    [mubi/lc] Relax transient SVA checks
    
    Fix #14925.
    
    Signed-off-by: Michael Schaffner <msf@google.com>

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
