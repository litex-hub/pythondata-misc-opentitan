import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9765"
version_tuple = (0, 0, 9765)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9765")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9643"
data_version_tuple = (0, 0, 9643)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9643")
except ImportError:
    pass
data_git_hash = "14b2217fbfe2d3707ce068df06c58f8688139447"
data_git_describe = "v0.0-9643-g14b2217fb"
data_git_msg = """\
commit 14b2217fbfe2d3707ce068df06c58f8688139447
Author: Martin Lueker-Boden <martin.lueker-boden@wdc.com>
Date:   Wed Jan 19 08:15:01 2022 -0800

    [entropy_src] Fix 1-clk timing error in Bucket Test output
    
    Fixes #10226.  See that issue for motivation.
    
    Signed-off-by: Martin Lueker-Boden <martin.lueker-boden@wdc.com>

"""

# Tool version info
tool_version_str = "0.0.post122"
tool_version_tuple = (0, 0, 122)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post122")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
