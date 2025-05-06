package RMI;

import java.rmi.Naming;
import java.util.Scanner;

public class RMIStringClient {
    public static void main(String[] args) {
        try {
            StringService stringService = (StringService) Naming.lookup("rmi://localhost:1099/StringOperations");

            Scanner sc = new Scanner(System.in);
            System.out.print("Enter the first string: ");
            String str1 = sc.nextLine();
            System.out.print("Enter the second string: ");
            String str2 = sc.nextLine();

            System.out.println("Concatenated string: " + stringService.concatenate(str1, str2));

            sc.close();
        } catch (Exception e) {
            System.out.println("Error: " + e);
        }
    }
}