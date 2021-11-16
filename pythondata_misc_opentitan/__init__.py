import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8726"
version_tuple = (0, 0, 8726)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8726")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8614"
data_version_tuple = (0, 0, 8614)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8614")
except ImportError:
    pass
data_git_hash = "1330f8548ed014a3ef5ff9a051bf11a78c5b520b"
data_git_describe = "v0.0-8614-g1330f8548"
data_git_msg = """\
commit 1330f8548ed014a3ef5ff9a051bf11a78c5b520b
Author: Miguel Osorio <miguelosorio@google.com>
Date:   Wed Nov 10 07:52:20 2021 -0800

    [fpga] Update slice to work with 32kB ROM
    
    The 32kB ROM configuration uses 4-bit RAM cells which were previously
    not supported by the slice scripts. This commit adds the following
    changes:
    
    * Update the Vivado rom.mmi generation script to support 4bit wide
      address ranges.
    * Update the gen_vivado_mem_image.py to support swapping of byte
      nibbles. This is needed in order to match the expected bit order in
      the updatemem command.
    
    Signed-off-by: Miguel Osorio <miguelosorio@google.com>

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
