import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10045"
version_tuple = (0, 0, 10045)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10045")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9921"
data_version_tuple = (0, 0, 9921)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9921")
except ImportError:
    pass
data_git_hash = "fc31f2be84afcaee9c1450f770525e966e6d4e11"
data_git_describe = "v0.0-9921-gfc31f2be8"
data_git_msg = """\
commit fc31f2be84afcaee9c1450f770525e966e6d4e11
Author: Timothy Chen <timothytim@google.com>
Date:   Wed Feb 2 17:24:41 2022 -0800

    [dv] Fixes to enable foundry database pwrmgr_smoketest
    
    - The old sram randomization scheme did not work because it treated each
      tile as an independent memory.  This meant if the address scramble caused
      a word to be relocated to another tile, the write would not work correctly.
    
    - This PR addes some enhancements to calculate the target tile and ensures the
      scrmabled data is written to the right place.
    
    - A few helper functions are added to mem_bkdr_util__sram.sv, these should be
      used locally in the other functions as well to reduce code duplication.
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

"""

# Tool version info
tool_version_str = "0.0.post124"
tool_version_tuple = (0, 0, 124)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post124")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
