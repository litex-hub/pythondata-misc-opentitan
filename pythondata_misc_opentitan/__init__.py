import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8446"
version_tuple = (0, 0, 8446)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8446")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8334"
data_version_tuple = (0, 0, 8334)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8334")
except ImportError:
    pass
data_git_hash = "fa9ed4b0125c8b5dc0eca8f3d092ba14d310c548"
data_git_describe = "v0.0-8334-gfa9ed4b01"
data_git_msg = """\
commit fa9ed4b0125c8b5dc0eca8f3d092ba14d310c548
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Thu Oct 21 17:27:39 2021 -0700

    [dv/chip_level] Disable signal integrity check
    
    Because of lpg and alert init are not fully supported in top-level
    environment with alert_esc_agent, we will disable the alert's signal
    integrity check.
    This should have minimal impact because prim_receiver's assertions can
    still check signal integrity error.
    This also fixes issue #8715
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

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
