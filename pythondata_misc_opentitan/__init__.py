import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10423"
version_tuple = (0, 0, 10423)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10423")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10297"
data_version_tuple = (0, 0, 10297)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10297")
except ImportError:
    pass
data_git_hash = "b555ffa9b461f2e4b513e0d6d538c2f6475b9911"
data_git_describe = "v0.0-10297-gb555ffa9b"
data_git_msg = """\
commit b555ffa9b461f2e4b513e0d6d538c2f6475b9911
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Thu Feb 17 15:09:34 2022 -0800

    [conn] Update csv files
    
    1). Update rv_core_ibex path because it uses `prim_ram_1p_adv`.
    2). Update otbn ast connection to avoid width mismatch warning.
    
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
