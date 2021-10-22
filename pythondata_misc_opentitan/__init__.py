import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8406"
version_tuple = (0, 0, 8406)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8406")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8294"
data_version_tuple = (0, 0, 8294)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8294")
except ImportError:
    pass
data_git_hash = "b76772206fdb7839b4ee0f586de309826611b8f5"
data_git_describe = "v0.0-8294-gb76772206"
data_git_msg = """\
commit b76772206fdb7839b4ee0f586de309826611b8f5
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Thu Oct 21 16:33:16 2021 +0100

    [spi_device,lint] Remove double-import of parameters
    
    In spid_status, we're already importing spi_device_pkg::* into the
    module's scope, so this line was shadowing CmdInfoIdxW (with itself!)
    and Verilator spat out a warning.
    
    In spi_passthrough, we were importing spi_device_pkg, which exports
    NumCmdInfo, shadowed by the NumCmdInfo parameter. We then instantiate
    it (in spi_device.sv), setting the parameter to the thing it's
    shadowing. Get rid of the parameter entirely.
    
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
