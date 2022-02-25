import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10543"
version_tuple = (0, 0, 10543)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10543")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10417"
data_version_tuple = (0, 0, 10417)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10417")
except ImportError:
    pass
data_git_hash = "3b9f3d078eb3c8c947889bfc3a3d30af1b0b3b1a"
data_git_describe = "v0.0-10417-g3b9f3d078"
data_git_msg = """\
commit 3b9f3d078eb3c8c947889bfc3a3d30af1b0b3b1a
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Thu Feb 24 15:47:43 2022 +0000

    [otbn,dv] Extend window at end of IMEM error sequence
    
    This is all about an awkward situation where we happen to inject an
    IMEM error just after we've fetched the last instruction that we were
    going to execute. In this case, there will be no error, which is fine,
    but I'd mis-calculated how long you need to wait to figure out whether
    it's happened. Fix that.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

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
