import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10973"
version_tuple = (0, 0, 10973)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10973")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10847"
data_version_tuple = (0, 0, 10847)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10847")
except ImportError:
    pass
data_git_hash = "d3b641f28ab59516d3855af6548a8f796a2686b0"
data_git_describe = "v0.0-10847-gd3b641f28"
data_git_msg = """\
commit d3b641f28ab59516d3855af6548a8f796a2686b0
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Fri Mar 18 09:31:54 2022 +0000

    [doc] Fix rendering of special characters in testplan table
    
    The actual change here is quite small (pass 'unsafehtml' to tabulate
    when generating HTML output), but the patch is a bit bigger because it
    includes comments that nail down exactly what format the text is in at
    each stage (it took me a while to figure out!)
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

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
