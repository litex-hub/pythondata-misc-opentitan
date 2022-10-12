import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14690"
version_tuple = (0, 0, 14690)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14690")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14548"
data_version_tuple = (0, 0, 14548)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14548")
except ImportError:
    pass
data_git_hash = "dfb2e5306a82128dc6305d9f4940e44ce14129ed"
data_git_describe = "v0.0-14548-gdfb2e5306a"
data_git_msg = """\
commit dfb2e5306a82128dc6305d9f4940e44ce14129ed
Author: Michael Schaffner <msf@google.com>
Date:   Mon Oct 10 21:30:04 2022 -0700

    [test] Add test for LC access control signal going to OTP
    
    This test checks the following life cycle signals going to OTP:
    lc_creator_seed_sw_rw_en
    lc_seed_hw_rd_en
    
    Since this uses the keymgr, we also test the effects of the
    lc_keymgr_en signal (enable/disable).
    
    Fixes #15272 and #14139.
    
    Signed-off-by: Michael Schaffner <msf@google.com>

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
