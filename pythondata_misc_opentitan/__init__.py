import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5647"
version_tuple = (0, 0, 5647)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5647")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5552"
data_version_tuple = (0, 0, 5552)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5552")
except ImportError:
    pass
data_git_hash = "f87ad8a574888a33f920b0c9e09beea5a33f690a"
data_git_describe = "v0.0-5552-gf87ad8a57"
data_git_msg = """\
commit f87ad8a574888a33f920b0c9e09beea5a33f690a
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Tue Mar 30 11:25:37 2021 +0100

    [otbn] Move from V0 to V1
    
    For the checklist items that have changed:
    
     - We're not using FPV for OTBN at the moment
    
     - We've seen OTBN tests run on xcelium
    
     - The nightly and CI regressions are now running (at last!)
    
     - The design spec has had innumerable reviews and discussions, as
       you'd expect given how complicated the block is.
    
     - We've had a DV plan / testplan review (with Cindy, Sri, Weicai,
       Chris Gori, Philipp and me) and the testplan has been updated as a
       result.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
