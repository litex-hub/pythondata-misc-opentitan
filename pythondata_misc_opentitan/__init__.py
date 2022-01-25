import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9796"
version_tuple = (0, 0, 9796)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9796")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9674"
data_version_tuple = (0, 0, 9674)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9674")
except ImportError:
    pass
data_git_hash = "89da9f00f08426ca8d1977b0390d68dd33ceddc7"
data_git_describe = "v0.0-9674-g89da9f00f"
data_git_msg = """\
commit 89da9f00f08426ca8d1977b0390d68dd33ceddc7
Author: Guillermo Maturana <maturana@google.com>
Date:   Tue Jan 25 06:47:42 2022 -0800

    [dv/pwrmgr] Fix failure due to timing conflicts
    
    The pwrmgr_wakeup_reset sequence occasionally fails because
    twirl_rom_response waits conflict with other waits for checking
    wakeup status.
    
    Signed-off-by: Guillermo Maturana <maturana@google.com>

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
