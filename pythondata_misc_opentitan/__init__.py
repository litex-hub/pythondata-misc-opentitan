import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14713"
version_tuple = (0, 0, 14713)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14713")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14571"
data_version_tuple = (0, 0, 14571)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14571")
except ImportError:
    pass
data_git_hash = "d072ac505f82152678d6e04be95c72b728a347b8"
data_git_describe = "v0.0-14571-gd072ac505f"
data_git_msg = """\
commit d072ac505f82152678d6e04be95c72b728a347b8
Author: Jes B. Klinke <jbk@chromium.org>
Date:   Fri Oct 7 14:54:34 2022 -0700

    [opentitantool] Support multi-layer alias conf
    
    We have an agreed way of connecting HyperDebug to CW310, which should be
    declared in a JSON conf file, such that opentitan tool understands a
    name such as A3 to be an alias of the HyperDebug native pin CN7_18.
    
    Separately, the ChromeOS team has a particular idea of how to use the
    OpenTitan chip pins, and wishes to use the name AP_FLASH_SEL as an alias
    for A3.  This is mostly independent of CW310 and HyperDebug, and would
    apply even to future ASIC development board.
    
    Because of the above, I foresee that we would want to simultaneously
    provide a CW310/HyperDebug configuration file, and a CromeOS/EarlGrey
    configuration file to OpenTitan tool.
    
    This PR allows the --conf option to take multiple arguments, and it
    adapts the alias resolution logic to be transitive.
    
    Change-Id: I6f8a328f269dfee246a19c4d3bae9fd60f056aec
    Signed-off-by: Jes B. Klinke <jbk@chromium.org>

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
