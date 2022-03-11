import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10849"
version_tuple = (0, 0, 10849)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10849")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10723"
data_version_tuple = (0, 0, 10723)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10723")
except ImportError:
    pass
data_git_hash = "48f14bc59126055488290fef9ca34e77a29685fd"
data_git_describe = "v0.0-10723-g48f14bc59"
data_git_msg = """\
commit 48f14bc59126055488290fef9ca34e77a29685fd
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Fri Mar 11 10:42:51 2022 +0000

    [otbn, rtl] Fix `idle_o` timing
    
    `idle_o` will gate the clock if clock hints are setup to do so. Any done
    interrupt raised must occur at or before the cycle `idle_o` changes to
    ensure the clock gating doesn't erase the interrupt.
    
    This adds a delay to the externally visible `idle_o` to ensure it
    synchronises with changes to the status register and gives correct
    interrupt timing.
    
    Signed-off-by: Greg Chadwick <gac@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post126"
tool_version_tuple = (0, 0, 126)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post126")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
