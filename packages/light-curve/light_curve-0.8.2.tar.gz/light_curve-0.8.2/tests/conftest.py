import sys


def patch_astropy_for_feets():
    """Feets is incompatible with astropy v6.0 because of backward incompatible
    changes in the subpackage structure. This function monkey patches astropy
    to make it compatible with feets.
    """
    import importlib
    from importlib.metadata import version

    try:
        astropy_version = version("astropy")
    except ImportError:
        # astropy is not installed
        return
    if int(astropy_version.split(".")[0]) < 6:
        # astropy is older than v6.0
        return

    lombscargle = importlib.import_module("astropy.timeseries.periodograms.lombscargle")
    sys.modules["astropy.stats.lombscargle"] = lombscargle


# Astropy 6 is py3.9+, importlib.metadata is py3.8+
if sys.version_info >= (3, 8):
    patch_astropy_for_feets()
