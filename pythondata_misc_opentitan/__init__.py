import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15135"
version_tuple = (0, 0, 15135)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15135")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14993"
data_version_tuple = (0, 0, 14993)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14993")
except ImportError:
    pass
data_git_hash = "62844d571109f0ad2d02dc762528e6d097e7cc74"
data_git_describe = "v0.0-14993-g62844d5711"
data_git_msg = """\
commit 62844d571109f0ad2d02dc762528e6d097e7cc74
Author: Jaedon Kim <jdonjdon@google.com>
Date:   Mon Oct 31 04:00:15 2022 +0000

    [i2c,dv] initial tb refactoring
    
    Signed-off-by: Jaedon Kim <jdonjdon@google.com>
    
    [i2c,dv] refactoring host mode tb
    
    - rewrite 'host_send_trans' task to simplify randomization
    - Add place holder for device mode monitor
    - Remove unnecessary code from i2c_base_seq
    
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
