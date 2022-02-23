import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10485"
version_tuple = (0, 0, 10485)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10485")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10359"
data_version_tuple = (0, 0, 10359)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10359")
except ImportError:
    pass
data_git_hash = "ef5c29e8514a6a771df0dee275f23f1b0e08b136"
data_git_describe = "v0.0-10359-gef5c29e85"
data_git_msg = """\
commit ef5c29e8514a6a771df0dee275f23f1b0e08b136
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Wed Feb 23 12:23:17 2022 +0000

    [otbn,dv] Bump some reseed counts as discussed in V2 meeting
    
    This commit also adds/edits some comments explaining the reasoning
    behind the chosen reseed counts.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

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
