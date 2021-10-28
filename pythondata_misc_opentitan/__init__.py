import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8504"
version_tuple = (0, 0, 8504)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8504")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8392"
data_version_tuple = (0, 0, 8392)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8392")
except ImportError:
    pass
data_git_hash = "4418f7d1b91f515dffe4b8ee13dc77d3fce98ecd"
data_git_describe = "v0.0-8392-g4418f7d1b"
data_git_msg = """\
commit 4418f7d1b91f515dffe4b8ee13dc77d3fce98ecd
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Thu Oct 28 17:48:10 2021 +0100

    [otbn,dv] Fix bad type in bad_ispr.py
    
    This happened because I merged two PRs that broke each other. Oops!
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
