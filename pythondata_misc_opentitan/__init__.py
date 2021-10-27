import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8466"
version_tuple = (0, 0, 8466)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8466")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8354"
data_version_tuple = (0, 0, 8354)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8354")
except ImportError:
    pass
data_git_hash = "ed0abd253128063bc86a3ded500b7f2ada3a7910"
data_git_describe = "v0.0-8354-ged0abd253"
data_git_msg = """\
commit ed0abd253128063bc86a3ded500b7f2ada3a7910
Author: Timothy Trippel <ttrippel@google.com>
Date:   Tue Oct 26 03:24:23 2021 +0000

    [dif] Add overwrite safety check to `util/make_new_dif.py`
    
    If `util/make_new_dif.py` is run initially to auto-generate a DIF header
    and checklist boilerplate code/markdown (respectively), and accidentally
    run again shortly after manualy modifying the boilerplate code (before
    the modifications are checked-in to the repo), the modifications would
    be overwritten. This commit adds a check to prevent such a mistake from
    happening, partially addressing an action item in #8142.
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

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
