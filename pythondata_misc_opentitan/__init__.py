import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8867"
version_tuple = (0, 0, 8867)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8867")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8755"
data_version_tuple = (0, 0, 8755)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8755")
except ImportError:
    pass
data_git_hash = "6e7187bf8872e91c99e06e96ab224f06b58af8e0"
data_git_describe = "v0.0-8755-g6e7187bf8"
data_git_msg = """\
commit 6e7187bf8872e91c99e06e96ab224f06b58af8e0
Author: Douglas Reis <doreis@lowrisc.org>
Date:   Wed Nov 24 11:02:56 2021 +0000

    [sw,tests] Remove the duplicate kmac smoke test
    
    FIX #9363
    
    Signed-off-by: Douglas Reis <doreis@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
