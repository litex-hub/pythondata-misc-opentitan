import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5733"
version_tuple = (0, 0, 5733)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5733")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5638"
data_version_tuple = (0, 0, 5638)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5638")
except ImportError:
    pass
data_git_hash = "d4d59930e0091fe5b45e0a9d079962b27e430bcc"
data_git_describe = "v0.0-5638-gd4d59930e"
data_git_msg = """\
commit d4d59930e0091fe5b45e0a9d079962b27e430bcc
Author: Chris Frantz <cfrantz@google.com>
Date:   Fri Apr 2 08:03:58 2021 -0700

    Correct a documentation error regarding DIFs
    
    DIFs are a verification resource and are intended to make writing DV and
    silicon bringup code easier.
    
    DIFs are not primitives for writing production code such as ROM, ROM_EXT,
    bootloaders or kernel drivers.
    
    Signed-off-by: Chris Frantz <cfrantz@google.com>

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
