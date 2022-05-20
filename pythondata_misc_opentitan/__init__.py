import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12257"
version_tuple = (0, 0, 12257)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12257")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12129"
data_version_tuple = (0, 0, 12129)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12129")
except ImportError:
    pass
data_git_hash = "2f16efd630e32884772a4c3446c57109a995cf5a"
data_git_describe = "v0.0-12129-g2f16efd63"
data_git_msg = """\
commit 2f16efd630e32884772a4c3446c57109a995cf5a
Author: Eunchan Kim <eunchan@opentitan.org>
Date:   Thu May 19 17:03:04 2022 -0700

    fix(ottf): Make SWI asynchronous ISR
    
    https://github.com/lowRISC/opentitan/issues/12787
    
    SWI in `ottf_isrs.S` was synchronous, where the logic changes MEPC by
    adding the instruction size.
    
    However, SWI in Opentitan (and according to Spec) is asynchronous. In
    OpenTitan, after setting MSIP (Memory Mapped CSR in RV_PLIC), the
    software interrupt occurs two cycles later due to the fabric latency and
    the register update in RV_PLIC.
    
    So, `handler_software_isr` is revised to store MEPC directly to the
    stack not manipulating it.
    
    Signed-off-by: Eunchan Kim <eunchan@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post128"
tool_version_tuple = (0, 0, 128)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post128")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
