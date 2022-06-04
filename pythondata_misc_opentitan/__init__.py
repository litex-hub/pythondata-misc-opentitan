import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12501"
version_tuple = (0, 0, 12501)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12501")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12359"
data_version_tuple = (0, 0, 12359)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12359")
except ImportError:
    pass
data_git_hash = "e4effa3a6b67c9c5a7a536873b58e3e4fbdc93c3"
data_git_describe = "v0.0-12359-ge4effa3a6"
data_git_msg = """\
commit e4effa3a6b67c9c5a7a536873b58e3e4fbdc93c3
Author: Miguel Osorio <miguelosorio@google.com>
Date:   Fri May 27 10:35:50 2022 -0700

    [sw/silicon_creator] Update keymgr functest
    
    Update the keymgr functest to use software initiated reset instead of
    low power entry/exit. Also update flash and OTP configuration to use
    available device testutils.
    
    Signed-off-by: Miguel Osorio <miguelosorio@google.com>

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
