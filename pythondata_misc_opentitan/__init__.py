import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12408"
version_tuple = (0, 0, 12408)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12408")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12268"
data_version_tuple = (0, 0, 12268)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12268")
except ImportError:
    pass
data_git_hash = "6c79c3b8b387f39aad3aecb2d985a8c06b76cc34"
data_git_describe = "v0.0-12268-g6c79c3b8b"
data_git_msg = """\
commit 6c79c3b8b387f39aad3aecb2d985a8c06b76cc34
Author: Steve Nelson <steve.nelson@wdc.com>
Date:   Fri May 27 11:43:14 2022 -0700

    [edn/dv] Change type from bit->mubi4_t, remove redundant constraints
    
    Signed-off-by: Steve Nelson <steve.nelson@wdc.com>

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
