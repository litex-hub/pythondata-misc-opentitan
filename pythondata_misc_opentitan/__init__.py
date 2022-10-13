import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14738"
version_tuple = (0, 0, 14738)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14738")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14596"
data_version_tuple = (0, 0, 14596)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14596")
except ImportError:
    pass
data_git_hash = "f1288c8633be5f0459e12a3557a4a25dab4eb3d1"
data_git_describe = "v0.0-14596-gf1288c8633"
data_git_msg = """\
commit f1288c8633be5f0459e12a3557a4a25dab4eb3d1
Author: Eli Kim <eli@opentitan.org>
Date:   Thu Oct 13 10:49:07 2022 -0700

    doc(spid): TPM_CMDADDR_NOTEMPTY interrupt
    
    * _Related PR: https://github.com/lowRISC/opentitan/pull/15442_
    * _Related Issue: https://github.com/lowRISC/opentitan/issues/15282_
    
    This commit describes how-to process the `tpm_cmdaddr_notempty`
    interrupt.
    
    Signed-off-by: Eli Kim <eli@opentitan.org>

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
