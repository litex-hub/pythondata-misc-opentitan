import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10445"
version_tuple = (0, 0, 10445)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10445")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10319"
data_version_tuple = (0, 0, 10319)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10319")
except ImportError:
    pass
data_git_hash = "cf1c301d96ac9242f974972c65026c3a71cb86a7"
data_git_describe = "v0.0-10319-gcf1c301d9"
data_git_msg = """\
commit cf1c301d96ac9242f974972c65026c3a71cb86a7
Author: Nikola Miladinovic <nikola.miladinovic@ensilica.com>
Date:   Thu Feb 10 15:10:05 2022 +0000

    [flash_ctrl] ADD ERASE SUSPEND TEST
    
    Test erase suspend while random erase is in progress and also when there is
    no erase at all. Added support for backdoor reading of erased bank and page.
    
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
