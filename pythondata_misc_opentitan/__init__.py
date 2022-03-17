import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10955"
version_tuple = (0, 0, 10955)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10955")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10829"
data_version_tuple = (0, 0, 10829)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10829")
except ImportError:
    pass
data_git_hash = "cbe41e0de3047b1fec8cdaac21ac11910df1859b"
data_git_describe = "v0.0-10829-gcbe41e0de"
data_git_msg = """\
commit cbe41e0de3047b1fec8cdaac21ac11910df1859b
Author: Guillermo Maturana <maturana@google.com>
Date:   Mon Mar 14 15:43:33 2022 -0700

    [dv/clkmgr] Fix external clock handling
    
    The RTL handling of external clock was recently changed.
    Update DV to match interface changes.
    
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
