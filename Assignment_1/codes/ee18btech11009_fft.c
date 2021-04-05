#include <stdio.h>
#include <stdlib.h>
#include <math.h>

typedef struct
{
	double Real;
	double Imag;
} complex;


int main()
{
	int N = 8;
	int x[] = {1,2,3,4,2,1,0,0};

	complex *X = (complex *) malloc(N * sizeof(complex));

	for(int i = 0; i < N; i++)
	{
		X[i].Real = x[i];
		X[i].Imag = 0;
	}
	FFT(X,N);

	//Displaying X(k)
	printf("X(k)= (X{Re} , X{Img})\n");
	for(int i = 0; i < N; i++){
		printf("X(%d)= (%.5lf, %.5lf)\n",i, X[i].Real, X[i].Imag);
}
}

void FFT(complex *X, int n)
{

	if(n <= 1) return;

	//Allocating an array of size n/2 for even and odd arrays
	complex *Xe = (complex *) malloc(n/2 * sizeof(complex));
	complex *Xo = (complex *) malloc(n/2 * sizeof(complex));

	for(int i = 0; i < n/2; i++)
	{
		Xe[i] = X[2*i];
		Xo[i] = X[2*i+1];
	}

	//Recursive use of FFT function
	FFT(Xe,n/2);
	FFT(Xo,n/2);

	//FFT computation
	for(int i = 0; i < n/2; i++)
	{
		double cosine = cos(2*M_PI*i/n);
		double sine = sin(2*M_PI*i/n);

		complex z;

		// W_N*Xo term
		z.Real = cosine * Xo[i].Real + sine * Xo[i].Imag;
		z.Imag = cosine * Xo[i].Imag - sine * Xo[i].Real;

		// X_a = Xe + W_N*Xo
		// upper half of the DFT X, for k: [0,n/2 -1]
		X[i].Real = Xe[i].Real + z.Real;
		X[i].Imag = Xe[i].Imag + z.Imag;

		//X_b = Xe - W_N*Xo
		//Lower half of the DFT X, for k: [n/2,n]
		X[i+n/2].Real = Xe[i].Real - z.Real;
		X[i+n/2].Imag = Xe[i].Imag - z.Imag;
	}
}
