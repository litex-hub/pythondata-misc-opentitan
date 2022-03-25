import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11129"
version_tuple = (0, 0, 11129)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11129")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11003"
data_version_tuple = (0, 0, 11003)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11003")
except ImportError:
    pass
data_git_hash = "391f1892b1e7406816bb6da2c698565429a95212"
data_git_describe = "v0.0-11003-g391f1892b"
data_git_msg = """\
commit 391f1892b1e7406816bb6da2c698565429a95212
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Thu Mar 24 17:23:31 2022 -0700

    [dv/jtag] Fix chip_level jtag csr rw failure [part 2]
    
    This PR fixes chip_level jtag test comparison failure.
    This is because the sequence write to `sbcs` register but forget to
    write `access32`, so in sba bus, rv_dm did not send out transaction with
    the correct mask.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

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
