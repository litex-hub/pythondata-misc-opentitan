import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8193"
version_tuple = (0, 0, 8193)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8193")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8081"
data_version_tuple = (0, 0, 8081)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8081")
except ImportError:
    pass
data_git_hash = "ae48437a36306e22e5d0e7b2c08eeccbc1ae0d3e"
data_git_describe = "v0.0-8081-gae48437a3"
data_git_msg = """\
commit ae48437a36306e22e5d0e7b2c08eeccbc1ae0d3e
Author: Timothy Trippel <ttrippel@google.com>
Date:   Thu Oct 7 06:42:41 2021 +0000

    [dif/usbdev] Integrate autogen'd DIF artifacts into src tree.
    
    This commit partially addresses #8142. Specifically it:
    1. deprecates existing (manually implemented) **USB Device**
       specific DIF return codes and toggle types,
    2. integrates the auto-generated **USB Device** DIFs into meson build
       targets, and.
    3. refactors all existing source code to make use of the new shared DIF
       types and error codes.
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

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
