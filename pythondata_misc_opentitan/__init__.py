import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15212"
version_tuple = (0, 0, 15212)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15212")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post15070"
data_version_tuple = (0, 0, 15070)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post15070")
except ImportError:
    pass
data_git_hash = "9b3ebf49cd9c99f9b818d1bfde2e9fbe455f540d"
data_git_describe = "v0.0-15070-g9b3ebf49cd"
data_git_msg = """\
commit 9b3ebf49cd9c99f9b818d1bfde2e9fbe455f540d
Author: Timothy Chen <timothytim@google.com>
Date:   Wed Nov 2 23:24:43 2022 -0700

    [top] Update cpu_info test
    
    Due to #15219, it appears the current PC information on double
    faults is now changed. Update to reflect the latest.
    
    Also change illegal read to an illegal write at address 0, since
    this reduces the number of "glue" instructions surrounding the one
    that actually creates the illegal access.
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
