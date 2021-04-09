import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5793"
version_tuple = (0, 0, 5793)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5793")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5698"
data_version_tuple = (0, 0, 5698)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5698")
except ImportError:
    pass
data_git_hash = "a0980d323ab319d2467e6bc79dfc9331b0649654"
data_git_describe = "v0.0-5698-ga0980d323"
data_git_msg = """\
commit a0980d323ab319d2467e6bc79dfc9331b0649654
Author: Timothy Chen <timothytim@google.com>
Date:   Wed Apr 7 22:34:02 2021 -0700

    [flash_ctrl] Correct behavior when buffer not enabled.
    
    When buffer is not enabled, the flash_phy_rd may erroneously return data
    to back to back transactions when it is not supposed to.
    
    This happens because even when buffers are not enabled, the read data is
    written into the holding FIFO between read and descramble stages.  As a
    result, the return path falsely thinks the data is available and returns
    it.
    
    This causes an issue because even though the data is returned, the front door
    logic has already created 2 transactions to the flash, and a result, we have
    extra data returning.
    
    The buffer not enabled case can be caused by otp_ctrl not returning the
    flash controller's request for a key.  This in turn can happen because
    entropy is not yet enabled.  This latter point deserves a wider discussion
    as to the right solution.
    
    To fix this, the forward hint is used to distinguish when the data in the
    FIFO is valid vs when it is not.
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
