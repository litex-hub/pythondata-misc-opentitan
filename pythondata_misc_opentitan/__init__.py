import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13072"
version_tuple = (0, 0, 13072)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13072")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12930"
data_version_tuple = (0, 0, 12930)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12930")
except ImportError:
    pass
data_git_hash = "f3266dc363ee3c5f0a8a2a65381dfb9797a4fc26"
data_git_describe = "v0.0-12930-gf3266dc363"
data_git_msg = """\
commit f3266dc363ee3c5f0a8a2a65381dfb9797a4fc26
Author: Guillermo Maturana <maturana@google.com>
Date:   Wed Jul 13 12:21:49 2022 -0700

    [dv/rstrmgr] Update list of rstmgr_leaf_rst
    
    Update list per design change, and suggest a way to generate the list to
    ease updates. The incorrect list was causing all rstmgr_leaf_rst_cnsty
    tests to fail.
    
    Signed-off-by: Guillermo Maturana <maturana@google.com>

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
