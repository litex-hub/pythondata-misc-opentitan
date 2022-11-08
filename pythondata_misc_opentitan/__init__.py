import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15318"
version_tuple = (0, 0, 15318)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15318")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post15176"
data_version_tuple = (0, 0, 15176)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post15176")
except ImportError:
    pass
data_git_hash = "719e263118cb7da28a295345d70868230ed39907"
data_git_describe = "v0.0-15176-g719e263118"
data_git_msg = """\
commit 719e263118cb7da28a295345d70868230ed39907
Author: Michael Schaffner <msf@google.com>
Date:   Mon Nov 7 14:53:20 2022 -0800

    [otbn] Do not error in otbn_busy_wait_for_done
    
    The status of this function should be checked by the caller.
    
    This fixes #16030.
    
    Signed-off-by: Michael Schaffner <msf@google.com>

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
