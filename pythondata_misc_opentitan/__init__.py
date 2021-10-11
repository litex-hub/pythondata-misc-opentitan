import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8208"
version_tuple = (0, 0, 8208)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8208")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8096"
data_version_tuple = (0, 0, 8096)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8096")
except ImportError:
    pass
data_git_hash = "d0ae0ebb12ad4a3e29985913802606704360c6ac"
data_git_describe = "v0.0-8096-gd0ae0ebb1"
data_git_msg = """\
commit d0ae0ebb12ad4a3e29985913802606704360c6ac
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Thu Sep 30 00:08:30 2021 -0700

    [dv/shadow_reg] Fix aes shadow reg failure
    
    This PR fixes aes shadow reg failure:
    1). AES ctrl shadow reg write needs to update its write value before
    predicting the shadow reg.
    2). AES added a few more field in shadow reg.
    
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
