import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12967"
version_tuple = (0, 0, 12967)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12967")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12825"
data_version_tuple = (0, 0, 12825)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12825")
except ImportError:
    pass
data_git_hash = "06d2247c2e528c35e1803818a9a74e3bd9c48d38"
data_git_describe = "v0.0-12825-g06d2247c2e"
data_git_msg = """\
commit 06d2247c2e528c35e1803818a9a74e3bd9c48d38
Author: Michael Schaffner <msf@google.com>
Date:   Thu Jul 7 12:51:08 2022 -0700

    [sw] Fix clang format errors
    
    Signed-off-by: Michael Schaffner <msf@google.com>

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
