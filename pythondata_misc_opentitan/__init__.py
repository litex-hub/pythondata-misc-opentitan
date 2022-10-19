import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14814"
version_tuple = (0, 0, 14814)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14814")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14672"
data_version_tuple = (0, 0, 14672)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14672")
except ImportError:
    pass
data_git_hash = "059aa08d33a8e01bd033b0c81d0c0ecee5e1800e"
data_git_describe = "v0.0-14672-g059aa08d33"
data_git_msg = """\
commit 059aa08d33a8e01bd033b0c81d0c0ecee5e1800e
Author: Jaedon Kim <jdonjdon@google.com>
Date:   Tue Oct 18 22:16:14 2022 +0000

    [flash_ctrl,dv] update coverage collection
    
    - Add coverage collection to wr_intg test
    - Remove reg_intg cover point because it is covered by autogen
      covergroup
    
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
