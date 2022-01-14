import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9543"
version_tuple = (0, 0, 9543)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9543")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9421"
data_version_tuple = (0, 0, 9421)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9421")
except ImportError:
    pass
data_git_hash = "c4cebb2b261ebc30e1998fdbdaf843e96b72b3ec"
data_git_describe = "v0.0-9421-gc4cebb2b2"
data_git_msg = """\
commit c4cebb2b261ebc30e1998fdbdaf843e96b72b3ec
Author: Alphan Ulusoy <alphan@google.com>
Date:   Wed Jan 12 08:27:49 2022 -0500

    [sw/silicon_creator] Harden encoded message check
    
    This change hardens the encoded message check, i.e. the last step of
    signature verification, by producing the value that will unlock flash
    execution (written to the EXEC register of flash_ctrl) using shares.
    
    Signed-off-by: Alphan Ulusoy <alphan@google.com>

"""

# Tool version info
tool_version_str = "0.0.post122"
tool_version_tuple = (0, 0, 122)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post122")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
