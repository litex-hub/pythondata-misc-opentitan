import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12839"
version_tuple = (0, 0, 12839)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12839")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12697"
data_version_tuple = (0, 0, 12697)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12697")
except ImportError:
    pass
data_git_hash = "4a9e9fbb6c91e25ddfe5612b740ccadbb53e61ba"
data_git_describe = "v0.0-12697-g4a9e9fbb6c"
data_git_msg = """\
commit 4a9e9fbb6c91e25ddfe5612b740ccadbb53e61ba
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Fri Jun 24 11:38:32 2022 -0700

    [formal/conn] Update chip level connectivity csvs
    
    This PR updates two mismatches in connectivity test:
    1). Fix an ibex memory path
    2). Fix usb clock connection
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post142"
tool_version_tuple = (0, 0, 142)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post142")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
