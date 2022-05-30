import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12405"
version_tuple = (0, 0, 12405)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12405")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12265"
data_version_tuple = (0, 0, 12265)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12265")
except ImportError:
    pass
data_git_hash = "510f1832bbd6179042e29884c765c82c41cce4b1"
data_git_describe = "v0.0-12265-g510f1832b"
data_git_msg = """\
commit 510f1832bbd6179042e29884c765c82c41cce4b1
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Sun May 29 23:19:08 2022 +0100

    [otbn,dv] Correct bogus assertion in on_otp_cdc_done
    
    I'd forgotten that we also rotate memory keys when locking on a fatal
    error.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post140"
tool_version_tuple = (0, 0, 140)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post140")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
