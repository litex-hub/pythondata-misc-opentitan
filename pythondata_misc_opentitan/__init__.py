import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5539"
version_tuple = (0, 0, 5539)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5539")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5444"
data_version_tuple = (0, 0, 5444)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5444")
except ImportError:
    pass
data_git_hash = "02eaac710afb2080e64706e73b1b5d0f8d017e1b"
data_git_describe = "v0.0-5444-g02eaac710"
data_git_msg = """\
commit 02eaac710afb2080e64706e73b1b5d0f8d017e1b
Author: Eunchan Kim <eunchan@opentitan.org>
Date:   Tue Mar 23 10:54:25 2021 -0700

    [kmac] Moving KDF struct to KMAC IP
    
    Previously KeyMgr KDF interface was defined in KeyMgr IP. The interface
    has been used for KeyMgr to initiate KMAC operation via side channel
    interface.
    
    As rom_ctrl and otp_ctrl plan to use KMAC as signature verification
    function, KMAC needs to have more general application interface now.
    
    This commit is to move the KDF struct into KMAC and renames it to
    `app_{req/rsp}_t`.
    
    Signed-off-by: Eunchan Kim <eunchan@opentitan.org>

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
