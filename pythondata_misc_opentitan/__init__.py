import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14515"
version_tuple = (0, 0, 14515)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14515")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14373"
data_version_tuple = (0, 0, 14373)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14373")
except ImportError:
    pass
data_git_hash = "c64e5f1785046c9a545427bd280100c2ddd92e3f"
data_git_describe = "v0.0-14373-gc64e5f1785"
data_git_msg = """\
commit c64e5f1785046c9a545427bd280100c2ddd92e3f
Author: Weicai Yang <weicai@google.com>
Date:   Thu Sep 29 16:35:11 2022 -0700

    [spi_device/dv] update scb for TPM HW returned reg
    
    1. predict and compare HW returned reg in scb
    2. renamed tpm_locality_vseq -> tpm_sts_read_vseq
    3. Removed some unused parameters
    
    Signed-off-by: Weicai Yang <weicai@google.com>

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
