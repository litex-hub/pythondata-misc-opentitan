import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8862"
version_tuple = (0, 0, 8862)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8862")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8750"
data_version_tuple = (0, 0, 8750)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8750")
except ImportError:
    pass
data_git_hash = "bb1d4754e787a043021e06c3e169665aef9d1943"
data_git_describe = "v0.0-8750-gbb1d4754e"
data_git_msg = """\
commit bb1d4754e787a043021e06c3e169665aef9d1943
Author: Canberk Topal <ctopal@lowrisc.org>
Date:   Wed Oct 27 01:26:19 2021 +0100

    [otbn,dv] Fully Implementing URND PRNG
    
    This commit includes necessary additions inside the OTBN environment
    for enabling URND seed processing from EDN and modelling PRNG inside
    wsr.py
    
    Signed-off-by: Canberk Topal <ctopal@lowrisc.org>

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
