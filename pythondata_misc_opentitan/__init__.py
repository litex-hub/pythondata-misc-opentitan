import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11028"
version_tuple = (0, 0, 11028)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11028")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10902"
data_version_tuple = (0, 0, 10902)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10902")
except ImportError:
    pass
data_git_hash = "80bc06cb8940588d970b3ee05468978067c1e244"
data_git_describe = "v0.0-10902-g80bc06cb8"
data_git_msg = """\
commit 80bc06cb8940588d970b3ee05468978067c1e244
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Tue Mar 22 13:15:30 2022 -0700

    [dv/otp] Add cov for sw partition lock status
    
    this PR adds a covergroup for sw partition lock status:
    1). Collect which SW partition it is.
    2). Collect if it is write locked.
    3). Collect if it is read locked.
    4). Collect the current operation type.
    Then cross the above coverpoints.
    
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
