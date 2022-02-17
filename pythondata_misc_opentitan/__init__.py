import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10384"
version_tuple = (0, 0, 10384)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10384")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10258"
data_version_tuple = (0, 0, 10258)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10258")
except ImportError:
    pass
data_git_hash = "79e6216d6531cd72e276dadb72e3871e3bfc03c6"
data_git_describe = "v0.0-10258-g79e6216d6"
data_git_msg = """\
commit 79e6216d6531cd72e276dadb72e3871e3bfc03c6
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Tue Feb 15 21:59:58 2022 -0800

    [dv/kmac] Add entropy_mode error support
    
    This PR creates error case when entropy_mode is configured incorrectly.
    Then it will check err_code, interrupt, and make sure kmac can operate
    correct afterwards.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

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
