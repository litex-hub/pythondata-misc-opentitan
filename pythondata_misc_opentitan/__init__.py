import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11391"
version_tuple = (0, 0, 11391)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11391")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11265"
data_version_tuple = (0, 0, 11265)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11265")
except ImportError:
    pass
data_git_hash = "75082fb5a6a92ec58d7adfb9abf7bfacb26f87c7"
data_git_describe = "v0.0-11265-g75082fb5a"
data_git_msg = """\
commit 75082fb5a6a92ec58d7adfb9abf7bfacb26f87c7
Author: Timothy Chen <timothytim@google.com>
Date:   Mon Apr 4 10:52:33 2022 -0700

    [flash_ctrl] Incorporate flash disable into flash_exec
    
    - also add handling for what happens if instr_type is invalid
      This was previously handled as part of transmission integrity, but
      it does not hurt to make it more explicit.
    
    - fixes #11883
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
