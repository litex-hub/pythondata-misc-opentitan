import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14496"
version_tuple = (0, 0, 14496)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14496")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14354"
data_version_tuple = (0, 0, 14354)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14354")
except ImportError:
    pass
data_git_hash = "53135de258fd00475d3004d33b2a593558ba05d9"
data_git_describe = "v0.0-14354-g53135de258"
data_git_msg = """\
commit 53135de258fd00475d3004d33b2a593558ba05d9
Author: Eli Kim <eli@opentitan.org>
Date:   Wed Sep 28 17:10:22 2022 -0700

    feat(prim): prim_rst_sync
    
    This commit adds a reset synchronizer for async resets.
    
    Signed-off-by: Eli Kim <eli@opentitan.org>

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
