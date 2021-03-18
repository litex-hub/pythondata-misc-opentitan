import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5447"
version_tuple = (0, 0, 5447)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5447")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5352"
data_version_tuple = (0, 0, 5352)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5352")
except ImportError:
    pass
data_git_hash = "da03e2fce6b2683f4e0e2da82e40bc056910fa03"
data_git_describe = "v0.0-5352-gda03e2fce"
data_git_msg = """\
commit da03e2fce6b2683f4e0e2da82e40bc056910fa03
Author: Cindy Chen <chencindy@google.com>
Date:   Wed Mar 17 15:04:18 2021 -0700

    [dv/uvmdvgen] Add comment for testplan
    
    This PR adds a comment to remind user to add testplan to the
    `util/build_docs.py` to avoid doc generation error.
    
    Signed-off-by: Cindy Chen <chencindy@google.com>

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
