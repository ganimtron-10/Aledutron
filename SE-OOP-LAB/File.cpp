#include<iostream>
#include<fstream>
using namespace std;

int main(){

	// fstream file;

	// // modes
	// // in, out, app, bin

	// //open
	// file.open("test.txt", ios::out);
	// //execute
	// if(file.is_open()){
	// 	file << "Hello" << endl;
	// }
	// //close
	// file.close();

	// //open
	// file.open("test.txt", ios::app);
	// //execute
	// if(file.is_open()){
	// 	file << "Hello2" << endl;
	// }
	// //close
	// file.close();

	// string line,line2;
	// file.open("test.txt", ios::in);
	// if(file.is_open()){
	// 	getline(file,line);
	// 	getline(file,line2);
	// }
	// file.close();

	// cout << line << " " << line2;

	ifstream ifile;
	ofstream ofile;

	// ofile.open("test.txt");
	// ofile << "Hello" << endl;
	// ofile.close();

	// ofile.open("test.txt", ios::app);
	// ofile << "Hello2" << endl;
	// ofile.close();

	string line;
	ifile.open("test.txt");
	while(!ifile.eof()){
		ifile >> line;
		cout << line << endl;
	}
	ifile.close();

	// cout << line << " " << line2;
}