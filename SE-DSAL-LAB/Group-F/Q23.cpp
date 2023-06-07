#include<iostream>
#include<fstream>
#include<iomanip>
using namespace std;

void addStudent(){
	ofstream f("db.txt",ios::app);

	string rn,name,div,add;
	cout << "Enter Student Roll No.: ";
	cin >> rn;
	cout << "Enter Student Name: ";
	cin >> name;
	cout << "Enter Student Division: ";
	cin >> div;
	cout << "Enter Student Address: ";
	cin >> add;

	f << left << setw(20) << rn << setw(20)  << name << setw(20) << div << setw(20) << add << endl;

	f.close();

	cout << "Student Added Sucessfully.\n";
}

void deleteStudent(){
	ifstream f("db.txt");
	string line;

	string rn;
	cout << "Enter Student Roll No. To Delete: ";
	cin >> rn;

	string fileData;

	while(getline(f,line)){
		if(line.find(rn) == string::npos){
			fileData += line;
			fileData += "\n";
		}
	}
	f.close();

	ofstream f1("db.txt",ios::out);
	f1 << fileData;
	f1.close();


}

void searchStudent(){
	ifstream f("db.txt");
	string line;

	string rn;
	cout << "Enter Student Roll No. To Search: ";
	cin >> rn;

	bool found = false;

	while(getline(f,line)){
		if(line.find(rn) != string::npos){
			cout << "Student Details:" << endl;
			cout << line << endl;
			found = true;
			break;
		}
	}
	f.close();

	if(!found){
		cout << "Student Doesn't Exist!" << endl;
	}
}

void printStudent(){
	ifstream f("db.txt");
	string line;
	cout << "\nPrinting File Data..." << endl;
	while(getline(f,line)){
		cout << line << endl;
	}
	cout << "Printing Complete!\n";
	f.close();
}

int main(){

	ofstream f("db.txt",ios::out);
	f << left << setw(20) << "Roll No." << setw(20)  << "Name" << setw(20) << "Division" << setw(20) << "Address" << endl;
	f.close();

	int ip;
	while(ip != -1){
		cout << "\nEnter your choice\n1. Add Student\n2. Delete Student\n3. Search Student\n4. Print Data\n5. Exit\n---> ";
		cin >> ip;
		switch(ip){
			case 1:
				addStudent();
				break;
			case 2:
				deleteStudent();
				break;
			case 3:
				searchStudent();
				break;
			case 4:
				printStudent();
				break;
			case 5:
				return 0;
				break;
			default:
				cout << "Please ReEnter your Choice.";
				break;
		}
	}

}