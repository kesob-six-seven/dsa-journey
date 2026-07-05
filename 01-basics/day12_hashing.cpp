#include<bits/stdc++.h>
using namespace std;
 /*
 today im learning recursion heheheh
 question :
 the fequency of a number in array ,
 
 tc is too much O(Q*N)
 where N is the number of times for which loops running 
 Q is toatl nos in array
 */
 int f(int num, int arr[]){
     int count =0;
     int n; // 🔄 Flagged: n is uninitialized!
     for(int i=0;i<n;i++){
         if (arr[i]==num)
             count++;
     }
     return count ;
     
 }

/*  on doing the same thing with hashing 
  Definition:
    hashing is prestoring something and fetching
    */
 int mainhash(){
     int n;
     cin>>n;
     int arr[n];
     for(int i=0;i<n;i++){
         cin>>arr[i];
     }
    //precompute 
     int hash [13]={0};
     for(int i=0;i<n;i++){
         hash[arr[i]]+=1;
     }

     int q;
     cin>>q;
     while (q--){
         int number;
         cin>>number;
         //fetch
         cout<<hash[number]<<endl;
     }

     return 0;
 }

 /*
  question :
  now doing it for srtring
  
  we use ASCII for this 
  every alphabet is assigned a value so we need to do that

  approach :
  ch-'a' this gives the index in the hash array
  we will take only 26 sized array as we are only using lowercase
  alphabets , we can take 255 sized array as well ass it will contain
  all the ascii values 
  */

 int main(){
     string  s;
     cin>>s;

     //pre compute
     int hash[256]={0};
     for(int i=0;i<s.size();i++){
         // hash[s[i]-'a']++; (for only lowercase)
         hash[s[i]]++;//auto cast itself into (ASCII) integr 
     }
    int q;
    cin>>q;
    while (q--){
        char c;
        cin>>c;
        //fetch;
        // cout<<hash[c-'a']<<endl;(for only lower case)
        cout<<hash[c]<<endl;
    }
     return 0;
 }