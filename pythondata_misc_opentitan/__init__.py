import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14542"
version_tuple = (0, 0, 14542)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14542")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14400"
data_version_tuple = (0, 0, 14400)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14400")
except ImportError:
    pass
data_git_hash = "c9fece32a8e753c0d1975ec8034c11be0998a6c8"
data_git_describe = "v0.0-14400-gc9fece32a8"
data_git_msg = """\
commit c9fece32a8e753c0d1975ec8034c11be0998a6c8
Author: Jaedon Kim <jdonjdon@google.com>
Date:   Tue Oct 4 02:46:30 2022 +0000

    [chip,dv] add run time limit for chip_sw_pwrmgr_b2b_sleep_reset_req
    
    Signed-off-by: Jaedon Kim <jdonjdon@google.com>

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
