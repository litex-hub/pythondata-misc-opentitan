import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14767"
version_tuple = (0, 0, 14767)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14767")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14625"
data_version_tuple = (0, 0, 14625)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14625")
except ImportError:
    pass
data_git_hash = "8c8a3a83645ee23ef762234371ce77f58dea6190"
data_git_describe = "v0.0-14625-g8c8a3a8364"
data_git_msg = """\
commit 8c8a3a83645ee23ef762234371ce77f58dea6190
Author: Jaedon Kim <jdonjdon@google.com>
Date:   Fri Oct 14 02:42:46 2022 +0000

    [flash_ctrl,dv] hw fault_status coverage
    
    - Add a few new tests to hit covergropu 'hw_error_cg'
    - Add flip_2bits function to accomodate asserting 2 bit error
    - Reactor flash_ctrl_err_base_vseq and childrun sequences to be more reusable
    
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
