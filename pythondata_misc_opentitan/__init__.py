import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5480"
version_tuple = (0, 0, 5480)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5480")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5385"
data_version_tuple = (0, 0, 5385)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5385")
except ImportError:
    pass
data_git_hash = "95d23d98b2050f353499e06907c11903ae2ac707"
data_git_describe = "v0.0-5385-g95d23d98b"
data_git_msg = """\
commit 95d23d98b2050f353499e06907c11903ae2ac707
Author: Timothy Chen <timothytim@google.com>
Date:   Thu Mar 11 17:44:59 2021 -0800

    [sram] Add memory initialization
    
    - Software can request memory initialization
    - Memory contents will be written with "random" values
    - During the duration of initialization, memory reads are blocked
    - Software should poll on initialization completion before continuing
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
