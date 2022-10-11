import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14672"
version_tuple = (0, 0, 14672)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14672")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14530"
data_version_tuple = (0, 0, 14530)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14530")
except ImportError:
    pass
data_git_hash = "cc7d363b4eaf952dd08a79eeacaa4d4d7a58f35a"
data_git_describe = "v0.0-14530-gcc7d363b4e"
data_git_msg = """\
commit cc7d363b4eaf952dd08a79eeacaa4d4d7a58f35a
Author: Timothy Chen <timothytim@google.com>
Date:   Fri Oct 7 20:42:15 2022 -0700

    [rv_dm] Stall tlul transactions when issuing ndm reset
    
    - fixes #15242
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
