import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8150"
version_tuple = (0, 0, 8150)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8150")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8042"
data_version_tuple = (0, 0, 8042)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8042")
except ImportError:
    pass
data_git_hash = "e3315cc32be531d7bbbf2a44dfd7f2af286bd559"
data_git_describe = "v0.0-8042-ge3315cc32"
data_git_msg = """\
commit e3315cc32be531d7bbbf2a44dfd7f2af286bd559
Author: Michael Schaffner <msf@google.com>
Date:   Tue Oct 5 16:18:17 2021 -0700

    [prim_mubi] Add decoder module similar to prim_lc_dec
    
    Signed-off-by: Michael Schaffner <msf@google.com>

"""

# Tool version info
tool_version_str = "0.0.post108"
tool_version_tuple = (0, 0, 108)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post108")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
