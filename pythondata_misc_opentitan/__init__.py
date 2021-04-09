import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5813"
version_tuple = (0, 0, 5813)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5813")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5718"
data_version_tuple = (0, 0, 5718)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5718")
except ImportError:
    pass
data_git_hash = "ea71b7116ac631f3fd752bf9decf9dc4ea8545c2"
data_git_describe = "v0.0-5718-gea71b7116"
data_git_msg = """\
commit ea71b7116ac631f3fd752bf9decf9dc4ea8545c2
Author: Michael Schaffner <msf@google.com>
Date:   Thu Apr 8 17:13:44 2021 -0700

    [padring] Scan role parameters
    
    Ideally, the scan role (none, scan-in, scan-out) would be captured as
    part of the pinout Hjson description.
    However, due to the need to keep this information in the foundry
    repo, an approach with a separate SV package is taken.
    
    The open-source version is just a generic assignment of scan roles.
    The scan role parameters for the synthesized ASIC target are defined in
    the foundry repo and will be read in when the "fileset_partner" flag is
    defined in the build flow.
    
    Signed-off-by: Michael Schaffner <msf@google.com>

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
