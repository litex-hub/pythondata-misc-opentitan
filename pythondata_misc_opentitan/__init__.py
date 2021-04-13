import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5839"
version_tuple = (0, 0, 5839)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5839")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5744"
data_version_tuple = (0, 0, 5744)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5744")
except ImportError:
    pass
data_git_hash = "5b548d5645334578da42e06c8539c57a2a8bffaf"
data_git_describe = "v0.0-5744-g5b548d564"
data_git_msg = """\
commit 5b548d5645334578da42e06c8539c57a2a8bffaf
Author: Mark Branstad <mark.branstad@wdc.com>
Date:   Mon Apr 12 11:15:22 2021 -0700

    [csrng/rtl] Two csrng app interfaces working
    
    Fixes to remove hang conditions.
    
    Signed-off-by: Mark Branstad <mark.branstad@wdc.com>

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
