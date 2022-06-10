import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12625"
version_tuple = (0, 0, 12625)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12625")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12483"
data_version_tuple = (0, 0, 12483)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12483")
except ImportError:
    pass
data_git_hash = "f446683d7e76c511ff214a059141b9b6ebb64611"
data_git_describe = "v0.0-12483-gf446683d7"
data_git_msg = """\
commit f446683d7e76c511ff214a059141b9b6ebb64611
Author: Timothy Chen <timothytim@google.com>
Date:   Fri May 27 15:07:21 2022 -0700

    [clkmgr] Fix cdc issues from reg status
    
    - Addresses #12921
    - The transactional clock group currently feeds the status
      and error information into the wrong domain.  Add
      appropriate synchronizers to handle the crossing.
    
    Signed-off-by: Timothy Chen <timothytim@google.com>
    
    more fixes
    
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
