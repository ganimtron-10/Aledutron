#include<iostream>
#include<algorithm>
using namespace std;

class Node{
	public:
		int data = 0;
		Node* left = NULL;
		Node* right = NULL;
};

class BST{
	public:
		Node* root = NULL;
		
		void insert(int val){
			Node* temp = new Node();
			temp->data = val;

			if(this->root == NULL){
				this->root = temp;
			}else{

				Node* cur = this->root;
				while(true){
					if(val > cur->data){
						if(cur->right == NULL){
							cur->right = temp;
							break;
						}
						cur = cur->right;
					}else{
						if(cur->left == NULL){
							cur->left = temp;
							break;
						}
						cur = cur->left;
					}
				}

			}

		}


		void inorder(Node* node){
			if(node == NULL){
				return;
			}

			inorder(node->left);
			cout << node->data << " ";
			inorder(node->right);
		}

		bool search(int val, Node* node){
			if(node == NULL){
				return false;
			}
			bool ans = false;

			ans |= search(val,node->left);
			if(node->data == val){
				return true;
			}
			ans |= search(val,node->right);

			return ans;
		}

		int minValue(Node* node){
			if(node->left == NULL){
				return node->data;
			}
			minValue(node->left);
		}

		int maxValue(Node* node){
			if(node->right == NULL){
				return node->data;
			}
			maxValue(node->right);
		}

		int calHeight(Node* node){
			if(node == NULL){
				return 0;
			}
			return max(1+calHeight(node->left), 1+calHeight(node->right));
		}

		void swapTree(Node* node){
			if(node == NULL){
				return;
			}

			swapTree(node->left);
			swapTree(node->right);

			Node* temp = node->right;
			node->right = node->left;
			node->left = temp;
		}

};

int main(){
	BST t;

	t.insert(10);
	t.insert(-1);
	t.insert(15);
	t.insert(3);
	t.insert(10);
	t.insert(1);
	t.insert(15);
	t.insert(3);

	cout << "Inorder: ";
	t.inorder(t.root);
	cout << endl;

	cout << t.search(11, t.root) << endl; 

	cout << t.minValue(t.root) << endl;

	cout << t.maxValue(t.root) << endl; 

	cout << t.calHeight(t.root) << endl; 

	t.swapTree(t.root);

	cout << "Inorder: ";
	t.inorder(t.root);
	cout << endl;
}