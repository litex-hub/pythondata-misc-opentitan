import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11273"
version_tuple = (0, 0, 11273)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11273")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11147"
data_version_tuple = (0, 0, 11147)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11147")
except ImportError:
    pass
data_git_hash = "dbf6803b799c214f6e75a8449216c8e556d58998"
data_git_describe = "v0.0-11147-gdbf6803b7"
data_git_msg = """\
commit dbf6803b799c214f6e75a8449216c8e556d58998
Author: Miguel Young de la Sota <mcyoung@google.com>
Date:   Tue Mar 29 15:02:32 2022 -0400

    [lib] Use dual_cc_library for core mockable libraries
    
    Signed-off-by: Miguel Young de la Sota <mcyoung@google.com>

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
