import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10281"
version_tuple = (0, 0, 10281)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10281")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10155"
data_version_tuple = (0, 0, 10155)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10155")
except ImportError:
    pass
data_git_hash = "1e28703e3e1644bb8ca772fef8d306d1d0b5e595"
data_git_describe = "v0.0-10155-g1e28703e3"
data_git_msg = """\
commit 1e28703e3e1644bb8ca772fef8d306d1d0b5e595
Author: Alphan Ulusoy <alphan@google.com>
Date:   Sun Feb 13 12:26:14 2022 -0500

    [sw/silicon_creator] Move watchdog calls to primitive_bootstrap()
    
    Signed-off-by: Alphan Ulusoy <alphan@google.com>

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
