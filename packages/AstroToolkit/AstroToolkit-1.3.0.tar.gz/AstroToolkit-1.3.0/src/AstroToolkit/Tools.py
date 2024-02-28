'''
Changelog:
- optimizations and bug fixes
- plotting functions now catch a None input (i.e. if no data was found), and return None rather than failing.
- fixed an error with flux calculations overflowing for bad mag values.
- increased sdss request timeout.
- added a simple 'getdistance' tool to convert parallax into pc.
- added eROSITA integration
- added conversion tools for converting deg -> hms/dms and vice versa.
- added a tool to export any plot to a PNG.
- added ATLAS forced photometry integration.
- running most tools now prints to the terminal to notify that it is running, and gives its basic input information (can be enabled/disabled using the new configuration functionality).
- added new configuration functionality through a config.ini file (with its own tool to edit the contained configuration parameters - see README).
- added a function to return the reddening of a given Gaia source.
- added a function to save plots through bokeh (just uses bokeh's functionality, but allows you to import it from ATK rather than bokeh).
- added J... identifier to savedata file names, and made savedata return the file name to making reading these files easier.
- added Gaia lightcurve integration.
- added ASAS-SN lightcurve integration.
- improved lightcurve plotting, allowing for any number of lightcurves from different bands to be placed on same axis, with each band being hideable using legend.
  Different bands retain accurate observation date.
- added hydrogen and helium spectral line identifiers with labels and toggles.
- improved grid functionality for easier datapage creation
	- Made 'None' (i.e. missing/filler) plots in grid functions invisible
- added a default plot_size argument to config which scales all plots automatically
- changed erosita detections to differentiate between corrected/uncorrected
- added gaia time photometry as an imaging overlay
- split asassn data by camera into separate v/g bands
- added asassn lightcurves as an imaging overlay
- added survey to ATK filenames where appropriate
- updated sed error bars to multi_line format, now hides with data when toggled via the legend
- added a sigma clipping argument for lightcurvequery, performs sigma clipping on retrieved data.
- added an additional filter to limit huge errors in ATLAS/ASAS-SN lightcurves
- Upper limits are now denoted by a different marker in SED plots
- rewrote README
'''

'''
To-Do:
HIGH PRIORITY
- Comment new code
- add selenium as a dependency, with install instructions in README (ALSO ADD NOTE ABOUT ATLAS TRACERS ONLY WORKING FOR CENTRAL OBJECT OF IMAGE (I.E. SOURCE GIVEN WHEN MAKING IMAGE), as would take far too long otherwise (would have to run atlas query for each object))

MEDIUM PRIORITY
- improve fits reading functionality for getting source/pos list
- 'plot has no renderer' bokeh warning
- sort out lightcurve times, i.e. could in theory combine mjd/hjd lightcurves currently (not properly) --> starts to get into combining lightcurves across time domain (Boris spoke about this)
- improve datapage grid functionality > plot.min_border_top/bottom/left/right, add a min_border setting in config for this, and apply to all plots (as can't use this on layouts)
- comment code + clean up / optimize anything that needs it to make development easier

LOW PRIORITY
- could maybe try to draw lines between consecutive points for true tracers to show path of object through time? (?)
- make some sort of error log that notes any errors encountered during runtime - similar to metadata table, a datapage element that stores these, maybe via a log file of some sort (?)
- convert all lists to np arrays so that reading them is easier (?)
- update ASASA-SN SkyPatrol to v2 (not a fan of having to github clone it to install, still in beta)
- add setting to config to change default hierarchy in 'any' survey searches (currently images/lightcurves)
'''

# Imports -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

from bokeh.plotting import output_file
import re

from .Misc.file_naming import name_file
from .Misc.input_validation import validateinput

from importlib_resources import files
import configparser
import os

newline='\n'

# Configuration -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

config_file=files('AstroToolkit.Settings').joinpath('config.ini')	

# Create default config file if the file doesn't already exist (i.e. when the package is first installed)
# This handles all default parameters unless they are passed to a tool by the user, in which case these are overwritten
if not os.path.isfile(config_file):
	config=configparser.ConfigParser()

	config.add_section('settings')
	config.set('settings','enable_notifications','True')
	config.set('settings','dataquery_radius','3')
	config.set('settings','photquery_radius','3')
	config.set('settings','bulkphotquery_radius','3')
	config.set('settings','imagequery_size','30')
	config.set('settings','imagequery_overlays','gaia')
	config.set('settings','lightcurvequery_radius','3')
	config.set('settings','atlas_username','None')
	config.set('settings','atlas_password','None')
	config.set('settings','sed_radius','3')
	config.set('settings','spectrum_radius','3')
	config.set('settings','grid_size','250')
	config.set('settings','button_simbad_radius','3')
	config.set('settings','button_vizier_radius','3')
	config.set('settings','plot_size','400')

	with open(config_file,'w') as configfile:
		config.write(configfile)

# allows user to edit the config file
def editconfig(options):
	edit=configparser.ConfigParser()
	edit.read(config_file)
	settings=edit['settings']		

	accepted_keys=list(settings.keys())

	for key in options:
		if key not in accepted_keys:
			raise Exception(f'Invalid configuration parameter. Accepted parameters are {accepted_keys}.')
	
		settings[key]=str(options[key])
		
	with open(config_file,'w') as configfile:
		edit.write(configfile)
	
# Read config file
def readconfig():
	Config=configparser.ConfigParser()
	Config.read(config_file)

	settings=Config['settings']
	for key in settings:
		if settings[key]=='True':
			settings[key]='1'
		elif settings[key]=='False':
			settings[key]='0'

	config={}		

	config['ENABLE_NOTIFICATIONS']=int(settings['enable_notifications'])
	config['DATAQUERY_RADIUS']=float(settings['dataquery_radius'])
	config['PHOTQUERY_RADIUS']=float(settings['photquery_radius'])
	config['BULKPHOTQUERY_RADIUS']=float(settings['bulkphotquery_radius'])
	config['IMAGEQUERY_SIZE']=float(settings['imagequery_size'])
	config['IMAGEQUERY_OVERLAYS']=str(settings['imagequery_overlays'])
	config['LIGHTCURVEQUERY_RADIUS']=float(settings['lightcurvequery_radius'])
	config['ATLAS_USERNAME']=str(settings['atlas_username'])
	config['ATLAS_PASSWORD']=str(settings['atlas_password'])
	config['SED_RADIUS']=float(settings['sed_radius'])
	config['SPECTRUM_RADIUS']=float(settings['spectrum_radius'])
	config['GRID_SIZE']=int(settings['grid_size'])
	config['SIMBAD_RADIUS']=int(settings['button_simbad_radius'])
	config['VIZIER_RADIUS']=int(settings['button_vizier_radius'])
	config['PLOT_SIZE']=int(settings['plot_size'])
	
	return config

# Data Query --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def dataquery(survey,pos=None,source=None,radius=None):
	config=readconfig()
	
	if radius==None:
		radius=config['DATAQUERY_RADIUS']

	if config['ENABLE_NOTIFICATIONS']==1:
		print(f'Running {survey} dataquery...{newline}source = {source}{newline}pos = {pos}{newline}radius = {radius}{newline}')

	from .Data.data import survey_map

	validateinput({'survey':survey,'pos':pos,'source':source,'radius':radius},'dataquery')

	if source!=None and pos!=None:
		raise Exception('Simultaneous pos and source input detected in dataquery.')
	elif source==None and pos==None:
		raise Exception('pos or source input required in dataquery.')

	data=survey_map(survey=survey,pos=pos,source=source,radius=radius)

	return data

# Phot Queries ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def photquery(survey,pos=None,source=None,radius=None):
	config=readconfig()
	
	if radius==None:
		radius=config['PHOTQUERY_RADIUS']

	if config['ENABLE_NOTIFICATIONS']==1:
		print(f'Running {survey} photquery...{newline}source = {source}{newline}pos = {pos}{newline}radius = {radius}{newline}')

	from .Data.photometry import phot_query
	
	validateinput({'survey':survey,'pos':pos,'source':source,'radius':radius},'photquery')
	
	if source!=None and pos!=None:
		raise Exception('Simultaneous pos and source input detected in photquery.')
	elif source==None and pos==None:
		raise Exception('pos or source input required in photquery.')

	photometry=phot_query(survey=survey,pos=pos,source=source,radius=radius)

	return photometry

def bulkphotquery(pos=None,source=None,radius=None):
	config=readconfig()
	
	if radius==None:
		radius=config['BULKPHOTQUERY_RADIUS']

	if config['ENABLE_NOTIFICATIONS']==1:
		print(f'Running bulkphotquery...{newline}source = {source}{newline}pos = {pos}{newline}radius = {radius}{newline}')

	from .Data.photometry import bulk_query
	
	validateinput({'pos':pos,'source':source,'radius':radius},'bulkphot')

	if source!=None and pos!=None:
		raise Exception('Simultaneous pos and source input detected in bulkphotquery.')
	elif source==None and pos==None:
		raise Exception('pos or source input required in bulkphotquery.')

	data=bulk_query(pos=pos,source=source,radius=radius)
	
	return data

# Imaging -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def imagequery(survey,pos=None,source=None,size=None,overlays='default',band='g'):
	config=readconfig()

	if size==None:
		size=config['IMAGEQUERY_SIZE']
	if overlays=='default':
		overlays=config['IMAGEQUERY_OVERLAYS']
	
	if not isinstance(size,int):
		try:
			size=int(size)
		except:
			size_type=type(size)
			print(f'Invalid size data type. Expected int, got {size_type}.')

	if config['ENABLE_NOTIFICATIONS']==1:
		print(f'Running {survey} imagequery...{newline}source = {source}{newline}pos = {pos}{newline}size = {size}{newline}overlays = {overlays}{newline}')

	from .Data.imaging import image_correction

	f_return=None
		
	validateinput({'survey':survey,'pos':pos,'source':source},'imagequery')

	if source!=None and pos!=None:
		raise Exception('Simultaneous pos and source input detected in imagequery.')
	elif source==None and pos==None:
		raise Exception('pos or source input required in imagequery.')

	if overlays=='all':
		overlays='gaia,galex_nuv,galex_fuv,rosat,sdss,twomass,wise,ztf,erosita,atlas,gaia_lc,asassn'

	if overlays!=None:
		overlay_list=overlays.split(',')

		for i in range(0,len(overlay_list)):
			overlay_list[i]=overlay_list[i].lower()
		for i in range(0,len(overlay_list)):
			if overlay_list[i] not in ['gaia','galex_nuv','galex_fuv','rosat','ztf','wise','twomass','sdss','erosita','atlas','gaia_lc','asassn']:
				raise Exception('invalid overlay')
	else:
		overlay_list=[]
		
	if survey=='panstarrs':
		if size>1500:
			raise Exception(f'Maximum supported size in {survey} is 1500 arcsec.')
		if not re.match('^[grizy]+$', band):
			raise Exception(f'Invalid {survey} bands. Supported bands are [g,r,i,z,y].')
	
	elif survey=='skymapper':
		if size>600:
			raise Exception(f'Maximum supported size in {survey} is 600 arcsec.')
		if re.match('^[grizuv]+$', band):
			pass
		else:
			raise Exception(f'Invalid {survey} bands. Supported bands are [g,r,i,z,u,v].')
	
		band=list(band)
		temp_string=''
		for i in range(0,len(band)):
			temp_string+=(band[i]+',')
		band=temp_string[:-1]
		
	elif survey=='dss':
		if band!='g':
			print('Note: DSS only supports g band imaging, input band has been ignored.')
		if size>7200:
			print(f'Maximum supported size in {survey} is 7200 arcsec.')

	
	if survey=='any':
		image=image_correction(survey='panstarrs',pos=pos,source=source,size=size,band=band,overlay=overlay_list)
		if image==None:
			image=image_correction(survey='skymapper',pos=pos,source=source,size=size,band=band,overlay=overlay_list)
			if image==None:
				image=image_correction(survey='dss',pos=pos,source=source,size=size,band=band,overlay=overlay_list)
				if image==None:
					print('Note: No image found in any supported imaging survey.')
					return f_return
	else:
		image=image_correction(survey=survey,pos=pos,source=source,size=size,band=band,overlay=overlay_list)
	
	return image

def plotimage(data):
	config=readconfig()
	if config['ENABLE_NOTIFICATIONS']==1:
		print(f'Plotting image...{newline}')	

	from .Plotting.imaging import plot_image
	
	plot=plot_image(image_dict=data)

	if plot==None:
		return None

	filename=name_file(data=data,data_type='ATKimage')
	output_file(filename)

	plot.width,plot.height=config['PLOT_SIZE'],config['PLOT_SIZE']

	return plot

# HRD Plotting ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def plothrd(source=None,sources=None):
	config=readconfig()
	if config['ENABLE_NOTIFICATIONS']==1:
		print(f'Plotting HRD...{newline}source = {source}{newline}sources = {sources}{newline}')

	from bokeh.plotting import output_file

	from .Plotting.HRD import get_plot
	
	validateinput({'source':source},'plothrd')

	if source!=None and sources!=None:
		raise Exception('Simultaneous source and sources input detected in plothrd.')

	if source!=None:
		plot=get_plot(source=source)
	elif sources!=None:
		for element in sources:
			if not isinstance(element,int):
				data_type=type(element)
				raise Exception(f'Incorrect source data type in sources. Expected int, got {data_type}.')
		plot=get_plot(sources=sources)
	else:
		raise Exception('source or sources input required in plothrd.')

	if plot==None:
		return None

	filename=name_file(data={'source':source,'sources':sources},data_type='ATKhrd')
	output_file(filename)

	plot.width,plot.height=config['PLOT_SIZE'],config['PLOT_SIZE']

	return plot

# Light Curves ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def lightcurvequery(survey,pos=None,source=None,radius=None,username=None,password=None,sigmaclip=None):
	from .Data.lightcurve_sigma_clip import sigma_clip

	config=readconfig()

	if radius==None:
		radius=config['LIGHTCURVEQUERY_RADIUS']
	if username==None:
		username=config['ATLAS_USERNAME']
	if password==None:
		password=config['ATLAS_PASSWORD']

	if config['ENABLE_NOTIFICATIONS']==1:
		print(f'Running {survey} lightcurvequery...{newline}source = {source}{newline}pos = {pos}{newline}radius = {radius}{newline}')

	from .Data.lightcurves import lightcurve_handling
	
	validateinput({'survey':survey,'pos':pos,'source':source,'radius':radius},'lightcurvequery')

	if source!=None and pos!=None:
		raise Exception('Simultaneous pos and source input detected in lightcurvequery')
	elif source==None and pos==None:
		raise Exception('pos or source input required in lightcurvequery.')

	def check_exists(data):
		data_exists=False
		for element in data:
			if element!=None:
				data_exists=True
		
		return data_exists

	if survey=='any':
		data=lightcurvequery(survey='ztf',pos=pos,source=source,radius=radius)
		if check_exists(data)==False:
			data=lightcurvequery(survey='atlas',pos=pos,source=source,radius=radius,username=username,password=password)
			if check_exists(data)==False:
				data=lightcurvequery(survey='asassn',pos=pos,source=source,radius=radius)
				if check_exists(data)==False:
					data=lightcurvequery(survey='gaia',pos=pos,source=source,radius=radius)
		
	else:
		data=lightcurve_handling(survey=survey,pos=pos,source=source,radius=radius,username=username,password=password)
	
	if sigmaclip!=None:
		clipped_data=[]
		for element in data:
			if element!=None:
				clipped=sigma_clip(data=element,sigma=sigmaclip)
				clipped_data.append(clipped)
			else:
				clipped_data.append(None)

	return data

def plotlightcurve(data,colour='black',colours=None):
	config=readconfig()
	if config['ENABLE_NOTIFICATIONS']==1:
		print(f'Plotting lightcurve...{newline}')	

	from .Plotting.lightcurves import plot_lightcurve
	
	if colour not in ['green','red','blue','purple','orange','black']:
		raise Exception('Unsupported colour in plotlightcurve.')

	plot=plot_lightcurve(data=data,colour=colour,colours=colours)
		
	if plot==None:
		return None

	filename=name_file(data=data,data_type='ATKlightcurve')
	output_file(filename)
	
	plot.width,plot.height=config['PLOT_SIZE']*2,config['PLOT_SIZE']

	return plot

# SEDs --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def sedquery(pos=None,source=None,radius=None):
	config=readconfig()

	if radius==None:
		radius=config['SED_RADIUS']	

	if config['ENABLE_NOTIFICATIONS']==1:
		print(f'Running sedquery...{newline}source = {source}{newline}pos = {pos}{newline}radius = {radius}{newline}')	

	from .Data.sed import get_data
	
	data=get_data(pos=pos,source=source,radius=radius)
	
	validateinput({'source':source,'pos':pos},'sedquery')

	if source!=None and pos!=None:
		raise Exception('Simultaneous pos and source input detected in dataquery.')
	elif source==None and pos==None:
		raise Exception('pos or source input required in dataquery.')

	return data

def plotsed(data):
	config=readconfig()
	if config['ENABLE_NOTIFICATIONS']==1:
		print(f'Plotting SED...{newline}')	

	from .Plotting.sed import plot_sed
	
	plot=plot_sed(sed_data=data)
	
	if plot==None:
		return None

	filename=name_file(data=data,data_type='ATKsed')
	output_file(filename)
	
	plot.width,plot.height=config['PLOT_SIZE']*2,config['PLOT_SIZE']

	return plot

# Spectra -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def spectrumquery(survey=None,pos=None,source=None,radius=None):
	config=readconfig()

	if radius==None:
		radius=config['SPECTRUM_RADIUS']	

	if config['ENABLE_NOTIFICATIONS']==1:
		print(f'Running {survey} spectrumquery...{newline}source = {source}{newline}pos = {pos}{newline}radius = {radius}{newline}')	

	from .Data.spectra import survey_map
	
	validateinput({'survey':survey,'pos':pos,'source':source,'radius':radius},'spectrumquery')

	if source!=None and pos!=None:
		raise Exception('Simultaneous pos and source input detected in spectrumquery.')
	elif source==None and pos==None:
		raise Exception('pos or source input required in spectrumquery.')

	data=survey_map(survey=survey,pos=pos,source=source,radius=radius)
	
	return data

def plotspectrum(data):
	config=readconfig()
	if config['ENABLE_NOTIFICATIONS']==1:
		print(f'Plotting spectrum...{newline}')	

	from .Plotting.spectra import get_plot
	
	plot=get_plot(spectrum_dict=data)
	
	if plot==None:
		return None

	filename=name_file(data=data,data_type='ATKspectrum')
	output_file(filename)

	plot.width,plot.height=config['PLOT_SIZE']*2,config['PLOT_SIZE']

	return plot

# Timeseries --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def plotpowspec(data):
	config=readconfig()
	if config['ENABLE_NOTIFICATIONS']==1:
		print(f'Plotting power spectrum...{newline}')	

	from .Plotting.powspec import get_plot
	
	plot=get_plot(dataset=data)
	
	if plot==None:
		return None

	filename=name_file(data=data,data_type='ATKpowspec')
	output_file(filename)
	
	plot.width,plot.height=config['PLOT_SIZE']*2,config['PLOT_SIZE']

	return plot

def tsanalysis(data):
	config=readconfig()
	if config['ENABLE_NOTIFICATIONS']==1:
		print(f'Running time series analysis...{newline}')	

	from .Timeseries.ztfanalysis import get_analysis
	
	get_analysis(dataset=data)

# Data Pages --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def gridsetup(dimensions,plots,grid_size=None):
	config=readconfig()
	
	if grid_size==None:
		grid_size=config['GRID_SIZE']

	if config['ENABLE_NOTIFICATIONS']==1:
		print(f'Creating grid...{newline}width = {dimensions[0]}{newline}height = {dimensions[1]}{newline}grid_size = {grid_size}{newline}')

	from .Datapages.grid import get_grid
	
	plots=get_grid(dimensions=dimensions,plots=plots,grid_size=grid_size)
	
	return plots

def getbuttons(grid_size=None,source=None,pos=None,simbad_radius=None,vizier_radius=None):
	config=readconfig()
	
	if grid_size==None:
		grid_size=config['GRID_SIZE']
	if simbad_radius==None:
		simbad_radius=config['SIMBAD_RADIUS']
	if vizier_radius==None:
		vizier_radius=config['VIZIER_RADIUS']

	if config['ENABLE_NOTIFICATIONS']==1:
		print(f'Generating info buttons...{newline}source = {source}{newline}pos = {pos}{newline} simbad_radius = {simbad_radius}{newline}vizier_radius = {vizier_radius}{newline}')

	from .Datapages.buttons import getinfobuttons	

	validateinput({'source':source,'pos':pos},'databuttons')

	if source!=None and pos!=None:
		raise Exception('Simultaneous pos and source input detected in getbuttons.')
	elif source==None and pos==None:
		raise Exception('pos or source input detected in getbuttons.')

	if not (isinstance(simbad_radius,int) or isinstance(simbad_radius,float)):
		data_type=type(simbad_radius)
		raise Exception(f'Incorrect simbad_radius data type. Expected float/int, got {data_type}.')
	if not (isinstance(vizier_radius,int) or isinstance(vizier_radius,float)):
		data_type=type(vizier_radius)
		raise Exception(f'Incorrect vizier_radius data type. Expected float/int, got {data_type}.')
	if not (isinstance(grid_size,int) or isinstance(grid_size,float)):
		data_type=type(grid_size)
		raise Exception(f'Incorrect grid_size data type. Expected float/int, got {data_type}.')

	plot=getinfobuttons(grid_size=grid_size,source=source,pos=pos,simbad_radius=simbad_radius,vizier_radius=vizier_radius)
	
	return plot

def getmdtable(metadata,pos=None,source=None):
	config=readconfig()
	if config['ENABLE_NOTIFICATIONS']==1:
		print(f'Generating metadata table...{newline}source = {source}{newline}pos = {pos}{newline}')	

	from .Datapages.metadata import gettable

	if source!=None and pos!=None:
		raise Exception('Simultaneous pos and source input detected in getmdtable.')
	elif source==None and pos==None:
		raise Exception('pos or source input required in getmdtable.')
	
	plot=gettable(metadata_dict=metadata,pos=pos,source=source)
	
	return plot

# Reddening query ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def getreddening(source=None):
	from .Data.reddening import getreddening
	
	if source==None:
		raise Exception('getreddening requires source input.')

	validateinput({'source':source})

	reddening=getreddening(source=source)
	
	return reddening

# File Handling -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def savedata(data):
	config=readconfig()
	if config['ENABLE_NOTIFICATIONS']==1:
		print(f'Saving data to local storage...{newline}')	

	from .Misc.file_handling import create_file
	
	fname=create_file(data_copy=data)
	
	return fname
	
def readdata(filename):
	config=readconfig()
	if config['ENABLE_NOTIFICATIONS']==1:
		print(f'Reading data from local storage...{newline}')	

	from .Misc.file_handling import read_file
	
	if not isinstance(filename,str):
		data_type=type(filename)
		raise Exception(f'Incorrect filename datatype. Expected str, got {data_type}.')

	data=read_file(file_name=filename)
	
	return data

def showplot(plot):
	from bokeh.plotting import show
	
	show(plot)
	
def saveplot(plot):
	from bokeh.plotting import save

	fname=save(plot)
	
	print(f'Saved file to {fname}.')

# exports plots to PNG. Have to use bokeh save() as a proxy to get the filename, so give an option to keep/delete the .html file.
def export(plot,keephtml=True):
	config=readconfig()
	if config['ENABLE_NOTIFICATIONS']==1:
		print(f'Exporting plot to PNG...{newline}')

	from bokeh.io import export_png
	from bokeh.plotting import save

	fname=save(plot)
	if keephtml==False:
		os.remove(fname)

	export_png(plot,filename=f'{fname[:-5]}.png')

	return None

# Miscellaneous -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def correctpm(inputtime,targettime,ra,dec,pmra,pmdec):
	from .Misc.ProperMotionCorrection import PMCorrection
	
	pos=PMCorrection(input=inputtime,target=targettime,ra=ra,dec=dec,pmra=pmra,pmdec=pmdec)

	return pos

def getdistance(parallax):
	# parallax must be in mas
	distance=1/(parallax*10**-3)
	return distance

def convfromdeg(pos):
	from .Misc.coord_conversion import convert_to_hmsdms

	pos=convert_to_hmsdms(pos)
	
	return pos

def convtodeg(pos):
	from .Misc.coord_conversion import convert_to_deg
	
	pos=convert_to_deg(pos)
	
	return pos

# not in README as need to improve functionality
def getsources(file_name):
	from .Misc.read_fits import get_source_list
	
	sources=get_source_list(file_name)
	return sources

# not in README as need to improve functionality
def getpositions(file_name):
	from .Misc.read_fits import get_pos_list
	pos_list=get_pos_list(file_name)
	return pos_list

def getpath():
	path = os.path.dirname(__file__)
	print(path)