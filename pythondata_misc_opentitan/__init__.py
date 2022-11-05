import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15257"
version_tuple = (0, 0, 15257)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15257")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post15115"
data_version_tuple = (0, 0, 15115)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post15115")
except ImportError:
    pass
data_git_hash = "fd97785a85b530dd3bbcabcfcd24b0210194ff5c"
data_git_describe = "v0.0-15115-gfd97785a85"
data_git_msg = """\
commit fd97785a85b530dd3bbcabcfcd24b0210194ff5c
Author: Michael Schaffner <msf@google.com>
Date:   Fri Nov 4 14:22:59 2022 -0700

    [rv_core_ibex] Add assertions for ibex fetch enable
    
    Fixes #15217
    
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
