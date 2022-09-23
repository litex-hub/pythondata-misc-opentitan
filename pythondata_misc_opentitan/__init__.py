import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14390"
version_tuple = (0, 0, 14390)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14390")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14248"
data_version_tuple = (0, 0, 14248)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14248")
except ImportError:
    pass
data_git_hash = "be4132c4f87303e9bb83c81e6fc38b40a1716132"
data_git_describe = "v0.0-14248-gbe4132c4f8"
data_git_msg = """\
commit be4132c4f87303e9bb83c81e6fc38b40a1716132
Author: Timothy Chen <timothytim@google.com>
Date:   Thu Sep 22 13:29:39 2022 -0700

    [i2c/dv] update scoreboard handling for chained reads
    
    - fixes #14990
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
