import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13181"
version_tuple = (0, 0, 13181)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13181")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13039"
data_version_tuple = (0, 0, 13039)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13039")
except ImportError:
    pass
data_git_hash = "9fac57c085f9d5910d758a983b7b78087274c96d"
data_git_describe = "v0.0-13039-g9fac57c085"
data_git_msg = """\
commit 9fac57c085f9d5910d758a983b7b78087274c96d
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Tue Jul 19 11:02:15 2022 -0700

    [dv/kmac] improve app interface sequence
    
    Remove the constraint to configure kmac cfg_shadow register hash_mode
    field. Kmac should be able to select the correct mode when using the app
    interface.
    
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
