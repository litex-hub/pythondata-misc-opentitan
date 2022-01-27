import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9827"
version_tuple = (0, 0, 9827)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9827")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9705"
data_version_tuple = (0, 0, 9705)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9705")
except ImportError:
    pass
data_git_hash = "a07ba27d992d79b2e77480523232e5e1eadab35f"
data_git_describe = "v0.0-9705-ga07ba27d9"
data_git_msg = """\
commit a07ba27d992d79b2e77480523232e5e1eadab35f
Author: Guillermo Maturana <maturana@google.com>
Date:   Tue Jan 25 08:15:04 2022 -0800

    [sw,tests,pwrmgr] Improve synchronization
    
    Allow each CSR updates that need to transfer to the slow domain to make
    synchronization optional.
    This enables entry into low power to use a single synchronization when
    it is done with the last update.
    Update pwrmgr unittests for this change.
    Change some tests to use pwrmgr_testutils_enable_low_power.
    
    Signed-off-by: Guillermo Maturana <maturana@google.com>

"""

# Tool version info
tool_version_str = "0.0.post122"
tool_version_tuple = (0, 0, 122)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post122")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
