import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10017"
version_tuple = (0, 0, 10017)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10017")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9893"
data_version_tuple = (0, 0, 9893)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9893")
except ImportError:
    pass
data_git_hash = "16b622ff84076e1e024b41303f64b5fcb8fa6822"
data_git_describe = "v0.0-9893-g16b622ff8"
data_git_msg = """\
commit 16b622ff84076e1e024b41303f64b5fcb8fa6822
Author: Michael Schaffner <msf@google.com>
Date:   Wed Feb 2 20:00:09 2022 +0000

    [prim_max_tree] Remove dedicated FPV TB since all SVAs are embedded
    
    Signed-off-by: Michael Schaffner <msf@google.com>

"""

# Tool version info
tool_version_str = "0.0.post124"
tool_version_tuple = (0, 0, 124)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post124")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
