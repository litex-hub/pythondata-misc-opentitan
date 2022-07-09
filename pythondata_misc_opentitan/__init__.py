import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13006"
version_tuple = (0, 0, 13006)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13006")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12864"
data_version_tuple = (0, 0, 12864)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12864")
except ImportError:
    pass
data_git_hash = "aabcd2c3063cf0d093df10d423b4a6568d90b8de"
data_git_describe = "v0.0-12864-gaabcd2c306"
data_git_msg = """\
commit aabcd2c3063cf0d093df10d423b4a6568d90b8de
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Fri Jul 8 15:52:46 2022 -0700

    [formal/fpv] support onehot register check [Part1]
    
    This PR supports onehot register check by blackboxing the
    prim_onehot_check module, so that the err_o will be triggered randomly,
    and we will check if alert is firing.
    
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
