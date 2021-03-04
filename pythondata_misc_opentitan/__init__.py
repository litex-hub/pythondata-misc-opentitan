import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5243"
version_tuple = (0, 0, 5243)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5243")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5152"
data_version_tuple = (0, 0, 5152)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5152")
except ImportError:
    pass
data_git_hash = "55b2f89bfdfce0227216000a963f09fdf6b143d6"
data_git_describe = "v0.0-5152-g55b2f89bf"
data_git_msg = """\
commit 55b2f89bfdfce0227216000a963f09fdf6b143d6
Author: Cindy Chen <chencindy@google.com>
Date:   Wed Mar 3 18:48:58 2021 -0800

    [fpv] enable tlul check in fpv
    
    This PR removes the temp assumption to disable the TLUL check, as
    PR #5435 is merged.
    
    Signed-off-by: Cindy Chen <chencindy@google.com>

"""

# Tool version info
tool_version_str = "0.0.post91"
tool_version_tuple = (0, 0, 91)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post91")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
