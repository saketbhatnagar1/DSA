#include<iostream>
#include "utils.h"
using namespace std;
#include<bits/stdc++.h>

//BinaryTreeImplementation:
class Node{
public:
    int data;
    Node* right;
    Node* left;
    Node(int val)
    {
        data = val;
        left = NULL;
        right = NULL;
    } 
};

static int indexx= -1;
 Node* preOrderBuild(vector<int> &preordersequence)
    {
        indexx++;
        if (preordersequence[indexx]==-1) {return NULL;}
        Node* root =new Node(preordersequence[indexx]);
        root->left = preOrderBuild(preordersequence);
        root->right = preOrderBuild(preordersequence);
        return root;

    }
int main()
{
    
vector<int> data = {1,2,-1,-1,3,4,-1,-1,5,-1,-1};
Node *root = preOrderBuild(data);

PreOrdTra(root);
    return 69;
}
//pre order traversel: Root->left->Right 

void PreOrdTra(Node* root)
{
    if (root==NULL)
    {
        return;
    }
    cout<<root->data;
    PreOrdTra(root->left);
    PreOrdTra(root->right);
}

