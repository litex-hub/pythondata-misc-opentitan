import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5259"
version_tuple = (0, 0, 5259)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5259")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5167"
data_version_tuple = (0, 0, 5167)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5167")
except ImportError:
    pass
data_git_hash = "a63640ec01fbac7a8c43d75ca461faf97675654f"
data_git_describe = "v0.0-5167-ga63640ec0"
data_git_msg = """\
commit a63640ec01fbac7a8c43d75ca461faf97675654f
Author: Tung Hoang <hoang.tung@wdc.com>
Date:   Sun Feb 28 15:20:22 2021 -0800

    [i2c, dv] Update i2c_testplan to include tests required to verify i2c target rtl
    
    Signed-off-by: Tung Hoang <hoang.tung@wdc.com>

"""

# Tool version info
tool_version_str = "0.0.post92"
tool_version_tuple = (0, 0, 92)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post92")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
