import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8896"
version_tuple = (0, 0, 8896)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8896")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8784"
data_version_tuple = (0, 0, 8784)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8784")
except ImportError:
    pass
data_git_hash = "3a1b09f6cb48b4fccd8cc58f8a0d94b49a4cd8fc"
data_git_describe = "v0.0-8784-g3a1b09f6c"
data_git_msg = """\
commit 3a1b09f6cb48b4fccd8cc58f8a0d94b49a4cd8fc
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Fri Nov 26 11:13:09 2021 +0000

    [rom_ctrl] Correctly wire up fatal alerts from bus integrity errors
    
    Way back in April (da74794), I fixed up the connections so that
    FATAL_ALERT_CAUSE would reflect a bus integrity error even when it
    didn't come from the register interface. Unfortunately, I didn't make
    the corresponding change in the trigger for the alert itself. Oops.
    
    Caught by Prajwala debugging failures in the tl_intg_err tests. Nice!
    
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
