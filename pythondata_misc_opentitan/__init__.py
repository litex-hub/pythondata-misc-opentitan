import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10811"
version_tuple = (0, 0, 10811)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10811")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10685"
data_version_tuple = (0, 0, 10685)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10685")
except ImportError:
    pass
data_git_hash = "ad92b6f0a347f967cb82e06e508ddd6d08afa936"
data_git_describe = "v0.0-10685-gad92b6f0a"
data_git_msg = """\
commit ad92b6f0a347f967cb82e06e508ddd6d08afa936
Author: Timothy Chen <timothytim@google.com>
Date:   Tue Mar 8 18:33:43 2022 -0800

    [top] auto generate
    
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
