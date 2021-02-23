import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5122"
version_tuple = (0, 0, 5122)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5122")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5031"
data_version_tuple = (0, 0, 5031)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5031")
except ImportError:
    pass
data_git_hash = "2cdc9f691c471813d6217d57d23715aa1c7d024f"
data_git_describe = "v0.0-5031-g2cdc9f691"
data_git_msg = """\
commit 2cdc9f691c471813d6217d57d23715aa1c7d024f
Author: Michael Schaffner <msf@opentitan.org>
Date:   Wed Dec 30 16:17:33 2020 -0800

    [sram_ctrl] Transition into D2
    
    Signed-off-by: Michael Schaffner <msf@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post91"
tool_version_tuple = (0, 0, 91)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post91")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
