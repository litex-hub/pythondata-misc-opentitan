import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15055"
version_tuple = (0, 0, 15055)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15055")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14913"
data_version_tuple = (0, 0, 14913)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14913")
except ImportError:
    pass
data_git_hash = "ea2bc0dad0d8ccc7cac031af6483d6efc1458cef"
data_git_describe = "v0.0-14913-gea2bc0dad0"
data_git_msg = """\
commit ea2bc0dad0d8ccc7cac031af6483d6efc1458cef
Author: Weicai Yang <weicai@google.com>
Date:   Sun Oct 30 22:09:57 2022 -0700

    [spi_device/dv] Update scb as tpm_header_not_empty is a status interrupt
    
    Aligned with recent design update #15580
    Since tpm_header_not_empty is a status interrupt now, need to clear when it's read out
    
    Signed-off-by: Weicai Yang <weicai@google.com>

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
