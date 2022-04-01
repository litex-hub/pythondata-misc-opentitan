import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11277"
version_tuple = (0, 0, 11277)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11277")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11151"
data_version_tuple = (0, 0, 11151)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11151")
except ImportError:
    pass
data_git_hash = "5263dc320c6408a9ce5aece71274d60d0c05a096"
data_git_describe = "v0.0-11151-g5263dc320"
data_git_msg = """\
commit 5263dc320c6408a9ce5aece71274d60d0c05a096
Author: Timothy Trippel <ttrippel@google.com>
Date:   Thu Mar 31 16:35:40 2022 -0700

    [bazel] move opentitan_test macro to separate rules file
    
    The `rules/opentitan.bzl` was overwhelming large due to the macros and
    helper functions needed define tests and produce OpenTitan device
    images. This moves all test related macros and helper functions to a
    separate rules file `rules/opentitan_test.bzl` to improve readability.
    
    This addresses a task in #11805.
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

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
