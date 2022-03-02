import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10641"
version_tuple = (0, 0, 10641)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10641")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10515"
data_version_tuple = (0, 0, 10515)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10515")
except ImportError:
    pass
data_git_hash = "331d4826bc18069d25fe207c088dfcd99fe3cd57"
data_git_describe = "v0.0-10515-g331d4826b"
data_git_msg = """\
commit 331d4826bc18069d25fe207c088dfcd99fe3cd57
Author: Alexander Williams <awill@google.com>
Date:   Tue Mar 1 13:18:26 2022 -0800

    [entropy_src/dif] Disable flaky smoke test
    
    entropy_src_smoketest performs an invalid check against a hard-coded
    constant. It reads the data from entropy_src, but it does not control
    the environment that generates that data. Consequently, various factors
    can cause CI to break from this test spuriously failing.
    
    Disable the test and downgrade the DIF to S0 until a replacement
    strategy is implemented.
    
    Signed-off-by: Alexander Williams <awill@google.com>

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
