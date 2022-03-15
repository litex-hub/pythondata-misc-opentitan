import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10886"
version_tuple = (0, 0, 10886)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10886")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10760"
data_version_tuple = (0, 0, 10760)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10760")
except ImportError:
    pass
data_git_hash = "be0f83a7d7a8238a0e5a4411818b05c7379761a0"
data_git_describe = "v0.0-10760-gbe0f83a7d"
data_git_msg = """\
commit be0f83a7d7a8238a0e5a4411818b05c7379761a0
Author: Srikrishna Iyer <sriyer@google.com>
Date:   Thu Mar 10 09:22:36 2022 -0800

    chip dv] Fix AST initialization routine
    
    Use absolute address range of AST rather than reference the AST CSRs via
    RAL, because those structures do not exist in the closed source.
    
    Signed-off-by: Srikrishna Iyer <sriyer@google.com>

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
