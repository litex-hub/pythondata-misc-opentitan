import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10789"
version_tuple = (0, 0, 10789)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10789")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10663"
data_version_tuple = (0, 0, 10663)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10663")
except ImportError:
    pass
data_git_hash = "6292b1ac4388d9c0278b2b4ef569cd36138a5455"
data_git_describe = "v0.0-10663-g6292b1ac4"
data_git_msg = """\
commit 6292b1ac4388d9c0278b2b4ef569cd36138a5455
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Tue Mar 8 16:21:20 2022 -0800

    [dv/entropy_src] Temp remove stress_all_with_rand_reset test
    
    Because some of the `stress_all_with_rand_reset` tests seem to hang
    during nightly regression, we decided to temp remove that test.
    
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
