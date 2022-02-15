import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10316"
version_tuple = (0, 0, 10316)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10316")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10190"
data_version_tuple = (0, 0, 10190)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10190")
except ImportError:
    pass
data_git_hash = "640c1f1b9bea5e5b77704539a3b05cdcceac48c1"
data_git_describe = "v0.0-10190-g640c1f1b9"
data_git_msg = """\
commit 640c1f1b9bea5e5b77704539a3b05cdcceac48c1
Author: Mark Branstad <mark.branstad@wdc.com>
Date:   Mon Feb 14 15:02:09 2022 -0800

    [csrng/rtl] Change cs_aes_halt_o to a pulse
    
    To be able to reuse the DV req/ack module for this simple interface,
    the cs_aes_halt_o will be a single clock in pulse size.
    
    Signed-off-by: Mark Branstad <mark.branstad@wdc.com>

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
