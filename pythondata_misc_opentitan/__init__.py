import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10492"
version_tuple = (0, 0, 10492)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10492")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10366"
data_version_tuple = (0, 0, 10366)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10366")
except ImportError:
    pass
data_git_hash = "f5e710ca42580ab9c43c5b1e7d0a1f88fd8bd37f"
data_git_describe = "v0.0-10366-gf5e710ca4"
data_git_msg = """\
commit f5e710ca42580ab9c43c5b1e7d0a1f88fd8bd37f
Author: Kosta Kojdic <kosta.kojdic@ensilica.com>
Date:   Mon Feb 21 13:53:52 2022 +0000

    Command filtering passthrough and start of scb for it
    
    Signed-off-by: Kosta Kojdic <kosta.kojdic@ensilica.com>

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
