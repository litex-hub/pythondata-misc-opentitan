import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5862"
version_tuple = (0, 0, 5862)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5862")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5767"
data_version_tuple = (0, 0, 5767)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5767")
except ImportError:
    pass
data_git_hash = "0e8660b15f0f27bfbadc7dacfd0aae0542be3b0e"
data_git_describe = "v0.0-5767-g0e8660b15"
data_git_msg = """\
commit 0e8660b15f0f27bfbadc7dacfd0aae0542be3b0e
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Mon Apr 12 14:59:18 2021 +0100

    [top] Slightly tidy up some auto-generated signals
    
    Group together adjacent bits into a range select to make the generated
    code a bit easier to read.
    
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
