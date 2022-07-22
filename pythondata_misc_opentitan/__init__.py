import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13254"
version_tuple = (0, 0, 13254)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13254")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13112"
data_version_tuple = (0, 0, 13112)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13112")
except ImportError:
    pass
data_git_hash = "95e1d0c901b1232ae39cea663b34c59be6f2422b"
data_git_describe = "v0.0-13112-g95e1d0c901"
data_git_msg = """\
commit 95e1d0c901b1232ae39cea663b34c59be6f2422b
Author: Miguel Osorio <miguelosorio@google.com>
Date:   Fri Jul 22 13:28:15 2022 -0700

    [doc] Move style guides into a separate section
    
    Move style guides into a separate section so that they are easier to
    find from the navigation panels.
    
    Signed-off-by: Miguel Osorio <miguelosorio@google.com>

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
