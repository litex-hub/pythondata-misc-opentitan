import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10273"
version_tuple = (0, 0, 10273)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10273")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10149"
data_version_tuple = (0, 0, 10149)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10149")
except ImportError:
    pass
data_git_hash = "e0349bb3391d3d6cbb8eb7288b0f21d819cc0e9b"
data_git_describe = "v0.0-10149-ge0349bb33"
data_git_msg = """\
commit e0349bb3391d3d6cbb8eb7288b0f21d819cc0e9b
Author: Alphan Ulusoy <alphan@google.com>
Date:   Thu Feb 10 15:21:47 2022 -0500

    [sw/silicon_creator] Add a redundant check for lc_shift in shutdown_init()
    
    Signed-off-by: Alphan Ulusoy <alphan@google.com>

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
