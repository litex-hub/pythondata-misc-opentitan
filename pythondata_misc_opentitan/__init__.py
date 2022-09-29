import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14497"
version_tuple = (0, 0, 14497)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14497")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14355"
data_version_tuple = (0, 0, 14355)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14355")
except ImportError:
    pass
data_git_hash = "a79dd98548cf1c6940d133516221769508316b8e"
data_git_describe = "v0.0-14355-ga79dd98548"
data_git_msg = """\
commit a79dd98548cf1c6940d133516221769508316b8e
Author: Drew Macrae <drewmacrae@google.com>
Date:   Wed Sep 28 10:15:00 2022 -0400

    [CODEOWNERS] Stop reviewing Bazel BUILD files directly
    
    * added @drewmacrae to CI to help monitor flows related to
      azure-pipelines.yml and CI scripting
    
    Signed-off-by: Drew Macrae <drewmacrae@google.com>

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
