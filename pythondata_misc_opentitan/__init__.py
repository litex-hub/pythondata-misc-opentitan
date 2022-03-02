import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10660"
version_tuple = (0, 0, 10660)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10660")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10534"
data_version_tuple = (0, 0, 10534)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10534")
except ImportError:
    pass
data_git_hash = "071283e7b1ed675807077751e689c94ed3707b87"
data_git_describe = "v0.0-10534-g071283e7b"
data_git_msg = """\
commit 071283e7b1ed675807077751e689c94ed3707b87
Author: Timothy Chen <timothytim@google.com>
Date:   Fri Feb 18 18:45:48 2022 -0800

    [pwrmgr] Address several d2s review items
    
    - convert entire rom_ctrl logic to mubi4
    - change countermeasure name
    - fix _index.md to makes sure countermeasure list is generated
    
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
