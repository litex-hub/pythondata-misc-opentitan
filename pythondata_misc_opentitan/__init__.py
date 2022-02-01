import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9931"
version_tuple = (0, 0, 9931)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9931")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9807"
data_version_tuple = (0, 0, 9807)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9807")
except ImportError:
    pass
data_git_hash = "9ab907b98e275f5bb86f06add43e280b4eb234c6"
data_git_describe = "v0.0-9807-g9ab907b98"
data_git_msg = """\
commit 9ab907b98e275f5bb86f06add43e280b4eb234c6
Author: Nikola Miladinovic <nikola.miladinovic@ensilica.com>
Date:   Thu Jan 13 14:30:20 2022 +0000

    [flash_ctrl] ADD TEST FOR HOST DIRECT READ DATA
    
    Add flash_ctrl_host_rd_dir_test. Add randomization
    for scramble,ecc and he. Add checking host direct read
    data transactions in scoreboard when scramble is disabled.
    
    Signed-off-by: Nikola Miladinovic <nikola.miladinovic@ensilica.com>

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
