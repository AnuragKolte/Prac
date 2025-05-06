package Hotel_Booking;

import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.util.Scanner;

public class HotelClient {
    public static void main(String[] args) {
        try {
            Registry registry = LocateRegistry.getRegistry("localhost", 1099);
            HotelInterface stub = (HotelInterface) registry.lookup("HotelService");

            Scanner sc = new Scanner(System.in);
            while (true) {
                System.out.println("\nHotel Booking System");
                System.out.println("1. Book Room");
                System.out.println("2. Cancel Booking");
                System.out.println("3. Exit");
                System.out.print("Enter your choice: ");
                int choice = sc.nextInt();
                sc.nextLine(); // consume newline

                switch (choice) {
                    case 1:
                        System.out.print("Enter guest name: ");
                        String name1 = sc.nextLine();
                        System.out.println(stub.bookRoom(name1));
                        break;
                    case 2:
                        System.out.print("Enter guest name: ");
                        String name2 = sc.nextLine();
                        System.out.println(stub.cancelBooking(name2));
                        break;
                    case 3:
                        System.out.println("Thank you!");
                        return;
                    default:
                        System.out.println("Invalid choice!");
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
