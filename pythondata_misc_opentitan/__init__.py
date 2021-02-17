import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5025"
version_tuple = (0, 0, 5025)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5025")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post4934"
data_version_tuple = (0, 0, 4934)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post4934")
except ImportError:
    pass
data_git_hash = "37dc92c4eec2c506a246ee284412b6797f703f51"
data_git_describe = "v0.0-4934-g37dc92c4e"
data_git_msg = """\
commit 37dc92c4eec2c506a246ee284412b6797f703f51
Author: Eitan Shapira <eitan.shapira@nuvoton.com>
Date:   Wed Feb 17 12:42:23 2021 +0200

    [dv/tools] Bug fix to common.tcl tb_top section.
    
    Signed-off-by: Eitan Shapira <eitan.shapira@nuvoton.com>

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
