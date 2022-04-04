import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11355"
version_tuple = (0, 0, 11355)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11355")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11229"
data_version_tuple = (0, 0, 11229)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11229")
except ImportError:
    pass
data_git_hash = "acecea1bc16ef75080003a06742082c90f7e86cd"
data_git_describe = "v0.0-11229-gacecea1bc"
data_git_msg = """\
commit acecea1bc16ef75080003a06742082c90f7e86cd
Author: Timothy Chen <timothytim@google.com>
Date:   Mon Apr 4 12:46:49 2022 -0700

    [flash_ctrl] correct cm label
    
    - there was a cross PR change in label name that was lost during
      rebase.
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

"""

# Tool version info
tool_version_str = "0.0.post126"
tool_version_tuple = (0, 0, 126)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post126")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
