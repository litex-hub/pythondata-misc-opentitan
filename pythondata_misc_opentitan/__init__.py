import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8546"
version_tuple = (0, 0, 8546)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8546")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8434"
data_version_tuple = (0, 0, 8434)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8434")
except ImportError:
    pass
data_git_hash = "ddcfe93f1f669f192ff4a33f1c19d827663a921f"
data_git_describe = "v0.0-8434-gddcfe93f1"
data_git_msg = """\
commit ddcfe93f1f669f192ff4a33f1c19d827663a921f
Author: Michael Schaffner <msf@opentitan.org>
Date:   Tue Oct 26 15:24:23 2021 -0700

    Update pulp_riscv_dbg to pulp-platform/riscv-dbg@4befe83
    
    Update code from upstream repository https://github.com/pulp-
    platform/riscv-dbg to revision
    4befe83b03f43cef72486e0078cca0126e2680a0
    
    Signed-off-by: Michael Schaffner <msf@opentitan.org>

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
