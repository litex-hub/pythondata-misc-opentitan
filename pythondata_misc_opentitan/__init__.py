import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13184"
version_tuple = (0, 0, 13184)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13184")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13042"
data_version_tuple = (0, 0, 13042)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13042")
except ImportError:
    pass
data_git_hash = "12c9d0b5924f0403b3b349e963f36c1796676a0d"
data_git_describe = "v0.0-13042-g12c9d0b592"
data_git_msg = """\
commit 12c9d0b5924f0403b3b349e963f36c1796676a0d
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Tue Jul 19 16:44:11 2022 -0700

    [dv/entropy_src] temp disable entropy_rng_test
    
    This PR temp disables entropy_rng_test with issue #13741 filed for
    tracking.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

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
