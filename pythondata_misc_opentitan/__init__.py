import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15118"
version_tuple = (0, 0, 15118)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15118")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14976"
data_version_tuple = (0, 0, 14976)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14976")
except ImportError:
    pass
data_git_hash = "a40885552d0776e909a41cdb71095b76cd3bbcbf"
data_git_describe = "v0.0-14976-ga40885552d"
data_git_msg = """\
commit a40885552d0776e909a41cdb71095b76cd3bbcbf
Author: Srikrishna Iyer <sriyer@google.com>
Date:   Fri Oct 28 11:09:31 2022 -0700

    [rtl, chip dv] Coverage exclusions for pinmux / padring
    
    This commit adds a large number of exclusions for pinmux / padctrl
    / top_earlgrey, related to the tieoffs in `*attr*` signals.
    
    It also marks unused signals in `prim_generic_pad_wrapper` with
    inline coverage off pragmas, and excludes `prim_generic_pad_attr`
    entirely from coverage collection (LOW_RISK).
    
    Signed-off-by: Srikrishna Iyer <sriyer@google.com>

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
