#include<bits/stdc++.h>
using namespace std;

//this is shift 2 im doing recursson
void recursion(){
    cout<<"recurring"<<endl;
    recursion();
}

//2nd example 
int rec() {
    int count = 0; 
    if (count == 4) {
        return count;
    } else {
        count++;
        return rec(); 
    }
}

//print Name N times using recursiom
 void rec1(int i,int n){
     if (i>n){
         return;
     }
     else {
         i++;
         cout<<"kesob"<<endl;
          rec1(i,n);
     }
    
}//tc is O(n) and sc is same as well

//print linearly from one to n
void rec2(int i,int n){
    if (i>n){
        return;
    }
    else {
        cout<<i<<endl;
        i++;
         rec2(i,n);
    }
}

//print from N to one
void rec3(int i,int n){
    if (i<1){
        return;}
    else{
        cout<<i<<endl;
        i--; 
   rec3(i,n);}
}

//basic BackTracking 
//print line executes first 
// the last guy gets executed first
void backrec(int i,int n){
    if (i<1){
        return;}
    else{
        backrec(i-1,n);
        cout<<i<<endl;
    }
    
}//need revision 
//2nd back track from n to i
void backtec2(int i,int n){
    if (i>n){
        return ;
    }
    else {
        backtec2(i+1,n);
        cout<<i<<endl;
    }
}//need revision


int main(){
    int i=1;
    int n;
    cin>>n;
    backtec2(i,n);
    return 0;
}