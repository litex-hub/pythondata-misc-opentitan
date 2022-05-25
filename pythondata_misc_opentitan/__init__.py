import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12313"
version_tuple = (0, 0, 12313)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12313")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12182"
data_version_tuple = (0, 0, 12182)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12182")
except ImportError:
    pass
data_git_hash = "2d87fb6fbdab8ea4186cb4350e95f415ecf2d321"
data_git_describe = "v0.0-12182-g2d87fb6fb"
data_git_msg = """\
commit 2d87fb6fbdab8ea4186cb4350e95f415ecf2d321
Author: Michael Schaffner <msf@opentitan.org>
Date:   Mon May 9 18:16:35 2022 -0700

    [regtool] Extend UVM backend to support alias definitions
    
    Signed-off-by: Michael Schaffner <msf@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post131"
tool_version_tuple = (0, 0, 131)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post131")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
