import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9399"
version_tuple = (0, 0, 9399)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9399")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9281"
data_version_tuple = (0, 0, 9281)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9281")
except ImportError:
    pass
data_git_hash = "405e3219f6b4081a18255dca7a67678b9051c4f7"
data_git_describe = "v0.0-9281-g405e3219f"
data_git_msg = """\
commit 405e3219f6b4081a18255dca7a67678b9051c4f7
Author: Jade Philipoom <jadep@google.com>
Date:   Fri Jan 7 18:07:21 2022 +0000

    [sw,crypto] Adjust parameters for R^2 algorithm on Ibex.
    
    Because the operands in this computation are always powers of 2, it is
    equivalent to square the operand or to perform a certain number of
    (modular) doublings. For small numbers the doublings are faster and for
    larger ones the squaring is faster; the cutoff where this happens for
    our implementation is at 2^96 (empirically determined).
    
    Signed-off-by: Jade Philipoom <jadep@google.com>

"""

# Tool version info
tool_version_str = "0.0.post118"
tool_version_tuple = (0, 0, 118)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post118")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
