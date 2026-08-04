#include<bits/stdc++.h>
using namespace std;
//basic stdl in c++ 
// pairs in c++
void explainpair(){
    pair<int,int>p={1,3};
    cout<<p.first<<""<<p.second;
    //  1 3 as output
    pair<int,pair<int,int>>p1 ={1,{3,4}};
    cout<<p1.first<<" "<<p1.second.second<<" "<<p1.second.first;
    //gives output 1 4 3
    pair<int,int>arr[]={{1,2},{3,4},{3,2}};
    cout<<arr[1].second;
}

void explainVector(){
    vector <int>v;//as array's size is already defined , vector is 
                   //dynamic in nature 
    v.push_back(1);//it creates a emty container and put 1  {1}
    v.emplace_back(2);//{1} -->  {1,2} faster than push_back
   
    vector<pair<int,int>>vec;
    vec.push_back({1,2});//pairs needs to be in curly bracekts
    vec.emplace_back(1,2);//assumes it to be
    
    vector<int> v1(5);//this means the vector defined as{0,0,0,0,0}
    vector<int> v2(5,100);//this means the vector is stored as{100,100,100,100,100}
    //vector an be accessed 
    cout<<v[0]<<" "<<v.at(0);
    //and can be accessed by **itrator**(accessing vector in the memorory/accto INDEX)
    vector<int>::iterator it=v2.begin();//{100,100,100,100,100} currently at first 100
    it++;//at second hundred 
    cout<<*it<<" ";//prints 2nd hundred
   // exammple v={10,20,30,40}
   // vec<int>::interator it=v.end; then it--is 40 , end is after index of 40
          //rend rbegin never used 
   // rend - reverse end {10,20,30,40}, rend =index before 10 ; 
   //rbegin is reverse begin  it++is 30 move backward
  cout<<v.back()<<" "; //element at the last index
}