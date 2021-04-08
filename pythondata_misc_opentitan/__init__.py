import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5771"
version_tuple = (0, 0, 5771)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5771")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5676"
data_version_tuple = (0, 0, 5676)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5676")
except ImportError:
    pass
data_git_hash = "7651597e2db5c021ee004b7b23395483df477378"
data_git_describe = "v0.0-5676-g7651597e2"
data_git_msg = """\
commit 7651597e2db5c021ee004b7b23395483df477378
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Thu Apr 8 07:41:34 2021 +0100

    [otbn] Wire up bus intg_error_o signals
    
    These are merged together and cause a "bus integrity error", which is
    a fatal alert.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

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
