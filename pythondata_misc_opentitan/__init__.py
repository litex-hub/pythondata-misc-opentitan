import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9984"
version_tuple = (0, 0, 9984)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9984")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9860"
data_version_tuple = (0, 0, 9860)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9860")
except ImportError:
    pass
data_git_hash = "abf1af631b42f482ae60798736ed1c0d03feb9f5"
data_git_describe = "v0.0-9860-gabf1af631"
data_git_msg = """\
commit abf1af631b42f482ae60798736ed1c0d03feb9f5
Author: Jon Flatley <jflat@google.com>
Date:   Fri Jan 28 13:38:00 2022 -0500

    [opentitantool] Fix OTP tests to work under bazel
    
    Moves OTP test data to a more appropriate location and adds them to the
    bazel BUILD file to fix "file not found" errors encountered when running
    `bazel run //sw/host/opentitanlib:opentitanlib_test`.
    
    Signed-off-by: Jon Flatley <jflat@google.com>

"""

# Tool version info
tool_version_str = "0.0.post124"
tool_version_tuple = (0, 0, 124)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post124")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
