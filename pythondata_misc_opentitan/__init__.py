import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5410"
version_tuple = (0, 0, 5410)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5410")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5315"
data_version_tuple = (0, 0, 5315)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5315")
except ImportError:
    pass
data_git_hash = "58f3297109e4c51b6c68386f14323ac441287082"
data_git_describe = "v0.0-5315-g58f329710"
data_git_msg = """\
commit 58f3297109e4c51b6c68386f14323ac441287082
Author: Philipp Wagner <phw@lowrisc.org>
Date:   Tue Mar 16 13:57:23 2021 +0000

    [doc] Make URLs in prj.hjson files relative to the containing file
    
    Paths to documentation content, such as the test plan, the design
    specification, etc., were given in the ipname.prj.hjson file as relative
    path, which was resolved relative to REPO_TOP. This makes IP blocks
    non-relocateable.
    
    With this PR the paths become relative to the file they are written in,
    i.e. relative to the ipname.prj.hjson file. Absolute paths are resolved
    absolute to REPO_TOP, effectively producing the previous behavior.
    
    Signed-off-by: Philipp Wagner <phw@lowrisc.org>

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
