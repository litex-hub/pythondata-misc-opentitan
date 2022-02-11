import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10263"
version_tuple = (0, 0, 10263)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10263")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10139"
data_version_tuple = (0, 0, 10139)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10139")
except ImportError:
    pass
data_git_hash = "3f05591fd2eec3638309e70836ef3c3af62aa998"
data_git_describe = "v0.0-10139-g3f05591fd"
data_git_msg = """\
commit 3f05591fd2eec3638309e70836ef3c3af62aa998
Author: Jes B. Klinke <jbk@chromium.org>
Date:   Fri Feb 11 10:49:35 2022 -0800

    [opentitantoo] Move backend/ into opentitanlib
    
    The backend/ directory contains logic for processing command line
    arguments and constructing an instance of the Transport trait
    accordingly.
    
    This functionality will be needed outside of opentitantool proper.
    Both in dedicated test programs using a Verilator backend, and for the
    new session support for opentitantool.
    
    Signed-off-by: Jes B. Klinke <jbk@chromium.org>
    Change-Id: I197176efb9e46af107f38e2f66f395b6aa92648b

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
