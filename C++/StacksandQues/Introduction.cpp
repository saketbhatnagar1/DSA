/*****************************************************************/

#include <iostream>
using namespace std;
#include<bits/stdc++.h>

class Stack{
  vector<int> v;
  
  public:
  void push(int val)
  {
      v.push_back(val);//constant time operation
      
  }
  void pop()
  {
      v.pop_back();//constant time operation
  }
  int top(){
      return v[v.size()-1];//constatn time operation
  }
  
  bool empty(){
      if (v.size() == 0)
        {
            return true;
        }
        else{
            return false;
        }
      
  }
    
};

int main()
{

Stack S;

S.push(10);
S.push(20);
int a = S.top();
cout<<a;
    return 0;
}