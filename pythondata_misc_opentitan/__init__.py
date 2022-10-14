import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14745"
version_tuple = (0, 0, 14745)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14745")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14603"
data_version_tuple = (0, 0, 14603)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14603")
except ImportError:
    pass
data_git_hash = "5e4f0a35fc1013616566157d0a8a5fc164391b54"
data_git_describe = "v0.0-14603-g5e4f0a35fc"
data_git_msg = """\
commit 5e4f0a35fc1013616566157d0a8a5fc164391b54
Author: Pirmin Vogel <vogelpi@lowrisc.org>
Date:   Mon Oct 10 23:18:36 2022 +0200

    [edn, dif] Rework/enable additional data for INS, RES and GEN commands
    
    Previously, the different commands had varying and at most incomplete
    support for sending additional data/seed material to CSRNG, which didn't
    allow making use of many of the features provided by the hardware:
    - INS didn't support additional data at all.
    - RES and GEN were overloading the seed data structure for storing the
      actual application interface command header. As a result, they were
      supporting up to 11 words of additional data/seed material only where
      the hardware allows up to twelve.
    
    The main change of this commit is to add a new dif_edn_cmt_t data
    structure holding the actual application interface command header
    as well as the existing dif_edn_seed_material_t structure
    containing the seed material, and then rework the
    dif_edn_set_auto_mode() function using these structures. The underlying
    dif_edn_instantiate/reseed/generate() functions are left untouched.
    
    With this commit, three commands can take up to 12 words of additional
    data thereby making full use of the hardware.
    
    Signed-off-by: Pirmin Vogel <vogelpi@lowrisc.org>

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
