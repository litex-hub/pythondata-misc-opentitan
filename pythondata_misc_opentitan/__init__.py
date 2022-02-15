import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10301"
version_tuple = (0, 0, 10301)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10301")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10175"
data_version_tuple = (0, 0, 10175)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10175")
except ImportError:
    pass
data_git_hash = "752e9c90a8cbc524274c771e3858c90e0b10e1e5"
data_git_describe = "v0.0-10175-g752e9c90a"
data_git_msg = """\
commit 752e9c90a8cbc524274c771e3858c90e0b10e1e5
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Sat Feb 12 12:26:00 2022 -0800

    [dv/lc_ctrl] Add unr file
    
    This PR adds VC Formal generated unr file to LC testbench.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

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
