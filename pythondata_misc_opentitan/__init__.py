import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15101"
version_tuple = (0, 0, 15101)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15101")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14959"
data_version_tuple = (0, 0, 14959)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14959")
except ImportError:
    pass
data_git_hash = "ba225dec09fecfdbd2cad36a913a2c252e2077ed"
data_git_describe = "v0.0-14959-gba225dec09"
data_git_msg = """\
commit ba225dec09fecfdbd2cad36a913a2c252e2077ed
Author: Timothy Trippel <ttrippel@google.com>
Date:   Tue Nov 1 11:32:01 2022 -0700

    [bazel] exclude foundry repo from Verilator build
    
    HDL constructs in the foundry repo are preventing Verilator builds from
    succeeding. This is addresses #15882 in the short term, by excluding the
    foundry repo from Verilator sim binary builds.
    
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
