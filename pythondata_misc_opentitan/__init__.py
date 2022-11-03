import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15159"
version_tuple = (0, 0, 15159)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15159")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post15017"
data_version_tuple = (0, 0, 15017)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post15017")
except ImportError:
    pass
data_git_hash = "ba9eccf37e2f6b5f44d84ad02f2c5d8f9a6154e8"
data_git_describe = "v0.0-15017-gba9eccf37e"
data_git_msg = """\
commit ba9eccf37e2f6b5f44d84ad02f2c5d8f9a6154e8
Author: Michael Schaffner <msf@google.com>
Date:   Wed Nov 2 18:46:24 2022 -0700

    [pinmux] use JTAG TAP input assumptions only in FPV
    
    Simulations may fail if the TAP inputs are not fully stable (which
    cannot be guaranteed within the pinmux).
    
    Signed-off-by: Michael Schaffner <msf@google.com>

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
