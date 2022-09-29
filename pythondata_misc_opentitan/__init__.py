import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14495"
version_tuple = (0, 0, 14495)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14495")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14353"
data_version_tuple = (0, 0, 14353)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14353")
except ImportError:
    pass
data_git_hash = "701b38232eb5746efa8a391ab172113366073e2c"
data_git_describe = "v0.0-14353-g701b38232e"
data_git_msg = """\
commit 701b38232eb5746efa8a391ab172113366073e2c
Author: Timothy Trippel <ttrippel@google.com>
Date:   Wed Sep 28 16:47:06 2022 -0700

    [rom_e2e] run `rom_e2e_static_critical` in DV
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

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
