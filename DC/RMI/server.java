

package dcrmi;
import java.rmi.*;
import java.rmi.registry.*;
import java.rmi.server.*;
import java.net.*;


public class server extends java.rmi.server.UnicastRemoteObject implements receivemessageinterface
{
    int      thisPort;
    String   thisAddress;
    Registry registry; 
    
     public void receiveMessage(String x) throws RemoteException
    {
        System.out.println(x);
    }
     
        public server() throws RemoteException
    {
        try{
           
            thisAddress="127.0.0.1";
            System.out.println(thisAddress);
        }
        catch(Exception e){
            throw new RemoteException("can't get inet address.");
        }
        thisPort=3232;  
        System.out.println("this address="+thisAddress+",port="+thisPort);
        try{
        
        registry = LocateRegistry.createRegistry( thisPort );
            registry.rebind("rmiServer", this);
        }
        catch(RemoteException e){
        throw e;
        }
    }
         static public void main(String args[])
    {
        try{
            server s=new server();
    }
    catch (Exception e) {
           e.printStackTrace();
           System.exit(1);
    }
     }
}
