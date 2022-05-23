import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12286"
version_tuple = (0, 0, 12286)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12286")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12158"
data_version_tuple = (0, 0, 12158)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12158")
except ImportError:
    pass
data_git_hash = "b42dbc2d004358a7036ab4eee2c02b79e091bead"
data_git_describe = "v0.0-12158-gb42dbc2d0"
data_git_msg = """\
commit b42dbc2d004358a7036ab4eee2c02b79e091bead
Author: Timothy Trippel <ttrippel@google.com>
Date:   Tue May 17 17:02:42 2022 -0700

    [bazel,dvsim] update dvsim.py to use Bazel to build SW
    
    This fixes #11563 by updating dvsim.py, and the chip-level testbench, to
    build SW artifacts with Bazel (instead of meson).
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

"""

# Tool version info
tool_version_str = "0.0.post128"
tool_version_tuple = (0, 0, 128)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post128")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
