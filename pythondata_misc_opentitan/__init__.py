import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10753"
version_tuple = (0, 0, 10753)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10753")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10627"
data_version_tuple = (0, 0, 10627)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10627")
except ImportError:
    pass
data_git_hash = "befb772694c1be1cf3e7fb9ad323c115a94e91e8"
data_git_describe = "v0.0-10627-gbefb77269"
data_git_msg = """\
commit befb772694c1be1cf3e7fb9ad323c115a94e91e8
Author: Jes B. Klinke <jbk@chromium.org>
Date:   Fri Mar 4 14:34:41 2022 -0800

    [opentitantool] Refactor TCP port search
    
    When attempting to find an available TCP port to bind to, the current
    code catches any error from the JsonSocketServer constructor and
    handles it by calling the constructor again with the next candidate
    port.
    
    This change makes sure that unrelated errors to not get handled as
    above.  The constructor is changed to take a ready TcpListener, and
    the loop over available ports can then happen before the constructor
    is called, and any Err() return from the constructor is now treated as
    a fatal exception.
    
    Signed-off-by: Jes B. Klinke <jbk@chromium.org>
    Change-Id: I765ba8897c2e7d20004056de92e260ef274144fd

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
