import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13050"
version_tuple = (0, 0, 13050)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13050")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12908"
data_version_tuple = (0, 0, 12908)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12908")
except ImportError:
    pass
data_git_hash = "3fd4423be52e699214d629c397ef12b54d891d3e"
data_git_describe = "v0.0-12908-g3fd4423be5"
data_git_msg = """\
commit 3fd4423be52e699214d629c397ef12b54d891d3e
Author: Guillermo Maturana <maturana@google.com>
Date:   Mon Jul 11 15:59:04 2022 -0700

    [dv,chip,clkmgr] Make expected cycle counts device-independent
    
    Compute the expected cycle counts from the device frequencies. This was
    formerly done so it predicted sim_dv counts only, and other devices
    (like fpga or verilator) would get wrong predictions.
    
    Signed-off-by: Guillermo Maturana <maturana@google.com>

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
