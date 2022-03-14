import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10865"
version_tuple = (0, 0, 10865)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10865")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10739"
data_version_tuple = (0, 0, 10739)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10739")
except ImportError:
    pass
data_git_hash = "2f33ce93cade409b32739570882199cc1d850e16"
data_git_describe = "v0.0-10739-g2f33ce93c"
data_git_msg = """\
commit 2f33ce93cade409b32739570882199cc1d850e16
Author: Miguel Young de la Sota <mcyoung@google.com>
Date:   Thu Mar 3 10:20:38 2022 -0500

    [sw, base] Add a macro for creating addressable code labels
    
    This macro is intended for writing chip-level tests that want to check
    that some kind of exception-ey thing happened in a range of program
    counters. It is a maximally compiler-portable implementation that won't
    be optimization-hostile like GCC's label references (&&label), whose
    support in LLVM is... not something we should rely on.
    
    This macro is mostly made of caveats, but it has a narrow use
    regardless.
    
    Signed-off-by: Miguel Young de la Sota <mcyoung@google.com>

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
