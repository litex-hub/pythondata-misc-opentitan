import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10464"
version_tuple = (0, 0, 10464)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10464")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10338"
data_version_tuple = (0, 0, 10338)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10338")
except ImportError:
    pass
data_git_hash = "75e2a78669091adf5dcab7bb7e4e1bbfb3484886"
data_git_describe = "v0.0-10338-g75e2a7866"
data_git_msg = """\
commit 75e2a78669091adf5dcab7bb7e4e1bbfb3484886
Author: Nikola Miladinovic <nikola.miladinovic@ensilica.com>
Date:   Mon Feb 21 11:35:44 2022 +0000

    [flash_ctrl] Small fix of rd buff eviction test
    
    Due to update of flash read backdoor function, this test was failing
    in regression. Simple fix is implemented to directly modify flash operations
    
    Signed-off-by: Nikola Miladinovic <nikola.miladinovic@ensilica.com>

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
