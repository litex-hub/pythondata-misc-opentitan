import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9294"
version_tuple = (0, 0, 9294)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9294")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9177"
data_version_tuple = (0, 0, 9177)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9177")
except ImportError:
    pass
data_git_hash = "fe17d1cae4c7226d39284fa081de25e33b7e6b0d"
data_git_describe = "v0.0-9177-gfe17d1cae"
data_git_msg = """\
commit fe17d1cae4c7226d39284fa081de25e33b7e6b0d
Author: Martin Lueker-Boden <martin.lueker-boden@wdc.com>
Date:   Thu Dec 23 17:06:10 2021 -0800

    [ entropy_src ] Minor bug-fix in scoreboarding for repcnt & repcnts
    
    Whenever a new bit value or symbol is encountered, the repcnt and repcnts
    scores should be expected to reset to 1 (1 repetition of most recent value).
    
    Previously the scoreboard expected a reset to 0 when finding a new bit/symbol.
    
    Signed-off-by: Martin Lueker-Boden <martin.lueker-boden@wdc.com>

"""

# Tool version info
tool_version_str = "0.0.post117"
tool_version_tuple = (0, 0, 117)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post117")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
