import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12865"
version_tuple = (0, 0, 12865)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12865")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12723"
data_version_tuple = (0, 0, 12723)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12723")
except ImportError:
    pass
data_git_hash = "8e0201f02d54d4edddb9d803cf431e71823ea7ee"
data_git_describe = "v0.0-12723-g8e0201f02d"
data_git_msg = """\
commit 8e0201f02d54d4edddb9d803cf431e71823ea7ee
Author: Douglas Reis <doreis@lowrisc.org>
Date:   Thu Jun 16 17:16:34 2022 +0100

    [dif, rv_core_ibex] Add the alerts errors functions
    
    Signed-off-by: Douglas Reis <doreis@lowrisc.org>

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
