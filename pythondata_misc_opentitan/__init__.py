import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14802"
version_tuple = (0, 0, 14802)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14802")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14660"
data_version_tuple = (0, 0, 14660)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14660")
except ImportError:
    pass
data_git_hash = "daf347013a100a8f36e4b43e0e727d89d1e25e5e"
data_git_describe = "v0.0-14660-gdaf347013a"
data_git_msg = """\
commit daf347013a100a8f36e4b43e0e727d89d1e25e5e
Author: Jade Philipoom <jadep@google.com>
Date:   Fri Oct 14 16:14:25 2022 +0200

    [crypto] Update API header file.
    
    Changes since the last update:
    - Key generation functions for symmetric crypto (AES, KMAC, HMAC) since
      these are needed for sideloading
    - New exposed blinded key configuration struct to help caller allocate
      space for blinded keys and communicate requirements
    - AES init/cipher merged into one function
    - DRBG state struct removed (the state is the hardware state, and
      providing a software state implies it's possible to instantiate
    multiple DRBGs)
    
    Signed-off-by: Jade Philipoom <jadep@google.com>

"""

# Tool version info
tool_version_str = "0.0.post142"
tool_version_tuple = (0, 0, 142)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post142")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
