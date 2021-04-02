import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5697"
version_tuple = (0, 0, 5697)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5697")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5602"
data_version_tuple = (0, 0, 5602)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5602")
except ImportError:
    pass
data_git_hash = "e96574134f987a91f05cd2c6e48782796f4101fd"
data_git_describe = "v0.0-5602-ge96574134"
data_git_msg = """\
commit e96574134f987a91f05cd2c6e48782796f4101fd
Author: Michael Schaffner <msf@opentitan.org>
Date:   Thu Apr 1 23:14:46 2021 -0700

    [top/arty] Remove artys7 target
    
    This deprecates and removes the artys7 target since it
    has become out of sync and it will not be maintained anymore
    going forward.
    
    Signed-off-by: Michael Schaffner <msf@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
