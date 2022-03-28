import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11161"
version_tuple = (0, 0, 11161)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11161")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11035"
data_version_tuple = (0, 0, 11035)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11035")
except ImportError:
    pass
data_git_hash = "68ce21e57a229c356b742752f007db49d44d884c"
data_git_describe = "v0.0-11035-g68ce21e57"
data_git_msg = """\
commit 68ce21e57a229c356b742752f007db49d44d884c
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Fri Mar 25 17:21:35 2022 -0700

    [conn] connectivity test naming fix
    
    This PR fixed a duplicated naming error.
    
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
