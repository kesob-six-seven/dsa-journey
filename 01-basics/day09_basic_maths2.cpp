#include<bits/stdc++.h>
using namespace std;
//print all divisors this is shift 1
void alldiv(int n){
   for (int i=1;i<=n;i++){
         if (n%i ==0){
          cout<<i<<" ";}
   }
}//all are connected to this 
void alldiv1(int n){
        vector<int>vec;
        for(int i=1;i*i<=n;i++){
            if (n%i ==0){
                cout<<i<<" ";
                if (n/i!=i){ 
                   vec.push_back(n/i);
                }
            }
        }
        sort (vec.begin(),vec.end());
        for(auto it:vec)cout<<it<<" ";
    
    //tc for this is 
    // O(num of factors )+log(num of factors):n is number of factor
}//this is flagged for revision 
//check for prime numbers
// -exactly 2 factors 1 and itself 
void primeno(int n){
    int count = 0;
    for(int i = 1; i * i <= n; i++){
        if (n % i == 0){
            count++;
            if((n / i) != i) {
                count++;
            }
        }
    }
    if (count == 2) {
        cout << "is prime ";
    } else {
        cout << "not prime";
    }
}

//gcd  (gretest commom divisor )
//OR
//Highest Common Divisor 
void gcd(int n1, int n2){
    
    for (int i=min(n1,n2);i>=1;i--){
        if (n1%i==0 && n2%i==0){
            cout<<i<<" ";
            break;//this breaks it from the outer loop
        }
    }    
}

//Euclidean algorithm
//gcd(a,b)=gcd (a-b,b) the greater is a 
// it can be furthur done the movement one no becomes
//  zero the other no is the gcd
// gcd(a,b)=(a%b,b)    the logic is 
// [greater % smaller] 
void eqgcd(int a ,int b){
 while (a>0&&b>0){
     if(a>b){
         a=a%b;
     }
     else{
         b=b%a;
     }
 }
if (a==0){
    cout<<"gcd = "<<b;
} 
else {cout<<"gcd = "<<a;}
    
}


int main(){
    int a, b;
    cin >>a>>b;
    eqgcd(a,b);
    
    
}