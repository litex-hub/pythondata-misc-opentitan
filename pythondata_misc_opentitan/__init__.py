import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5237"
version_tuple = (0, 0, 5237)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5237")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5146"
data_version_tuple = (0, 0, 5146)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5146")
except ImportError:
    pass
data_git_hash = "6940d94cd03b5f75aec543086182c4b8151e49fe"
data_git_describe = "v0.0-5146-g6940d94cd"
data_git_msg = """\
commit 6940d94cd03b5f75aec543086182c4b8151e49fe
Author: Silvestrs Timofejevs <silvestrst@lowrisc.org>
Date:   Thu Feb 4 16:29:33 2021 +0000

    [sw, rom_ext_signer] Add signing and remaining image update API
    
    - Retrieving exponent is work-in-progress, and at the moment
      dummy hardcoded vector of `0xA5` is used.
    - Retrieving modulus is work-in-progress, and at the moment
      dummy hardcoded vector of `0xA5` is used.
    - Peripheral Lockdown Info encodingis work in progress, and at
      the moment dummy hardcoded vector of `0xA5` is used.
    - It is not clear yet how the device_usage_value is encoded in
      the 256-bit usage_constraints blob, and at the moment dummy
      hardcoded vector of `0xA5` is used.
    
    This change adds image signing functionality through Mundane.
    
    * There was some refactoring done, missing fields
      `extension{0,1,2,3}_offset` have been added.
    
    * `image_length` is no longer passed in the config, as it is
      set automatically in the manifest assembly file.
    
    * `image_timestamp` is no longer passed in the config, and is
      calculated at runtime.
    
    Signed-off-by: Silvestrs Timofejevs <silvestrst@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post91"
tool_version_tuple = (0, 0, 91)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post91")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
