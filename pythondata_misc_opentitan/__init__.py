import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8640"
version_tuple = (0, 0, 8640)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8640")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8528"
data_version_tuple = (0, 0, 8528)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8528")
except ImportError:
    pass
data_git_hash = "31d5baad1cf10b5497b8541c28ed3384f2842f6e"
data_git_describe = "v0.0-8528-g31d5baad1"
data_git_msg = """\
commit 31d5baad1cf10b5497b8541c28ed3384f2842f6e
Author: Michael Munday <mike.munday@lowrisc.org>
Date:   Tue Nov 9 13:27:07 2021 +0000

    [CODEOWNERS] Add organization prefix to teams
    
    Teams need to prefixed with the organization name to be assigned as
    reviewers.
    
    Signed-off-by: Michael Munday <mike.munday@lowrisc.org>

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
