import java.util.Scanner;

public class Factorial {
    public static void main(String[] args) {
        // Create a scanner object to read input
        Scanner scanner = new Scanner(System.in);

        // Prompt the user to enter an integer
        System.out.print("Enter a non-negative integer: ");
        int n = scanner.nextInt();

        // Calculate the factorial
        long result = factorial(n);

        // Print the result
        System.out.println("The factorial of " + n + " is " + result);

        // Close the scanner
        scanner.close();
    }

    // Function to calculate factorial
    public static long factorial(int n) {
        if (n == 0 || n == 1) {
            return 1;
        }
        long result = 1;
        for (int i = 2; i <= n; i++) {
            result *= i;
        }
        return result;
    }
}