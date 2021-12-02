import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8956"
version_tuple = (0, 0, 8956)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8956")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8844"
data_version_tuple = (0, 0, 8844)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8844")
except ImportError:
    pass
data_git_hash = "d8b96e18a6b7c8f794bbf782667ec0b5fd6b9819"
data_git_describe = "v0.0-8844-gd8b96e18a"
data_git_msg = """\
commit d8b96e18a6b7c8f794bbf782667ec0b5fd6b9819
Author: Alphan Ulusoy <alphan@google.com>
Date:   Tue Nov 30 15:13:57 2021 -0500

    [sw/silicon_creator] Use flash_ctrl_info_mp_set() in boot_data and update functest
    
    Signed-off-by: Alphan Ulusoy <alphan@google.com>

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
