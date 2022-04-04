import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11353"
version_tuple = (0, 0, 11353)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11353")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11227"
data_version_tuple = (0, 0, 11227)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11227")
except ImportError:
    pass
data_git_hash = "8d799de2f298a08519de2b5de7ff6b46ab5e9f07"
data_git_describe = "v0.0-11227-g8d799de2f"
data_git_msg = """\
commit 8d799de2f298a08519de2b5de7ff6b46ab5e9f07
Author: Chris Frantz <cfrantz@google.com>
Date:   Mon Apr 4 11:19:15 2022 -0700

    [cleanup] Fix license checker after #11851
    
    1. Exclude //third_party from license checks.
    2. Add license headers to a few files.
    
    Signed-off-by: Chris Frantz <cfrantz@google.com>

"""

# Tool version info
tool_version_str = "0.0.post126"
tool_version_tuple = (0, 0, 126)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post126")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
