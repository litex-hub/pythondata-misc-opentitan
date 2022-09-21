import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14341"
version_tuple = (0, 0, 14341)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14341")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14199"
data_version_tuple = (0, 0, 14199)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14199")
except ImportError:
    pass
data_git_hash = "8bee7aa0fe3a882a96866ce621ec77f3847fa443"
data_git_describe = "v0.0-14199-g8bee7aa0fe"
data_git_msg = """\
commit 8bee7aa0fe3a882a96866ce621ec77f3847fa443
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Tue Sep 20 16:32:46 2022 -0700

    [dv/kmac] Add random pre-scaler and edn timeout val
    
    Previously if we do not want EDN timeout, we will just turn off the
    timer. This pr calculates the max edn return time with some buffer, then
    configure the EDN prescaler and wait time to make sure it should not
    timeout.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post142"
tool_version_tuple = (0, 0, 142)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post142")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
