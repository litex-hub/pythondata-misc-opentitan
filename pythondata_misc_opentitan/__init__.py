import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12785"
version_tuple = (0, 0, 12785)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12785")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12643"
data_version_tuple = (0, 0, 12643)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12643")
except ImportError:
    pass
data_git_hash = "a9f679394bdcb5fbb388145b1c605da6cab022a5"
data_git_describe = "v0.0-12643-ga9f679394b"
data_git_msg = """\
commit a9f679394bdcb5fbb388145b1c605da6cab022a5
Author: Drew Macrae <drewmacrae@google.com>
Date:   Wed Jun 15 14:27:02 2022 -0400

    [bazel] pwrmgr_deep_sleep_all_wake_ups isn't broken on other platforms
    
    Signed-off-by: Drew Macrae <drewmacrae@google.com>

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
