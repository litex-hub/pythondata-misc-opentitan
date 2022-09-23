import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14408"
version_tuple = (0, 0, 14408)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14408")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14266"
data_version_tuple = (0, 0, 14266)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14266")
except ImportError:
    pass
data_git_hash = "548339fb986cfb705d13541cc5083db07d4450e5"
data_git_describe = "v0.0-14266-g548339fb98"
data_git_msg = """\
commit 548339fb986cfb705d13541cc5083db07d4450e5
Author: Dan McArdle <dmcardle@google.com>
Date:   Thu Sep 22 11:43:05 2022 -0400

    [bazel] Add 'build-then' command to bazelisk.sh
    
    This is just a convenience feature that makes it easier to build a
    target and then do something with the output files.
    
    I found myself frequently building disassemblies, using "./bazelisk.sh
    outquery" to find the filename, and then opening the output file in
    "less". This workflow can now be accomplished with a command like this:
    
        ./bazelisk.sh build-then "less %s" //sw/device/silicon_creator/rom:rom_fpga_cw310_dis
    
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
