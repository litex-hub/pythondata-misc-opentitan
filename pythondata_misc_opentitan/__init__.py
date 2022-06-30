import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12899"
version_tuple = (0, 0, 12899)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12899")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12757"
data_version_tuple = (0, 0, 12757)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12757")
except ImportError:
    pass
data_git_hash = "54329ed9604fd4ec37cbeaba8c48a17c533d3c2e"
data_git_describe = "v0.0-12757-g54329ed960"
data_git_msg = """\
commit 54329ed9604fd4ec37cbeaba8c48a17c533d3c2e
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Thu Jun 30 12:10:28 2022 -0700

    [dv/pwm] Two small fixes
    
    Fix two TODOs in issue #13476:
    1). Fix max outstanding access coverage
    2). Fix regression unmapped memory tests.
    
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
