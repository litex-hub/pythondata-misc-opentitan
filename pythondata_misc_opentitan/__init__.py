import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5763"
version_tuple = (0, 0, 5763)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5763")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5668"
data_version_tuple = (0, 0, 5668)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5668")
except ImportError:
    pass
data_git_hash = "be6710805572fb696968751d1e679e783efae050"
data_git_describe = "v0.0-5668-gbe6710805"
data_git_msg = """\
commit be6710805572fb696968751d1e679e783efae050
Author: Michael Schaffner <msf@google.com>
Date:   Tue Apr 6 19:19:18 2021 -0700

    [pattgen] Add missing core file dependency
    
    Signed-off-by: Michael Schaffner <msf@google.com>

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
