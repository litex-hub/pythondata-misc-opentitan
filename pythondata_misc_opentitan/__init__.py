import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8594"
version_tuple = (0, 0, 8594)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8594")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8482"
data_version_tuple = (0, 0, 8482)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8482")
except ImportError:
    pass
data_git_hash = "1a84e2dc27cf027cd26bdbcea31c5f79aa0f7d65"
data_git_describe = "v0.0-8482-g1a84e2dc2"
data_git_msg = """\
commit 1a84e2dc27cf027cd26bdbcea31c5f79aa0f7d65
Author: Timothy Trippel <ttrippel@google.com>
Date:   Thu Nov 4 06:47:41 2021 +0000

    [ottf] Added test status reporting and teardown logic.
    
    When an on-device test completes, the OTTF now reports the test result
    over the same interface as the existing test_main.{h,c} framework to
    automatically terminate the test. This was accomplished by wrapping the
    test_main() test entry point function in a wrapper function that is the
    entry point to the FreeRTOS task the test runs in. The wrapper function
    is used to report the test status. Additionally by using a wrapper
    function, we can maintain the exact same function prototype used for
    existing on-device test to minimize overhead migrating chip-level tests
    to the OTTF.
    
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
