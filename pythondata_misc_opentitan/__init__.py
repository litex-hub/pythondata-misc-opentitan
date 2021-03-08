import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5285"
version_tuple = (0, 0, 5285)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5285")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5190"
data_version_tuple = (0, 0, 5190)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5190")
except ImportError:
    pass
data_git_hash = "0481a821c01424bb2271964104ce8849c258474b"
data_git_describe = "v0.0-5190-g0481a821c"
data_git_msg = """\
commit 0481a821c01424bb2271964104ce8849c258474b
Author: Timothy Chen <timothytim@google.com>
Date:   Fri Mar 5 14:30:17 2021 -0800

    [aon_timer] Change escalate_en control to cpu_en
    
    * The issue with using escalate_en is that if the software configures
      the alert handling to skip from normal directly to scrap, we may not
      halt the watchdog timer.  There are also similar issues with other
      invalid states.
    
    * By using cpu_en, we align the behavior of the aon_timer with that of
      the processing element (its main consumer) and thus is more consistent
      overall.  If the cpu is running, then the watchdog / wake timer should
      be in effect.  If the cpu is halted due to life cycle reasons, there
      would be no one to consume the output anyways.
    
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
