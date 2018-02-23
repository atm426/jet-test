//===============================================
// initial conditions for point-source explosion
//===============================================

#include "../paul.h"

void setICparams( struct domain * theDomain ){
}

void initial( double * prim, double * x){


  double r = x[0];
  double rho = 1.0e-7; 
  double Pmin = 1e-6; 
  double vel = 0.0;
  double gam = 4/3.;

  double Rexp = 1e-3;
  double E = 1.0;
  double ed = E / ((4/3.)*M_PI*(pow(Rexp,3)));

  double P = Pmin;
  if( r < Rexp ){

    P = (gam-1)*ed;

  }
  
  prim[RHO] = rho;
  prim[PPP] = P;
  prim[UU1] = vel;
  prim[UU2] = vel;

}
