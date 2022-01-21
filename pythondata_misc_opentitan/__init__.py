import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9690"
version_tuple = (0, 0, 9690)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9690")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9568"
data_version_tuple = (0, 0, 9568)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9568")
except ImportError:
    pass
data_git_hash = "ca1abd11608eb7d5f6e41e489bc9519f8bdcf4b7"
data_git_describe = "v0.0-9568-gca1abd116"
data_git_msg = """\
commit ca1abd11608eb7d5f6e41e489bc9519f8bdcf4b7
Author: Michael Munday <mike.munday@lowrisc.org>
Date:   Thu Jan 20 12:47:33 2022 +0000

    [rom] Setup watchdog timer in assembly before entropy setup
    
    This new code enables the watchdog timer right at the start of mask
    ROM execution (before entropy setup and SRAM scrambling). This means
    that unless the watchdog timer is 'petted' (i.e. the
    aon_timer.WDOG_COUNT register is reset to 0 periodically) the device
    will eventually reset itself.
    
    The timeout value is currently the maximum possible (~6 hours assuming
    a clock of 200KHz). This value should be reduced to something lower,
    issue #10215 tracks this.
    
    This change has been manually tested by setting the timer value to 0
    and checking that the device is quickly reset.
    
    Signed-off-by: Michael Munday <mike.munday@lowrisc.org>

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
