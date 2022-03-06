import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10731"
version_tuple = (0, 0, 10731)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10731")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10605"
data_version_tuple = (0, 0, 10605)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10605")
except ImportError:
    pass
data_git_hash = "59181de51c70b3cd6eff7037c302dca775bd7d82"
data_git_describe = "v0.0-10605-g59181de51"
data_git_msg = """\
commit 59181de51c70b3cd6eff7037c302dca775bd7d82
Author: Timothy Chen <timothytim@google.com>
Date:   Fri Mar 4 15:15:04 2022 -0800

    [adc_ctrl] Adjust fsm power-up timing and counter clearing
    
    - fixes #11256
    - Adjust fsm's such that initial power-up to sample and low power exit
      to sample have the same timing.  The IDLE state is removed as a result.
    - Update documentation to reflect change
    - Clear counters on adc disable otherwise the old count value carries over
      and affects the next round of detection.
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

"""

# Tool version info
tool_version_str = "0.0.post126"
tool_version_tuple = (0, 0, 126)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post126")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
