import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14984"
version_tuple = (0, 0, 14984)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14984")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14842"
data_version_tuple = (0, 0, 14842)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14842")
except ImportError:
    pass
data_git_hash = "acd08dbaa8e134979918ab220eabdcdaa092f33b"
data_git_describe = "v0.0-14842-gacd08dbaa8"
data_git_msg = """\
commit acd08dbaa8e134979918ab220eabdcdaa092f33b
Author: Douglas Reis <doreis@lowrisc.org>
Date:   Wed Oct 26 18:01:00 2022 +0100

    [dv, clkmgr] Remove test point `clkmgr_all_escalarion_reset`
    
     The test was incompletely removed in the commit 0dcb77b9c6.
    
    Signed-off-by: Douglas Reis <doreis@lowrisc.org>

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
