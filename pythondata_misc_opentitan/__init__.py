import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13069"
version_tuple = (0, 0, 13069)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13069")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12927"
data_version_tuple = (0, 0, 12927)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12927")
except ImportError:
    pass
data_git_hash = "0f7566f207657f39cb045ca18c97c3caef94c22c"
data_git_describe = "v0.0-12927-g0f7566f207"
data_git_msg = """\
commit 0f7566f207657f39cb045ca18c97c3caef94c22c
Author: Guillermo Maturana <maturana@google.com>
Date:   Tue Jul 12 14:55:03 2022 -0700

    [dv,chip,rstmgr] Send AON power glitch after CPU is up
    
    Enhance chip_sw_pwrmgr_full_aon_reset test to send an AON power glitch
    once the CPU is running.
    
    Fixes #13502
    
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
