#include <iostream>
#include <iomanip>
#include <vector>
#include <fstream>

#include <cmath>
#include <ctime>

#include <unistd.h>

#include <sys/resource.h>

#define RANGE		1000.0
#define PRECISION	1000.0

using namespace std;

const double a = 1.0/392.0;

const vector <vector <double>> D {
	{0, 2, 6, 9, 12, 16},
	{0, 4, 2, 9, 3, 4}
};

const int size = 6;

double psa(double x)
{
	return a * pow(x, 3) + (-27 * a - 5/49) * pow(x, 2)
		+  (195 * a + 90/49) * x + (-288 * a + 36/49);
}

double psa_opt(double x)
{
	return (-288 * a + 36/49) + x * ((195 * a + 90/49)
		+ x * ((-27 * a - 5/49) + x * a));
}

double e_f(double x, const vector <vector <double>> &D, int size)
{
	double sum = 0;

	for (int i = 0; i < size; i++) {
		double d = x - D[0][i];

		sum += D[1][i] * exp(-1 * d * d);
	}

	return sum;
}

double x_f(double x, const vector <vector <double>> &D, int size)
{
	double sum = 0;

	for (int i = 0; i < size; i++) {
		double d = x - D[0][i];

		sum += D[1][i] / (1 + d * d);
	}

	return sum;
}

ofstream fout("data.txt");

int main()
{
	setpriority(PRIO_PROCESS, getpid(), -20);

	double psa_t;
	double psa_opt_t;

	double e_f_t;
	double x_f_t;

	clock_t start;
	clock_t end;

	fout << fixed << setprecision(8);

	for (double k = 0; k < RANGE; k++) {
		// cout << getpriority(PRIO_PROCESS, getpid()) << endl;

		// Psa
		start = clock();

		for (double i = 0;  i < k; i += 1/PRECISION)
			// cout << psa(i) << endl;
			psa(i);

		end = clock();

		psa_t = (end - start)/(double) CLOCKS_PER_SEC;
		
		// Psa Opt
		start = clock();

		for (double i = 0;  i < k; i += 1/PRECISION)
			psa_opt(i);

		end = clock();

		psa_opt_t = (end - start)/(double) CLOCKS_PER_SEC;
		
		// E_f
		start = clock();

		for (double i = 0;  i < k; i += 1/PRECISION)
			e_f(i, D, size);

		end = clock();

		e_f_t = (end - start)/(double) CLOCKS_PER_SEC;
		
		// X_f
		start = clock();

		for (double i = 0;  i < k; i += 1/PRECISION)
			x_f(i, D, size);

		end = clock();

		x_f_t = (end - start)/(double) CLOCKS_PER_SEC;

		// Results
		
		fout << PRECISION * k << "\t" << psa_t
			<< "\t" << psa_opt_t << "\t"
			<< e_f_t << "\t" << x_f_t << endl;
	}
}
