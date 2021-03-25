import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5587"
version_tuple = (0, 0, 5587)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5587")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5492"
data_version_tuple = (0, 0, 5492)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5492")
except ImportError:
    pass
data_git_hash = "4791da5f71cb7c93104059fe6ffd120091cf9622"
data_git_describe = "v0.0-5492-g4791da5f7"
data_git_msg = """\
commit 4791da5f71cb7c93104059fe6ffd120091cf9622
Author: Timothy Chen <timothytim@google.com>
Date:   Wed Mar 24 20:45:45 2021 -0700

    [pwrmgr / usbdev] Minor fixes for low power entry / exit
    
    - fix wakeup reason mapping to be consistent with registers
    - correct reversed polarity on low power activation
    - add missing dependency in core file
    
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
