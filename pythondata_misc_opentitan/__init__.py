import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12826"
version_tuple = (0, 0, 12826)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12826")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12684"
data_version_tuple = (0, 0, 12684)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12684")
except ImportError:
    pass
data_git_hash = "3a97dbfaad9847ca68614f46f1369298745c7a76"
data_git_describe = "v0.0-12684-g3a97dbfaad"
data_git_msg = """\
commit 3a97dbfaad9847ca68614f46f1369298745c7a76
Author: Timothy Chen <timothytim@google.com>
Date:   Thu Jun 23 15:07:43 2022 -0700

    [dv] Add build rule for sensor_ctrl_status
    
    - also move to sim_dv directory since this test does not work
      for fpga / verilator natively
    
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
