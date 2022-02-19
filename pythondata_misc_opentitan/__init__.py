import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10451"
version_tuple = (0, 0, 10451)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10451")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10325"
data_version_tuple = (0, 0, 10325)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10325")
except ImportError:
    pass
data_git_hash = "2f11710ed27371762bf118e634d13d81caf729c5"
data_git_describe = "v0.0-10325-g2f11710ed"
data_git_msg = """\
commit 2f11710ed27371762bf118e634d13d81caf729c5
Author: Jes B. Klinke <jbk@chromium.org>
Date:   Fri Feb 18 11:49:51 2022 -0800

    [opentitantool] Use Result<> on all Transport methods
    
    As we plan to introduce a Transport implementation backed by a network
    protocol, I/O errors could occur even for the simplest methods (such
    as "get baud rate").
    
    This change ensures that every single method in the Transport trait
    and its delegates return their value through a transport::Result<...>
    to accomodate this future.
    
    Signed-off-by: Jes B. Klinke <jbk@chromium.org>
    Change-Id: I88b3a48a1910cb3a5211c3dc6e84a8553300c53b

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
