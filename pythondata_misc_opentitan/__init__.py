import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9539"
version_tuple = (0, 0, 9539)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9539")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9417"
data_version_tuple = (0, 0, 9417)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9417")
except ImportError:
    pass
data_git_hash = "ee5604553d080abc708f526bcc69f5fe886987e2"
data_git_describe = "v0.0-9417-gee5604553"
data_git_msg = """\
commit ee5604553d080abc708f526bcc69f5fe886987e2
Author: Eunchan Kim <eunchan@opentitan.org>
Date:   Tue Jan 4 22:58:13 2022 +0000

    [spi_device] Add valid check in CmdParse
    
    Add cmd_info_slot valid field to the opcode_* conditions. With the
    change, the cmdparse won't raise OnlyOneDatapath_A assertion for
    unprogrammed cmd_info slot.
    
    Signed-off-by: Eunchan Kim <eunchan@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post122"
tool_version_tuple = (0, 0, 122)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post122")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
