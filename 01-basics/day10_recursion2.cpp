#include<bits/stdc++.h>
using namespace std;

//sum of first N numbers 
//1.parameterised 
void re (int i, int sum){
    if(i<1){
        cout<<sum;
        return;
    }
    else {
        re(i-1,sum+i);
    }
    
}

//functional recurssion 
  int re1(int i){
    if (i==0) {return  0;} 
      return i+ re1(i-1);
}

//in fundtonal  factorial of n 
// tc is O(n), sc(N)
int re2(int i){
    if (i==0)
        return 1;
    else return (i)*re2(i-1); 
    
}

//reversing an arry 
void rev(int l, int r, int a[]) {
    if (l >= r) return;
    swap(a[l], a[r]);
    rev(l + 1, r - 1, a);
}//revison 

// doing sam e with one variable 
void rev1(int i, int arr[], int n) {
    if (i >= n / 2) return;
    swap(arr[i], arr[n - i - 1]);
    rev1(i + 1, arr, n);
}//revison 

//main for array problem 
// int main() {
//      int n;
//      cin>>n;
//      int arr[n];
//      for(int i=0;i<n;i++)cin>>arr[i];
//      rev1(0, arr, n );  
//      for(int i=0;i<n;i++)cout<<arr[i]<<" ";
//      return 0;
// }


// check if the string is palindrome or not
bool palin(int i,string s){
    if (i>=s.size()/2) return true ;//true is 1 
    if (s[i]!=s[s.size()-i-1]) return false;//false is 0
    return palin(i+1,s);
    
}//revison



int main(){
    string s="madsam";
    cout<<palin(0,s);
    return 0;
}