import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8196"
version_tuple = (0, 0, 8196)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8196")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8084"
data_version_tuple = (0, 0, 8084)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8084")
except ImportError:
    pass
data_git_hash = "5733445f8032d616b1179591c37c2264f6b217ec"
data_git_describe = "v0.0-8084-g5733445f8"
data_git_msg = """\
commit 5733445f8032d616b1179591c37c2264f6b217ec
Author: Muqing Liu <muqing.liu@wdc.com>
Date:   Wed Oct 6 11:17:28 2021 -0700

    [pwm, rtl] PWM D2 checklist update
    
      - Update the D2 checklist for PWM module
      - Update pwm.prj.hjson file to D2 design stage
    
    Signed-off-by: Muqing Liu <muqing.liu@wdc.com>

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
