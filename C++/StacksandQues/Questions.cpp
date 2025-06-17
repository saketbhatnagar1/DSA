#include<iostream>
using namespace std;








/////Valid Parenthesis leetcode 20 
class Solution {
public:
    bool isValid(string s) {
        stack<char> st;
        for (int i = 0; i < s.size(); i++) {
            if (s[i] == '(' || s[i] == '{' || s[i] == '[') {
                                st.push(s[i]);
            } else {
                if (st.empty()) {
                    return false;
                }
                
                if ((s[i] == ')' && st.top() == '(') ||
            (s[i] == ']' && st.top() == '[') ||
                    (s[i] == '}' && st.top() == '{')) {
                    st.pop();
                } else {
                    
                    return false;
                }
            }
        }
        // If the stack is empty, all brackets matched properly
        return st.empty();
    }
};


int main()
{
    return 0;
}