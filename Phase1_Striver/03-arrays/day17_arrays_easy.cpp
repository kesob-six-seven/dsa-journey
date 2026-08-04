#include<bits/stdc++.h>
using namespace std;
/* 
array inside the main max size -10^6
outside the main is -10^7  
 Today im gonna start with array problmes (easy)
 */


//largest elemet of the array 
int largestElement(vector<int>& nums) {
        if(nums.empty()){return -1;}
        int largest =nums[0];       
        for(int i=0;i<nums.size();i++){
            if ( nums[i]>largest){
           largest =nums[i];}
        }
        return largest;


} 

//second largest
int secondLargestElement(vector<int>& nums) {
       if (nums.size()<2){return-1;}
       int largest=INT_MIN;    
       int second=INT_MIN;
       for(int i=0;i<nums.size();i++){
           if (nums[i]>largest){
               second =largest;
               largest=nums[i];
           }
           else if (nums[i]<largest&&nums[i]>second){
               second=nums[i];
           }
       }
       if (second==INT_MIN){
           return -1;
       }
     return second;
  
} 

//check if array is sorted and shifted 
bool check(vector<int>& nums) {
       int n =nums.size();
        int breaks=0;
     for (int i=0;i<n;i++){
     if (nums[i]>nums[(i+1)%n])
     breaks ++;
     }
     return breaks<=1;

}


//remove duplicates
int removeDuplicates(vector<int>& nums) {
        int n = nums.size();
        int i = 0;

        for (int j = 1; j < n; j++) {
            if (nums[j] != nums[i]) {
                i++;
                nums[i] = nums[j];
            }
        }

        return i + 1;
   
}