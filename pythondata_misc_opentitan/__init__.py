import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12667"
version_tuple = (0, 0, 12667)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12667")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12525"
data_version_tuple = (0, 0, 12525)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12525")
except ImportError:
    pass
data_git_hash = "f7833ca52cd57fde08023b273b7c29cde133e771"
data_git_describe = "v0.0-12525-gf7833ca52"
data_git_msg = """\
commit f7833ca52cd57fde08023b273b7c29cde133e771
Author: Alexander Williams <awill@google.com>
Date:   Thu Jun 2 14:53:57 2022 -0700

    [usbdev/dif] Add half the unit tests
    
    This covers checking null arguments, direct interaction with the PHY,
    OUT transaction handling, and some basic endpoint configuration.
    
    Signed-off-by: Alexander Williams <awill@google.com>

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
