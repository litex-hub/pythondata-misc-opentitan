import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14585"
version_tuple = (0, 0, 14585)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14585")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14443"
data_version_tuple = (0, 0, 14443)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14443")
except ImportError:
    pass
data_git_hash = "797eb3088b2103222b93c9853449cf1f584a791b"
data_git_describe = "v0.0-14443-g797eb3088b"
data_git_msg = """\
commit 797eb3088b2103222b93c9853449cf1f584a791b
Author: Alphan Ulusoy <alphan@google.com>
Date:   Wed Oct 5 17:42:00 2022 -0400

    [sw/silicon_creator] Minor changes in sec_mmio.c
    
    This commit launders i in upsert_register and caches
    sec_mmio_ctx.last_index to reduce code size.
    
    Signed-off-by: Alphan Ulusoy <alphan@google.com>

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
