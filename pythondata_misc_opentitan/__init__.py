import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14535"
version_tuple = (0, 0, 14535)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14535")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14393"
data_version_tuple = (0, 0, 14393)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14393")
except ImportError:
    pass
data_git_hash = "0ea3c9ccf15917b9e61bfdef6c0637c5c2a42cf0"
data_git_describe = "v0.0-14393-g0ea3c9ccf1"
data_git_msg = """\
commit 0ea3c9ccf15917b9e61bfdef6c0637c5c2a42cf0
Author: Timothy Trippel <ttrippel@google.com>
Date:   Thu Sep 29 17:14:30 2022 -0700

    [top] compute virtual mem size from eflash size
    
    This updates the toplevel linker script template to compute the virtual
    slot region size from the eflash size, since they size of eflash is
    different between Earlgrey and English Breakfast toplevels, and cause
    the English Breakfast builds to fail now that address translation is
    added to test ROM.
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

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
