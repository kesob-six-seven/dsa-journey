// the last 2 remaining hard patterns
 
#include <bits/stdc++.h>
using namespace std;
void fun(int n){
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){ //shit needs revision and practice
            if (i==0||j==0||i==n-1||j== n-1){
                cout<<"*";
            } else cout<<" ";
        }cout<<endl;
    }
    
}
void fun1(int n){
    for(int i=0;i<2*n-1;i++){
        for(int j=0;j<2*n-1;j++){
            int top=i;
            int left=j;      //shit needs revision and practice
            int  bottom=2*(n-1)-i;
            int right=2*(n-1)-j;
            cout<<(n-min(min(top,bottom),min(left,right)));
            
        }
        cout<<endl;
    }
    
}


int main(){
    int t;  //t is the test subject and runs it  
cin>>t;     //for the number of test time.
for(int i=0;i<t;i++){
    int n;
    cin>>n;
    fun1(n);
    
    
    
} return 0;}
    
   



