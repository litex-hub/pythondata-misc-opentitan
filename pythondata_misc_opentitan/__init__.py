import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5662"
version_tuple = (0, 0, 5662)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5662")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5567"
data_version_tuple = (0, 0, 5567)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5567")
except ImportError:
    pass
data_git_hash = "3d70205aa1aac2abbccbea2743293a589b404330"
data_git_describe = "v0.0-5567-g3d70205aa"
data_git_msg = """\
commit 3d70205aa1aac2abbccbea2743293a589b404330
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Thu Mar 25 08:51:18 2021 +0000

    [flash_ctrl,lint] Fix width mismatch warnings
    
    The idx variable has width WordSelW, which is at least
    $clog2(WidthMultiple). Explicitly slice out the relevant bits from
    WidthMultiple - 1 to avoid a Verilator width mismatch warning.
    
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
