# Module for platform specific stuff. Automatically generated.
# Timestamp : 2024-03-02T10:51:04.172542


DIFFERENTIAL_RETURN_MODE = 'v2'


def get_platform_specifics():
    pf_specifics = {}
    pf_specifics["os_id"] = "linux"
    pf_specifics["prefix"] = "__"
    pf_specifics["module"] = "_MOD_"
    pf_specifics["postfix"] = ""
    pf_specifics["postfix_no_module"] = "_"
    pf_specifics["dyn_lib"] = "libthermopack.so"
    pf_specifics["diff_return_mode"] = "v2"
    return pf_specifics
