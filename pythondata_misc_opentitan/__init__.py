import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12958"
version_tuple = (0, 0, 12958)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12958")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12816"
data_version_tuple = (0, 0, 12816)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12816")
except ImportError:
    pass
data_git_hash = "498cdc60b4719bf232a1fdc586ff3addd58c5961"
data_git_describe = "v0.0-12816-g498cdc60b4"
data_git_msg = """\
commit 498cdc60b4719bf232a1fdc586ff3addd58c5961
Author: Viswanadha Bazawada <viswanadha.bazawada@ensilica.com>
Date:   Tue Jun 28 12:18:05 2022 +0100

    [SPI_HOST/DV] Regression Fixes
    
    - Fixed event test when txwm is set 1
    - Txwm and Rxwm checked for edge trigger
    - Fixed txwm and rxwm entries constraint cannot be 0
    - Check event task modified to check intr and state values
    
    Signed-off-by: Viswanadha Bazawada <viswanadha.bazawada@ensilica.com>

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
