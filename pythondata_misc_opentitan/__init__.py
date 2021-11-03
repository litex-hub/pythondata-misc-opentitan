import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8575"
version_tuple = (0, 0, 8575)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8575")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8463"
data_version_tuple = (0, 0, 8463)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8463")
except ImportError:
    pass
data_git_hash = "1b73f8090033839b73de6b5954702137d723948e"
data_git_describe = "v0.0-8463-g1b73f8090"
data_git_msg = """\
commit 1b73f8090033839b73de6b5954702137d723948e
Author: Timothy Trippel <ttrippel@google.com>
Date:   Mon Nov 1 23:16:50 2021 +0000

    [sw/testing] Make `CHECK_BUFFER` consistent with other `CHECK*` macros.
    
    The `CHECK_BUFFER(...)` macro in `sw/device/lib/testing/check.h` has a
    slightly different format than other `CHECK*(...)` macros. Specifically
    it does not set the test status directly, and does not support printing
    a user-supplied error message. The result tests having to call the
    `CHECK_BUFFER(...)` macro followed by the `CHECK(...)` macro in test
    code.
    
    This commit makes the `CHECK_BUFFER(...)` macro look more like the
    `CHECK(...)` macro, thereby fixing #9002.
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
