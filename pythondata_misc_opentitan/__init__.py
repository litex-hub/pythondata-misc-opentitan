import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12912"
version_tuple = (0, 0, 12912)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12912")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12770"
data_version_tuple = (0, 0, 12770)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12770")
except ImportError:
    pass
data_git_hash = "dbc470d2bfcb528a996db9060294207a9ffbdffd"
data_git_describe = "v0.0-12770-gdbc470d2bf"
data_git_msg = """\
commit dbc470d2bfcb528a996db9060294207a9ffbdffd
Author: Michał Mazurek <maz@semihalf.com>
Date:   Wed Jun 29 16:46:43 2022 +0200

    [opentitanlib] Fix Ti50Emulator Uart Sub-process state handling.
    
    Fix state handling due to changes introduced by PR#13277
    with function get_socket(..).
    
    Signed-off-by: Michał Mazurek <maz@semihalf.com>

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
