#include<bits/stdc++.h>

using namespace std;
//im gonna complete whole basic maths lets fucking go
//1.Digits
// extraction of diigts in reverse fashion
// n%10, then n/10 till n=0 , use while loop
//this code for count of digits 
int count (int n){
    int cnt=0;
    while(n>0){
        int lastdigit=n%10;//this just gives last didit no need in prob
        cnt =cnt++;
        n=n/10;
    }
    return cnt;
}//also can be used (int)(log10(n)+1) as count
//2nd reverse of a number
int reversenumber(int x){
    long long revnum=0;
    while(x!=0){
        int ld=x%10;
        revnum =(revnum *10)+ld;
        x=x/10;
    }//there was an int min int max if but it  was not in video 
    return revnum;
}
//3rd palindrome no
bool isPalindrome(int x) {
        if (x < 0) {
            return false;
        }
       int dupe =x;
       
        long long revnum =0;
        while (x!=0){
            int ls=x%10;
            revnum=(revnum*10)+ls;
            x=x/10;
        }
        return (revnum == dupe);
      }
//ARMSTRONG NO 
 int armstrong(int x){
    int dup=x;
    int num=0;
while (x!=0){
    int ls=x%10;
    num=num+(ls*ls*ls);
    x=x/10;
    }
if(num==dup) return true;
else return false;

}
//print all divisors