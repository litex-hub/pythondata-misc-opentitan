import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8709"
version_tuple = (0, 0, 8709)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8709")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8597"
data_version_tuple = (0, 0, 8597)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8597")
except ImportError:
    pass
data_git_hash = "fe2779ee5413a14815112c1e8ae78378dc07e54b"
data_git_describe = "v0.0-8597-gfe2779ee5"
data_git_msg = """\
commit fe2779ee5413a14815112c1e8ae78378dc07e54b
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Thu Oct 21 17:04:54 2021 +0100

    [rstmgr] Fix width of counter in rstmgr_cnsty_chk
    
    The definition of CntWidth wasn't correct for all values of
    MaxSyncDelay. In particular, it wouldn't work properly for a
    MaxSyncDelay of 3 (where representing the next value takes another
    bit).
    
    Also, add an explicit cast to avoid a width mismatch warning. Now that
    we've got the widths right, we could alternatively slice MaxSyncDelay.
    But this seems slightly safer (and we've just got it wrong once!).
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

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
