import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12752"
version_tuple = (0, 0, 12752)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12752")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12610"
data_version_tuple = (0, 0, 12610)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12610")
except ImportError:
    pass
data_git_hash = "47dc84b5279fe7cd6a00c2a132837e0b5e56bb25"
data_git_describe = "v0.0-12610-g47dc84b527"
data_git_msg = """\
commit 47dc84b5279fe7cd6a00c2a132837e0b5e56bb25
Author: Chris Frantz <cfrantz@google.com>
Date:   Thu Jun 16 16:38:08 2022 -0700

    [ottool] Fold the `sign` command into `manifest update`
    
    1. Add signing functionality to `manifest update`, as the requirments
       of `sign` include a manifest update.
    2. Rename `--hjson_file` to `--manifest`.
    
    Signed-off-by: Chris Frantz <cfrantz@google.com>

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
