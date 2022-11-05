import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15261"
version_tuple = (0, 0, 15261)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15261")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post15119"
data_version_tuple = (0, 0, 15119)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post15119")
except ImportError:
    pass
data_git_hash = "84179cd4bea2a52f171d7583300bdeda4f141ce8"
data_git_describe = "v0.0-15119-g84179cd4be"
data_git_msg = """\
commit 84179cd4bea2a52f171d7583300bdeda4f141ce8
Author: Dan McArdle <dmcardle@google.com>
Date:   Thu Nov 3 16:27:36 2022 -0400

    [ci] Remove deprecated OpenOCD arg from package installer
    
    This commit causes ci/install-package-dependencies.sh to fail when it
    receives --openocd-version.
    
    Now that private CI is no longer specifying the --openocd-version flag,
    we should stop ignoring the flag.
    
    Signed-off-by: Dan McArdle <dmcardle@google.com>

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
