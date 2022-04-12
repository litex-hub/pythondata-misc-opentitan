import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11527"
version_tuple = (0, 0, 11527)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11527")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11401"
data_version_tuple = (0, 0, 11401)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11401")
except ImportError:
    pass
data_git_hash = "ec4ba7fbeee61e23cfa328921342a7fb4cfe10ee"
data_git_describe = "v0.0-11401-gec4ba7fbe"
data_git_msg = """\
commit ec4ba7fbeee61e23cfa328921342a7fb4cfe10ee
Author: Eunchan Kim <eunchan@opentitan.org>
Date:   Mon Apr 11 16:26:32 2022 -0700

    [spi_device] Add payloadptr (last written) and overflow event
    
    Add last written payloadptr and overflow event and synchronization logic
    to SYS clock domain.
    
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
