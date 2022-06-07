import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12559"
version_tuple = (0, 0, 12559)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12559")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12417"
data_version_tuple = (0, 0, 12417)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12417")
except ImportError:
    pass
data_git_hash = "1ba8b40b2cff38ae2fe105ecce9b5d17a2dab725"
data_git_describe = "v0.0-12417-g1ba8b40b2"
data_git_msg = """\
commit 1ba8b40b2cff38ae2fe105ecce9b5d17a2dab725
Author: Guillermo Maturana <maturana@google.com>
Date:   Thu Jun 2 23:46:40 2022 -0700

    [dw,chip_sw] Add clkmgr_off_trans tests
    
    Signed-off-by: Guillermo Maturana <maturana@google.com>

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
