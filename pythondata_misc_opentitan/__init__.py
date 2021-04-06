import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5723"
version_tuple = (0, 0, 5723)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5723")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5628"
data_version_tuple = (0, 0, 5628)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5628")
except ImportError:
    pass
data_git_hash = "751a37dd5cee1822c6c706c1c9a4f9210f322997"
data_git_describe = "v0.0-5628-g751a37dd5"
data_git_msg = """\
commit 751a37dd5cee1822c6c706c1c9a4f9210f322997
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Mon Apr 5 11:13:40 2021 +0100

    [otp_ctrl,lint] Explicitly compare multi-bit signals with zero
    
    This is actually in our style guide ("Do not use multi-bit signals in
    a boolean context"). The implicit boolean conversion also caused a
    Verilator width warning. Use the relevant enum value (NoError)
    instead.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

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
