import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10761"
version_tuple = (0, 0, 10761)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10761")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10635"
data_version_tuple = (0, 0, 10635)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10635")
except ImportError:
    pass
data_git_hash = "42b6418983636ae28f4f7de2b25380bd7543277a"
data_git_describe = "v0.0-10635-g42b641898"
data_git_msg = """\
commit 42b6418983636ae28f4f7de2b25380bd7543277a
Author: Eunchan Kim <eunchan@opentitan.org>
Date:   Mon Mar 7 13:52:56 2022 -0800

    [kmac] Lint fix
    
    entropy_refresh_threshold_shadowed q and qe were AND-ed, which results
    the signal becomes 1 bit signal. `qe` signal has been removed in this
    commit.
    
    Signed-off-by: Eunchan Kim <eunchan@opentitan.org>

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
