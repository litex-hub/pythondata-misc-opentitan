import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10168"
version_tuple = (0, 0, 10168)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10168")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10044"
data_version_tuple = (0, 0, 10044)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10044")
except ImportError:
    pass
data_git_hash = "6acdfbdc3349765949e83055849cbb6ac97756b4"
data_git_describe = "v0.0-10044-g6acdfbdc3"
data_git_msg = """\
commit 6acdfbdc3349765949e83055849cbb6ac97756b4
Author: Miguel Osorio <miguelosorio@google.com>
Date:   Fri Oct 8 20:22:22 2021 -0700

    [doc] Introduce Secure Hardware Design Guidelines
    
    Commits the first version of the Secure Hardware Design Guidelines
    authored by @cdgori and @tjaychen with various contributions from the
    OpenTitan community.
    
    Signed-off-by: Miguel Osorio <miguelosorio@google.com>

"""

# Tool version info
tool_version_str = "0.0.post124"
tool_version_tuple = (0, 0, 124)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post124")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
