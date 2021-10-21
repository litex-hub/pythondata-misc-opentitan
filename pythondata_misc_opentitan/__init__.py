import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8367"
version_tuple = (0, 0, 8367)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8367")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8255"
data_version_tuple = (0, 0, 8255)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8255")
except ImportError:
    pass
data_git_hash = "ddea231c278fc3d7dbc3625c43ad6b995730bfc9"
data_git_describe = "v0.0-8255-gddea231c2"
data_git_msg = """\
commit ddea231c278fc3d7dbc3625c43ad6b995730bfc9
Author: Miguel Osorio <miguelosorio@google.com>
Date:   Fri Oct 15 14:42:15 2021 -0700

    [sw/rom] Add rom_ext sec_mmio initialization
    
    sec_mmio initialization for the ROM_EXT clears the current check count
    expectation and resets all entries in the expectation table that were
    not used by the ROM. This is to ensure that an attacker is not able to
    recreate the state of the expectation table after injecting a reset
    fault.
    
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
