import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10550"
version_tuple = (0, 0, 10550)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10550")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10424"
data_version_tuple = (0, 0, 10424)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10424")
except ImportError:
    pass
data_git_hash = "be42c349621dfc9d8d2cbb1e949a70d28462b7e0"
data_git_describe = "v0.0-10424-gbe42c3496"
data_git_msg = """\
commit be42c349621dfc9d8d2cbb1e949a70d28462b7e0
Author: Guillermo Maturana <maturana@google.com>
Date:   Thu Feb 24 18:12:18 2022 -0800

    [dv/rstmgr] Fix handling cpu dump info
    
    Enhance the cpu dump info check to go through all words.
    Consistently use rv_core_ibex_pkg instead of ibex_pkg for the dump info.
    
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
