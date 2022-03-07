import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10734"
version_tuple = (0, 0, 10734)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10734")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10608"
data_version_tuple = (0, 0, 10608)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10608")
except ImportError:
    pass
data_git_hash = "caac850c7a837ecbfcc1027197d856d696f902ae"
data_git_describe = "v0.0-10608-gcaac850c7"
data_git_msg = """\
commit caac850c7a837ecbfcc1027197d856d696f902ae
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Fri Mar 4 15:33:34 2022 -0800

    [prim/security] Improve the code for prim_sparse_fsm security check
    
    According to the discussion in PR #11129, we update the enum checks from
    generate block to a function.
    JasperGold does support simple function syntax.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

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
