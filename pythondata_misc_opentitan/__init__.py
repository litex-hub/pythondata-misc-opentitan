import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11372"
version_tuple = (0, 0, 11372)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11372")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11246"
data_version_tuple = (0, 0, 11246)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11246")
except ImportError:
    pass
data_git_hash = "27e2b13464ecc5a322922da9b00cd91e9f77ebfe"
data_git_describe = "v0.0-11246-g27e2b1346"
data_git_msg = """\
commit 27e2b13464ecc5a322922da9b00cd91e9f77ebfe
Author: Andreas Kurth <adk@lowrisc.org>
Date:   Mon Apr 4 15:03:27 2022 +0200

    [otbn] Propagate lc_escalate inside mubi escalate
    
    Signed-off-by: Andreas Kurth <adk@lowrisc.org>

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
