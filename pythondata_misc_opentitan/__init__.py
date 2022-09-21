import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14356"
version_tuple = (0, 0, 14356)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14356")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14214"
data_version_tuple = (0, 0, 14214)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14214")
except ImportError:
    pass
data_git_hash = "75b37362afef4de946b109d584df385ef226bc84"
data_git_describe = "v0.0-14214-g75b37362af"
data_git_msg = """\
commit 75b37362afef4de946b109d584df385ef226bc84
Author: Jacob Levy <jacob.levy@nuvoton.com>
Date:   Wed Sep 21 10:01:52 2022 +0300

    [adc_crrl test] Fix ADC enum kPower-upTimeAonCycles from 2 to 6
    
    Signed-off-by: Jacob Levy <jacob.levy@nuvoton.com>

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
