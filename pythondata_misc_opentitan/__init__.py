import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5357"
version_tuple = (0, 0, 5357)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5357")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5262"
data_version_tuple = (0, 0, 5262)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5262")
except ImportError:
    pass
data_git_hash = "685d649abc269548124e1e16761cf69eb0fef278"
data_git_describe = "v0.0-5262-g685d649ab"
data_git_msg = """\
commit 685d649abc269548124e1e16761cf69eb0fef278
Author: Timothy Chen <timothytim@google.com>
Date:   Tue Mar 9 21:28:39 2021 -0800

    [top / ast] Continued ast integration
    
    - wire up memory configuration
    - wire up digital test inputs / outputs
    - wire up dft_en
    
    Minor updates to intermodule script required for memory configuration.
    Added prim_ram*_pkg and prim_rom*_pkg to represent configuration information.
    
    In the future, it would be ideal for ast to directly re-use these declarations.
    
    Signed-off-by: Timothy Chen <timothytim@google.com>
    
    [top] Auto generate files
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
