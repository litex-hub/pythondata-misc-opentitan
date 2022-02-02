import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9980"
version_tuple = (0, 0, 9980)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9980")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9856"
data_version_tuple = (0, 0, 9856)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9856")
except ImportError:
    pass
data_git_hash = "793f62345064f1944db99f1fd3fd490248f0dee3"
data_git_describe = "v0.0-9856-g793f62345"
data_git_msg = """\
commit 793f62345064f1944db99f1fd3fd490248f0dee3
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Tue Feb 1 14:00:02 2022 -0800

    [dv/kmac] Shadow reg common test
    
    This PR adds shadow reg common tests to kmac.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

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
