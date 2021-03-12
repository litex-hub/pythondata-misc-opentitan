import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5369"
version_tuple = (0, 0, 5369)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5369")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5274"
data_version_tuple = (0, 0, 5274)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5274")
except ImportError:
    pass
data_git_hash = "e6e919fc89eea96c1e593112009fda349db5949c"
data_git_describe = "v0.0-5274-ge6e919fc8"
data_git_msg = """\
commit e6e919fc89eea96c1e593112009fda349db5949c
Author: Udi Jonnalagadda <udij@google.com>
Date:   Fri Mar 12 04:04:45 2021 -0800

    [dv/sram] add address comparison function in SCB
    
    this minor patch updates how the scoreboard does address comparisons in
    case of read-after-write hazards to handle data forwarding.
    
    we add a function to properly mask off the address widths and compare,
    which allows for better reuse in the scoreboard if needed.
    
    Signed-off-by: Udi Jonnalagadda <udij@google.com>

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
