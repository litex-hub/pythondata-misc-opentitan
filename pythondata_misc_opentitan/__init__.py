import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8833"
version_tuple = (0, 0, 8833)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8833")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8721"
data_version_tuple = (0, 0, 8721)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8721")
except ImportError:
    pass
data_git_hash = "201acb720e5d518623f08de532f28d3b8dac552c"
data_git_describe = "v0.0-8721-g201acb720"
data_git_msg = """\
commit 201acb720e5d518623f08de532f28d3b8dac552c
Author: Silvestrs Timofejevs <silvestrst@lowrisc.org>
Date:   Tue Nov 9 17:01:51 2021 +0000

    [sw, tests] Refactor sram_ctrl scramble test and test utils
    
    The main purpose of this change is to make the test util more
    generic. It also includes some suggestions from the other PRs, such as
    avoiding dependencies on top_earlgrey in test utils.
    
    - Renamed test utils API to match accepted style
      `sram_ctrl_testutils_<...>`.
    
    - Testutils are more generic, they operate on the passed in address
      instead of top_earlgrey addresses calculated inside the util.
    
    - Init functions have been removed from test utils.
    
    - Unnecessary data structures have been removed from test utils.
    
    - Test has been simplified to only perform a single check at the start
      of RAM, as opposed to former the start and the end of RAM. If
      required, we can always add the end of RAM check later.
    
    In a nutshell, the test util API was simplified and some of this
    complexity was moved to the test instead.
    
    Signed-off-by: Silvestrs Timofejevs <silvestrst@lowrisc.org>

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
