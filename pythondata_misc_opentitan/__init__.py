import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8859"
version_tuple = (0, 0, 8859)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8859")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8747"
data_version_tuple = (0, 0, 8747)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8747")
except ImportError:
    pass
data_git_hash = "a9aec87b1fdd7426082e032b47e5e6760aa3de8f"
data_git_describe = "v0.0-8747-ga9aec87b1"
data_git_msg = """\
commit a9aec87b1fdd7426082e032b47e5e6760aa3de8f
Author: Martin Lueker-Boden <martin.lueker-boden@wdc.com>
Date:   Tue Nov 23 17:35:22 2021 -0800

    [ spi_host, rtl ] Properly handle back-to-back segments
    
    Issue #9285 uncovers a bug whereby back-to-back segments are not being properly handled in the rtl.
    
    The issue is that when processing back to back segments, the FSM needs to carefully choose which copy
    of the segment parameters to look at.  For anything initializing states for the following segment the
    FSM needs to look at the new incoming segment parameters.  For finalizing processing of the previous segment
    (e.g., flushing data out of the shift register) the FSM needs to look at the previous parameters.
    
    This commit manages this subtlety.
    
    Fixes #9285 (with patch to test bench in @rasmus-madsen's offline TB, see issue for patch)
    
    Signed-off-by: Martin Lueker-Boden <martin.lueker-boden@wdc.com>

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
