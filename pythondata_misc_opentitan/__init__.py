import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15045"
version_tuple = (0, 0, 15045)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15045")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14903"
data_version_tuple = (0, 0, 14903)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14903")
except ImportError:
    pass
data_git_hash = "c32b3887d1fdce34d50068061a61b4926126e6be"
data_git_describe = "v0.0-14903-gc32b3887d1"
data_git_msg = """\
commit c32b3887d1fdce34d50068061a61b4926126e6be
Author: Weicai Yang <weicai@google.com>
Date:   Fri Oct 28 17:17:21 2022 -0700

    [keymgr/dv] Update the checks after fault injection
    
    Updated it to check any operation and move it to base_vseq for other vseq to reuse.
    
    Signed-off-by: Weicai Yang <weicai@google.com>

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
