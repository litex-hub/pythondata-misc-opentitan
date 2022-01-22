import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9711"
version_tuple = (0, 0, 9711)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9711")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9589"
data_version_tuple = (0, 0, 9589)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9589")
except ImportError:
    pass
data_git_hash = "dc40cb5774741bca306f536b1f5abe1f59cb1319"
data_git_describe = "v0.0-9589-gdc40cb577"
data_git_msg = """\
commit dc40cb5774741bca306f536b1f5abe1f59cb1319
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Fri Jan 21 15:28:23 2022 -0800

    [dv/otp_ctrl] Add checkings for vendor_test partition
    
    This PR adds two items for vendor_test partition:
    1). Read lock vendor test partition via csr.
    2). Read out vendor test partition digest value via csrs.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post122"
tool_version_tuple = (0, 0, 122)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post122")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
