import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11457"
version_tuple = (0, 0, 11457)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11457")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11331"
data_version_tuple = (0, 0, 11331)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11331")
except ImportError:
    pass
data_git_hash = "ff3e01ef465b04c303331ac81f925febc44d3003"
data_git_describe = "v0.0-11331-gff3e01ef4"
data_git_msg = """\
commit ff3e01ef465b04c303331ac81f925febc44d3003
Author: Michael Schaffner <msf@google.com>
Date:   Tue Apr 5 18:30:39 2022 -0700

    [lc_ctrl] Add static pkg assertion for lc_tx_t values
    
    Signed-off-by: Michael Schaffner <msf@google.com>

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
