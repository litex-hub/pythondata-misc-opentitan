import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11175"
version_tuple = (0, 0, 11175)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11175")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11049"
data_version_tuple = (0, 0, 11049)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11049")
except ImportError:
    pass
data_git_hash = "6981fd4149ba360119cd2437c828d7285af64302"
data_git_describe = "v0.0-11049-g6981fd414"
data_git_msg = """\
commit 6981fd4149ba360119cd2437c828d7285af64302
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Thu Mar 24 15:53:48 2022 +0000

    [otbn,doc] Fix description of memory accesses when OTBN is busy
    
    This behaviour is described in detail in the reggen-generated stuff
    that shows the windows themselves, but the text here still reflected
    the old design (where we'd completely ignore the bus access and stall
    the bus).
    
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
