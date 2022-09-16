import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14264"
version_tuple = (0, 0, 14264)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14264")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14122"
data_version_tuple = (0, 0, 14122)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14122")
except ImportError:
    pass
data_git_hash = "f89fce8767805dd174f1674e8886864ca958b214"
data_git_describe = "v0.0-14122-gf89fce8767"
data_git_msg = """\
commit f89fce8767805dd174f1674e8886864ca958b214
Author: Miles Dai <milesdai@google.com>
Date:   Mon Sep 12 22:40:01 2022 -0400

    [bazel/otp] Consolidate OTP bazel rules
    
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
