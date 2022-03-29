import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11170"
version_tuple = (0, 0, 11170)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11170")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11044"
data_version_tuple = (0, 0, 11044)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11044")
except ImportError:
    pass
data_git_hash = "d492aee8887afdf87c7125e7cef3f743f116e894"
data_git_describe = "v0.0-11044-gd492aee88"
data_git_msg = """\
commit d492aee8887afdf87c7125e7cef3f743f116e894
Author: Michael Munday <mike.munday@lowrisc.org>
Date:   Thu Mar 24 17:23:04 2022 +0000

    [sw/silicon_creator] Move exception handler into .shutdown section
    
    Move the assembly exception handler into the `.shutdown` section. The
    `.shutdown` section is the last section in the executable part of the
    ROM and is where the `shutdown_finalize` function is (which serves a
    similar function).
    
    Signed-off-by: Michael Munday <mike.munday@lowrisc.org>

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
