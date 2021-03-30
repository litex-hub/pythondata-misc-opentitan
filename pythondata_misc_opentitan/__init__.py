import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5628"
version_tuple = (0, 0, 5628)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5628")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5533"
data_version_tuple = (0, 0, 5533)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5533")
except ImportError:
    pass
data_git_hash = "fd9f58c7d21564d67a17c6d0cce3465beeca70a2"
data_git_describe = "v0.0-5533-gfd9f58c7d"
data_git_msg = """\
commit fd9f58c7d21564d67a17c6d0cce3465beeca70a2
Author: Michael Munday <mike.munday@lowrisc.org>
Date:   Tue Mar 30 09:56:23 2021 +0100

    [sw] Add MSECCFGH register to CSR library
    
    This CSR represents the high 32 bits of MSECCFG and was added to
    Ibex in:
    
    https://github.com/lowRISC/ibex/pull/1310
    
    We should probably autogenerate this list at some point but it
    isn't a priority right now.
    
    Signed-off-by: Michael Munday <mike.munday@lowrisc.org>

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
