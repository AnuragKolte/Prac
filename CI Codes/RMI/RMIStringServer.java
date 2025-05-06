package RMI;
import java.rmi.*;
import java.rmi.registry.LocateRegistry;
import java.rmi.server.UnicastRemoteObject;

interface StringService extends Remote {
    String concatenate(String str1, String str2) throws RemoteException;
}

class StringServiceImpl extends UnicastRemoteObject implements StringService {
    protected StringServiceImpl() throws RemoteException {
        super();
    }

    @Override
    public String concatenate(String str1, String str2) throws RemoteException {
        return str1 + " " + str2;
    }
}

public class RMIStringServer {
    public static void main(String[] args) {
        try {
            LocateRegistry.createRegistry(1099);

            StringService obj = new StringServiceImpl();

            Naming.rebind("StringOperations", obj);

            System.out.println("Server is running...");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}