import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8686"
version_tuple = (0, 0, 8686)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8686")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8574"
data_version_tuple = (0, 0, 8574)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8574")
except ImportError:
    pass
data_git_hash = "c4f342b9349ba033a5f22fba9349999299a1b2bf"
data_git_describe = "v0.0-8574-gc4f342b93"
data_git_msg = """\
commit c4f342b9349ba033a5f22fba9349999299a1b2bf
Author: Timothy Chen <timothytim@google.com>
Date:   Tue Nov 9 16:54:16 2021 -0800

    [top] Move spi_host* in memory map
    
    - Fixes #8748
    - This reduces the amount of asynchronous latency when accessing
      the spi_host modules.
    - Note, ideally there should be another xbar that is "hi_speed" xbar,
      but that is overkill for only 2 peripherals.  Just tack it onto the
      main xbar.
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
