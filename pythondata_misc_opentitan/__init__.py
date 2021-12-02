import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8950"
version_tuple = (0, 0, 8950)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8950")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8838"
data_version_tuple = (0, 0, 8838)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8838")
except ImportError:
    pass
data_git_hash = "15daa83ee2abb7abecc0140bcbe043a013111dfd"
data_git_describe = "v0.0-8838-g15daa83ee"
data_git_msg = """\
commit 15daa83ee2abb7abecc0140bcbe043a013111dfd
Author: Timothy Trippel <ttrippel@google.com>
Date:   Tue Nov 30 00:38:11 2021 +0000

    [sw/ottf] Fix bugs saving/restoring stack pointer in ISRs.
    
    The OTTF was optimized in #9158 to allow running bare-metal tests (in
    place of running each test as a FreeRTOS "task") if the test did NOT
    require spawning (additional) concurrenct tasks.
    
    This introduced a bug in the ISR assembly that saves/restores the current
    execution context to the stack upon entry/exit from the ISR. For tests run
    as a FreeRTOS task, i.e., tests that set the `enable_concurrency` flag in
    the test configuration struct (see `test_config_t` in
    `sw/device/lib/testing/test_framework/ottf.h`), the current stack pointer must
    be saved/restored from the current Task Control Block (TCB) because each
    FreeRTOS task maintains a separate stack and a context switch could
    happen in an exception handler (task yield) or ISR (preemption).
    
    However, for bare-metal tests, the current TCB pointer (which is initialized
    and maintained by FreeRTOS) is NULL. Therefore attempting to dereference
    said pointer results in a store access fault.
    
    This commit fixes this bug by checking the test mode (bare-metal vs.
    concurrency) in the ISR entry/exit assembly to store/load the proper
    execution context state.
    
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
