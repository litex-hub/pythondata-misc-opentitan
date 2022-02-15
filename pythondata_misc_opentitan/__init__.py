import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10309"
version_tuple = (0, 0, 10309)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10309")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10183"
data_version_tuple = (0, 0, 10183)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10183")
except ImportError:
    pass
data_git_hash = "d88f78d913e10314322727bb4982ca9ea1c496be"
data_git_describe = "v0.0-10183-gd88f78d91"
data_git_msg = """\
commit d88f78d913e10314322727bb4982ca9ea1c496be
Author: Canberk Topal <ctopal@lowrisc.org>
Date:   Fri Feb 11 16:45:16 2022 +0000

    [aon_timer,dv] Waiving UVM_WARNING for intr_enable
    
    This commit includes a demotion of UVM_WARNING into UVM_INFO about
    not having an intr_enable register for AON timer. We don't need
    intr_enable because it is directly tied to the enables of timers
    themselves.
    
    Signed-off-by: Canberk Topal <ctopal@lowrisc.org>

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
