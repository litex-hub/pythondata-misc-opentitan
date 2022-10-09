import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14631"
version_tuple = (0, 0, 14631)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14631")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14489"
data_version_tuple = (0, 0, 14489)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14489")
except ImportError:
    pass
data_git_hash = "6913573c70e0bd2916c76294bb0229f38a8f9fac"
data_git_describe = "v0.0-14489-g6913573c70"
data_git_msg = """\
commit 6913573c70e0bd2916c76294bb0229f38a8f9fac
Author: Miguel Osorio <miguelosorio@google.com>
Date:   Mon Oct 3 17:20:24 2022 -0700

    [top-test] csrng_lc_hw_debug_en_test
    
    This commits adds a default OTP image for unlocked_test0 LC state, and
    implements the csrng_lc_hw_debug_en_test as a sim_dv target.
    
    There are additional changes made to the entropy_src firmware override
    interface to enable conditioner bypass mode. An additional test case
    will be added later to cover that functionality.
    
    Signed-off-by: Miguel Osorio <miguelosorio@google.com>

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
