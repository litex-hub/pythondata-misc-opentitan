import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11097"
version_tuple = (0, 0, 11097)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11097")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10971"
data_version_tuple = (0, 0, 10971)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10971")
except ImportError:
    pass
data_git_hash = "640f3f3ebd92a4310b60f0884d403f90c36eb01f"
data_git_describe = "v0.0-10971-g640f3f3eb"
data_git_msg = """\
commit 640f3f3ebd92a4310b60f0884d403f90c36eb01f
Author: Douglas Reis <doreis@lowrisc.org>
Date:   Thu Feb 24 16:30:42 2022 +0000

    [test, otbn] Add the otbn_mem_scramble chip level test
    
    Signed-off-by: Douglas Reis <doreis@lowrisc.org>

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
