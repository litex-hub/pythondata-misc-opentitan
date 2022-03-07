import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10748"
version_tuple = (0, 0, 10748)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10748")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10622"
data_version_tuple = (0, 0, 10622)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10622")
except ImportError:
    pass
data_git_hash = "f20ce2ae6f95448305ef88a9a43349364feb4f34"
data_git_describe = "v0.0-10622-gf20ce2ae6"
data_git_msg = """\
commit f20ce2ae6f95448305ef88a9a43349364feb4f34
Author: Martin Lueker-Boden <martin.lueker-boden@wdc.com>
Date:   Thu Mar 3 16:32:52 2022 -0800

    [Entropy_src/dv] Flesh out test plan more fully
    
    - Adds many more cover points for all registers and usage models
    - Minor updates & formatting fixes to testplan
    
    Signed-off-by: Martin Lueker-Boden <martin.lueker-boden@wdc.com>
    Co-authored-by: cindychip <cindy.chen0316@gmail.com>
    Signed-off-by: Martin Lueker-Boden <martin.lueker-boden@wdc.com>

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
