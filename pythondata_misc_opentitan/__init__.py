import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10169"
version_tuple = (0, 0, 10169)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10169")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10045"
data_version_tuple = (0, 0, 10045)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10045")
except ImportError:
    pass
data_git_hash = "d7475c68dfd864117543843bdae1bf956b642011"
data_git_describe = "v0.0-10045-gd7475c68d"
data_git_msg = """\
commit d7475c68dfd864117543843bdae1bf956b642011
Author: Timothy Chen <timothytim@google.com>
Date:   Fri Feb 4 13:21:37 2022 -0800

    [flash_ctral] Various security item clean-up
    
    - harden rma_wipe_idx with prim_count
    - connect seed_err
    - minor documentation clean-up
    
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
