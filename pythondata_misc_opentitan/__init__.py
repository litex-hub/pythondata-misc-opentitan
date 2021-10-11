import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8195"
version_tuple = (0, 0, 8195)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8195")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8083"
data_version_tuple = (0, 0, 8083)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8083")
except ImportError:
    pass
data_git_hash = "bf944b6b36b4c4e6ab89c6748754951a786dcb91"
data_git_describe = "v0.0-8083-gbf944b6b3"
data_git_msg = """\
commit bf944b6b36b4c4e6ab89c6748754951a786dcb91
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Thu Oct 7 13:34:29 2021 +0100

    [otbn,dv] Move decision about stats collection to start()
    
    This tidies up some downstream logic (especially with an upcoming
    refactoring) because we can collect statistics iff the self.stats
    object is not None. Much easier than wiring through a flag.
    
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
