import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8536"
version_tuple = (0, 0, 8536)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8536")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8424"
data_version_tuple = (0, 0, 8424)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8424")
except ImportError:
    pass
data_git_hash = "dd81b3f8953683318424af1903f53bc3a8687d53"
data_git_describe = "v0.0-8424-gdd81b3f89"
data_git_msg = """\
commit dd81b3f8953683318424af1903f53bc3a8687d53
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Thu Oct 21 17:17:12 2021 +0100

    [spi_device,lint] Waive width mismatch warning
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

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
