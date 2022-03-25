import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11119"
version_tuple = (0, 0, 11119)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11119")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10993"
data_version_tuple = (0, 0, 10993)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10993")
except ImportError:
    pass
data_git_hash = "0f5611182ec6c4bd127b72fe032d24bcd809a15e"
data_git_describe = "v0.0-10993-g0f5611182"
data_git_msg = """\
commit 0f5611182ec6c4bd127b72fe032d24bcd809a15e
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Tue Mar 22 16:24:12 2022 -0700

    [dv/otp] Probe internal mubi interface
    
    Force internal mubi types to values that are not true or false.
    Make sure design locked the part accesses.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post126"
tool_version_tuple = (0, 0, 126)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post126")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
