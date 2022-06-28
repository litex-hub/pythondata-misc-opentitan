import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12872"
version_tuple = (0, 0, 12872)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12872")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12730"
data_version_tuple = (0, 0, 12730)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12730")
except ImportError:
    pass
data_git_hash = "b342745890ee3faeeb4db1db6aae6b5857c165c2"
data_git_describe = "v0.0-12730-gb342745890"
data_git_msg = """\
commit b342745890ee3faeeb4db1db6aae6b5857c165c2
Author: Muqing Liu <muqing.liu@wdc.com>
Date:   Mon Jun 27 10:27:27 2022 -0700

    [pwm, rtl] PWM RTL fix for issue mentioned in PR#13295
    
      - Fix the duty cycle state transistion issue in heart beat mode
    
    Signed-off-by: Muqing Liu <muqing.liu@wdc.com>
    Signed-off-by: Michael Schaffner <msf@opentitan.org>

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
