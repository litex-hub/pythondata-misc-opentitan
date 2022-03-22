import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11016"
version_tuple = (0, 0, 11016)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11016")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10890"
data_version_tuple = (0, 0, 10890)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10890")
except ImportError:
    pass
data_git_hash = "af9be146c5bb650176b4b23972d37fea9f07149f"
data_git_describe = "v0.0-10890-gaf9be146c"
data_git_msg = """\
commit af9be146c5bb650176b4b23972d37fea9f07149f
Author: Drew Macrae <drewmacrae@google.com>
Date:   Mon Mar 21 21:24:40 2022 -0400

    [bazel] fixup CI for batched testing of merge
    
    I mispelled newresult.txt so the cat command is failing as seen here
    https://dev.azure.com/lowrisc/opentitan/_build/results?buildId=73045
    the switch afterwards is a nop and not worth the risk.
    
    Signed-off-by: Drew Macrae <drewmacrae@google.com>

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
