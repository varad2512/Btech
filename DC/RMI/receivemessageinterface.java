/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

package dcrmi;
import java.rmi.*;

public interface receivemessageinterface extends Remote {
    void receiveMessage(String x) throws RemoteException;
}
