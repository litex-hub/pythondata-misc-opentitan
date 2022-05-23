import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12280"
version_tuple = (0, 0, 12280)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12280")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12152"
data_version_tuple = (0, 0, 12152)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12152")
except ImportError:
    pass
data_git_hash = "bfbbbdd62355067ffc52d6c6fd60bd5948db3530"
data_git_describe = "v0.0-12152-gbfbbbdd62"
data_git_msg = """\
commit bfbbbdd62355067ffc52d6c6fd60bd5948db3530
Author: Alexander Williams <awill@google.com>
Date:   Fri May 20 08:45:02 2022 -0700

    [spi_device/dif] Update DIF checklist
    
    Signed-off-by: Alexander Williams <awill@google.com>

"""

# Tool version info
tool_version_str = "0.0.post128"
tool_version_tuple = (0, 0, 128)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post128")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
