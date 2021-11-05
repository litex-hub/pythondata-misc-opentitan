import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8604"
version_tuple = (0, 0, 8604)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8604")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8492"
data_version_tuple = (0, 0, 8492)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8492")
except ImportError:
    pass
data_git_hash = "e7615f5074daeb38a4aaf99368ec11ff2879469c"
data_git_describe = "v0.0-8492-ge7615f507"
data_git_msg = """\
commit e7615f5074daeb38a4aaf99368ec11ff2879469c
Author: Miguel Osorio <miguelosorio@google.com>
Date:   Wed Nov 3 17:51:28 2021 -0700

    [sw/rom_ext] Rename rom_ext folder.
    
    sw/device/silicon_creator/rom_exts to sw/device/silicon_creator/rom_ext
    to avoid ambiguity.
    
    Signed-off-by: Miguel Osorio <miguelosorio@google.com>

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
