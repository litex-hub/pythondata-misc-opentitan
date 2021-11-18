import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8768"
version_tuple = (0, 0, 8768)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8768")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8656"
data_version_tuple = (0, 0, 8656)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8656")
except ImportError:
    pass
data_git_hash = "ce3374c2ab0e9c35a48170508c23c2c3403e2147"
data_git_describe = "v0.0-8656-gce3374c2a"
data_git_msg = """\
commit ce3374c2ab0e9c35a48170508c23c2c3403e2147
Author: Timothy Trippel <ttrippel@google.com>
Date:   Fri Nov 12 01:54:12 2021 +0000

    [sw/ottf] Add malloc failure and stack overflow hooks.
    
    The OTTF uses FreeRTOS to enable running concurrent tasks within a test.
    When a new task is created, memory for the TCB and stack are allocated
    using FreeRTOS's malloc implementation. Currently the size of the heap
    is fixed to 0x800u bytes. This commit adds FreeRTOS hooks that display
    a useful message to test developers and abort the test when FreeRTOS
    detects a malloc failure or stack overflow.
    
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
