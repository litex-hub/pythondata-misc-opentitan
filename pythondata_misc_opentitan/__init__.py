import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11014"
version_tuple = (0, 0, 11014)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11014")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10888"
data_version_tuple = (0, 0, 10888)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10888")
except ImportError:
    pass
data_git_hash = "b5596ad48518a8b227979afffc7d87472c181e00"
data_git_describe = "v0.0-10888-gb5596ad48"
data_git_msg = """\
commit b5596ad48518a8b227979afffc7d87472c181e00
Author: Srikrishna Iyer <sriyer@google.com>
Date:   Sat Mar 19 01:04:15 2022 -0700

    [rvdm dv] SBA access with autoincrement test
    
    This commit refactors the rv_dm_sba_access_vseq to:
    - Enable setting autoincrement
    - Create a lib of sequences with the base vseq doing all the work, but
      turning off 'advanced' access types, and extended vseqs turning them
      on instead.
    - Fixes in sba monitor to make autoincrement mode prediction work correctly
    - Addition of rv_dm_autoincr_sba_access_vseq and test
    - Remove constraints in sba_access_item - no longer needed
    - Increase test timeout to 50ms
    
    Signed-off-by: Srikrishna Iyer <sriyer@google.com>
    
    [rv_dm dv] Fixes to enable Xcelium
    
    Signed-off-by: Srikrishna Iyer <sriyer@google.com>

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
