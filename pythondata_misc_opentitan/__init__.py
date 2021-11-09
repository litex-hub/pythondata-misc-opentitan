import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8651"
version_tuple = (0, 0, 8651)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8651")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8539"
data_version_tuple = (0, 0, 8539)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8539")
except ImportError:
    pass
data_git_hash = "89df3eb3a3736ac08410758631ed1ca10884db1b"
data_git_describe = "v0.0-8539-g89df3eb3a"
data_git_msg = """\
commit 89df3eb3a3736ac08410758631ed1ca10884db1b
Author: Timothy Trippel <ttrippel@google.com>
Date:   Fri Nov 5 06:32:48 2021 +0000

    [dif/rom_ctrl] Add DIF header and implementation.
    
    This completes the header and implementation of all ROM Controller DIFs.
    At this time, the ROM Controller is a very simple IP, so there are only
    three DIFs.
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

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
