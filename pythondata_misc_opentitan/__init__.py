import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14416"
version_tuple = (0, 0, 14416)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14416")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14274"
data_version_tuple = (0, 0, 14274)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14274")
except ImportError:
    pass
data_git_hash = "40ac0e7b8706ab20743cb23ccc4b518901b82832"
data_git_describe = "v0.0-14274-g40ac0e7b87"
data_git_msg = """\
commit 40ac0e7b8706ab20743cb23ccc4b518901b82832
Author: Chris Frantz <cfrantz@google.com>
Date:   Wed Sep 21 11:40:11 2022 -0700

    [ottool] Fix invocations of `opentitantool` by bazel
    
    Invocations of `opentitantool` under bazel automation should always
    include `--rcfile=` to prevent parsing the user's local configuration.
    
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
