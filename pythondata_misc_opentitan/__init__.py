import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12573"
version_tuple = (0, 0, 12573)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12573")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12431"
data_version_tuple = (0, 0, 12431)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12431")
except ImportError:
    pass
data_git_hash = "2f640af93a68580265ede307c6129e4e153a8116"
data_git_describe = "v0.0-12431-g2f640af93"
data_git_msg = """\
commit 2f640af93a68580265ede307c6129e4e153a8116
Author: Chris Frantz <cfrantz@google.com>
Date:   Wed Jun 8 08:20:41 2022 -0700

    [cleanup] Make `bazelisk.sh` operate in the workspace
    
    The `bazelisk.sh` script should chdir to its containing subdirectory
    so that it always operates in the project's workspace.  This will allow
    other projects (e.g. tock) to invoke bazelisk to build binaries or
    execute tools.
    
    Signed-off-by: Chris Frantz <cfrantz@google.com>

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
