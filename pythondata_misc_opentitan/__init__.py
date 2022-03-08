import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10763"
version_tuple = (0, 0, 10763)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10763")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10637"
data_version_tuple = (0, 0, 10637)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10637")
except ImportError:
    pass
data_git_hash = "c126c1716037643fe31b6f08875e25bf1bc51c95"
data_git_describe = "v0.0-10637-gc126c1716"
data_git_msg = """\
commit c126c1716037643fe31b6f08875e25bf1bc51c95
Author: Jes B. Klinke <jbk@chromium.org>
Date:   Fri Mar 4 13:35:16 2022 -0800

    [opentitantool] Pass capabilities via proxy protocol
    
    Until now, the Proxy implementation of Transport has claimed to
    support all of GPIO, SPI, I2C, etc.  And if a user attempted to get
    e.g. an SPI instance and the remote session process had an underlying
    Transport which did not support SPI, a TransportError would be
    returned.
    
    This change adds a GetCapabilities request/response to the protocol,
    so that the Proxy object can properly advertise what the caller can
    expect to be able to use it for.
    
    Signed-off-by: Jes B. Klinke <jbk@chromium.org>
    Change-Id: I3391f4dfb739c0ec45dbcb7754a3494d18dc2138

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
