/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package ventanastc;

import com.mysql.jdbc.Connection;
import javax.swing.JOptionPane;
import java.sql.DriverManager;
import java.sql.*;

/**
 *
 * @author PC05
 */
public class Conexion {
    Connection conectar=null;
public Connection conectar (){
    try{
        Class.forName ("com.mysql.jdbc.Driver");
        conectar=(Connection) DriverManager.getConnection ("jdbc:mysql://localhost/cheersct","root","");
        JOptionPane.showMessageDialog(null, "Conexión exitosa", "conexión", JOptionPane.INFORMATION_MESSAGE);
    }catch (ClassNotFoundException| SQLException e) {
        JOptionPane.showMessageDialog(null, "Sin conexion"+e, "conexion", JOptionPane.ERROR_MESSAGE);
    }
return conectar;
}

}
    
    
        

