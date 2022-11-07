import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15312"
version_tuple = (0, 0, 15312)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15312")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post15170"
data_version_tuple = (0, 0, 15170)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post15170")
except ImportError:
    pass
data_git_hash = "140e189eeb30b0474eb8483a2604b9a8d6f753f2"
data_git_describe = "v0.0-15170-g140e189eeb"
data_git_msg = """\
commit 140e189eeb30b0474eb8483a2604b9a8d6f753f2
Author: Martin Lueker-Boden <martin.lueker-boden@wdc.com>
Date:   Sat Oct 29 10:02:22 2022 -0700

    [entropy_src/dv] Updates to FSM closure (PR #15663)
    
    - Fixes an interrupt handler bug by from the DV_WAIT watchdog's added in
      PR #15663. (Thanks for the suggestion @waicaiyang).
    - Adds more states the list of rare transitions.
    - Updates RNG VSEQ to force some transtions using backdoor operations
      (when frontdoor CSR transactions are not fast enough to rapidly turn
      the FSM on and off)
    
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
