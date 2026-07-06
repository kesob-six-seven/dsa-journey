#include<bits/stdc++.h>
using namespace std;
// again hashing 
/*
so we use stls  for hashing 
-in stl we have map & unodered -map 

map<key ,value > // any datatye can be a key in ordered map 

key is the number and value is the frequency 
map takes less memory than that of hash as it 
just stores the elemets that are required 

it stores value in sorted order 
 */

/*
  in all cases the time complexity of the map is 
     O LOG(N)   - in all worst,best, average 
     N is nothing but number of elements in the map 


    
 */
int mainodered(){
    int n;
    cin>>n;
    int arr[n];
    map<int , int> mpp;
    for (int i=0;i<n;i++){
        cin>>arr[i];
        mpp[arr[i]]++; // precomputation 
    }
  //iterate in the map 
  for (auto it:mpp){
      cout<<it.first<<"->"<<it.second <<endl;
  }

  int q;
  cin>>q;
  while(q--){
      int number ;
      cin>>number;
      //fetch 
      cout<<mpp[number]<<endl;
  }

return 0;   
}



//unordered map 
/*
 only int , double,char,string can be the key her 
as the name says its unordered 

for best and average case the time complexity is 
   O(1) - for best and average 

   O(N) - for the worst case 
   the worst case happens because of internal collision 
   it happens very very less , when it happens we use ordered map 
   
   but generally we use unordered  map as it tc is less 
 
 */
int main(){
    int n;
    cin>>n;
    int arr[n];
    unordered_map<int , int> mpp;
    for (int i=0;i<n;i++){
        cin>>arr[i];
        mpp[arr[i]]++; // precomputation 
    }
  //iterate in the map 
  for (auto it:mpp){
      cout<<it.first<<"->"<<it.second <<endl;
  }

  int q;
  cin>>q;
  while(q--){
      int number ;
      cin>>number;
      //fetch 
      cout<<mpp[number]<<endl;
  }

return 0;   
}

/*
 hashing can't be done if arr[i], i >10^7

 we have 3 methods 
 - division method
 - folding method
 - mid square method
 The important one is Division method by using it we can change the 
 limit of the array 
  DIVISION METHOD 
 for example we have array arr [2,5,16,28,139] & i>=10 is not allowed
 we do is arr[i]%10 so we get[0 0 1 0 0 1 0 0 1 1]
                              0 1 2 3 4 5 6 7 8 9 
                    SO 139 is 1 time as 9 is 1 time 
            but for numbers with same reaminders we use linked list
            will get it soon (use the process of chaining )
            (chained in a sorted order )
 */

/*
 what is collision , how does it happen ?
 all of keys end up in the same hash index 
   
 */