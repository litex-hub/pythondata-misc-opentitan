import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13088"
version_tuple = (0, 0, 13088)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13088")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12946"
data_version_tuple = (0, 0, 12946)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12946")
except ImportError:
    pass
data_git_hash = "5b0733bf6688c70548a5ef9bf3bfeb16dc08aa36"
data_git_describe = "v0.0-12946-g5b0733bf66"
data_git_msg = """\
commit 5b0733bf6688c70548a5ef9bf3bfeb16dc08aa36
Author: Eunchan Kim <eunchan@opentitan.org>
Date:   Tue Jul 12 16:41:22 2022 -0700

    fix(kmac): Relax KeyLen Assertion conditions
    
    @weicaiyang reported an issue
    https://github.com/lowRISC/opentitan/issues/13594
    
    When an Application Interface using KMAC initiates the hashing
    operation, the `kmac_app` prepares the KMAC configs (strength, mode,
    keylen, keydata) for the specific App. At the same time, the App FSM
    asserts the `start` signal for KMAC core to run the SHA3 logic.
    
    This violates the KeyLengthStable_M assumption as the kmac_core already
    moved to `StKey` state when `key_len_i` is changed.
    
    This commit relaxes the condition by checking the previous value of `st`
    is `StKmacIdle`.
    
    Signed-off-by: Eunchan Kim <eunchan@opentitan.org>

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
