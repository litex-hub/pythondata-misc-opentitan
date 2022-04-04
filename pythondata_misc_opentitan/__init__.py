import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11318"
version_tuple = (0, 0, 11318)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11318")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11192"
data_version_tuple = (0, 0, 11192)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11192")
except ImportError:
    pass
data_git_hash = "98114295f3ee93a4b4ebf1b7326645a5962eb67c"
data_git_describe = "v0.0-11192-g98114295f"
data_git_msg = """\
commit 98114295f3ee93a4b4ebf1b7326645a5962eb67c
Author: Madhuri Patel <madhuri.patel@ensilica.com>
Date:   Thu Mar 31 17:42:02 2022 +0100

    [sysrst_ctrl,dv] Added register reads to fill coverage holes
    
    Few register reads are added in the functional tests to fill
    in the assert coverage holes from sysrst_ctrl_csr_assert module.
    
    Signed-off-by: Madhuri Patel <madhuri.patel@ensilica.com>

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
