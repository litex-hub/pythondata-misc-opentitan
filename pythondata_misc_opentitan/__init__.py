import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15260"
version_tuple = (0, 0, 15260)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15260")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post15118"
data_version_tuple = (0, 0, 15118)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post15118")
except ImportError:
    pass
data_git_hash = "c9b812f581cfd4e595a455620c0a5e14f0fdc370"
data_git_describe = "v0.0-15118-gc9b812f581"
data_git_msg = """\
commit c9b812f581cfd4e595a455620c0a5e14f0fdc370
Author: Guillermo Maturana <maturana@google.com>
Date:   Sat Nov 5 08:15:45 2022 -0700

    [tools/dvsim] Remove old cdc plusargs from common_sim_cfg
    
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
