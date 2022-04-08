import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11462"
version_tuple = (0, 0, 11462)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11462")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11336"
data_version_tuple = (0, 0, 11336)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11336")
except ImportError:
    pass
data_git_hash = "ef0063c1167897d722242ffc11a2890eb363b508"
data_git_describe = "v0.0-11336-gef0063c11"
data_git_msg = """\
commit ef0063c1167897d722242ffc11a2890eb363b508
Author: Douglas Reis <doreis@lowrisc.org>
Date:   Mon Apr 4 16:56:16 2022 +0100

    [dif, aes] Refactor aes unittest
    
    Signed-off-by: Douglas Reis <doreis@lowrisc.org>

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
