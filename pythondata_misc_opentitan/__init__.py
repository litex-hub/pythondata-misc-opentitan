import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14586"
version_tuple = (0, 0, 14586)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14586")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14444"
data_version_tuple = (0, 0, 14444)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14444")
except ImportError:
    pass
data_git_hash = "ac8ee81c2be56af617446ffc652d22572501f1f2"
data_git_describe = "v0.0-14444-gac8ee81c2b"
data_git_msg = """\
commit ac8ee81c2be56af617446ffc652d22572501f1f2
Author: Chris Frantz <cfrantz@google.com>
Date:   Thu Sep 22 16:23:37 2022 -0700

    [ottool] Initial hyperdebug pin configuration
    
    1. Write an initial configuration for hyperdebug pins to allow resets
       and setting the SW straps.
    2. Most transports call their console UART "0".  Hyperdebug does not.
       All of the opentitantool configs have an alias named "console";
       change all references to uart "0" to "console".
    3. Fix the hyperdebug SPI implementation.
    3a. Set the max chunk size to a power of two.
    3b. Assert CS over an entire SPI transaction; refactor CS assert
        counting.
    
    Signed-off-by: Chris Frantz <cfrantz@google.com>

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
