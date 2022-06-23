import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12806"
version_tuple = (0, 0, 12806)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12806")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12664"
data_version_tuple = (0, 0, 12664)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12664")
except ImportError:
    pass
data_git_hash = "1e4c69cf1e0bbe4aebd3e3a8c1f8673860964cbb"
data_git_describe = "v0.0-12664-g1e4c69cf1e"
data_git_msg = """\
commit 1e4c69cf1e0bbe4aebd3e3a8c1f8673860964cbb
Author: Viswanadha Bazawada <viswanadha.bazawada@ensilica.com>
Date:   Wed Jun 22 23:04:46 2022 +0100

    [SPI/DV] Regression Failure Fixes And Testplan Update
    
    - Fixed regression failures
    - Testplan update for unmapped tests
    
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
