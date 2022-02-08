import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10128"
version_tuple = (0, 0, 10128)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10128")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10004"
data_version_tuple = (0, 0, 10004)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10004")
except ImportError:
    pass
data_git_hash = "cc159e919757a96b2ece03b1099139978e248380"
data_git_describe = "v0.0-10004-gcc159e919"
data_git_msg = """\
commit cc159e919757a96b2ece03b1099139978e248380
Author: Miguel Osorio <miguelosorio@google.com>
Date:   Wed Feb 2 20:57:01 2022 -0800

    [sw/rom] Remove sec_mmio_write_increment function.
    
    Remove sec_mmio_write_increment function as it is only replaced by a
    macro.
    
    Signed-off-by: Miguel Osorio <miguelosorio@google.com>

"""

# Tool version info
tool_version_str = "0.0.post124"
tool_version_tuple = (0, 0, 124)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post124")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
