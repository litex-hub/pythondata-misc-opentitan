import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9660"
version_tuple = (0, 0, 9660)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9660")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9538"
data_version_tuple = (0, 0, 9538)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9538")
except ImportError:
    pass
data_git_hash = "722d1fa9d62abf1c1a2cc8d06eba7eae0c540c47"
data_git_describe = "v0.0-9538-g722d1fa9d"
data_git_msg = """\
commit 722d1fa9d62abf1c1a2cc8d06eba7eae0c540c47
Author: Timothy Trippel <ttrippel@google.com>
Date:   Tue Jan 18 14:58:14 2022 -0800

    [dif/alert_handler] Fix bug in ping timer lock DIFs.
    
    The DIFs that checked whether the ping timer configuration was locked,
    and locked it, read-from/wrote-to the wrong CSR (the ping timer enable
    CSR). This commit fixes these two DIFs to write to the correct ping
    timer REGWEN CSR.
    
    This partially addresses a task in #9899.
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

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
