import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8995"
version_tuple = (0, 0, 8995)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8995")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8883"
data_version_tuple = (0, 0, 8883)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8883")
except ImportError:
    pass
data_git_hash = "9cb3da85f2a1c8c84e38913b6febac9d40b49446"
data_git_describe = "v0.0-8883-g9cb3da85f"
data_git_msg = """\
commit 9cb3da85f2a1c8c84e38913b6febac9d40b49446
Author: Guillermo Maturana <maturana@google.com>
Date:   Tue Nov 30 20:06:05 2021 -0800

    [dv/pwrmgr] Add lowpower wakeup race test
    
    Add ignore_bins directive for no reset case.
    Add sw_rst_req_i to interface in order to trigger sw resets.
    Enhance reset_cg for sw_rst and improve crosses.
    Fix sampling of wakeup_status in interface.
    
    Signed-off-by: Guillermo Maturana <maturana@google.com>

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
