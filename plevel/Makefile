# The following three directory may need to set.
NETCDFPATH = /opt/cray/pe/netcdf/4.4.1.1.3/intel/160/
HDF5PATH = 
POSTPPATH  = .
FFLAGS = -I${NETCDFPATH}/include -I/usr/include -fltconsistency -fno-alias -stack_temps -safe_cray_ptr -ftz -static -assume byterecl -g -O2 -i4 -r8 -nowarn -Wp,-w
LDFLAGS =  -L${NETCDFPATH}/lib -L${HDF5PATH}/lib -lnetcdff -lnetcdf 
DEFFLAG = -Duse_netCDF
#LNFLAGS = -v
FC      = ftn

OBJS = plev_constants.o moisture_convert.o pressure_interp.o pinterp_utilities.o run_pressure_interp.o getopts.o

PLEV.exe: $(OBJS)
	$(FC) $(LNFLAGS) -o $@ $(OBJS) $(LDFLAGS)

run_pressure_interp.o: $(POSTPPATH)/run_pressure_interp.F90
	$(FC) $(FFLAGS) -c $(POSTPPATH)/run_pressure_interp.F90

getopts.o: $(POSTPPATH)/getopts.F90
	$(FC) $(FFLAGS) -c $(POSTPPATH)/getopts.F90

pinterp_utilities.o: $(POSTPPATH)/pinterp_utilities.F90
	$(FC) $(FFLAGS) -c $(POSTPPATH)/pinterp_utilities.F90

pressure_interp.o: $(POSTPPATH)/pressure_interp.F90
	$(FC) $(FFLAGS) -c $(POSTPPATH)/pressure_interp.F90

moisture_convert.o: $(POSTPPATH)/moisture_convert.F90
	$(FC) $(FFLAGS) -c $(POSTPPATH)/moisture_convert.F90

plev_constants.o: $(POSTPPATH)/plev_constants.F90
	$(FC) $(FFLAGS) -c $(POSTPPATH)/plev_constants.F90

clean:
	rm -f *.o *.mod PLEV.exe
