import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8572"
version_tuple = (0, 0, 8572)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8572")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8460"
data_version_tuple = (0, 0, 8460)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8460")
except ImportError:
    pass
data_git_hash = "7d6d53d11f21675a558da1eb51fc93c1329ca7c9"
data_git_describe = "v0.0-8460-g7d6d53d11"
data_git_msg = """\
commit 7d6d53d11f21675a558da1eb51fc93c1329ca7c9
Author: Timothy Chen <timothytim@google.com>
Date:   Mon Nov 1 15:17:08 2021 -0700

    [sram_ctrl] Fix sram error checking and byte sequencing
    
    - Should fix #8905
    - Previously, the error checking was mostly done downstream of
      sram_byte. This meant that illegal write transactions would
      become correctly transformed by the sram_byte module, and thus
      the would-be error silenced.
    - This PR moves all the error checking upstream of the sram byte
      module and passes the error through if it is observed. This is
      more consistent error behavior.
    - The documentation is also updated with a high level overview on
      how the adapater sram behaves.
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
