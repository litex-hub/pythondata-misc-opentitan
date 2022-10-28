import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15013"
version_tuple = (0, 0, 15013)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15013")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14871"
data_version_tuple = (0, 0, 14871)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14871")
except ImportError:
    pass
data_git_hash = "5c6af90a78e21fef7c9f01e4718e33fda3419260"
data_git_describe = "v0.0-14871-g5c6af90a78"
data_git_msg = """\
commit 5c6af90a78e21fef7c9f01e4718e33fda3419260
Author: Dan McArdle <dmcardle@google.com>
Date:   Wed Oct 26 17:39:02 2022 -0400

    [bazel] Set hello_world example visibility to public
    
    I was playing with 'bazel cquery //...' and was unable to run any
    queries because of this error:
    
    ERROR: $my_repo_path/release/BUILD:10:8: in pkg_tar_impl rule          \
    //release:opentitan: target '//sw/device/examples/hello_world:package' \
    is not visible from target '//release:opentitan'. Check the visibility \
    declaration of the former target if you think the dependency is        \
    legitimate
    
    Signed-off-by: Dan McArdle <dmcardle@google.com>

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
