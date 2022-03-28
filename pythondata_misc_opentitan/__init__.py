import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11150"
version_tuple = (0, 0, 11150)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11150")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11024"
data_version_tuple = (0, 0, 11024)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11024")
except ImportError:
    pass
data_git_hash = "983c46c1ecf86f4ef3e4ab0b93e185d1c373ebd3"
data_git_describe = "v0.0-11024-g983c46c1e"
data_git_msg = """\
commit 983c46c1ecf86f4ef3e4ab0b93e185d1c373ebd3
Author: Madhuri Patel <madhuri.patel@ensilica.com>
Date:   Thu Mar 24 21:45:19 2022 +0000

    [sysrst_ctrl,dv] Add misc fix
    
    This pull request has misc fix for the failing tests in regression
    
    Signed-off-by: Madhuri Patel <madhuri.patel@ensilica.com>

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
