import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12779"
version_tuple = (0, 0, 12779)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12779")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12637"
data_version_tuple = (0, 0, 12637)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12637")
except ImportError:
    pass
data_git_hash = "5b4768ea0836cd694f70e93d92c53f69e1896487"
data_git_describe = "v0.0-12637-g5b4768ea08"
data_git_msg = """\
commit 5b4768ea0836cd694f70e93d92c53f69e1896487
Author: Alphan Ulusoy <alphan@google.com>
Date:   Thu Jun 16 08:09:27 2022 -0400

    [sw/silicon_creator] Add device_fpga_version_print()
    
    [sw/silicon_creator] Add device_fpga_version_print()
    
    This commit moves the code that the prints the fpga version in
    `test_rom` and `mask_rom` so that we can customize it for the target
    platform, i.e. NOP unless building for an FPGA.
    
    Signed-off-by: Alphan Ulusoy <alphan@google.com>

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
