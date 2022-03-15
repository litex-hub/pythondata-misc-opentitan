import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10890"
version_tuple = (0, 0, 10890)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10890")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10764"
data_version_tuple = (0, 0, 10764)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10764")
except ImportError:
    pass
data_git_hash = "f4e384542ae19c85e3573caabb17dc1dc8cf2bbb"
data_git_describe = "v0.0-10764-gf4e384542"
data_git_msg = """\
commit f4e384542ae19c85e3573caabb17dc1dc8cf2bbb
Author: Douglas Reis <doreis@lowrisc.org>
Date:   Thu Mar 10 11:12:33 2022 +0000

    [test, aon_timer] Fix bug on the aon bite reset test
    
     - The bug was caused by a delay of 3 cycles between the matching of timer counter with the threshold and the irq state register to rise, which becomes more evident when the cpu clock is higher.
    
    Signed-off-by: Douglas Reis <doreis@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post126"
tool_version_tuple = (0, 0, 126)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post126")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
