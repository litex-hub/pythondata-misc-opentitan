import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10733"
version_tuple = (0, 0, 10733)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10733")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10607"
data_version_tuple = (0, 0, 10607)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10607")
except ImportError:
    pass
data_git_hash = "a44bb9681ea186fb8ca2171fdceee86efa35d272"
data_git_describe = "v0.0-10607-ga44bb9681"
data_git_msg = """\
commit a44bb9681ea186fb8ca2171fdceee86efa35d272
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Fri Mar 4 16:45:07 2022 -0800

    [fpv/sec cm] Update the list of sec IPs
    
    This PR updates the IPs that has security countermeasures.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

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
