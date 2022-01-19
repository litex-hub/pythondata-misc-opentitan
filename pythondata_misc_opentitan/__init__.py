import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9620"
version_tuple = (0, 0, 9620)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9620")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9498"
data_version_tuple = (0, 0, 9498)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9498")
except ImportError:
    pass
data_git_hash = "0510546e5031b7723737bd71903626b315c74dae"
data_git_describe = "v0.0-9498-g0510546e5"
data_git_msg = """\
commit 0510546e5031b7723737bd71903626b315c74dae
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Fri Jan 14 17:34:27 2022 -0800

    [dv/jtag] support rv_dm in jtag_riscv_reg_adapter
    
    This PR adds a flag in jtag_riscv_agent_cfg to support accessing jtag
    csr_rd/wr via rv_dm.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post122"
tool_version_tuple = (0, 0, 122)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post122")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
