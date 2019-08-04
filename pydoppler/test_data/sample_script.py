import imp
import pydoppler
imp.reload(pydoppler)

# Import sample data
#pydoppler.test_data()

# Load base object for tomography
dop = pydoppler.spruit()

# Basic data for the tomography to work
dop.object = 'U Gem'
dop.base_dir = 'ugem99' # Base directory for input spectra
dop.list = 'ugem0all.fas'		# Name of the input file
dop.lam0 = 6562.8 # Wavelength zero in units of the original spectra
dop.delta_phase = 0.003
dop.delw = 35	# size of Doppler map in wavelenght
dop.overs = 0.3 # between 0-1, Undersampling of the spectra. 1= Full resolution
dop.gama = 36.0  # km /s
dop.nbins = 28

# Read in the individual spectra and orbital phase information
dop.Foldspec()

# Normalise the spectra
dop.Dopin(continnum_band=[6500,6537,6591,6620],
        plot_median=False,poly_degree=2)