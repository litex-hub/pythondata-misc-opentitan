import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13160"
version_tuple = (0, 0, 13160)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13160")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13018"
data_version_tuple = (0, 0, 13018)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13018")
except ImportError:
    pass
data_git_hash = "e9e192a73efc0562cb31daa19e3e58e9a92cc7d8"
data_git_describe = "v0.0-13018-ge9e192a73e"
data_git_msg = """\
commit e9e192a73efc0562cb31daa19e3e58e9a92cc7d8
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Thu Jul 14 16:16:39 2022 -0700

    [dv/kmac] Collecting coverage for app interface and sideload
    
    Update fcov to collect coverage where sideload is set to 0, but kmac
    keymgr app interface request is sent.
    
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
