import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5321"
version_tuple = (0, 0, 5321)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5321")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5226"
data_version_tuple = (0, 0, 5226)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5226")
except ImportError:
    pass
data_git_hash = "11a19b891689f9142d03f44f2879153facc08e7e"
data_git_describe = "v0.0-5226-g11a19b891"
data_git_msg = """\
commit 11a19b891689f9142d03f44f2879153facc08e7e
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Tue Mar 9 16:43:18 2021 +0000

    [spi_host] Remove the ByteOrder and MaxCS parameters from the module
    
    These didn't do anything except to shadow the parameters that are set
    by reggen (to hopefully the correct values) in spi_host_reg_pkg.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

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
