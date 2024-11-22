import java.util.Scanner;

public class SquareNumber {
    public static void main(String[] args) {
        // Create a Scanner object to read input
        Scanner scanner = new Scanner(System.in);
        
        // Prompt the user to enter an integer
        System.out.print("Enter an integer: ");
        
        // Read the integer input
        int number = scanner.nextInt();
        
        // Calculate the square of the number
        int square = number * number;
        
        // Output the square of the number
        System.out.println("The square of " + number + " is " + square);
        
        // Close the scanner to avoid resource leak
        scanner.close();
    }
}