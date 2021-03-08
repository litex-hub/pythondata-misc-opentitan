import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5280"
version_tuple = (0, 0, 5280)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5280")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5185"
data_version_tuple = (0, 0, 5185)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5185")
except ImportError:
    pass
data_git_hash = "f5fb61f2a41734365c039024a355630725a5b15c"
data_git_describe = "v0.0-5185-gf5fb61f2a"
data_git_msg = """\
commit f5fb61f2a41734365c039024a355630725a5b15c
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Wed Mar 3 12:20:55 2021 +0000

    [reggen] Add typing annotations to gen_html.py
    
    Also remove the (unused) toc and toclvl arguments. We don't have any
    typing checks in CI at the moment, but adding this sort of thing makes
    it much easier to spot if we miss something when refactoring (relevant
    for the multi-interface work that I'm doing at the moment).
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

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
