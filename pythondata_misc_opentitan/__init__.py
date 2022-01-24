import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9727"
version_tuple = (0, 0, 9727)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9727")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9605"
data_version_tuple = (0, 0, 9605)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9605")
except ImportError:
    pass
data_git_hash = "7852bf9b79b1372a5571f4a7535b84fda1532cd8"
data_git_describe = "v0.0-9605-g7852bf9b7"
data_git_msg = """\
commit 7852bf9b79b1372a5571f4a7535b84fda1532cd8
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Tue Jan 18 15:38:28 2022 +0000

    [otbn,dv] Add a sequence that drives the lc_escalate_en_i input
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

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
