import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15129"
version_tuple = (0, 0, 15129)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15129")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14987"
data_version_tuple = (0, 0, 14987)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14987")
except ImportError:
    pass
data_git_hash = "3b4b30e4875994e1c91619e99bcc6789e9b8cedc"
data_git_describe = "v0.0-14987-g3b4b30e487"
data_git_msg = """\
commit 3b4b30e4875994e1c91619e99bcc6789e9b8cedc
Author: Alphan Ulusoy <alphan@google.com>
Date:   Tue Nov 1 15:31:18 2022 -0400

    [test] Run rom_e2e_shutdown_output for remaining life cycle states
    
    Fixes #14270
    
    Signed-off-by: Alphan Ulusoy <alphan@google.com>

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
