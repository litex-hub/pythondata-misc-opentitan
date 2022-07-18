import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13149"
version_tuple = (0, 0, 13149)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13149")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13007"
data_version_tuple = (0, 0, 13007)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13007")
except ImportError:
    pass
data_git_hash = "13baddf15c1520df1b569acec49c540fac12d8e8"
data_git_describe = "v0.0-13007-g13baddf15c"
data_git_msg = """\
commit 13baddf15c1520df1b569acec49c540fac12d8e8
Author: Dan McArdle <dmcardle@google.com>
Date:   Fri Jul 15 16:14:18 2022 -0400

    [bazel] Refactor Bazel gen in bitstreams_workspace.py
    
    * Factor long triple-quote string literals into line lists that get
      joined by '\n'.
    
    * Add helper function to generate `filegroup` blocks.
    
    Signed-off-by: Dan McArdle <dmcardle@google.com>

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
