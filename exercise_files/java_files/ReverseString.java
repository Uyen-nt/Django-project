public class ReverseString {
    public static String reverse(String input) {
        StringBuilder reversed = new StringBuilder(input);
        return reversed.reverse().toString();
    }

    public static void main(String[] args) {
        String input = "hello";
        String result = reverse(input);
        System.out.println(result); // Output: olleh
    }
}