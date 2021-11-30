import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8900"
version_tuple = (0, 0, 8900)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8900")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8788"
data_version_tuple = (0, 0, 8788)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8788")
except ImportError:
    pass
data_git_hash = "13ed3e95572168f7db0e3178d06a72e72ee5a745"
data_git_describe = "v0.0-8788-g13ed3e955"
data_git_msg = """\
commit 13ed3e95572168f7db0e3178d06a72e72ee5a745
Author: Timothy Chen <timothytim@google.com>
Date:   Mon Nov 29 17:51:57 2021 -0800

    [flash_ctrl] First step fix for flash ECC
    
    - Should address #9397
    - Merge the separate flash data / metadata memories back into one
    - Update the backdoor path to use the full 76_68 ECC scheme
    - Update flash backdoor load to create the extra 4-bits of integrity
      ECC for the purposes of backdoor load.
    - The flash routine is responsible for the 4-bit integrity ECC, while
      the mem_bkdr_util routine is responsible for the 8-bit reliability
      ECC
    
    - In the future, the same routine that creates the 4-bit integrity
      ECC will also be responsible for scramble, the final backdoor load
      will only be aware of the 8-bit reliability ECC.
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
