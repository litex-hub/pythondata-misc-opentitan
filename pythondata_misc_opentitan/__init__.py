import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14968"
version_tuple = (0, 0, 14968)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14968")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14826"
data_version_tuple = (0, 0, 14826)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14826")
except ImportError:
    pass
data_git_hash = "850f2ac7ba4b301e8bd7bda17884fff5157230c7"
data_git_describe = "v0.0-14826-g850f2ac7ba"
data_git_msg = """\
commit 850f2ac7ba4b301e8bd7bda17884fff5157230c7
Author: Guillermo Maturana <maturana@google.com>
Date:   Tue Oct 25 16:04:50 2022 -0700

    [dv/rstmgr] Fix rstmgr_sec_cm_scan_intersig_mubi_vseq
    
    The scanmode_i changes need to track scan_rst_ni so the underlying test
    will correctly predict when scan reset occur. Change the duration of
    settings of scanmode_i so it will have a chance to change value when
    scan_rst_ni changes.
    
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
