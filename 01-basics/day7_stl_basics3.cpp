#include<bits/stdc++.h>
using namespace std;
//basic stdl in c++ 
// conyinue from vector 
void explainMAP(){
    map<int,int>mp1;//map stores unique key in sotrd order 
    map<int,pair<int,int>>mp2;//no duplicates all uniques 
    map<pair<int,int>,int>mpp;
    
     
    mp1[1]=2;
    mp1.emplace(3,1);
   
    mp1.insert({3,2});
    mpp[{2,3}]=10;
    for(auto it:mp1){//for printing the whole , map in pairs 
        cout<<it.first<<""<<it.second<<endl;
    }
    cout<<mp1[1];
    cout<<mp1[5];
    auto it1=mp1.find(3);
    cout<<(it1->second);
      auto it=mp1.find(5);
    auto it2=mp1.lower_bound(2);
    auto it3=mp1.lower_bound(3);
  //erase,swap,size,empty,are same as above
}
 void explainmultimap(){
     //everything same as map, it can store multiple keys
     // {1,2}{1,3}
     // only mp1[key] cannot be used here 
 }
 void explainunorderedmap(){
     //same difference as set and unordered_Set difference
     // but it has unique keys 
 }
 void explainsort(){
     int arr[4]={1,5,4,3};
     sort(arr,arr+3);//sorts array 
     vector<int>v;
     sort(v.begin(),v.end());
     sort(arr,arr+3,greater<int>());//sorts in descending order
     //we can make our own boolian comaparitor
     int num=7;//{111}
     int cnt=__builtin_popcount(num);//gives three ar there are 1's
     long long num2=16589089089;
     int cnt2=__builtin_popcountll(num2);//long long
 }
 bool comp(pair<int,int>p1,pair<int,int>p2){
     if(p1.second<p2.second)return true;//just compare 2 pairs 
     if(p1.second >p2.second)return false;
     //they are same 
     if(p1.first>p2.first)return true;
     return false;
 }
     void basicpermuatation(){
         string s="123";
         sort(s.begin(),s.end());
         do{
             cout<<s<<endl;// this is for permuataion 
         }while(next_permutation(s.begin(),s.end()));
         //
         int a[]={3,1,4,1,5};
         int n=5;
         int maxi=*max_element(a,a+n); //gives the max element in an array
        //min_elemrnt is also there sam use case for the minimum element in array 
         int mini=*min_element(a,a+n);
         }
         
int main(){
    return 0;
}