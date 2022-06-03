import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12493"
version_tuple = (0, 0, 12493)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12493")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12351"
data_version_tuple = (0, 0, 12351)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12351")
except ImportError:
    pass
data_git_hash = "7be036f3ce1c3b99b9eaafaf30207f9e62d916ef"
data_git_describe = "v0.0-12351-g7be036f3c"
data_git_msg = """\
commit 7be036f3ce1c3b99b9eaafaf30207f9e62d916ef
Author: Viswanadha Bazawada <viswanadha.bazawada@ensilica.com>
Date:   Sun May 22 22:48:33 2022 +0100

    [SPI_HOST/DV] Regression FIX and Assertion Cov
    
    - Regression Fixes For Over & Under Flow Test
    - Assertion Coverage Test for Reg Rd
    - Coverage Sample Status Reg Changed
    - Removed Assertion Coverage Test
    - Refactored Error Cmd Test
    - Added Assertions Passthrough
    - Added Spi Host Status Stall Test
    - Added Regression Failures Fix Performance Test
    - Added Regression Failures Fix Error Cmd Test
    - Removed Spi Host Status Stall Test Will be Added Seperate PR
    
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
