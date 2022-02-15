import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10322"
version_tuple = (0, 0, 10322)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10322")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10196"
data_version_tuple = (0, 0, 10196)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10196")
except ImportError:
    pass
data_git_hash = "c0e30c5b698d5a62a90101fe52fa04009657cf76"
data_git_describe = "v0.0-10196-gc0e30c5b6"
data_git_msg = """\
commit c0e30c5b698d5a62a90101fe52fa04009657cf76
Author: Michael Schaffner <msf@opentitan.org>
Date:   Mon Feb 14 17:28:50 2022 -0800

    [rv_dm] Enumerate all countermeasure IDs and annotate RTL
    
    Signed-off-by: Michael Schaffner <msf@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post126"
tool_version_tuple = (0, 0, 126)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post126")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
