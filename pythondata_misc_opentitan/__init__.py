import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12643"
version_tuple = (0, 0, 12643)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12643")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12501"
data_version_tuple = (0, 0, 12501)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12501")
except ImportError:
    pass
data_git_hash = "aa87069dcb5f8d9430f175f93341d9c50663dcc8"
data_git_describe = "v0.0-12501-gaa87069dc"
data_git_msg = """\
commit aa87069dcb5f8d9430f175f93341d9c50663dcc8
Author: Timothy Trippel <ttrippel@google.com>
Date:   Thu Jun 9 16:38:23 2022 -0700

    [doc] update SW build and Verilator docs to reference Bazel
    
    Now that all meson build files have been removed in favor of Bazel, this
    commit updates the SW build and Verilator build documentation on the
    website. Note, the FPGA documentation will be updated in a follow on
    commit.
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

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
