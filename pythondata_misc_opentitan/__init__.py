import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10898"
version_tuple = (0, 0, 10898)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10898")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10772"
data_version_tuple = (0, 0, 10772)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10772")
except ImportError:
    pass
data_git_hash = "e3a148bc38ccf5e555d3644682b714e21d185042"
data_git_describe = "v0.0-10772-ge3a148bc3"
data_git_msg = """\
commit e3a148bc38ccf5e555d3644682b714e21d185042
Author: Nikola Miladinovic <nikola.miladinovic@ensilica.com>
Date:   Tue Mar 15 14:21:02 2022 +0000

    [flash_ctrl] Small fix for flash_ctrl_phy_arb test
    
    Enabling creator and owner pages for sw rw access.
    
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
