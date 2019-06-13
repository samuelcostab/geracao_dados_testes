package teste;

import classes.Senha;
import junit.framework.TestCase; 


public class testeSenha extends TestCase {
	
	Senha senha = new Senha();
	
	public void testQtdCaracteres(){  
    	assertEquals(true , senha.verificaQtdCaracteres("AAAAA"));
    } 
    
    public void testAlfaNumerico(){  
    	assertEquals(true , senha.verificaAlfaNumerico("1S3NH4"));
    }
	
	

}
