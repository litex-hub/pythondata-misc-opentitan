import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12258"
version_tuple = (0, 0, 12258)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12258")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12130"
data_version_tuple = (0, 0, 12130)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12130")
except ImportError:
    pass
data_git_hash = "60490355a29fb9bf1277bd780c5835729547afcb"
data_git_describe = "v0.0-12130-g60490355a"
data_git_msg = """\
commit 60490355a29fb9bf1277bd780c5835729547afcb
Author: Madhuri Patel <madhuri.patel@ensilica.com>
Date:   Wed May 18 15:45:21 2022 +0100

    [sysrst_ctrl,dv] Improve the combo detect group coverage
    
    Signed-off-by: Madhuri Patel <madhuri.patel@ensilica.com>

"""

# Tool version info
tool_version_str = "0.0.post128"
tool_version_tuple = (0, 0, 128)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post128")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
