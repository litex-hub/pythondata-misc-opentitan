import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5188"
version_tuple = (0, 0, 5188)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5188")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5097"
data_version_tuple = (0, 0, 5097)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5097")
except ImportError:
    pass
data_git_hash = "11f4081a226cb41f1897eac44ea27d7e716db279"
data_git_describe = "v0.0-5097-g11f4081a2"
data_git_msg = """\
commit 11f4081a226cb41f1897eac44ea27d7e716db279
Author: Michael Schaffner <msf@opentitan.org>
Date:   Fri Feb 26 20:06:45 2021 -0800

    [dvsim/verilator] Fix pre-build cmd failure when hw/foundry is absent
    
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
