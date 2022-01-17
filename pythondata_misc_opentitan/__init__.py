import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9562"
version_tuple = (0, 0, 9562)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9562")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9440"
data_version_tuple = (0, 0, 9440)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9440")
except ImportError:
    pass
data_git_hash = "90ff24f3a186d6015d7f80e2b50eea3925c59125"
data_git_describe = "v0.0-9440-g90ff24f3a"
data_git_msg = """\
commit 90ff24f3a186d6015d7f80e2b50eea3925c59125
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Thu Dec 16 17:04:34 2021 +0000

    [otbn,dv] Document how we cover integrity protection
    
    Also mark the existing mem_integrity testpoint and the new
    internal_integrity testpoint as V2S since they're testing fault
    detection.
    
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
