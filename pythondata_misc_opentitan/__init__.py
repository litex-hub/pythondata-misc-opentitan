import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8299"
version_tuple = (0, 0, 8299)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8299")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8187"
data_version_tuple = (0, 0, 8187)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8187")
except ImportError:
    pass
data_git_hash = "2db51d2441bb2c9e643774432c0ae45f6b09e33d"
data_git_describe = "v0.0-8187-g2db51d244"
data_git_msg = """\
commit 2db51d2441bb2c9e643774432c0ae45f6b09e33d
Author: Mark Branstad <mark.branstad@wdc.com>
Date:   Thu Oct 14 07:21:01 2021 -0700

    [entropy_src/rtl] fix rng bit mode
    
    RNG bit mode is a diagnostic mode that needed a bug fix.
    
    Signed-off-by: Mark Branstad <mark.branstad@wdc.com>

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
