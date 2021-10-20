import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8362"
version_tuple = (0, 0, 8362)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8362")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8250"
data_version_tuple = (0, 0, 8250)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8250")
except ImportError:
    pass
data_git_hash = "72c3314692fb3ba4440c9bdc03919645689798fb"
data_git_describe = "v0.0-8250-g72c331469"
data_git_msg = """\
commit 72c3314692fb3ba4440c9bdc03919645689798fb
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Wed Oct 20 17:13:55 2021 +0100

    [otbn,dv] Correct an assertion in BadBranch generator
    
    We mis-counted the number of branches!
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

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
