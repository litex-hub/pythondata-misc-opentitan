import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5591"
version_tuple = (0, 0, 5591)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5591")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5496"
data_version_tuple = (0, 0, 5496)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5496")
except ImportError:
    pass
data_git_hash = "2a142ffbbe2f65367e03852f75bb18be4e79e75c"
data_git_describe = "v0.0-5496-g2a142ffbb"
data_git_msg = """\
commit 2a142ffbbe2f65367e03852f75bb18be4e79e75c
Author: Michael Schaffner <msf@opentitan.org>
Date:   Thu Mar 25 11:31:16 2021 -0700

    [prim_prince] Reverse the k0||k1 mapping to match with the paper
    
    This aligns the logical mapping of the key into the k0/k1 halves.
    The implementation and golden model mapped the LSBs of the key to k0,
    and the MSBs to k1, whereas they are actually reversed in the paper.
    
    Signed-off-by: Michael Schaffner <msf@opentitan.org>

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
