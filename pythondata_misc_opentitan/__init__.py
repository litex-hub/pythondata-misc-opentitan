import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11366"
version_tuple = (0, 0, 11366)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11366")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11240"
data_version_tuple = (0, 0, 11240)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11240")
except ImportError:
    pass
data_git_hash = "f3433db6c2411d74dc55664fd68f2ec82c67c214"
data_git_describe = "v0.0-11240-gf3433db6c"
data_git_msg = """\
commit f3433db6c2411d74dc55664fd68f2ec82c67c214
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Mon Apr 4 17:30:03 2022 -0700

    [dv/otp_ctrl] Fix assertion error
    
    Fix assertion error because it sampled design input instead of output.
    
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
