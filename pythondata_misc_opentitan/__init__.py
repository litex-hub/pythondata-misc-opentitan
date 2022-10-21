import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14874"
version_tuple = (0, 0, 14874)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14874")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14732"
data_version_tuple = (0, 0, 14732)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14732")
except ImportError:
    pass
data_git_hash = "7c5837b7ada5c32280c9c18b473388354766f807"
data_git_describe = "v0.0-14732-g7c5837b7ad"
data_git_msg = """\
commit 7c5837b7ada5c32280c9c18b473388354766f807
Author: Jade Philipoom <jadep@google.com>
Date:   Tue Oct 18 12:55:45 2022 +0200

    [crypto] Reorder AES driver checks to avoid race condition.
    
    The AES driver documentation specifies that the `dest` pointer should
    accept the output from the *previous* input block (if any), not the
    current one. However, the implementation actually passed the next block
    of input before reading the output, which could lead to a race condition
    where the AES block overwrites the output data before it is copied to
    `dest`. This has not been triggered by any tests but it seems better to
    be on the safe side and fix it preemptively.
    
    Signed-off-by: Jade Philipoom <jadep@google.com>

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
