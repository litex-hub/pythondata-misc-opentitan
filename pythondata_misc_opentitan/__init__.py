import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8753"
version_tuple = (0, 0, 8753)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8753")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8641"
data_version_tuple = (0, 0, 8641)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8641")
except ImportError:
    pass
data_git_hash = "6a2713ba38efc0f0026858aa93076f53a8ab9bbc"
data_git_describe = "v0.0-8641-g6a2713ba3"
data_git_msg = """\
commit 6a2713ba38efc0f0026858aa93076f53a8ab9bbc
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Tue Nov 16 15:06:34 2021 -0800

    [dv/alert] Support LPG in alert_sender/receiver pair
    
    This PR supports LPG in prim_alert testbench by randomly issue
    init_trigger_i in alert_receiver side when alert handshake is on-going.
    This PR implements part of the TODO in issue #8814.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
