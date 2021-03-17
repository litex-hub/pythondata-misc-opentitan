import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5417"
version_tuple = (0, 0, 5417)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5417")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5322"
data_version_tuple = (0, 0, 5322)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5322")
except ImportError:
    pass
data_git_hash = "bcf75e589ce8590d5e74be15f4c0113e998b2c60"
data_git_describe = "v0.0-5322-gbcf75e589"
data_git_msg = """\
commit bcf75e589ce8590d5e74be15f4c0113e998b2c60
Author: Eitan Shapira <eitan.shapira@nuvoton.com>
Date:   Sun Mar 14 12:41:18 2021 +0200

    [dv/flash_ctrl] Added some configs to flash_ctrl_seq_cfg & rand_ops_vseq
    
    Signed-off-by: Eitan Shapira <eitan.shapira@nuvoton.com>

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
