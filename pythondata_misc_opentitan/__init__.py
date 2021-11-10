import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8657"
version_tuple = (0, 0, 8657)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8657")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8545"
data_version_tuple = (0, 0, 8545)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8545")
except ImportError:
    pass
data_git_hash = "7c3a3cf66f98addd676933b8cc26e90cd46fd9a4"
data_git_describe = "v0.0-8545-g7c3a3cf66"
data_git_msg = """\
commit 7c3a3cf66f98addd676933b8cc26e90cd46fd9a4
Author: Miguel Osorio <miguelosorio@google.com>
Date:   Thu Nov 4 09:24:14 2021 -0700

    [sw/mask_rom] Move keys inside the mask_rom folder
    
    This comming implement the following changes:
    
    * Move ROM public keys inside the sw/device/silicon_creator/mask_rom/keys folder.
    * Split keys into header files to simplify auditing.
    * Update the key policies to TEST, as the device boots by default in RMA
      mode in the repository.
    * Change the key names from fpga_key to test_key.
    
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
