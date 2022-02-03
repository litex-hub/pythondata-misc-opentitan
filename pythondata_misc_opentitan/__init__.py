import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10039"
version_tuple = (0, 0, 10039)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10039")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9915"
data_version_tuple = (0, 0, 9915)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9915")
except ImportError:
    pass
data_git_hash = "262651b7db24d593b5ac697b6701da0ed3123628"
data_git_describe = "v0.0-9915-g262651b7d"
data_git_msg = """\
commit 262651b7db24d593b5ac697b6701da0ed3123628
Author: Eunchan Kim <eunchan@opentitan.org>
Date:   Wed Feb 2 18:31:29 2022 -0800

    [gpio] Waive Reconvergence CDC warning
    
    As GPIO inputs are not assumed as a bus signal, it is OK to just 2FF
    PAD_IN values.
    
    Signed-off-by: Eunchan Kim <eunchan@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post124"
tool_version_tuple = (0, 0, 124)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post124")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
