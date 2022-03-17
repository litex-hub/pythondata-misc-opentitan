import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10952"
version_tuple = (0, 0, 10952)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10952")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10826"
data_version_tuple = (0, 0, 10826)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10826")
except ImportError:
    pass
data_git_hash = "770fb8f3eeb952097e7d2d6319bc74311910c169"
data_git_describe = "v0.0-10826-g770fb8f3e"
data_git_msg = """\
commit 770fb8f3eeb952097e7d2d6319bc74311910c169
Author: Miguel Young de la Sota <mcyoung@google.com>
Date:   Wed Mar 16 15:12:42 2022 -0400

    [sw, style] Replace LLVM-style X macro guidance
    
    The new guidance is consistent with the far more common practice
    throughout the project; we also eliminate the sole LLVM-style X macro.
    
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
