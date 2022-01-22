import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9712"
version_tuple = (0, 0, 9712)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9712")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9590"
data_version_tuple = (0, 0, 9590)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9590")
except ImportError:
    pass
data_git_hash = "3b291e7be5b0614d14ee97089b3749f7ad81f051"
data_git_describe = "v0.0-9590-g3b291e7be"
data_git_msg = """\
commit 3b291e7be5b0614d14ee97089b3749f7ad81f051
Author: Martin Lueker-Boden <martin.lueker-boden@wdc.com>
Date:   Sat Jan 1 16:56:39 2022 -0800

    [ entropy_src/dv ] SB Handling for interrupts, disables and resets
    
    - Health test alerts can now be cleared by interrupt handlers for longer
      simulations
    - Restructured scoreboard to properly support rest and disable events
    - Scoreboard bug-fix: it turns out that in ES_TYPE == BYPASS MODE the
      DUT FSM effectively stays in BOOT mode
    
    Signed-off-by: Martin Lueker-Boden <martin.lueker-boden@wdc.com>
    Co-authored-by: weicaiyang <49293026+weicaiyang@users.noreply.github.com>

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
