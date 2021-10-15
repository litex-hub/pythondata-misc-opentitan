import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8295"
version_tuple = (0, 0, 8295)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8295")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8183"
data_version_tuple = (0, 0, 8183)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8183")
except ImportError:
    pass
data_git_hash = "6cc78111c39bd27939cc562169ed0eeefb534036"
data_git_describe = "v0.0-8183-g6cc78111c"
data_git_msg = """\
commit 6cc78111c39bd27939cc562169ed0eeefb534036
Author: Miguel Osorio <miguelosorio@google.com>
Date:   Tue Sep 28 16:45:05 2021 -0700

    [sw/dif] Add FW override support to entropy src.
    
    The entropy src allows the firmware to disconnect the raw entropy from
    the pre-conditioner block at the output of the health checks. This
    allows firmware to access raw entropy.
    
    The firmware can also write data into the pre-conditioner block to
    provide firmware-controlled entropy at the output of the entropy src.
    
    This functionality can be useful to implement KAT tests of the
    pre-conditioner block.
    
    Signed-off-by: Miguel Osorio <miguelosorio@google.com>

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
