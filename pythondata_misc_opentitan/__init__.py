import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12500"
version_tuple = (0, 0, 12500)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12500")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12358"
data_version_tuple = (0, 0, 12358)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12358")
except ImportError:
    pass
data_git_hash = "1241a73768fa7a2cf3296716dc0f4801ad3a61df"
data_git_describe = "v0.0-12358-g1241a7376"
data_git_msg = """\
commit 1241a73768fa7a2cf3296716dc0f4801ad3a61df
Author: Eunchan Kim <eunchan@opentitan.org>
Date:   Fri Jun 3 11:28:34 2022 -0700

    fix(spi_device): Lint error
    
    This commit fixes unused cmdfifo_depth errors in the lint tool. The
    signal is being used in the assertion not in the actual logic.
    
    Signed-off-by: Eunchan Kim <eunchan@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post142"
tool_version_tuple = (0, 0, 142)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post142")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
