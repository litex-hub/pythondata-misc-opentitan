import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9299"
version_tuple = (0, 0, 9299)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9299")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9182"
data_version_tuple = (0, 0, 9182)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9182")
except ImportError:
    pass
data_git_hash = "28b1ab1451ee70ee6cee068b2f399aeea615cb5b"
data_git_describe = "v0.0-9182-g28b1ab145"
data_git_msg = """\
commit 28b1ab1451ee70ee6cee068b2f399aeea615cb5b
Author: Dror Kabely <dror.kabely@opentitan.org>
Date:   Thu Dec 23 17:36:52 2021 +0200

    [dv/mem_bkdr_util] added backdoor write of LC counter into LC partition in OTP
    
    Signed-off-by: Dror Kabely <dror.kabely@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post117"
tool_version_tuple = (0, 0, 117)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post117")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
