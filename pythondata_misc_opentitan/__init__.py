import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14609"
version_tuple = (0, 0, 14609)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14609")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14467"
data_version_tuple = (0, 0, 14467)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14467")
except ImportError:
    pass
data_git_hash = "cc15a925b80c71a7a503948afbda78840cca9a44"
data_git_describe = "v0.0-14467-gcc15a925b8"
data_git_msg = """\
commit cc15a925b80c71a7a503948afbda78840cca9a44
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Thu Oct 6 11:03:25 2022 -0700

    [dv/kmac] Fix KMAC errors
    
    This PR fixes two KMAC nightly issues:
    1). entropy failure: Cannot write `err_process` and `entropy_ready`
      field together after an entropy error.
      Design will clarify that in the design doc.
    2). Add a testplan entry for kmac_entropy_ready test.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post142"
tool_version_tuple = (0, 0, 142)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post142")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
