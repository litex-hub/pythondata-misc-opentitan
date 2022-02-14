import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10289"
version_tuple = (0, 0, 10289)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10289")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10163"
data_version_tuple = (0, 0, 10163)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10163")
except ImportError:
    pass
data_git_hash = "82b618f23564cde97fb21271d7d3cfdcb95826d2"
data_git_describe = "v0.0-10163-g82b618f23"
data_git_msg = """\
commit 82b618f23564cde97fb21271d7d3cfdcb95826d2
Author: Weicai Yang <weicai@google.com>
Date:   Wed Feb 9 15:56:31 2022 -0800

    [dv] add mubi coverage for CSR and update reggen
    
    1. reggen is udpated to know if this reg field is mubi or not
    2. add functional coverage for mubi type CSRs
    3. disable sampling mubi covergroup in CSR tests as CSR tests won't
       really take the effect of CSRs
    Signed-off-by: Weicai Yang <weicai@google.com>

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
