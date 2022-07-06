import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12944"
version_tuple = (0, 0, 12944)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12944")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12802"
data_version_tuple = (0, 0, 12802)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12802")
except ImportError:
    pass
data_git_hash = "9591e1f25d02e10673e259d9c29b42bf0686bfcc"
data_git_describe = "v0.0-12802-g9591e1f25d"
data_git_msg = """\
commit 9591e1f25d02e10673e259d9c29b42bf0686bfcc
Author: Muqing Liu <muqing.liu@wdc.com>
Date:   Thu Jun 30 13:25:11 2022 -0700

    [pwm, rtl] PWM RTL fix for duty cycle overflow/underflow
    
      - Fix the PWM RTL duty cycle overflow/underflow issue to match the spec
      - Fixes #13434
    
    Signed-off-by: Muqing Liu <muqing.liu@wdc.com>

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
