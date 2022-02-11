import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10248"
version_tuple = (0, 0, 10248)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10248")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10124"
data_version_tuple = (0, 0, 10124)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10124")
except ImportError:
    pass
data_git_hash = "490776858ecc183874bc15df0ae8ccf5a5399332"
data_git_describe = "v0.0-10124-g490776858"
data_git_msg = """\
commit 490776858ecc183874bc15df0ae8ccf5a5399332
Author: Alphan Ulusoy <alphan@google.com>
Date:   Wed Feb 2 13:24:22 2022 -0500

    [sw/silicon_creator] Use EXPECT_DEATH in unit tests
    
    Fixes #10549
    
    Signed-off-by: Alphan Ulusoy <alphan@google.com>

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
