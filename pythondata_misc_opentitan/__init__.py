import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14633"
version_tuple = (0, 0, 14633)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14633")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14491"
data_version_tuple = (0, 0, 14491)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14491")
except ImportError:
    pass
data_git_hash = "5ed2fcbac1ecd25c4a0b4485213b08985aaeaac6"
data_git_describe = "v0.0-14491-g5ed2fcbac1"
data_git_msg = """\
commit 5ed2fcbac1ecd25c4a0b4485213b08985aaeaac6
Author: Weicai Yang <weicai@google.com>
Date:   Fri Oct 7 16:04:56 2022 -0700

    [spi_device/dv] Add flash and TPM concurrent sequence
    
    1. Run both sequences in parallel
    2. update seq/scb to fix a few issues
      - CSB needs to be set via transactions
      - avoid accessing the same CFG csr at the same time
      - In some extrem case, tpm_write_spi_q may contains 2 items
    
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
