//all the patterns i have studied 
// code 1 for pattern of square 
#include <bits/stdc++.h>
using namespace std;
void fun(int n){
    for (int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            cout<<"* ";
        }
        cout<<endl;
    }
}
void fun1(int n){
    for (int i =0;i<n;i++){
        for (int j=0;j<=i;j++){
            cout<<"* ";
        } cout<<endl;
    }
}
void fun2(int n){
    for (int i =1;i<=n;i++){
        for (int j=1;j<=i;j++){
            cout<<j;
        } cout<<endl;
    }
}
void fun3(int n){
    for (int i =1;i<=n;i++){
        for (int j=1;j<=i;j++){
            cout<<i<<" ";
        } cout<<endl;
    }
}
void fun4(int n){
    for (int i =1;i<=n;i++){
        for (int j=0;j<n-i+1;j++){
            cout<<"* ";
        } cout<<endl;
    }
}
void fun5(int n){
    for (int i =1;i<=n;i++){
        for (int j=1;j<=n-i+1;j++){
            cout<<j<<" ";
        } cout<<endl;
    }
}
void fun6(int n){
    for (int i =0;i<n;i++){
        for (int j=0;j<n-i-1;j++){
            cout<<" ";
        }
        
          for(int j=0;j<2*i+1;j++){
                cout<<"*";
            }
          for (int j=0;j<n-i-1;j++){
              cout<<" ";
          }
          cout<<endl;
    }
}
void fun7(int n){
    for (int i =0;i<n;i++){
        for (int j=0;j<i;j++){
            cout<<" ";
        }
        
          for(int j=0;j<2*n-(2*i+1);j++){
                cout<<"*";
            }
          for (int j=0;j<i;j++){
              cout<<" ";
          }
          cout<<endl;
    }
}
//pattern 9 was just a mix of function fun6,fun 7 just print them one by one 
 void fun9(int n){
     for(int i=1;i<=2*n-1;i++)
         {int stars =i;
             if (i>n) stars =2*n-i;
             for (int j=1;j<=stars; j++){
             cout<<"*";
             
         }cout <<endl;
      } 
}
int main(){
    int t;  //t is the test subject and runs it  
cin>>t;     //for the number of test time.
for(int i=0;i<t;i++){
    int n;
    cin>>n;
    fun9(n);
    
   
}
return 0;}