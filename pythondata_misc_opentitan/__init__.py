import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8827"
version_tuple = (0, 0, 8827)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8827")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8715"
data_version_tuple = (0, 0, 8715)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8715")
except ImportError:
    pass
data_git_hash = "9535680488dc26f85db16e033a223437af4bfac2"
data_git_describe = "v0.0-8715-g953568048"
data_git_msg = """\
commit 9535680488dc26f85db16e033a223437af4bfac2
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Tue Oct 26 13:12:31 2021 +0100

    [otbn,rtl] Narrow bus-visible DMEM to 2KiB
    
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
