import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5727"
version_tuple = (0, 0, 5727)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5727")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5632"
data_version_tuple = (0, 0, 5632)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5632")
except ImportError:
    pass
data_git_hash = "77106b793f5b60d6323d53c885f1d47d1efff76d"
data_git_describe = "v0.0-5632-g77106b793"
data_git_msg = """\
commit 77106b793f5b60d6323d53c885f1d47d1efff76d
Author: Colin O'Flynn <coflynn@newae.com>
Date:   Tue Apr 6 10:14:22 2021 -0300

    [doc] Remove separate doc build package list
    
    Signed-off-by: Colin O'Flynn <coflynn@newae.com>

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
