import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10784"
version_tuple = (0, 0, 10784)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10784")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10658"
data_version_tuple = (0, 0, 10658)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10658")
except ImportError:
    pass
data_git_hash = "76e0ccbb4cdcab0e177884c0975cc510cb26d290"
data_git_describe = "v0.0-10658-g76e0ccbb4"
data_git_msg = """\
commit 76e0ccbb4cdcab0e177884c0975cc510cb26d290
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Mon Mar 7 14:59:20 2022 -0800

    [fpv/tlul_assert] Support d_error[Part1]
    
    This PR supports common d_errors in `tlul_assert.sv`:
    1). legalAOpcodeErr
    2). sizeGTEMaskErr
    3). sizeMatchesMaskErr
    4). addrSizeAlignedErr
    The rest of errors I will cover them in generated csr assertions.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

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
