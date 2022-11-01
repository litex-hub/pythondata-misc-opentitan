import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15092"
version_tuple = (0, 0, 15092)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15092")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14950"
data_version_tuple = (0, 0, 14950)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14950")
except ImportError:
    pass
data_git_hash = "6f00d58c2028dcd984d0c56ac6bc9a3a6b530880"
data_git_describe = "v0.0-14950-g6f00d58c20"
data_git_msg = """\
commit 6f00d58c2028dcd984d0c56ac6bc9a3a6b530880
Author: Srikrishna Iyer <sriyer@google.com>
Date:   Mon Oct 31 10:57:43 2022 -0700

    [prim-lfsr] Fix DefaultSeedLocal compile scope
    
    Use `ifdef SIMULATION` compilation scope for DefaultSeedLocal`
    setting in prim_lfsr / prim_double_lfsr.
    
    Signed-off-by: Srikrishna Iyer <sriyer@google.com>

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
