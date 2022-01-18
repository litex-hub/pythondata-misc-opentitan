import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9571"
version_tuple = (0, 0, 9571)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9571")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9449"
data_version_tuple = (0, 0, 9449)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9449")
except ImportError:
    pass
data_git_hash = "39418a494fef3c225272aa1be681e089ee2b4319"
data_git_describe = "v0.0-9449-g39418a494"
data_git_msg = """\
commit 39418a494fef3c225272aa1be681e089ee2b4319
Author: Canberk Topal <ctopal@lowrisc.org>
Date:   Tue Jan 11 01:05:24 2022 +0000

    [aon_timer,dv] Testplan Update after V1 Review
    
    This change includes addition of prescaler test which explicitly
    tests the funcitonality of both timers while prescale configuration
    is set randomly while running.
    
    Also includes coverpoints from the DV document into the hjson.
    
    Signed-off-by: Canberk Topal <ctopal@lowrisc.org>

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
