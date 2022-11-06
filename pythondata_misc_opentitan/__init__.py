import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15262"
version_tuple = (0, 0, 15262)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15262")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post15120"
data_version_tuple = (0, 0, 15120)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post15120")
except ImportError:
    pass
data_git_hash = "2bf1fea0ba7a2dc0122deaee34ce63614356bfa4"
data_git_describe = "v0.0-15120-g2bf1fea0ba"
data_git_msg = """\
commit 2bf1fea0ba7a2dc0122deaee34ce63614356bfa4
Author: Cindy Liu <hcindyl@google.com>
Date:   Fri Nov 4 15:56:03 2022 -0700

    [bazel, reggen] Fix gen_rtl python library
    
    Signed-off-by: Cindy Liu <hcindyl@google.com>

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
