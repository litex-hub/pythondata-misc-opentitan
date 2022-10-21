import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14887"
version_tuple = (0, 0, 14887)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14887")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14745"
data_version_tuple = (0, 0, 14745)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14745")
except ImportError:
    pass
data_git_hash = "b64b6c0a8b1d17ff2d5b318bfde2346d61d2dc35"
data_git_describe = "v0.0-14745-gb64b6c0a8b"
data_git_msg = """\
commit b64b6c0a8b1d17ff2d5b318bfde2346d61d2dc35
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Fri Oct 21 12:15:48 2022 -0700

    [dv/xcelium] Add back prim_tl_access test
    
    Add back prim_tl_access test in chip level xcelium as the regression
    error is fixed.
    
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
