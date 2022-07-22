import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13243"
version_tuple = (0, 0, 13243)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13243")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13101"
data_version_tuple = (0, 0, 13101)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13101")
except ImportError:
    pass
data_git_hash = "995302c267e0ec18729e9e35b2607d6075ea470f"
data_git_describe = "v0.0-13101-g995302c267"
data_git_msg = """\
commit 995302c267e0ec18729e9e35b2607d6075ea470f
Author: Miguel Osorio <miguelosorio@google.com>
Date:   Thu Jul 21 20:16:36 2022 -0700

    [doc] Unlist dangling pages from menus.
    
    This commit introduces an 'unlist' parameter which can be used to remove
    dangling pages from menus to make the navigation experience more
    intuitive.
    
    Dangling pages make menus harder to follow as there is no intuitive
    ordering. For example, the hardware section had the following menu:
    
    hw
     - Design Verification
     - OpenTitan Assertions
     - IP Cores
     - Linting
     - Top Earlgrey
    
     After this change the menu is as follows:
    
     hw
      - Design Verification
      - IP Cores
      - Top Earlgrey
    
    This change does not affect the siteContent fragment, so it can still be
    used to get a full list of pages.
    
    Signed-off-by: Miguel Osorio <miguelosorio@google.com>

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
