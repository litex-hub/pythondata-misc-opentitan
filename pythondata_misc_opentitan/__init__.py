import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5681"
version_tuple = (0, 0, 5681)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5681")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5586"
data_version_tuple = (0, 0, 5586)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5586")
except ImportError:
    pass
data_git_hash = "10c6e5bfd6bbd2255a2f043ef34106b529eed481"
data_git_describe = "v0.0-5586-g10c6e5bfd"
data_git_msg = """\
commit 10c6e5bfd6bbd2255a2f043ef34106b529eed481
Author: Cindy Chen <chencindy@google.com>
Date:   Thu Apr 1 11:18:54 2021 -0700

    [dv/otp_ctrl] Support ecc correctable error in otp check
    
    This PR supports ECC correctable error in otp_checks.
    This error not trigger any alert, but just trigger an interrupt and
    update error code accordingly.
    
    Signed-off-by: Cindy Chen <chencindy@google.com>

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
