# CASA tutorials

'''
tclean task: create radio image from measurement sets

+ To run the script:
    - start CASA
    - execute the script inside CASA environment:

execfile ('CASA_Imaging.py')

+ To understand the defination of the parameters, in CASA environment, type: help (tclean)

+ Important parameters to change (in our case):
    - vis: visibility data (in string or list of string)
    - uvrange: the range of the uv data used for imaging. For example, uvrange = '>100lambda'
    - datacolumn: data column where data is saved. In our case, it's datacolumn = 'data'
    - imagename: the name of the output images. For example, imagename = 'Abell1213_uvrange100lambda_robust0'.
    - imsize: the size of the output images in pixels. For example, imsize = [1024, 1024]
    - cell: the angular size of the pixels. e.g., cell='2arcsec' means that the angular size of the pixel is 2 arcsec. This needs to be at least 3-5 times smaller than the resolution of the synthesized beam.
    - specmode = 'mfs', create a single continuum image
    - deconvolver. the deconvolver used during the creation of the images. deconvolver = 'mtmfs', meaning multi-scale, multi-frequency deconvolution and that the process takes into account the wide frequency and multi-scale of the diffuse emission.
    - scales. modeling diffuse emission with multiple scales
    - nsigma. the max pixel value, compared with the rms noise, to stop cleaning.
    - weighting. the weighting of uv data.
    - robust. parameters to adjust the briggs weighting. ranging from -2 (uniform weighting) to +2 (natural weighting).

+ experiment with following options
    - uvrange: '' (all), '>1klambda', '>3klambda'
    - robust: -0.5, 0.5
    - niter: 0 (dirty), 20000 (or any large number for deep clean)
    - scales: [] (single scale), [0,3,5] (for multi-scales)

'''
tclean (
    vis                  = ['P168+30_avg_180s.ms', 'P171+30_avg_180s.ms'],
    selectdata           = True,
    field                = '',
    spw                  = '',
    timerange            = '',
    uvrange              = '<10klambda',
    antenna              = '',
    scan                 = '',
    observation          = '',
    intent               = '',
    datacolumn           = 'data',
    imagename            = 'A1213_less10klambda_robust0.25_test2',
    imsize               = [1024, 1024],
    cell                 = '2arcsec',
    phasecenter          = '',
    stokes               = 'I',
    projection           = 'SIN',
    startmodel           = '',
    specmode             = 'mfs',
    reffreq              = '',
    nchan                = -1,
    start                = '',
    width                = '',
    outframe             = 'LSRK',
    veltype              = 'radio',
    restfreq             = [],
    interpolation        = 'linear',
    perchanweightdensity = True,
    gridder              = 'standard',
    facets               = 1,
    psfphasecenter       = '',
    wprojplanes          = 1,
    vptable              = '',
    mosweight            = True,
    aterm                = True,
    psterm               = False,
    wbawp                = True,
    conjbeams            = False,
    cfcache              = '',
    usepointing          = False,
    computepastep        = 360.0,
    rotatepastep         = 360.0,
    pointingoffsetsigdev = [],
    pblimit              = 0.2,
    normtype             = 'flatnoise',
    deconvolver          = 'mtmfs',
    scales               = [0, 3, 5],
    nterms               = 2,
    smallscalebias       = 0.0,
    fusedthreshold       = 0.0,
    largestscale         = -1,
    restoration          = True,
    restoringbeam        = [],
    pbcor                = False,
    outlierfile          = '',
    weighting            = 'briggs',
    robust               = 0.25,
    noise                = '1.0Jy',
    npixels              = 0,
    uvtaper              = [],
    niter                = 20000,
    gain                 = 0.1,
    threshold            = 0.0,
    nsigma               = 3,
    cycleniter           = -1,
    cyclefactor          = 1.0,
    minpsffraction       = 0.05,
    maxpsffraction       = 0.8,
    interactive          = False,
    fullsummary          = False,
    nmajor               = -1,
    usemask              = 'user',
    mask                 = '',
    pbmask               = 0.0,
    sidelobethreshold    = 3.0,
    noisethreshold       = 5.0,
    lownoisethreshold    = 1.5,
    negativethreshold    = 0.0,
    smoothfactor         = 1.0,
    minbeamfrac          = 0.3,
    cutthreshold         = 0.01,
    growiterations       = 75,
    dogrowprune          = True,
    minpercentchange     = -1.0,
    verbose              = False,
    fastnoise            = True,
    restart              = True,
    savemodel            = 'none',
    calcres              = True,
    calcpsf              = True,
    psfcutoff            = 0.35,
    parallel             = False )
