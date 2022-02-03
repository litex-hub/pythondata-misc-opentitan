import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10051"
version_tuple = (0, 0, 10051)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10051")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9927"
data_version_tuple = (0, 0, 9927)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9927")
except ImportError:
    pass
data_git_hash = "cd742d11147c817e8f63a49b4e5e83acbe9d7ac8"
data_git_describe = "v0.0-9927-gcd742d111"
data_git_msg = """\
commit cd742d11147c817e8f63a49b4e5e83acbe9d7ac8
Author: Eunchan Kim <eunchan@opentitan.org>
Date:   Tue Feb 1 15:01:31 2022 -0800

    [spi_device] Add flash/passthrouh modes in CFG.MODE
    
    Flash and Passthrough modes are added into CFG.MODE CSR.
    
    Signed-off-by: Eunchan Kim <eunchan@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post124"
tool_version_tuple = (0, 0, 124)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post124")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
