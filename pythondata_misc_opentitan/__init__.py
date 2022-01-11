import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9426"
version_tuple = (0, 0, 9426)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9426")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9308"
data_version_tuple = (0, 0, 9308)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9308")
except ImportError:
    pass
data_git_hash = "2d6cd7a7e3e112a8c73881e0330bbd5a26d3bce4"
data_git_describe = "v0.0-9308-g2d6cd7a7e"
data_git_msg = """\
commit 2d6cd7a7e3e112a8c73881e0330bbd5a26d3bce4
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Tue Jan 11 11:55:00 2022 +0000

    Revert "[pinmux_wkup] Change comparison to GE to stay on the safe side"
    
    This reverts commit 9f2fccf76a250c5398514da8a9bda98c544a9ee0.
    
    This fixes an FPGA timing failure that is breaking CI.
    
    Signed-off-by: Greg Chadwick <gac@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post118"
tool_version_tuple = (0, 0, 118)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post118")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
