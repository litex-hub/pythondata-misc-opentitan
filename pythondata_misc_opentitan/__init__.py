import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5189"
version_tuple = (0, 0, 5189)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5189")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5098"
data_version_tuple = (0, 0, 5098)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5098")
except ImportError:
    pass
data_git_hash = "383afb8a89e12c5c761c2222b2efa8b582bcf579"
data_git_describe = "v0.0-5098-g383afb8a8"
data_git_msg = """\
commit 383afb8a89e12c5c761c2222b2efa8b582bcf579
Author: Timothy Chen <timothytim@google.com>
Date:   Tue Feb 23 13:18:53 2021 -0800

    [top] Connect pwrmgr functions to pinmux and aon_timer
    
    - Add strap_o output to control strap timing after life cycle control initialization
    - Add low_power_o output to inform each module we are in low power mode
    - Swithc pinmux to powerup clock group to ensure it has clocks to handle the low power indication
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

"""

# Tool version info
tool_version_str = "0.0.post91"
tool_version_tuple = (0, 0, 91)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post91")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
