import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9999"
version_tuple = (0, 0, 9999)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9999")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9875"
data_version_tuple = (0, 0, 9875)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9875")
except ImportError:
    pass
data_git_hash = "9efd6445d44f27bc3e2f39598d4b15148188bee4"
data_git_describe = "v0.0-9875-g9efd6445d"
data_git_msg = """\
commit 9efd6445d44f27bc3e2f39598d4b15148188bee4
Author: Alphan Ulusoy <alphan@google.com>
Date:   Mon Jan 31 14:28:08 2022 -0500

    [sw/silicon_creator] Additional rollback protection in mask_rom_verify()
    
    This change adds an additional rollback protection in mask_rom_verify()
    that invalidates the digest computed for signature verification if the
    security version of the manifest is smaller than the minimum required
    security version.
    
    Signed-off-by: Alphan Ulusoy <alphan@google.com>

"""

# Tool version info
tool_version_str = "0.0.post124"
tool_version_tuple = (0, 0, 124)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post124")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
