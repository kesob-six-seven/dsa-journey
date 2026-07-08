#include<bits/stdc++.h>
using namespace std;
//this is shift 1
/*
 learning sort today 
 selction sort - select the minimum and swap it with the lowest index 
                then repeat until the array is sorted 
        swap at index 0 
        then at index 1 
        ...............
        till  index n-2
so the loop is going from 0 to n-2 ,
quite easy , yeah

how the swap works --
arr[i]     arr[min]

temp = arr[min]
arr[min] = arr[i]
arr [i] = temp(arr[min])

        */

void selection_sort(int arr[],int n){
    for(int i=0; i<=n-2;i++){
        int mini=i;
        for(int j=i;j<=n-1;j++){
            if(arr[j]<arr[mini]){
                mini=j;
            }
            int temp=arr[mini];
            arr[mini]=arr[i];
            arr[i]= temp;
        }
    }
}
  // its tc is n((n+1)/2)  =n^2/2+n/2 ---> n^2
  // so it is O(n^2)  


/*
 Bubble Sort - it pushes the maximum on the last by adjacent swapping 
 swaps-
 0 to n-1   if no swap is done for this then tc is O(n)
 0 to n-2
 ........
 0 to  01  

 the worst complexity is O(n^2)

 
 */
void bubblesort(int arr[], int n){
    int didswap=0;
    for(int i=n-1; i>=1;i--){
        for(int j=0;j<=i-1;j++){
            if (arr[j]>arr[j+1]){
                int temp =arr[j+1];
                arr[j+1] =arr[j];
                arr[j]= temp;
                didswap=1;
                
            }
        }
        if (didswap==0){
            break ;
        }
        cout<<"runs\n";
    }   
}

/*
inserion sort - takes an element & places it in its correct order 
    0 checks 
    +1 checks 
    +2 checks 
    ..........

    tc for avg and worst case O(n^2)
    the best case is O(n)
 */
void insertion_sort(int arr[],int n){
    
    for(int i=0;i<=n-1;i++){
        int j=i;
        while (j>0&& arr[j-1]>arr[j]){
            int temp =arr[j-1];
            arr[j-1]= arr[j];
            arr[j] =temp;
            j--;
        }
    }
}

int main(){
    int n;
    cin>>n;
    int arr[n];
    for(int i=0; i<n; i++) cin>>arr[i];
    bubblesort(arr,n);
    for(int i=0; i<n; i++){
        cout<<arr[i]<<" ";
    }

    return 0;
}