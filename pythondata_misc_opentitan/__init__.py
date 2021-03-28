import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5609"
version_tuple = (0, 0, 5609)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5609")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5514"
data_version_tuple = (0, 0, 5514)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5514")
except ImportError:
    pass
data_git_hash = "0c49992bc0b713f91bb7ba01cd78eaf89f49d04a"
data_git_describe = "v0.0-5514-g0c49992bc"
data_git_msg = """\
commit 0c49992bc0b713f91bb7ba01cd78eaf89f49d04a
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Fri Mar 26 11:05:20 2021 +0000

    [kmac] Fix app_config_t to work with Verilator
    
    Verilator doesn't have proper support for unpacked structs. Since we
    don't need one here, we can just declare app_config_t to be packed.
    
    Also, it seems to have rather strange behaviour with int enums when
    used as fields in a struct. I've reported this on the Verilator bug
    tracker as issue #2855 but there's an easy workaround here, which is
    probably what we'd want for synthesizable code anyway.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
