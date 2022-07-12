import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13029"
version_tuple = (0, 0, 13029)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13029")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12887"
data_version_tuple = (0, 0, 12887)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12887")
except ImportError:
    pass
data_git_hash = "7e2e6096a30cc74561300db7fb19fb4b12742f2f"
data_git_describe = "v0.0-12887-g7e2e6096a3"
data_git_msg = """\
commit 7e2e6096a30cc74561300db7fb19fb4b12742f2f
Author: Chris Frantz <cfrantz@google.com>
Date:   Mon Jul 11 14:34:19 2022 -0700

    [mask_rom] Allow tests to have a `.data` section.
    
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
