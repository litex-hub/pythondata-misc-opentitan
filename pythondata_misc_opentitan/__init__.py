import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12656"
version_tuple = (0, 0, 12656)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12656")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12514"
data_version_tuple = (0, 0, 12514)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12514")
except ImportError:
    pass
data_git_hash = "2cfcc5e86dda2ce34ffb9c16d4359d9364a85c47"
data_git_describe = "v0.0-12514-g2cfcc5e86"
data_git_msg = """\
commit 2cfcc5e86dda2ce34ffb9c16d4359d9364a85c47
Author: Prajwala Puttappa <prajwalaputtappa@lowrisc.org>
Date:   Tue May 31 12:00:54 2022 +0100

    [otbn, dv] Adds checks for GLOBAL_ESC and LOCAL_ESC
    
    This commit adds assertions for global and local escalation
    countermeasure.
    
    Signed-off-by: Prajwala Puttappa <prajwalaputtappa@lowrisc.org>

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
