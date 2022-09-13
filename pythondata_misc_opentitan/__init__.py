import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14175"
version_tuple = (0, 0, 14175)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14175")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14033"
data_version_tuple = (0, 0, 14033)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14033")
except ImportError:
    pass
data_git_hash = "1fb830b76ab75e1489857a67e7bf340fe493b23d"
data_git_describe = "v0.0-14033-g1fb830b76a"
data_git_msg = """\
commit 1fb830b76ab75e1489857a67e7bf340fe493b23d
Author: Sharon Topaz <sharon.topaz@nuvoton.com>
Date:   Thu Jun 3 22:22:56 2021 +0300

    SunGrid launcher support
    
    Signed-off-by: Sharon Topaz <sharon.topaz@nuvoton.com>
    
    lint fixes
    
    Signed-off-by: Sharon Topaz <sharon.topaz@nuvoton.com>
    
    fix lint issues
    
    Signed-off-by: Sharon Topaz <sharon.topaz@nuvoton.com>
    
    add open source header
    
    Signed-off-by: Sharon Topaz <sharon.topaz@nuvoton.com>
    
    update message in SGE.py and a comment in SgeLauncher.py
    
    Signed-off-by: Sharon Topaz <sharon.topaz@nuvoton.com>
    
    closing the log file
    
    Signed-off-by: Sharon Topaz <sharon.topaz@nuvoton.com>
    
    update SGE lower case and strings
    
    Signed-off-by: Sharon Topaz <sharon.topaz@nuvoton.com>
    
    update SGE PR
    
    Signed-off-by: Sharon Topaz <sharon.topaz@nuvoton.com>
    
    Resolving comments
    
    Signed-off-by: Sharon Topaz <sharon.topaz@nuvoton.com>
    
    Fix lint issues
    
    Signed-off-by: Sharon Topaz <sharon.topaz@nuvoton.com>
    
    Fix SGE lint issue
    
    Signed-off-by: Sharon Topaz <sharon.topaz@nuvoton.com>
    
    Fix SGE lint indent issue
    
    Signed-off-by: Sharon Topaz <sharon.topaz@nuvoton.com>
    
    Fix SGE lint indent issue2
    
    Signed-off-by: Sharon Topaz <sharon.topaz@nuvoton.com>
    
    Fix SGE lint indent issue3
    
    Signed-off-by: Sharon Topaz <sharon.topaz@nuvoton.com>
    
    Fix SGE comments 3-Aug
    
    Signed-off-by: Sharon Topaz <sharon.topaz@nuvoton.com>
    
    Fix SgeLauncher
    
    Signed-off-by: Sharon Topaz <sharon.topaz@nuvoton.com>
    
    Resolve SGE PR comments
    
    Signed-off-by: Sharon Topaz <sharon.topaz@nuvoton.com>
    
    Remove trailing spaces
    
    Signed-off-by: Sharon Topaz <sharon.topaz@nuvoton.com>
    
    Fix lint issues
    
    Signed-off-by: Sharon Topaz <sharon.topaz@nuvoton.com>
    
    Fix latest comments
    
    Signed-off-by: Sharon Topaz <sharon.topaz@nuvoton.com>
    
    Update exception description
    
    Signed-off-by: Sharon Topaz <sharon.topaz@nuvoton.com>

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
