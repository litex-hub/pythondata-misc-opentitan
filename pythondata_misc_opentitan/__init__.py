import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11317"
version_tuple = (0, 0, 11317)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11317")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11191"
data_version_tuple = (0, 0, 11191)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11191")
except ImportError:
    pass
data_git_hash = "4d69eb2c229973a0aa43ffab60721504ce79e0bc"
data_git_describe = "v0.0-11191-g4d69eb2c2"
data_git_msg = """\
commit 4d69eb2c229973a0aa43ffab60721504ce79e0bc
Author: Madhuri Patel <madhuri.patel@ensilica.com>
Date:   Thu Mar 31 10:33:22 2022 +0100

    [sysrst_ctrl,dv] Add sysrst_ctrl stress_all test
    
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
