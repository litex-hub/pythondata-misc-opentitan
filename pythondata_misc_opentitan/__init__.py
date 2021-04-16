import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5930"
version_tuple = (0, 0, 5930)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5930")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5835"
data_version_tuple = (0, 0, 5835)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5835")
except ImportError:
    pass
data_git_hash = "38f5cac489b1a30ee1555866178423327d4bcf53"
data_git_describe = "v0.0-5835-g38f5cac48"
data_git_msg = """\
commit 38f5cac489b1a30ee1555866178423327d4bcf53
Author: Mark Branstad <mark.branstad@wdc.com>
Date:   Wed Apr 14 07:34:23 2021 -0700

    [csrng/rtl] added tracking sm fields to reg for debug
    
    The csrng command tracking state machine values have now been attached to an
    observation register.
    
    Signed-off-by: Mark Branstad <mark.branstad@wdc.com>

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
