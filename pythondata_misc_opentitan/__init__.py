import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8702"
version_tuple = (0, 0, 8702)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8702")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8590"
data_version_tuple = (0, 0, 8590)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8590")
except ImportError:
    pass
data_git_hash = "ae2a883831dba118c816455cbc0f2adf3c117fd8"
data_git_describe = "v0.0-8590-gae2a88383"
data_git_msg = """\
commit ae2a883831dba118c816455cbc0f2adf3c117fd8
Author: Drew Macrae <drewmacrae@google.com>
Date:   Wed Nov 10 19:38:05 2021 +0000

    [dif unittests] fix mixed signedness warning
    
    Two of our unit-tests compare signed ints with unsigned ints and throw a
    warning when built. This fixes it to silence the error.
    
    Signed-off-by: Drew Macrae <drewmacrae@google.com>

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
