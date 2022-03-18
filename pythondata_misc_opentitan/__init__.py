import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10966"
version_tuple = (0, 0, 10966)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10966")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10840"
data_version_tuple = (0, 0, 10840)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10840")
except ImportError:
    pass
data_git_hash = "9aa75b6c931ada30eae0f41efde102e41ec808d2"
data_git_describe = "v0.0-10840-g9aa75b6c9"
data_git_msg = """\
commit 9aa75b6c931ada30eae0f41efde102e41ec808d2
Author: Guillermo Maturana <maturana@google.com>
Date:   Thu Mar 17 11:40:48 2022 -0700

    [dv/full_chip] Fix pwrmgr_rstmgr SVA
    
    This SVA has two problems:
    - The main_rst_req_i (connected to !rst_main_n) should be ignored
      while in deep sleep low power.
    - The ndm_sys_req input is not seen by pwrmgr, so this assertion
      needs to be bound to top_earlgrey at chip level.
    
    The latter problem needs manipulation of the binds for pwrmgr and
    the creation of a new top_earlgrey bind for this specific SVA.
    
    Signed-off-by: Guillermo Maturana <maturana@google.com>

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
