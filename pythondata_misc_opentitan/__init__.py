import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8625"
version_tuple = (0, 0, 8625)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8625")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8513"
data_version_tuple = (0, 0, 8513)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8513")
except ImportError:
    pass
data_git_hash = "0f60351bd8a440e5db031cf20f6d31d099700380"
data_git_describe = "v0.0-8513-g0f60351bd"
data_git_msg = """\
commit 0f60351bd8a440e5db031cf20f6d31d099700380
Author: Timothy Chen <timothytim@google.com>
Date:   Fri Nov 5 12:51:14 2021 -0700

    [util] Add generic ecc encode function for re-use
    
    Signed-off-by: Timothy Chen <timothytim@google.com>
    
    [util] secded_gen fixes
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
