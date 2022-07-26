import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13274"
version_tuple = (0, 0, 13274)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13274")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13132"
data_version_tuple = (0, 0, 13132)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13132")
except ImportError:
    pass
data_git_hash = "bee125246928489c7a9dac012c456aa04dd2e483"
data_git_describe = "v0.0-13132-gbee1252469"
data_git_msg = """\
commit bee125246928489c7a9dac012c456aa04dd2e483
Author: Martin Lueker-Boden <martin.lueker-boden@wdc.com>
Date:   Sat Jul 23 21:17:33 2022 -0700

    [entropy_src/dv] Account for SHA3 non-reset on disable
    
    Unlike most of the other blocks within the entropy_src, the SHA3 block
    is not cleared on a disable event. (The SHA3 requires particular
    sequencing to be shut down gracefully, and the disable operation
    is otherwise atomic).
    
    This is not a security problem as there is no harm if some excess
    entropy remains in the SHA3 state before starting the next seed.
    However this does need to be modelled properly in the scoreboard.
    
    This commit changes the process_fifo_q into a 64-bit fifo to
    reflect the fact that the SHA block receives data in 64 bit
    chunks.  This scoreboard FIFO is then not cleared during
    continuous-mode disable events.
    
    This SHA behavior is now properly modelled both in the default mode
    as well as in the FW_OV_INSERT mode.
    
    Signed-off-by: Martin Lueker-Boden <martin.lueker-boden@wdc.com>

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
