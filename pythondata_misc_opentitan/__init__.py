import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post4995"
version_tuple = (0, 0, 4995)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post4995")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post4905"
data_version_tuple = (0, 0, 4905)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post4905")
except ImportError:
    pass
data_git_hash = "c5841b7c2f875c018096a2d57bd652715b3146fb"
data_git_describe = "v0.0-4905-gc5841b7c2"
data_git_msg = """\
commit c5841b7c2f875c018096a2d57bd652715b3146fb
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Mon Feb 15 08:25:02 2021 +0000

    [regtool] Add reset values for hwext registers to reg_pkg
    
    The result (for AES) looks like
    
        // Default values for hwext registers
        parameter logic [1:0] AES_ALERT_TEST_RESVAL = 2'h 0;
        parameter logic [31:0] AES_KEY_SHARE0_0_RESVAL = 32'h 0;
        parameter logic [31:0] AES_KEY_SHARE0_1_RESVAL = 32'h 0;
        parameter logic [31:0] AES_KEY_SHARE0_2_RESVAL = 32'h 0;
        ...
    
    Doing this means that design code can look in FOO_reg_pkg to set its
    reset value as declared in the hjson, avoiding needing to duplicate
    any constants by hand.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post90"
tool_version_tuple = (0, 0, 90)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post90")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
