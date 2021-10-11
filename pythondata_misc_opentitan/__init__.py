import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8197"
version_tuple = (0, 0, 8197)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8197")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8085"
data_version_tuple = (0, 0, 8085)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8085")
except ImportError:
    pass
data_git_hash = "a43f4fa31ccf4805fcab307366f7a7b31da9a551"
data_git_describe = "v0.0-8085-ga43f4fa31"
data_git_msg = """\
commit a43f4fa31ccf4805fcab307366f7a7b31da9a551
Author: Miguel Osorio <miguelosorio@google.com>
Date:   Fri Oct 8 14:42:28 2021 -0700

    [sw/rom_ext] Sign ROM_EXT images with test keys
    
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
