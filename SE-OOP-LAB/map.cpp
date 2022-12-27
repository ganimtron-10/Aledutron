#include<bits/stdc++.h>
using namespace std;

int main(){

	unordered_map<string,int> sdb;

	sdb["s1"] = 46;
	sdb["s2"] = 78;
	sdb["s3"] = 943;

	string s;
	cout << "Enter name of the state: " ;
	cin >> s;
	cout << "State " << s << " has a population of " << sdb[s] << endl; 

}