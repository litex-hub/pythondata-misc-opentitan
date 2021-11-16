import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8721"
version_tuple = (0, 0, 8721)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8721")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8609"
data_version_tuple = (0, 0, 8609)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8609")
except ImportError:
    pass
data_git_hash = "1c2294a871357e9374a6aa036cfb3e02cd525e4a"
data_git_describe = "v0.0-8609-g1c2294a87"
data_git_msg = """\
commit 1c2294a871357e9374a6aa036cfb3e02cd525e4a
Author: Michael Schaffner <msf@opentitan.org>
Date:   Mon Nov 15 15:03:54 2021 -0800

    [ast] Add inline wavejson for waveform images
    
    Signed-off-by: Michael Schaffner <msf@opentitan.org>

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
