import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8654"
version_tuple = (0, 0, 8654)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8654")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8542"
data_version_tuple = (0, 0, 8542)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8542")
except ImportError:
    pass
data_git_hash = "feaf322edd8a0f7f6a032cbb6b7537005fd613d7"
data_git_describe = "v0.0-8542-gfeaf322ed"
data_git_msg = """\
commit feaf322edd8a0f7f6a032cbb6b7537005fd613d7
Author: Timothy Chen <timothytim@google.com>
Date:   Tue Nov 2 13:49:43 2021 -0700

    [flash_ctrl] Add plain text integrity in flash
    
    - Fixes https://github.com/lowRISC/opentitan/issues/8984
    - Takes the spare storage bits of flash and store a de-scrambled
      integrity. This allows flash to emulate the behavior of end-to-end
      storage despite its need for ECC reliability checks.
    
    Signed-off-by: Timothy Chen <timothytim@google.com>
    
    [sw, util] Add support for flash image generation
    
    - only supports the plain text ECC at the moment
    - scrambled will be added in the future
    
    Signed-off-by: Timothy Chen <timothytim@google.com>
    
    [test] update verilator CI test pathing
    
    flash now uses vmem instead of elf
    
    Signed-off-by: Timothy Chen <timothytim@google.com>
    
    [flash_ctrl] python updates per comments
    
    Signed-off-by: Timothy Chen <timothytim@google.com>
    
    [flash_ctrl] fix typo
    
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
