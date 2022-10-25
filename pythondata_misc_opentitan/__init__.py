import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14944"
version_tuple = (0, 0, 14944)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14944")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14802"
data_version_tuple = (0, 0, 14802)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14802")
except ImportError:
    pass
data_git_hash = "6923df040fc87f664a1307e56ba5ba9f65301a8a"
data_git_describe = "v0.0-14802-g6923df040f"
data_git_msg = """\
commit 6923df040fc87f664a1307e56ba5ba9f65301a8a
Author: Guillermo Maturana <maturana@google.com>
Date:   Fri Oct 21 15:26:35 2022 -0700

    [dv/rstmgr] Exclude sw_rst_ctrl_n CSR from unit csr tests
    
    Rapid flips of these CSR bits can occasionally trigger alerts, which
    can unpredictably update err_code CSR bits.
    
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
