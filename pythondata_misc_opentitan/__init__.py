import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12713"
version_tuple = (0, 0, 12713)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12713")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12571"
data_version_tuple = (0, 0, 12571)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12571")
except ImportError:
    pass
data_git_hash = "e9410b71e53a4de1193395555ac4daf1df5372f4"
data_git_describe = "v0.0-12571-ge9410b71e"
data_git_msg = """\
commit e9410b71e53a4de1193395555ac4daf1df5372f4
Author: Miles Dai <milesdai@google.com>
Date:   Wed Jun 15 17:30:06 2022 -0400

    [ci] Remove Verilator test's dependency on pre-fetched Bazel dependencies
    
    Signed-off-by: Miles Dai <milesdai@google.com>

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
