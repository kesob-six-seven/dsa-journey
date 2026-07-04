#include<bits/stdc++.h>
#include <queue>
using namespace std;
//basic stdl in c++ 
// conyinue from vector 
void explainvector(){
    vector<int> v;
    //printing the vector
    for(vector<int>::iterator it = v.begin();it!=v.end();it++){
        cout<<*(it)<<" ";
    }
    //auto assigns according to the data 
    for (auto it=v.begin();it!=v.end();it++){
        cout<<*(it)<<" ";
    }
    for(auto it :v){
        cout<<it<<" ";
    }
    //{10,20,30,40}
    v.erase(v.begin()+1);//20 delete

    //insertion in vector
    vector<int>v1(2,100);//{100,100}
    v1.insert (v1.begin(),300);//{300,100,100}
    v1.insert(v1.begin()+1,2,10);//{300,10,10,100,100}   
    vector <int>copy(2,50);//{50,50}
    v.insert(v.begin(),copy.begin(),copy.end());//{50,50,300,10,10,100,100}
   //{10,20}
    v.pop_back();//{10}
    v.swap(v1);//swaps the vector
    v.clear();//clear the entire vector
     cout<<v.empty();
}
void expalinlist(){
    list <int>ls;
    ls.push_back(2);//{2}
    ls.emplace_back(4);//{2,4}
    ls.push_front(5); //{5,2,4}
    ls.emplace_front(2,3); ;//{}
    //rest of the functions are same as vectors
    
}
void explainstack(){
    stack<int >s;//stack follows lifo (last in first out)
     s.push(1);//{1}
     s.push(2);//{2,1}
     s.push(3);//{3,2,1}
     s.push(3);//{4,3,2,1}
     cout<<s.top();//pritn5
     s.pop();//{3,3,2,1}
     cout<<s.top();//3
     cout<<s.size();//4
     cout<<s.empty();
     stack<int>s1,s2;
     s1.swap(s2);
     
}
void explainque(){
    queue<int>q;//queue is first in first out (fifo)
    q.push(1);//{1}
    q.push(2);//{1,2}
    q.emplace(3);//{1,2,3}
    q.back()+=5;

    cout<<q.back();
    cout<<q.front();
    q.pop();
    cout<<q.front();
    
}
void explainPQ(){
    //max_heap
    priority_queue<int>pq;//the largest no at the top 
    pq.push(5);//{5}
    pq.push(5);//{5,2}
    pq.push(5);//{8,5,2}
    pq.emplace(10);//{10,8,5,2}
    cout<<pq.top();//prints 10
    pq.pop();//{8,5,2}
    cout<<pq.top();//prints 8
    //size swap empty function same as others 
    // minimum heap (queue that stores minimum at the top)
    priority_queue<int,vector<int>,greater <int>>pq1;
    //you can perform all the functions 
}
void explain_set(){
    set<int>st;//only unique inserts
    st.insert(1);//{1}
    st.insert(2);//{1,2}
    st.insert(3);//{1,2}
    st.insert(4);//{1,2,4}
    st.insert(5);//{1,2,3,4}
    //functionally of insert in vector 
    // can be used alo 
    // begin(),end(),rbegin),rend(),sixe()
    // empty ()and swap ()are smae as thode of above 
    // {1,2,3,4,5}
    auto it=st.find(3);
    auto it1=st.find (6);//retuns st.end();
    st.erase(5);//logarithmic time comlexity
    int cnt=st.count(1);//only 0 and one output
    auto it2=st.find(1);
    auto it3=st.find(4);
    st .erase (it1,it2);//from  1 to 4 but not include them 
    
    
}
void multi_set(){
    //everting same as set 
    // only stores duplicate elements also
}
void expalinuset(){
    unordered_set<int>sut;
    //lower_bound and upper_doesnt work
    // rest,all functions are same 
    // doesnt have any order it has better time 
    // complexity than set in most cases , except
    // some when collision happens 
    
}