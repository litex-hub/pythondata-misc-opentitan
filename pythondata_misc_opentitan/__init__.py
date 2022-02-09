import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10183"
version_tuple = (0, 0, 10183)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10183")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10059"
data_version_tuple = (0, 0, 10059)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10059")
except ImportError:
    pass
data_git_hash = "d980684e2586a03c852196780c1e2ccd6467cf6b"
data_git_describe = "v0.0-10059-gd980684e2"
data_git_msg = """\
commit d980684e2586a03c852196780c1e2ccd6467cf6b
Author: Martin Lueker-Boden <martin.lueker-boden@wdc.com>
Date:   Tue Feb 8 09:22:45 2022 -0800

    [pwm/rtl] Handle rounding errors in pwm_chan
    
    This commit simplifies the duty_cycle rounding arithmetic in pwm_chan.
    The solution (as before) is to zero out unused bits in either the
    commanded phase_delay or the actual duty cycle.
    
    Signed-off-by: Martin Lueker-Boden <martin.lueker-boden@wdc.com>

"""

# Tool version info
tool_version_str = "0.0.post124"
tool_version_tuple = (0, 0, 124)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post124")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
