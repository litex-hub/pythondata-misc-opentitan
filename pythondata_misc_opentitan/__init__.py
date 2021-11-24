import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8848"
version_tuple = (0, 0, 8848)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8848")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8736"
data_version_tuple = (0, 0, 8736)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8736")
except ImportError:
    pass
data_git_hash = "2527f074c9a708b6a743774a9e9baa5ee85817de"
data_git_describe = "v0.0-8736-g2527f074c"
data_git_msg = """\
commit 2527f074c9a708b6a743774a9e9baa5ee85817de
Author: Jason Hoddinett <jason.hoddinett.ensilica@opentitan.org>
Date:   Mon Nov 22 10:25:15 2021 +0000

    [spi_device/testplan] Testplan with TPM testpoints
    
    Signed-off-by: Jason Hoddinett <jason.hoddinett.ensilica@opentitan.org>

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
