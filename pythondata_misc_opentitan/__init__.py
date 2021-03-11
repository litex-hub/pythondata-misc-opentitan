import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5345"
version_tuple = (0, 0, 5345)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5345")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5250"
data_version_tuple = (0, 0, 5250)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5250")
except ImportError:
    pass
data_git_hash = "e0d36964c4a56cd4dfb43900550590a45848f140"
data_git_describe = "v0.0-5250-ge0d36964c"
data_git_msg = """\
commit e0d36964c4a56cd4dfb43900550590a45848f140
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Thu Mar 11 11:47:45 2021 +0000

    [otbn] Expand OTBN DMem/IMem width
    
    Extra upper bits are ignored. This increase is required to aid area
    estimations for an OTBN design including integrity features.
    
    Signed-off-by: Greg Chadwick <gac@lowrisc.org>

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
