import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10902"
version_tuple = (0, 0, 10902)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10902")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10776"
data_version_tuple = (0, 0, 10776)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10776")
except ImportError:
    pass
data_git_hash = "d00f90249ca5008689420f7cc79a9d40b703bff4"
data_git_describe = "v0.0-10776-gd00f90249"
data_git_msg = """\
commit d00f90249ca5008689420f7cc79a9d40b703bff4
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Mon Mar 14 16:57:27 2022 -0700

    [conn] Update conn csv tests
    
    This PR cleans up the conn csv format:
    1). Implemented ports from src to dst
    2). Add spaces for readability
    3). Update some namings so it is easier to debug
    
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
