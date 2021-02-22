import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5102"
version_tuple = (0, 0, 5102)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5102")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5011"
data_version_tuple = (0, 0, 5011)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5011")
except ImportError:
    pass
data_git_hash = "5bc27bd66d61777a25fedc31b5233038be78f009"
data_git_describe = "v0.0-5011-g5bc27bd66"
data_git_msg = """\
commit 5bc27bd66d61777a25fedc31b5233038be78f009
Author: Udi Jonnalagadda <udij@google.com>
Date:   Fri Feb 12 10:59:47 2021 -0800

    [dv/kmac] kmac_burst_write test
    
    This PR implements the kmac_burst_wr test as described in the testplan.
    
    Signed-off-by: Udi Jonnalagadda <udij@google.com>

"""

# Tool version info
tool_version_str = "0.0.post91"
tool_version_tuple = (0, 0, 91)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post91")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
