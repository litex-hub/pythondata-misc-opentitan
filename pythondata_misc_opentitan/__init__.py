import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15014"
version_tuple = (0, 0, 15014)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15014")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14872"
data_version_tuple = (0, 0, 14872)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14872")
except ImportError:
    pass
data_git_hash = "92440a24af6e09e52551aa112c85dd0b5588acef"
data_git_describe = "v0.0-14872-g92440a24af"
data_git_msg = """\
commit 92440a24af6e09e52551aa112c85dd0b5588acef
Author: Timothy Chen <timothytim@google.com>
Date:   Thu Oct 27 12:26:23 2022 -0700

    [top/dv] Add lc_ctrl wait to wait_rom_check_done
    
    After the reset domain change, the rom_ctrl checks happen
    in parallel with life cycle control initilization.
    
    This means waiting for rom_ctrl alone to be done is insufficient
    and we need to wait for life cycle control to be done as well.
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
