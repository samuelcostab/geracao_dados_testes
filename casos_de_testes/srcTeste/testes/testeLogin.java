package teste;

import classes.Login;
import junit.framework.TestCase; 

public class testeLogin extends TestCase {
 
	    Login login = new Login();  
	  
	    public void testQtdCaracteres(){  
	    	assertEquals(true , login.verificaQtdCaracteres("AAAAAAAA"));
	    } 
	    
	    public void testAlfaNumerico(){  
	    	assertEquals(true , login.verificaAlfaNumerico("C12B123"));
	    }
	      
	   
	  
}
