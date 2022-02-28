import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10585"
version_tuple = (0, 0, 10585)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10585")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10459"
data_version_tuple = (0, 0, 10459)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10459")
except ImportError:
    pass
data_git_hash = "bd8902f33ead32f83e65715e3cda99b95b51bfd4"
data_git_describe = "v0.0-10459-gbd8902f33"
data_git_msg = """\
commit bd8902f33ead32f83e65715e3cda99b95b51bfd4
Author: Pirmin Vogel <vogelpi@lowrisc.org>
Date:   Thu Feb 24 15:22:29 2022 +0100

    [aes] Hold EDN request until acknowledgment in case of fatal alerts
    
    Previously, AES would drop a potentially asserted EDN request signal in
    case of a fatal alert which could leave the EDN interface including CDC
    in a weird state. With this commit, the request signal is always kept
    asserted until acknowledgment which is similar to what other entropy
    consumers do.
    
    This is related to lowRISC/OpenTitan#10991.
    
    Signed-off-by: Pirmin Vogel <vogelpi@lowrisc.org>

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
