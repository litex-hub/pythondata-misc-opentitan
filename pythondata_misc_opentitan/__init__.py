import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5096"
version_tuple = (0, 0, 5096)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5096")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5005"
data_version_tuple = (0, 0, 5005)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5005")
except ImportError:
    pass
data_git_hash = "53d24f1f1825f66ff1ed59bb2216b65ce40ffdc5"
data_git_describe = "v0.0-5005-g53d24f1f1"
data_git_msg = """\
commit 53d24f1f1825f66ff1ed59bb2216b65ce40ffdc5
Author: Silvestrs Timofejevs <silvestrst@lowrisc.org>
Date:   Mon Feb 22 14:41:34 2021 +0000

    [sw, mask_rom] Initialise Pinmux
    
    UART pins used to be dedicated, however with recent changes these
    became multiplexible. This means that in order to get any uart output
    in Mask ROM or ROM_EXT - the corresponding pins must be configured.
    
    This change adds call to pinmux_init at the beginning of
    mask_rom_boot. This ensures that the UART pins are configured in both
    Mask ROM and ROM_EXT.
    
    NOTE:
    DIF Pinmux is work in progress, however it is expected that Mask ROM
    will use the DIF directly to configure the pins. This also means that
    sw_lib_pinmux will cease to exist.
    
    Signed-off-by: Silvestrs Timofejevs <silvestrst@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post91"
tool_version_tuple = (0, 0, 91)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post91")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
