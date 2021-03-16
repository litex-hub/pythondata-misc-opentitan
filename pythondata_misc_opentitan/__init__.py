import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5406"
version_tuple = (0, 0, 5406)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5406")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5311"
data_version_tuple = (0, 0, 5311)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5311")
except ImportError:
    pass
data_git_hash = "e520362accc1c10b37d6b1c65c29de70dab266b8"
data_git_describe = "v0.0-5311-ge520362ac"
data_git_msg = """\
commit e520362accc1c10b37d6b1c65c29de70dab266b8
Author: Philipp Wagner <phw@lowrisc.org>
Date:   Mon Mar 15 19:59:09 2021 +0000

    [doc] Use relative links in Hjson-related shortcodes
    
    The testplan, hwcfg, and registers shortcodes currently take a single
    argument referring to the IP description file in Hjson format.
    
    Before this commit, the Hjson file path was relative to $REPO_TOP.
    After this commit, the path is relative to the file using the
    shortcode. The previous behavior can be achieved by using absolute
    paths, which are rooted in $REPO_TOP.
    
    With this change users of the short codes do not need knowledge
    about the overall file structure, making the IP directory "relocatable."
    
    To avoid doing the same change three times in the testplan, hwcfg, and
    registers shortcodes, this commit unifies them into a single shortcode.
    (Unfortunately "inheritance"/"nesting" isn't really easy with Hugo
    shortcodes.)
    
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
