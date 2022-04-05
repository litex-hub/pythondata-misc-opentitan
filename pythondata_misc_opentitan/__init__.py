import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11389"
version_tuple = (0, 0, 11389)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11389")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11263"
data_version_tuple = (0, 0, 11263)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11263")
except ImportError:
    pass
data_git_hash = "ec8fe82b8066af71aabdee1cd8baefac8a0a4251"
data_git_describe = "v0.0-11263-gec8fe82b8"
data_git_msg = """\
commit ec8fe82b8066af71aabdee1cd8baefac8a0a4251
Author: Chris Frantz <cfrantz@google.com>
Date:   Tue Apr 5 10:10:41 2022 -0700

    [cleanup] Fix spelling error
    
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
