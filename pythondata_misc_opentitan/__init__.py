import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8664"
version_tuple = (0, 0, 8664)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8664")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8552"
data_version_tuple = (0, 0, 8552)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8552")
except ImportError:
    pass
data_git_hash = "d4777ca3e80f843df41b6fb8a6836d4734721611"
data_git_describe = "v0.0-8552-gd4777ca3e"
data_git_msg = """\
commit d4777ca3e80f843df41b6fb8a6836d4734721611
Author: Srikrishna Iyer <sriyer@google.com>
Date:   Tue Nov 9 14:30:05 2021 -0800

    [chip,dv] Refactor CSR exclusion method
    
    - Minor refactor of `csr_excl_item`
      - fixed minor bugs that existed in original code
      - split `has_excl` to cleanly separate the task of retrieving the
      associative array index from `exclusions` data structure into a
      separate local task.
      - cleaned up method doc comments
    
    - Added support for tmporarily disable exclusions in effect (request
    from @NigelScales)
    
    Signed-off-by: Srikrishna Iyer <sriyer@google.com>

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
