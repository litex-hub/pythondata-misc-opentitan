import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12362"
version_tuple = (0, 0, 12362)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12362")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12222"
data_version_tuple = (0, 0, 12222)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12222")
except ImportError:
    pass
data_git_hash = "558942bb7869d9a5d8abd4bd0eb46dab820d3564"
data_git_describe = "v0.0-12222-g558942bb7"
data_git_msg = """\
commit 558942bb7869d9a5d8abd4bd0eb46dab820d3564
Author: Nikola Miladinovic <nikola.miladinovic@ensilica.com>
Date:   Tue May 17 17:37:43 2022 +0100

    [flash_ctrl] ADD FIRST CODE EXCLUSIONS
    
    Add code exclusions defined in issue #12325.
    
    Signed-off-by: Nikola Miladinovic <nikola.miladinovic@ensilica.com>

"""

# Tool version info
tool_version_str = "0.0.post140"
tool_version_tuple = (0, 0, 140)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post140")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
