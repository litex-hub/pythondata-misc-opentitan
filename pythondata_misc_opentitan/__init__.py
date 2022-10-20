import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14858"
version_tuple = (0, 0, 14858)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14858")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14716"
data_version_tuple = (0, 0, 14716)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14716")
except ImportError:
    pass
data_git_hash = "f17833bf0ea781f2f6bc0e975075720143bccee3"
data_git_describe = "v0.0-14716-gf17833bf0e"
data_git_msg = """\
commit f17833bf0ea781f2f6bc0e975075720143bccee3
Author: Timothy Chen <timothytim@google.com>
Date:   Tue Oct 18 13:30:21 2022 -0700

    [top/dv] Adjust setup for floating pin.
    
    - Previously, the test would enable the UART RX pins without
      a pull-up.  This meant that until the test bench environment
      actively drove, the pin was left floating and cause x propagation.
    
    - This update just sets the pull-up at the same time as enabling the
      pin to ensure this situation does not come up.  The pull-up setting
      is platform dependent since verilator / fpga do not have pull-up
      capabilities and must be excluded.
    
    - Similarly, the pull-up must be excluded for englishbreakfast since
      certain registers do not exist in that space.
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
