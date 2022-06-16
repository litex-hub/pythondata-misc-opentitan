import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12721"
version_tuple = (0, 0, 12721)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12721")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12579"
data_version_tuple = (0, 0, 12579)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12579")
except ImportError:
    pass
data_git_hash = "1b0ef51286760c2ce5e18b02bb7a022130d933a4"
data_git_describe = "v0.0-12579-g1b0ef5128"
data_git_msg = """\
commit 1b0ef51286760c2ce5e18b02bb7a022130d933a4
Author: Drew Macrae <drewmacrae@google.com>
Date:   Wed Jun 15 16:12:27 2022 -0400

    [bazel] sw/device/tests has a number of tests that are no longer broken
    
    Signed-off-by: Drew Macrae <drewmacrae@google.com>

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
