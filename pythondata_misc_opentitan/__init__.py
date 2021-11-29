import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8876"
version_tuple = (0, 0, 8876)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8876")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8764"
data_version_tuple = (0, 0, 8764)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8764")
except ImportError:
    pass
data_git_hash = "cc4e9fa2b1ed3384df7152b2698ba029452b734b"
data_git_describe = "v0.0-8764-gcc4e9fa2b"
data_git_msg = """\
commit cc4e9fa2b1ed3384df7152b2698ba029452b734b
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Fri Oct 22 16:41:51 2021 +0100

    [otbn,python] Wrap code to 79 columns
    
    Our Python style guide claims that we wrap code at 79 columns but our
    flake8 configuration is set to allow 100 (presumably because it's too
    much work to squeeze existing code into shape!).
    
    I wrote the OTBN Python code intending it to stay at 79. Put in a
    local .flake8 file to set the expected width correctly and then (lots
    of lines...) re-format comments and break strings to get everything
    sorted.
    
    This stricter formatting won't be checked by CI (which runs at
    top-level, so won't see the new .flake8 config file) but it *will* be
    checked by people's text editors if they've got the usual Python
    setup.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
