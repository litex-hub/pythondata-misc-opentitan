import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14281"
version_tuple = (0, 0, 14281)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14281")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14139"
data_version_tuple = (0, 0, 14139)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14139")
except ImportError:
    pass
data_git_hash = "ef2fc00e45e7b44e058a81a65614733ab0b91da6"
data_git_describe = "v0.0-14139-gef2fc00e45"
data_git_msg = """\
commit ef2fc00e45e7b44e058a81a65614733ab0b91da6
Author: Michael Schaffner <msf@google.com>
Date:   Fri Sep 16 14:38:38 2022 -0700

    [test/rv_dm] Consolidate two testpoints
    
    These two testpoints were essentially testing the same thing,
    hence they can be consolidated.
    
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
