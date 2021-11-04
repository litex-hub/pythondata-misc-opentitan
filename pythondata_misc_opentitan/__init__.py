import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8587"
version_tuple = (0, 0, 8587)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8587")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8475"
data_version_tuple = (0, 0, 8475)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8475")
except ImportError:
    pass
data_git_hash = "6f4052e5b34a61a057736741334347693dd45ded"
data_git_describe = "v0.0-8475-g6f4052e5b"
data_git_msg = """\
commit 6f4052e5b34a61a057736741334347693dd45ded
Author: Miguel Osorio <miguelosorio@google.com>
Date:   Fri Oct 15 18:28:03 2021 -0700

    [sw] silicon owner bare metal example
    
    This commit adds the sw/device/silicon_owner folder with a bare_metal
    executable which can be used to smoketest the ROM and ROM_EXT secure
    boot sequence.
    
    Signed-off-by: Miguel Osorio <miguelosorio@google.com>

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
