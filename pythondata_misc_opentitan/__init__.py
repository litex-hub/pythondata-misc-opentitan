import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12231"
version_tuple = (0, 0, 12231)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12231")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12103"
data_version_tuple = (0, 0, 12103)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12103")
except ImportError:
    pass
data_git_hash = "6372f683248c32b7c0a673e5184b539c52121661"
data_git_describe = "v0.0-12103-g6372f6832"
data_git_msg = """\
commit 6372f683248c32b7c0a673e5184b539c52121661
Author: Douglas Reis <doreis@lowrisc.org>
Date:   Wed May 18 10:56:01 2022 +0100

    [dif, rv_core_ibex] Add address translation and unittest
    
    Signed-off-by: Douglas Reis <doreis@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post128"
tool_version_tuple = (0, 0, 128)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post128")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
