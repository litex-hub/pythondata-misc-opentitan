import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8217"
version_tuple = (0, 0, 8217)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8217")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8105"
data_version_tuple = (0, 0, 8105)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8105")
except ImportError:
    pass
data_git_hash = "faddce146d4bcfd7079134d2adcdae05ccfe40cf"
data_git_describe = "v0.0-8105-gfaddce146"
data_git_msg = """\
commit faddce146d4bcfd7079134d2adcdae05ccfe40cf
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Fri Oct 8 11:37:08 2021 +0100

    [otbn,dv] Allow trace entries from stalls in ISS wrapper
    
    This lets us gets rid of some hacks in ISSWrapper::start(). Now, STALL
    lines can have some associated updates (in practice, these are always
    to external registers), which get reflected in the model immediately
    but are merged together with the next execute line to be checked
    against the RTL.
    
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
