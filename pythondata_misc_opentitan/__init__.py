import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14872"
version_tuple = (0, 0, 14872)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14872")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14730"
data_version_tuple = (0, 0, 14730)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14730")
except ImportError:
    pass
data_git_hash = "1c6f03666f77ee3d907d6daa3e9bfb19663e6b51"
data_git_describe = "v0.0-14730-g1c6f03666f"
data_git_msg = """\
commit 1c6f03666f77ee3d907d6daa3e9bfb19663e6b51
Author: Pirmin Vogel <vogelpi@lowrisc.org>
Date:   Thu Oct 20 13:22:37 2022 +0200

    [sw, sca] Rename aes_serial_encrypt() function for disambiguation
    
    This is the underlying function called by several simple serial commands
    but it is itself not a simple serial command.
    
    Signed-off-by: Pirmin Vogel <vogelpi@lowrisc.org>

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
