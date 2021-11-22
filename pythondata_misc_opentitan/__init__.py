import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8813"
version_tuple = (0, 0, 8813)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8813")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8701"
data_version_tuple = (0, 0, 8701)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8701")
except ImportError:
    pass
data_git_hash = "bd51d1852e1da8ee8d3687be196bcb0bd3421b12"
data_git_describe = "v0.0-8701-gbd51d1852"
data_git_msg = """\
commit bd51d1852e1da8ee8d3687be196bcb0bd3421b12
Author: Timothy Trippel <ttrippel@google.com>
Date:   Fri Nov 19 21:14:43 2021 +0000

    [sw/ottf] Fix typos in example OTTF test names.
    
    OTTF example test names accidentally had the word "lib" tacked on the
    end.
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

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
