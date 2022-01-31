import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9923"
version_tuple = (0, 0, 9923)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9923")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9799"
data_version_tuple = (0, 0, 9799)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9799")
except ImportError:
    pass
data_git_hash = "647f929903e33d2eef25506487522ae13de8296e"
data_git_describe = "v0.0-9799-g647f92990"
data_git_msg = """\
commit 647f929903e33d2eef25506487522ae13de8296e
Author: Timothy Chen <timothytim@google.com>
Date:   Thu Jan 27 22:25:32 2022 -0800

    [top] Verilator enhancements for new ast POR
    
    - toggle vcc_supp to emulate power on reset
    - this ensures AST's internal logic is correctly reset and can accept future por requests
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
