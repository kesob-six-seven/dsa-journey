//all the  remaining patterns i have studied 
 
#include <bits/stdc++.h>
using namespace std;
void fun(int n){
    int start =1;
    for (int i=0;i<n;i++){
        if (i%2==0) start=1;
        else start=0;
        for(int j=0;j<=i;j++){
            cout<<start;
            start=1-start;//this does all the flipping part 0101010
        }
        cout<<endl;
    }
    
}
void fun1(int n){
     int space = 2 * (n - 1);
    for (int i=1; i<=n;i++){
        //number 
      for(int j=1;j<=i;j++){
          cout<<j;
      }
        //space
    for (int j=1;j<=space;j++){
        cout<<"-";
    }
       //numbers
       for(int j=i;j>=1;j--){
           cout<<j;
       }
        cout<<endl;
        space =space-2;
    }
}
void fun2(int n){
    int count=1;
    for(int i=1;i<=n;i++){
        for(int j=1;j<=i; j++){
            cout<<count<<" ";
            count =count+1;
        }
        cout <<endl;
    }
    
}
void fun3(int n){
    for(int i=0;i<n;i++){
        for(char ch='A';ch<='A'+i;ch++){
            cout<<ch<<" ";
        }
        cout<<endl;
    }
}
void fun4(int n){
    for(int i=0;i<n;i++){
        for(char ch='A';ch<='A'+(n-i-1);ch++){
            cout<<ch<<" ";
        }
        cout<<endl;
    }
}
void fun5(int n){
    for(int i=0;i<n;i++){
       char ch='A'+i;
        for(int j=0;j<=i;j++){
            cout<<ch<<"";
        }cout<<endl;
    }
}
void fun6(int n){
    for(int i=0;i<n;i++){  //need fucking revision
        //space
        for(int j=0;j<(n-i-1);j++){
            cout<<"-";}
          //alpahbets
          char ch ='A';
          for(int j=0;j<2*i+1;j++){

              cout<<ch;
              if (j<(2*i+1)/2)
                  ch++;
              else ch--;
          }
          
            
            //space
            for(int j=0;j<(n-i-1);j++){
                cout<<"-";
        } cout<<endl;
    }
    
}
void fun7(int n){
    for(int i=0;i<n;i++){
        for(char ch='E'-i;ch<='E';ch++){
            cout<<ch<<" ";}cout<<endl;
    } ;
}
void fun8(int n){
     for(int i=0;i<n;i++){
         //stars 
     for(int j=1;j<=n-i;j++){        //not even looked at the aoltion he heheee
         cout<<"*";}
     
    //spaces
     for(int j=0;j<2*i;j++){
         cout<<"-";
     }
     //stars 
     for(int j=1;j<=n-i;j++){
     cout<<"*";
 } cout<<endl;}
      for (int i=1;i<=n;i++) {
          //stars
          for(int j=0;j<i;j++){
            cout<<"*";
          }
         //spaces
       for(int j=0;j<2*n-2*(i);j++)
        {cout<<"-";}
         
     //     //stars
          for(int j=0;j<i;j++){
              cout<<"*";
      } cout <<endl; }
}
void fun9(int n){
    int spaces =2*n-2;
    for(int i=1;i<=2*n-1;i++){
        int stars =i;
        if(i>n) stars =2*n-i;
        //stars 
        for(int j=1;j<=stars; j++){
            cout<<"*";}
            //spaces
            for(int j=1;j<=spaces;j++){
                cout<<"-";
            }

            //stars 
            for(int j=1;j<=stars; j++){
                cout<<"*";
        }
            cout<<endl;
            if(i<n)spaces-=2;
            else spaces +=2;
    }
}

int main(){
    int t;  //t is the test subject and runs it  
cin>>t;     //for the number of test time.
for(int i=0;i<t;i++){
    int n;
    cin>>n;
    fun9(n)
    ;
}}
    