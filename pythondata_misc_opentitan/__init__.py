import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12576"
version_tuple = (0, 0, 12576)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12576")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12434"
data_version_tuple = (0, 0, 12434)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12434")
except ImportError:
    pass
data_git_hash = "bee514ebf2daf59323de2cae5d01de31e5de97bc"
data_git_describe = "v0.0-12434-gbee514ebf"
data_git_msg = """\
commit bee514ebf2daf59323de2cae5d01de31e5de97bc
Author: Eunchan Kim <eunchan@opentitan.org>
Date:   Fri Jun 3 12:35:09 2022 -0700

    chore(cdc): SPI_DEV_CLK W_G_CLK_GLITCH waivers
    
    clock configurations affecting SPI_DEV_CLK:
    
    - Pinmux DIO PAD Attributes
    - SPI_DEVICE CFG.CPHA, CFG.CPOL
    - IO_DIV4 control signals in CLKMGR
    
    All those configs are programmed prior to SPI_DEV_CLK active. So, they
    are waived.
    
    Signed-off-by: Eunchan Kim <eunchan@opentitan.org>

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
