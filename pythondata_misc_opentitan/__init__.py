import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10530"
version_tuple = (0, 0, 10530)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10530")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10404"
data_version_tuple = (0, 0, 10404)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10404")
except ImportError:
    pass
data_git_hash = "11ff5c933d91a510661e2ea09c20cf6fbc835d49"
data_git_describe = "v0.0-10404-g11ff5c933"
data_git_msg = """\
commit 11ff5c933d91a510661e2ea09c20cf6fbc835d49
Author: Madhuri Patel <madhuri.patel@ensilica.com>
Date:   Thu Jan 6 14:21:46 2022 +0000

    [sysrst_ctrl,dv] Add sysrst_ctrl EC power-on-reset test
    
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
