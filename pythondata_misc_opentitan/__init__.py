import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5389"
version_tuple = (0, 0, 5389)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5389")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5294"
data_version_tuple = (0, 0, 5294)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5294")
except ImportError:
    pass
data_git_hash = "40030846f0d617fa191ea1fc45a1f7206b1f2dec"
data_git_describe = "v0.0-5294-g40030846f"
data_git_msg = """\
commit 40030846f0d617fa191ea1fc45a1f7206b1f2dec
Author: Rasmus Madsen <rasmus.madsen@wdc.com>
Date:   Mon Mar 8 11:41:51 2021 -0800

    [tools/dv] added UNR flow for xcelium
    
    Signed-off-by: Rasmus Madsen <rasmus.madsen@wdc.com>

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
