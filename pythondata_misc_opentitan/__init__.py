import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8678"
version_tuple = (0, 0, 8678)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8678")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8566"
data_version_tuple = (0, 0, 8566)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8566")
except ImportError:
    pass
data_git_hash = "4a807ec827b0e8c6c8a931ae596602485750361f"
data_git_describe = "v0.0-8566-g4a807ec82"
data_git_msg = """\
commit 4a807ec827b0e8c6c8a931ae596602485750361f
Author: Jade Philipoom <jadep@google.com>
Date:   Thu Nov 11 10:20:03 2021 +0000

    [sw/silicon_creator] Minor fixups for mask ROM OTBN driver.
    
    Follow-up to #8966
    
    Adjusts the return type and comment for `otbn_execute()` to reflect that
    it no longer has any path to return errors. Also fix the error code for
    OTBN internal errors.
    
    Signed-off-by: Jade Philipoom <jadep@google.com>

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
