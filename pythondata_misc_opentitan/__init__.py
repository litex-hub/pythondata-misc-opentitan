import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5370"
version_tuple = (0, 0, 5370)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5370")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5275"
data_version_tuple = (0, 0, 5275)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5275")
except ImportError:
    pass
data_git_hash = "534416961ec3bdb9c5ac09ebc62acfecc7165300"
data_git_describe = "v0.0-5275-g534416961"
data_git_msg = """\
commit 534416961ec3bdb9c5ac09ebc62acfecc7165300
Author: Tom Roberts <tomroberts@lowrisc.org>
Date:   Fri Mar 12 17:30:38 2021 +0000

    Update lowrisc_ibex to lowRISC/ibex@42827fc9
    
    Update code from upstream repository
    https://github.com/lowRISC/ibex.git to revision
    42827fc9cd0b2043d5d179cae46b0238a55d3652
    
    * [rtl/icache] Switch ECC granularity to 32bits (Tom Roberts)
    * Update lowrisc_ip to lowRISC/opentitan@1ae03937f (Tom Roberts)
    * [rtl] Fix lint issues (Greg Chadwick)
    * [dv/ibex] filter out tests on a per-config basis (Udi Jonnalagadda)
    
    Signed-off-by: Tom Roberts <tomroberts@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
