/*****************************************************************/
#include <iostream>
using namespace std;
#include<bits/stdc++.h>
#include <list>
#include<stack>
#include<deque>
class Queue{
  //using array
  int *arr;
  int front;
  int rear;
  int size;
  public:
   Queue(int capacity) {
        size = capacity;
        arr = new int[size];
        front = 0;
        rear = -1;
    }
    void enqueue(int element) {
        if (rear == size - 1) {
            cout << "Queue is full" << endl;
            return;
        }
        rear++;
        arr[rear] = element;
    }
     void dequeue() {
        if (front > rear) {
            cout << "Queue is empty" << endl;
            return;
        }
        front++;
    }
     void display() {
        if (front > rear) {
            cout << "Queue is empty" << endl;
            return;
        }
        cout << "Queue elements: ";
        for (int i = front; i <= rear; i++) {
            cout << arr[i] << " ";
        }
        cout << endl;
    }
};
//using LinkedList:



class Node{

    public:
    int data;
    Node* next;

    Node(int val)
    {
        next = NULL;
        data = val;
    }
}




class LinkedListQueue{

Node* head;
Node* tail;

public:
LinkedListQueue(){

    head = tail = NULL;
}
int front()
{
    if(empty())
    {
        cout<<"Empty Linked List";
        return-1;
    }

return head->data;

}

void push(int data)//insert data at tail of LL
{
    Node* newNode = Node(data);
    if(empty())
    {
        head = newNode;
        tail = newNode;
    }else{
        tail->next = newNode
        tail = newNode;
    }
}

void pop() // delete data from front/head,or move head by one
{

    if(empty())
    {
        cout<<"Empty Linked List";
        return;
    }else{
        Node*temp = head;
        head = head->next;
        delete temp;
    }
}

bool empty()
{

    return head == NULL;
}


};


//deque


int main()
{
    //deque
    deque<int> dq;
    dq.push_back(1);
    dq.push_front(4);
    



    return 0;
}