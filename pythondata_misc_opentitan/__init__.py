import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5858"
version_tuple = (0, 0, 5858)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5858")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5763"
data_version_tuple = (0, 0, 5763)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5763")
except ImportError:
    pass
data_git_hash = "07302adc818271b9d2d7e1c3c353053955183121"
data_git_describe = "v0.0-5763-g07302adc8"
data_git_msg = """\
commit 07302adc818271b9d2d7e1c3c353053955183121
Author: Timothy Chen <timothytim@google.com>
Date:   Tue Apr 13 11:50:31 2021 -0700

    [pwrmgr] Create an early indication of pwr_clamp
    
    The pwr_clamp_early signal asserts before pwr_clamp and de-asserts
    after pwr_clamp.
    
    This gives some modules an early indication that pwr_clamp is about
    to assert envelopes the pwr_clamp signal in timing.
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
