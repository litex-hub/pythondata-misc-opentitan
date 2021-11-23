import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8847"
version_tuple = (0, 0, 8847)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8847")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8735"
data_version_tuple = (0, 0, 8735)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8735")
except ImportError:
    pass
data_git_hash = "8bc0d84851b34c08a67728929532c9f8740dc471"
data_git_describe = "v0.0-8735-g8bc0d8485"
data_git_msg = """\
commit 8bc0d84851b34c08a67728929532c9f8740dc471
Author: Jes B. Klinke <jbk@chromium.org>
Date:   Wed Nov 3 19:10:59 2021 -0700

    [opentitantool] Support bootstrap protocol of legacy chips
    
    Implement the bootstrapping protocol used by previous generations of
    Google Titan chips.
    
    Signed-off-by: Jes B. Klinke <jbk@chromium.org>

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
