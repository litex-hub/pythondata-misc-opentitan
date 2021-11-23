import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8846"
version_tuple = (0, 0, 8846)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8846")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8734"
data_version_tuple = (0, 0, 8734)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8734")
except ImportError:
    pass
data_git_hash = "36030de58ba1c3f7f9afff96de15ff5723003ef7"
data_git_describe = "v0.0-8734-g36030de58"
data_git_msg = """\
commit 36030de58ba1c3f7f9afff96de15ff5723003ef7
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Tue Nov 23 11:35:05 2021 -0800

    [dv/aon_timer] rever temp fix regression error
    
    Reverts #6823
    
    Per Tom's comment on issue #6821, we are going to revert this temp fix and see if we can reproduce the assertion error.
    
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
