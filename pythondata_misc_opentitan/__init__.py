import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8947"
version_tuple = (0, 0, 8947)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8947")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8835"
data_version_tuple = (0, 0, 8835)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8835")
except ImportError:
    pass
data_git_hash = "1d43766387b8fd976c0d6d665298b885ccb1b68c"
data_git_describe = "v0.0-8835-g1d4376638"
data_git_msg = """\
commit 1d43766387b8fd976c0d6d665298b885ccb1b68c
Author: Nikola Miladinovic <nikola.miladinovic@ensilica.com>
Date:   Wed Nov 3 12:38:35 2021 +0000

    [flash_ctrl] Modification of testplan according to comments in pull request
    
    Signed-off-by: Nikola Miladinovic <nikola.miladinovic@ensilica.com>

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
