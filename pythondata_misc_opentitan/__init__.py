import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8701"
version_tuple = (0, 0, 8701)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8701")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8589"
data_version_tuple = (0, 0, 8589)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8589")
except ImportError:
    pass
data_git_hash = "f7562c70e677380b1970c4d92627963b0fcf9c77"
data_git_describe = "v0.0-8589-gf7562c70e"
data_git_msg = """\
commit f7562c70e677380b1970c4d92627963b0fcf9c77
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Fri Nov 12 09:57:24 2021 +0000

    [ipgen] Plumb TemplateParams through correctly
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

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
