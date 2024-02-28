from AstroToolkit.Tools import imagequery,plotimage,plothrd,sedquery,plotsed,spectrumquery,plotspectrum,lightcurvequery,plotlightcurve,plotpowspec,getbuttons,gridsetup,getmdtable,showplot,export
from bokeh.layouts import column,row,layout
from bokeh.plotting import output_file

# source = Hu Leo
source=587316166180416640

# set grid size (scales overally size of datapage)
grid_size=275

# get image data and plot it
image_data=imagequery(survey='any',source=source,overlays='gaia,galex_nuv,galex_fuv,twomass,wise')
image=plotimage(image_data)

# get hrd
hrd=plothrd(source=source)

# get sed data and plot it
sed_data=sedquery(source=source)
sed=plotsed(sed_data)

# get spectrum data and plot it
spectrum_data=spectrumquery(survey='sdss',source=source)
spectrum=plotspectrum(spectrum_data)

# get lightcurve data [g,r,i]
lightcurve_data=lightcurvequery(survey='ztf',source=source)

# plot each lightcurve in lightcurve_data and set colour of each plot
lightcurves=plotlightcurve(lightcurve_data,colours=['green','red','blue'])

# plot power spectrum data (lightcurve_data)
power_spectrum=plotpowspec(lightcurve_data)

# get SIMBAD and Vizier buttons
buttons=getbuttons(grid_size=grid_size,source=source)

# make a custom metadatatable entry
custom_entry={
    'parameters':['one'],
    'values':['two'],
    'errors':['three'],
    'notes':['four']
    }

# get metadata table
metadata=getmdtable(source=source,metadata={'gaia':'default','galex':'default','panstarrs':'default','skymapper':'default','sdss':'default','wise':'default','twomass':'default','custom':custom_entry})

# get plots, formatted into grid dimensions
plots=gridsetup(dimensions=[6,5],plots=[[image,2,2],[hrd,2,2],[sed,2,1],[lightcurves,2,1],[buttons,1,1],[spectrum,3,1],[power_spectrum,2,1],[metadata,6,2]],grid_size=grid_size)

# set up the final grid
datapage=layout(
		column(
            row(plots[0],plots[1],column(plots[2],plots[3])),
            row(plots[4],plots[5],plots[6]),
            row(plots[7])
	))

# set name of output file
output_file(f'{source}_datapage.html')

export(datapage)