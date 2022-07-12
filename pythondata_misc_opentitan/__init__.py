import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13037"
version_tuple = (0, 0, 13037)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13037")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12895"
data_version_tuple = (0, 0, 12895)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12895")
except ImportError:
    pass
data_git_hash = "2ac1e40acfbf90d3ba8b1d688317355b873207ab"
data_git_describe = "v0.0-12895-g2ac1e40acf"
data_git_msg = """\
commit 2ac1e40acfbf90d3ba8b1d688317355b873207ab
Author: Canberk Topal <ctopal@lowrisc.org>
Date:   Mon Jul 4 17:06:33 2022 +0100

    [otbn,dv] Set same sideload key in standalone sim
    
    Signed-off-by: Canberk Topal <ctopal@lowrisc.org>

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
