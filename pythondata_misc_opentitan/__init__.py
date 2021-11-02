import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8566"
version_tuple = (0, 0, 8566)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8566")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8454"
data_version_tuple = (0, 0, 8454)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8454")
except ImportError:
    pass
data_git_hash = "3eed80ec7ff241e51508ac9434f1bf48eea3da14"
data_git_describe = "v0.0-8454-g3eed80ec7"
data_git_msg = """\
commit 3eed80ec7ff241e51508ac9434f1bf48eea3da14
Author: Weicai Yang <weicai@google.com>
Date:   Mon Nov 1 11:36:47 2021 -0700

    [dv] change kmac_sideload_if to a common sideload if
    
    Also changed to a parameterized interface so that it can be resued for
    otbn
    Addressed #8944
    Signed-off-by: Weicai Yang <weicai@google.com>

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
