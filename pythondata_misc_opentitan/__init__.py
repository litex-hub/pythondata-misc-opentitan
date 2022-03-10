import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10831"
version_tuple = (0, 0, 10831)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10831")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10705"
data_version_tuple = (0, 0, 10705)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10705")
except ImportError:
    pass
data_git_hash = "de5926469c2d14a6427896a6e7b9040eeb4e65ce"
data_git_describe = "v0.0-10705-gde5926469"
data_git_msg = """\
commit de5926469c2d14a6427896a6e7b9040eeb4e65ce
Author: Guillermo Maturana <maturana@google.com>
Date:   Mon Mar 7 21:45:26 2022 -0800

    [sw/runtime] Add return code in CHECK_DIF_OK
    
    Signed-off-by: Guillermo Maturana <maturana@google.com>

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
