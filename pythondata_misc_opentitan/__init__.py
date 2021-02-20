import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5074"
version_tuple = (0, 0, 5074)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5074")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post4983"
data_version_tuple = (0, 0, 4983)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post4983")
except ImportError:
    pass
data_git_hash = "a70638097417cf8d7a39fa8a12f01cf1112c16f9"
data_git_describe = "v0.0-4983-ga70638097"
data_git_msg = """\
commit a70638097417cf8d7a39fa8a12f01cf1112c16f9
Author: Michael Schaffner <msf@opentitan.org>
Date:   Thu Feb 18 18:06:03 2021 -0800

    [pinmux] Add strap sampling and TAP qualification logic
    
    Signed-off-by: Michael Schaffner <msf@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post91"
tool_version_tuple = (0, 0, 91)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post91")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
