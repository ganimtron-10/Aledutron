// Represent a given graph using adjacency matrix/list to perform DFS and using adjacency 
// list to perform BFS. Use the map of the area around the college as the graph. Identify the 
// prominent land marks as nodes and perform DFS and BFS on that.

#include<iostream>
#include<vector>
#include<queue>

// #include<bits/stdc++.h>

using namespace std;

void dfs(vector<vector<int>>& g, int start, vector<int>& vis){
	vis[start] = 1;
	cout << start << " ";
	for(auto child: g[start]){
		if(!vis[child]){
			dfs(g,child,vis);
		}
	}
}

void bfs(vector<vector<int>>& g, int start){
	vector<int> vis(g.size(),0);
	queue<int> q;
	q.push(start);
	vis[start] = 1;

	while(!q.empty()){
		int cur = q.front();
		q.pop();
		cout << cur << " ";

		for(auto child: g[cur]){
			if(!vis[child]){
				q.push(child);
				vis[child] = 1;
			}
		}
	}


/*

0 -> 1 -> 3 -> 4 
     |
     ---> 2

*/


	
}

int main(){
	int V;
	cin >> V;
	vector<vector<int>> g;

	for(int i = 0; i < V; i++){
		vector<int> temp;
		g.push_back(temp);
	}

	int E;
	cin >> E;
	for(int i = 0; i < E; i++){
		int a,b;
		cin >> a >> b;
		g[a].push_back(b);
		g[b].push_back(a);
	}



	vector<int> vis(V,0);
	cout << "DFS: ";
	dfs(g,0,vis);
	cout << endl;


	cout << "BFS: ";
	bfs(g,0);
	cout << endl;
}