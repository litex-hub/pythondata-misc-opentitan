import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12344"
version_tuple = (0, 0, 12344)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12344")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12210"
data_version_tuple = (0, 0, 12210)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12210")
except ImportError:
    pass
data_git_hash = "9b014610cfc4a99a77414314a154883f6f1e24c6"
data_git_describe = "v0.0-12210-g9b014610c"
data_git_msg = """\
commit 9b014610cfc4a99a77414314a154883f6f1e24c6
Author: Nikola Miladinovic <nikola.miladinovic@ensilica.com>
Date:   Tue May 24 14:31:32 2022 +0100

    [flash_ctrl] Add flash invalid operation test
    
    Add flash invalid operation test. Check that invalid operation
    does not affect content of memory. Check all partitions.
    
    Signed-off-by: Nikola Miladinovic <nikola.miladinovic@ensilica.com>

"""

# Tool version info
tool_version_str = "0.0.post134"
tool_version_tuple = (0, 0, 134)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post134")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
