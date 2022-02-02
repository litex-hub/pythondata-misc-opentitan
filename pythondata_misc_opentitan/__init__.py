import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10014"
version_tuple = (0, 0, 10014)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10014")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9890"
data_version_tuple = (0, 0, 9890)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9890")
except ImportError:
    pass
data_git_hash = "3daf20973f1a1fcff30a4954880517f8dc12f6af"
data_git_describe = "v0.0-9890-g3daf20973"
data_git_msg = """\
commit 3daf20973f1a1fcff30a4954880517f8dc12f6af
Author: Timothy Chen <timothytim@google.com>
Date:   Fri Jan 28 11:17:06 2022 -0800

    [flash_ctrl] Add sva to check for rma prog / rd data match
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
