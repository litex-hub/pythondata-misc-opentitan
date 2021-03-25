import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5597"
version_tuple = (0, 0, 5597)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5597")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5502"
data_version_tuple = (0, 0, 5502)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5502")
except ImportError:
    pass
data_git_hash = "08adf5b3c38731c39a8bed1b40d7c67b8d8244e6"
data_git_describe = "v0.0-5502-g08adf5b3c"
data_git_msg = """\
commit 08adf5b3c38731c39a8bed1b40d7c67b8d8244e6
Author: Timothy Chen <timothytim@google.com>
Date:   Thu Mar 25 14:38:36 2021 -0700

    [otbn] Wrap non-synthesizeable code with defines
    
    Some dv code in otbn is included as part of the design core files
    to do side by side comparisons.  These files need to be wrapped with
    the SYNTHESIS flag to ensure they do not get parsed for synthesis.
    
    Applying this fix to otbn_memutil_pkg.sv (the same fix is already applied
    to various other model files).
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
