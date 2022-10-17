import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14788"
version_tuple = (0, 0, 14788)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14788")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14646"
data_version_tuple = (0, 0, 14646)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14646")
except ImportError:
    pass
data_git_hash = "559bcc276afc56be90e696337f0d4f1b297e4773"
data_git_describe = "v0.0-14646-g559bcc276a"
data_git_msg = """\
commit 559bcc276afc56be90e696337f0d4f1b297e4773
Author: Eli Kim <eli@opentitan.org>
Date:   Tue Oct 11 18:25:41 2022 -0700

    fix(chip): check `logic` compare and pins connection
    
    In the prev codes there were three bugs that falsely passes the test.
    
    1. The sample_gpio() should sample `ios_if.pins` not `ios_if.pins_o`.
    2. The DV checker should use `===` rather than `==`. The PADs are
       `logic` so the checker strictly compares all four types.
    3. The SW did not clear pinmux status after waking up from the sleep.
    
    Signed-off-by: Eli Kim <eli@opentitan.org>

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
