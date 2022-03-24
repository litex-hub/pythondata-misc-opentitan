import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11065"
version_tuple = (0, 0, 11065)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11065")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10939"
data_version_tuple = (0, 0, 10939)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10939")
except ImportError:
    pass
data_git_hash = "236a8d2c59c4b4eef903ca83abaa1a84fe52c162"
data_git_describe = "v0.0-10939-g236a8d2c5"
data_git_msg = """\
commit 236a8d2c59c4b4eef903ca83abaa1a84fe52c162
Author: Timothy Trippel <ttrippel@google.com>
Date:   Wed Mar 23 14:57:57 2022 -0700

    [dif/spi_host] update checklist and milestone
    
    This updates the DIF checklist and milestone to bring the DIF to S2.
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

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
