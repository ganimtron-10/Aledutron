#include<iostream>
#include<vector>
using namespace std;


template<typename T>
vector<T> take_ip(int n){
	vector<T> v;

	for(int i = 0 ; i < n; i++){
		T x;
		cout << "Enter " << i+1 << " value: ";
		cin >> x;
		v.push_back(x);
	}

	return v;
}

/*
23,7,8,4
4,7,8,23



*/



template<typename dt>
int min_val(vector<dt>& v, int i, int n){
	dt min = v[i];
	int min_index = i;
	for(int ind = i; ind < n;ind++){
		if(v[ind] < min){
			min = v[ind];
			min_index = ind;
		}
	}

	return min_index;
}


template<typename dt>
void selection_sort(vector<dt>& v){
	int n = v.size();
	for(int i = 0; i < n-1; i++){
		int minvali = min_val<dt>(v,i,n);
		swap(v[i],v[minvali]);
	}
}


int main(){
	int n;
	cout << "Enter number of element: ";
	cin >> n;


	auto v = take_ip<char>(n);
	

	for(int i = 0; i < v.size(); i++){
		cout << v[i] << " ";
	}
	cout << endl;
	selection_sort<char>(v);

	for(int i = 0; i < v.size(); i++){
		cout << v[i] << " ";
	}

}