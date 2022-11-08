import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15335"
version_tuple = (0, 0, 15335)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15335")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post15193"
data_version_tuple = (0, 0, 15193)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post15193")
except ImportError:
    pass
data_git_hash = "8d99a2acf58b997811072fa2066a7acd45bfefde"
data_git_describe = "v0.0-15193-g8d99a2acf5"
data_git_msg = """\
commit 8d99a2acf58b997811072fa2066a7acd45bfefde
Author: Dan McArdle <dmcardle@google.com>
Date:   Fri Oct 28 17:31:53 2022 -0400

    [test] Implement rom_e2e_asm_watchdog bite tests
    
    Test that the watchdog's bite resets the core. This is achieved outside
    of GDB, by inspecting its output.
    
    This commit adds the --gdb-expect-output-sequence flag to the GDB test
    coordinator script. When the script sees GDB print each of the given
    lines, in sequence, it will terminate GDB on the spot and consider it a
    success.
    
    This enables us to assert that GDB reaches an echo line from the GDB
    script and *then* sees the core reset.
    
    Signed-off-by: Dan McArdle <dmcardle@google.com>

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
