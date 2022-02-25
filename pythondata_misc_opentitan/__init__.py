import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10562"
version_tuple = (0, 0, 10562)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10562")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10436"
data_version_tuple = (0, 0, 10436)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10436")
except ImportError:
    pass
data_git_hash = "8073b2262a3970fca87dfdee1e624235f618f2bd"
data_git_describe = "v0.0-10436-g8073b2262"
data_git_msg = """\
commit 8073b2262a3970fca87dfdee1e624235f618f2bd
Author: Kosta Kojdic <kosta.kojdic@ensilica.com>
Date:   Thu Feb 24 16:16:33 2022 +0000

    Address and payload passthrough swap scenarios
    
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
