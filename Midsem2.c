#include <stdio.h>

int main() {
    printf("Prime numbers between 1 and 50 are:\n");
    
    for (int num = 2; num <= 50; num++) {
        int isPrime = 1; 
        
        
        for (int i = 2; i <= num / 2; i++) {
            if (num % i == 0) {
                isPrime = 0; 
                break;
            }
        }
        
        
        if (isPrime == 1) {
            printf("%d ", num);
        }
    }
    printf("\n");
    return 0;
}