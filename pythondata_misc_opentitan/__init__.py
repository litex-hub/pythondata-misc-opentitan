import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12739"
version_tuple = (0, 0, 12739)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12739")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12597"
data_version_tuple = (0, 0, 12597)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12597")
except ImportError:
    pass
data_git_hash = "0bbd8c6911c0bddc1d7679c7373c2f02a39c2542"
data_git_describe = "v0.0-12597-g0bbd8c6911"
data_git_msg = """\
commit 0bbd8c6911c0bddc1d7679c7373c2f02a39c2542
Author: Vladimir Rozic <vrozic@lowrisc.org>
Date:   Tue Jun 7 12:52:35 2022 +0100

    [sca] Batch-capture support for KMAC fixed-vs-random key.
    
    Signed-off-by: Vladimir Rozic <vrozic@lowrisc.org>

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
