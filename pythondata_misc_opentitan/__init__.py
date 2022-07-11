import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13020"
version_tuple = (0, 0, 13020)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13020")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12878"
data_version_tuple = (0, 0, 12878)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12878")
except ImportError:
    pass
data_git_hash = "5186d619617bcac1adbb484f9249cd12152c62c5"
data_git_describe = "v0.0-12878-g5186d61961"
data_git_msg = """\
commit 5186d619617bcac1adbb484f9249cd12152c62c5
Author: Michael Schaffner <msf@opentitan.org>
Date:   Fri Jul 8 17:16:25 2022 -0700

    [otbn/lint] rename branch field since it is reserved
    
    Signed-off-by: Michael Schaffner <msf@opentitan.org>

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
