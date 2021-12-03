import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8979"
version_tuple = (0, 0, 8979)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8979")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8867"
data_version_tuple = (0, 0, 8867)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8867")
except ImportError:
    pass
data_git_hash = "3f2e231e8da7b8cc5b309c080ca61d4fe3dcbc8c"
data_git_describe = "v0.0-8867-g3f2e231e8"
data_git_msg = """\
commit 3f2e231e8da7b8cc5b309c080ca61d4fe3dcbc8c
Author: Drew Macrae <drewmacrae@google.com>
Date:   Thu Dec 2 21:56:00 2021 +0000

    [bazel] build without -Wpedantic
    
    If we disable to all_warnings feature for bazel_embedded we can silence
    the variadic macro warnings and some others that result from building
    with -Wpedantic and -std=c11.
    
    Signed-off-by: Drew Macrae <drewmacrae@google.com>

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
