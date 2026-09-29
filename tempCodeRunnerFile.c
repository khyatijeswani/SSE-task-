#include <stdio.h>

// Function prototype
int riskScore(int n);

int main() {
    int n;
    
    printf("Enter the input value (n): ");
    if (scanf("%d", &n) != 1) {
        printf("Invalid input.\n");
        return 1;
    }
    
    // Call the recursive function
    int score = riskScore(n);
    
    // Output evaluation based on the given criteria
    if (score < 0) {
        printf("Risky\n");
    } else if (score >= 0 && score < 50) {
        printf("Moderate\n");
    } else if (score >= 50) {
        printf("Safe\n");
    }
    
    return 0;
}

// Recursive function definition
int riskScore(int n) {
    // PLACEHOLDER: Replace this logic with the specific recursive rules of your problem
    // Example: base case
    if (n <= 0) {
        return 0;
    }
    // Example: recursive step
    return n + riskScore(n - 1);
}
