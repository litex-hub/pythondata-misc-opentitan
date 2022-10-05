import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14565"
version_tuple = (0, 0, 14565)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14565")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14423"
data_version_tuple = (0, 0, 14423)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14423")
except ImportError:
    pass
data_git_hash = "46b156a66e1d0e4f7e651b55790347a8fae4fbc0"
data_git_describe = "v0.0-14423-g46b156a66e"
data_git_msg = """\
commit 46b156a66e1d0e4f7e651b55790347a8fae4fbc0
Author: Johnathan Van Why <jrvanwhy@google.com>
Date:   Mon Oct 3 11:31:58 2022 -0700

    [opentitantool] Add the `fpga reset` command.
    
    `opentitantool fpga reset` will reset the CW310's SAM3U chip. This change removes the `cw310_reboot.py` script that we previously used to reset the SAM3U.
    
    The new help text (`opentitantool fpga help`):
    
    ```
    opentitantool-fpga 0.0.0
    Commands for interacting with an FPGA instance
    
    USAGE:
        opentitantool fpga <SUBCOMMAND>
    
    FLAGS:
        -h, --help       Prints help information
        -V, --version    Prints version information
    
    SUBCOMMANDS:
        help              Prints this message or the help of the given subcommand(s)
        load-bitstream    Load a bitstream into the FPGA
        reset             Resets the SAM3U chip on the CW310 FPGA board
        set-pll           Program the CDCE906 PLL chip with defaults
    ```
    
    Signed-off-by: Johnathan Van Why <jrvanwhy@google.com>

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
