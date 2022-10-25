import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14930"
version_tuple = (0, 0, 14930)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14930")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14788"
data_version_tuple = (0, 0, 14788)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14788")
except ImportError:
    pass
data_git_hash = "0b7703e3a53abcfbf49e762e8448c1f6d6bb605d"
data_git_describe = "v0.0-14788-g0b7703e3a5"
data_git_msg = """\
commit 0b7703e3a53abcfbf49e762e8448c1f6d6bb605d
Author: Arun Thomas <arunthomas@google.com>
Date:   Thu Jul 14 14:41:50 2022 -0400

    [bazel] Update CoreMark version
    
    * Import files from commit eefc986ebd3452d6adde22eafaff3e5c859f29e4
    * Update OpenTitan port
    
    Signed-off-by: Arun Thomas <arunthomas@google.com>

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
