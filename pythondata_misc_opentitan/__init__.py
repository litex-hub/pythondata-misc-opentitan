import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9333"
version_tuple = (0, 0, 9333)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9333")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9216"
data_version_tuple = (0, 0, 9216)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9216")
except ImportError:
    pass
data_git_hash = "32517dee2de8b39438e289f85f4b4353683a9812"
data_git_describe = "v0.0-9216-g32517dee2"
data_git_msg = """\
commit 32517dee2de8b39438e289f85f4b4353683a9812
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Tue Jan 4 17:48:24 2022 +0000

    [otbn,dv] Fix loop warping for 1st iteration of single insn loop
    
    The previous code looked at current_loop_d.iterations but the problem
    is that if the loop has only one instruction then the count has
    already been decremented the first time we check.
    
    Fix things by looking at current_loop_q.iterations and then fixing
    things up appropriately for updating the "_d version" afterwards.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post117"
tool_version_tuple = (0, 0, 117)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post117")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
