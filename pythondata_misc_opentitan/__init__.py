import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12291"
version_tuple = (0, 0, 12291)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12291")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12163"
data_version_tuple = (0, 0, 12163)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12163")
except ImportError:
    pass
data_git_hash = "b56dcf8f01f9cbd87c52e597c3f3b28da786211c"
data_git_describe = "v0.0-12163-gb56dcf8f0"
data_git_msg = """\
commit b56dcf8f01f9cbd87c52e597c3f3b28da786211c
Author: Douglas Reis <doreis@lowrisc.org>
Date:   Fri May 20 18:15:27 2022 +0100

    [test, aes] Fix aes_idle chip test in the nightly regression
    
    Signed-off-by: Douglas Reis <doreis@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post128"
tool_version_tuple = (0, 0, 128)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post128")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
