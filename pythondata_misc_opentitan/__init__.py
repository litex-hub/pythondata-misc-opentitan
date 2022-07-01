import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12911"
version_tuple = (0, 0, 12911)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12911")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12769"
data_version_tuple = (0, 0, 12769)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12769")
except ImportError:
    pass
data_git_hash = "cbb1d8754089353268897cedd3416fc590f6f1d9"
data_git_describe = "v0.0-12769-gcbb1d87540"
data_git_msg = """\
commit cbb1d8754089353268897cedd3416fc590f6f1d9
Author: Steve Nelson <steve.nelson@wdc.com>
Date:   Tue Jun 28 08:07:31 2022 -0700

    [tools/dv] Modify common.ccf file for proper expression coverage
    
    Signed-off-by: Steve Nelson <steve.nelson@wdc.com>

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
