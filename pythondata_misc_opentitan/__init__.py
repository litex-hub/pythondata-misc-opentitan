import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10737"
version_tuple = (0, 0, 10737)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10737")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10611"
data_version_tuple = (0, 0, 10611)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10611")
except ImportError:
    pass
data_git_hash = "88661666fe205af9f8e10ee72c18e5002d092234"
data_git_describe = "v0.0-10611-g88661666f"
data_git_msg = """\
commit 88661666fe205af9f8e10ee72c18e5002d092234
Author: Alexander Williams <awill@google.com>
Date:   Fri Mar 4 18:16:20 2022 -0800

    [aes] Restore placement constraints
    
    clkmgr changed hierarchies, causing the AES placement constraints to
    be dropped. Restore these to bring back down FPGA build times.
    
    Also promote to an error the message about adding an empty list of cells
    to a pblock.
    
    Signed-off-by: Alexander Williams <awill@google.com>

"""

# Tool version info
tool_version_str = "0.0.post126"
tool_version_tuple = (0, 0, 126)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post126")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
