import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10483"
version_tuple = (0, 0, 10483)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10483")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10357"
data_version_tuple = (0, 0, 10357)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10357")
except ImportError:
    pass
data_git_hash = "7232a368d292fd9df69e38f85a6222e13be2f230"
data_git_describe = "v0.0-10357-g7232a368d"
data_git_msg = """\
commit 7232a368d292fd9df69e38f85a6222e13be2f230
Author: Nikola Miladinovic <nikola.miladinovic@ensilica.com>
Date:   Wed Feb 16 15:15:27 2022 +0000

    [flash_ctrl] ADD V2S TESTS
    
    Add label V2S for tests. Add new fetch test to V2. Remove obb error test.
    
    Signed-off-by: Nikola Miladinovic <nikola.miladinovic@ensilica.com>

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
