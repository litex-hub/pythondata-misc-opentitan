import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8804"
version_tuple = (0, 0, 8804)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8804")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8692"
data_version_tuple = (0, 0, 8692)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8692")
except ImportError:
    pass
data_git_hash = "fcb74e9fbd286875debe7f6c5a84932120655d80"
data_git_describe = "v0.0-8692-gfcb74e9fb"
data_git_msg = """\
commit fcb74e9fbd286875debe7f6c5a84932120655d80
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Thu Nov 18 15:49:04 2021 +0000

    [otbn,doc] Document what happens if URND LFSR gets stuck
    
    As well as adding to the documentation, this adds a new generic
    "internal state is corrupt" bit to ERR_BITS and FATAL_ALERT_CAUSE and
    wires everything up in the RTL. This is driven to zero for ERR_BITS in
    the controller and for FATAL_ALERT_CAUSE in otbn.sv.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

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
