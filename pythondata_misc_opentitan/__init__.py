import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11015"
version_tuple = (0, 0, 11015)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11015")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10889"
data_version_tuple = (0, 0, 10889)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10889")
except ImportError:
    pass
data_git_hash = "d4326b4d1a6941535d6859d6875c9408ac896934"
data_git_describe = "v0.0-10889-gd4326b4d1"
data_git_msg = """\
commit d4326b4d1a6941535d6859d6875c9408ac896934
Author: Drew Macrae <drewmacrae@google.com>
Date:   Thu Mar 17 10:16:53 2022 -0400

    [bazel/Mask ROM] Add a regression tests for CI
    
    Invoke regression tests with bazel to protect artifacts in the Mask ROM
    Only fail if targets begin to fail
    
    Signed-off-by: Drew Macrae <drewmacrae@google.com>

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
