import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14538"
version_tuple = (0, 0, 14538)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14538")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14396"
data_version_tuple = (0, 0, 14396)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14396")
except ImportError:
    pass
data_git_hash = "c4431db093aff020f9013950b97b496ea04655f9"
data_git_describe = "v0.0-14396-gc4431db093"
data_git_msg = """\
commit c4431db093aff020f9013950b97b496ea04655f9
Author: Eli Kim <eli@opentitan.org>
Date:   Mon Oct 3 13:59:43 2022 -0700

    feat(kmac): Error Check for Entropy Ready
    
    _Related Issue: https://github.com/lowRISC/opentitan/issues/15140 _
    
    This commit adds logic inside `kmac_errchk` module. It checks if SW
    requests a KMAC op. without configuring the entropy.
    
    The error is reported as `ErrSwHashingWithoutEntropyReady (0x09)` error
    code. The internal error status is cleared by `err_process`.
    
    Signed-off-by: Eli Kim <eli@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post142"
tool_version_tuple = (0, 0, 142)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post142")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
