import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14733"
version_tuple = (0, 0, 14733)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14733")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14591"
data_version_tuple = (0, 0, 14591)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14591")
except ImportError:
    pass
data_git_hash = "96bcebc722edc18f5999ab0edce1d75dd355f1be"
data_git_describe = "v0.0-14591-g96bcebc722"
data_git_msg = """\
commit 96bcebc722edc18f5999ab0edce1d75dd355f1be
Author: Andreas Kurth <adk@lowrisc.org>
Date:   Wed Oct 12 15:08:23 2022 +0200

    [otbn,doc] Add missing *fatal error* transition from init to locked
    
    Signed-off-by: Andreas Kurth <adk@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post142"
tool_version_tuple = (0, 0, 142)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post142")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
