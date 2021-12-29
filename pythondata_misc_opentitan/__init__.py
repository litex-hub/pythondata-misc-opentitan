import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9302"
version_tuple = (0, 0, 9302)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9302")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9185"
data_version_tuple = (0, 0, 9185)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9185")
except ImportError:
    pass
data_git_hash = "72068eb8d367060e9731d3f6537009c48db87481"
data_git_describe = "v0.0-9185-g72068eb8d"
data_git_msg = """\
commit 72068eb8d367060e9731d3f6537009c48db87481
Author: Martin Lueker-Boden <martin.lueker-boden@wdc.com>
Date:   Thu Dec 23 17:21:49 2021 -0800

    [ entropy_src, rtl ] Improve watermarking for repcnt & repcnts
    
    - repcnt and repcnts ht outputs now indicate the largest repetition
    count (regardless of threshold)
    - watermarking can be updated even if not on the boundary of a
    health check
    
    Fixes #9819
    
    Signed-off-by: Martin Lueker-Boden <martin.lueker-boden@wdc.com>

"""

# Tool version info
tool_version_str = "0.0.post117"
tool_version_tuple = (0, 0, 117)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post117")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
