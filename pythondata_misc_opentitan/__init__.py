import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8405"
version_tuple = (0, 0, 8405)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8405")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8293"
data_version_tuple = (0, 0, 8293)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8293")
except ImportError:
    pass
data_git_hash = "25212a9d2acc9b5fba26275b9bdeaea6ac306a21"
data_git_describe = "v0.0-8293-g25212a9d2"
data_git_msg = """\
commit 25212a9d2acc9b5fba26275b9bdeaea6ac306a21
Author: Silvestrs Timofejevs <silvestrst@lowrisc.org>
Date:   Wed Sep 29 15:39:10 2021 +0100

    [sw, tests] Introduce Retention SRAM scrambling chip level test
    
    - Routines have been written in a way that they can be used for
      both RAMs, by passing the correct handle. HOWEVER, Main RAM
      cannot be handled the same way as the Retention RAM, as
      scrambling would destroy the system configuration including
      the C runtime.
    
    Signed-off-by: Silvestrs Timofejevs <silvestrst@lowrisc.org>

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
