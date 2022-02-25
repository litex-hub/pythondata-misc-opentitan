import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10535"
version_tuple = (0, 0, 10535)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10535")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10409"
data_version_tuple = (0, 0, 10409)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10409")
except ImportError:
    pass
data_git_hash = "426665cb960a5b9741031c0f8e34f137abc21459"
data_git_describe = "v0.0-10409-g426665cb9"
data_git_msg = """\
commit 426665cb960a5b9741031c0f8e34f137abc21459
Author: Jes B. Klinke <jbk@chromium.org>
Date:   Fri Feb 18 12:01:26 2022 -0800

    [opentitantool] Proxy transport implementation
    
    Add a new implementation of the Transport trait, which forwards every
    method invocation via a network protocol to a separate session proxy
    process.
    
    This is to be used either with the session process being a software
    emulator of sorts, or with the session process managing a USB
    connection to a debugger device connected to hardware.
    
    This is one of the steps outlined in issue #10889.  Implementation of
    the session process is in PR #11054.
    
    Signed-off-by: Jes B. Klinke <jbk@chromium.org>
    Change-Id: I6d4cd777a122e3017763704df6632f6f769991fd

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
