import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8273"
version_tuple = (0, 0, 8273)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8273")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8161"
data_version_tuple = (0, 0, 8161)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8161")
except ImportError:
    pass
data_git_hash = "f6b50a0b96157d6c4d16d694151cb7a1493e4c56"
data_git_describe = "v0.0-8161-gf6b50a0b9"
data_git_msg = """\
commit f6b50a0b96157d6c4d16d694151cb7a1493e4c56
Author: Guillermo Maturana <maturana@google.com>
Date:   Thu Oct 14 08:37:26 2021 -0700

    [dv/clkmgr] Enable threshold writes
    
    Block writes to the measurement enable CSR fields, but allow writes
    to the threshold fields.
    
    Signed-off-by: Guillermo Maturana <maturana@google.com>

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
