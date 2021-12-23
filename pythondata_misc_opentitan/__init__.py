import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9283"
version_tuple = (0, 0, 9283)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9283")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9170"
data_version_tuple = (0, 0, 9170)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9170")
except ImportError:
    pass
data_git_hash = "a753200da1c33268c54c4dc3d3d2bec23d3349bc"
data_git_describe = "v0.0-9170-ga753200da"
data_git_msg = """\
commit a753200da1c33268c54c4dc3d3d2bec23d3349bc
Author: Steve Nelson <steve.nelson@wdc.com>
Date:   Wed Dec 22 13:50:35 2021 -0800

    [csrng/dv] Removed double cmd_rdy spin_waits. rtl fix in PR#9802
    
    Signed-off-by: Steve Nelson <steve.nelson@wdc.com>

"""

# Tool version info
tool_version_str = "0.0.post113"
tool_version_tuple = (0, 0, 113)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post113")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
