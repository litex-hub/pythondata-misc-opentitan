import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10457"
version_tuple = (0, 0, 10457)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10457")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10331"
data_version_tuple = (0, 0, 10331)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10331")
except ImportError:
    pass
data_git_hash = "9e14e830adf072f8c766278c855308e6a830f6fb"
data_git_describe = "v0.0-10331-g9e14e830a"
data_git_msg = """\
commit 9e14e830adf072f8c766278c855308e6a830f6fb
Author: Michael Munday <mike.munday@lowrisc.org>
Date:   Fri Feb 18 15:01:37 2022 +0000

    [ibex] Set ePMP reset values (ROM: LRX, MMIO: LRW, MMWP=1, RLB=1)
    
    After reset ePMP will be configured as follows:
    
     | Entry | Address Space | Encoding | Permissions |
     |-------|---------------|----------|-------------|
     | 2     | ROM           | NAPOT    | LRX         |
     | 11    | MMIO          | TOR      | LRW         |
    
    Machine mode whitelist policy (MMWP) and rule locking bypass (RLB)
    will also be enabled.
    
    This change also modifies the test ROM so that it sets up the ePMP
    configuration such that read, write and execute accesses are
    permitted anywhere in the address space to match the pre-existing
    behavior.
    
    Finally some ePMP configuration done by the mask ROM is redundant
    and so has been removed. The mask ROM checks the ePMP configuration
    is as expected and this code is not changed.
    
    Fixes #7834.
    
    Signed-off-by: Michael Munday <mike.munday@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post126"
tool_version_tuple = (0, 0, 126)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post126")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
