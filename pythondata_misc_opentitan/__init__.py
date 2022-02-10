import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10237"
version_tuple = (0, 0, 10237)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10237")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10113"
data_version_tuple = (0, 0, 10113)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10113")
except ImportError:
    pass
data_git_hash = "f86fcb99fe1cb1359c12876e208ff4853eafc0b5"
data_git_describe = "v0.0-10113-gf86fcb99f"
data_git_msg = """\
commit f86fcb99fe1cb1359c12876e208ff4853eafc0b5
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Thu Feb 10 10:05:32 2022 -0800

    [dv/shadow_reg] Move shadow_reg to V2S
    
    This PR cleans up the shadow reg testplan to move them to V2S.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post124"
tool_version_tuple = (0, 0, 124)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post124")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
