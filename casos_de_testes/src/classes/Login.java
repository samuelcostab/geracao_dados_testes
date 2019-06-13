package classes;


import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Login {
	
	public boolean verificaQtdCaracteres(String entrada){
		if(entrada.length() == 8){
			return true;
		}
		return false;
	}

	public boolean verificaAlfaNumerico(String entrada){
		String rL = "[a-zA-Z]";
		Pattern padrao = Pattern.compile(rL);
		Matcher matcherLetra = padrao.matcher(entrada);
		if(matcherLetra.find()){
			String rN = "[0-9]";
			padrao = Pattern.compile(rN);
			Matcher matcherNumero = padrao.matcher(entrada);
			if(matcherNumero.find()){
				return true;
			}
			
		}


        return false;
        
	}

}
