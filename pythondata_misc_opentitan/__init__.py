import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15102"
version_tuple = (0, 0, 15102)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15102")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14960"
data_version_tuple = (0, 0, 14960)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14960")
except ImportError:
    pass
data_git_hash = "f3e95c6d0bc66483c94bc07fed6aab8b9d38b25c"
data_git_describe = "v0.0-14960-gf3e95c6d0b"
data_git_msg = """\
commit f3e95c6d0bc66483c94bc07fed6aab8b9d38b25c
Author: Michael Schaffner <msf@google.com>
Date:   Tue Nov 1 11:13:51 2022 -0700

    [prim_diff_decode] Update SVAs to make them compatible with sim CDC
    
    This is done in preparation for CDC instrumentation in simulation,
    see here: #15863
    
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
