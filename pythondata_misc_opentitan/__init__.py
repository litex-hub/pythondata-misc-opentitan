import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12488"
version_tuple = (0, 0, 12488)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12488")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12346"
data_version_tuple = (0, 0, 12346)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12346")
except ImportError:
    pass
data_git_hash = "251674e04548cfac45bd3e20e45679dbf3c9f809"
data_git_describe = "v0.0-12346-g251674e04"
data_git_msg = """\
commit 251674e04548cfac45bd3e20e45679dbf3c9f809
Author: Jaedon Kim <jdonjdon@google.com>
Date:   Mon May 30 05:56:25 2022 +0000

    [dv,pwrmgr,top] update pwrmgr_deep_sleep_all_wake_ups test
    
    - Previously this test only covers wakeup source 1,2, and 3.
      and 4 and 5 are covered by other tests.
    - As we move forward to create two different sleep mode and
      randomize them, it would be beeter to have on test to cover
      all wakeup sources.
      So I added wakeup source 4 and 5 to this test
    
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
