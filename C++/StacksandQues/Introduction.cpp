/*****************************************************************/

#include <iostream>
using namespace std;
#include<bits/stdc++.h>

//using array:
class StackArray {
    int arr[100]; // maximum stack size
    int topIndex;

public:
    StackArray() {
        topIndex = -1; // initialize to -1 to represent an empty stack
    }

    void push(int val) {
        if (topIndex >= 99) {
            cout << "Stack Overflow!" << endl;
            return;
        }
        topIndex++;
        arr[topIndex] = val;
    }

    void pop() {
        if (topIndex < 0) {
            cout << "Stack Underflow!" << endl;
            return;
        }
        topIndex--;
    }

    int top() {
        if (topIndex < 0) {
            cout << "Stack is empty!" << endl;
            return -1; // default error value
        }
        return arr[topIndex];
    }

    bool empty() {
        return topIndex == -1;
    }

    int size() {
        return topIndex + 1;
    }
};

//using vector
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


class StackLinkedList{
    list <int> ll;
    public:
    void push(int val){
        ll.push_front(val);
    }
    
    void pop() //remove the head and head is head->next 
    {
        ll.pop_front(); //head should be moved to the next of the Linked List's head
         
    }
    int top()  //return head of Linked list
    {
        return ll.front();
        
    }
    bool empty()
    {
        if (ll.empty()){
            return true;
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