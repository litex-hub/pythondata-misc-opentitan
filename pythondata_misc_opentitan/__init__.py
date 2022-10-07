import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14625"
version_tuple = (0, 0, 14625)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14625")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14483"
data_version_tuple = (0, 0, 14483)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14483")
except ImportError:
    pass
data_git_hash = "8b107c473157f391d25654168b62911b02f3d205"
data_git_describe = "v0.0-14483-g8b107c4731"
data_git_msg = """\
commit 8b107c473157f391d25654168b62911b02f3d205
Author: Timothy Chen <timothytim@google.com>
Date:   Wed Oct 5 14:37:36 2022 -0700

    [top/dv] Add exit_test_unlock test.
    
    The primary difference between this test and the existing unlock
    test is that this sequence tries to simulate the liklihood system
    usage.
    
    Specifically, the ROM_EXEC_EN and the advance to PROD are done in
    the same power cycle.  Upon reboot, an image is then bootstrap
    into the device to ensure the behavior is correct.
    
    The bootstrap portion for this test is still missing.
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
