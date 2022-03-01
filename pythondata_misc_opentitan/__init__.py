import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10612"
version_tuple = (0, 0, 10612)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10612")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10486"
data_version_tuple = (0, 0, 10486)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10486")
except ImportError:
    pass
data_git_hash = "059578e555cb1319577dda5042163406d83368e8"
data_git_describe = "v0.0-10486-g059578e55"
data_git_msg = """\
commit 059578e555cb1319577dda5042163406d83368e8
Author: Timothy Trippel <ttrippel@google.com>
Date:   Fri Feb 25 20:04:55 2022 -0800

    [dif/alert_handler] Fix DIF doxygen comments
    
    This fixes some typos in a handful of alert_handler DIF comments that
    get rendered as API documentation via doxygen.
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

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
