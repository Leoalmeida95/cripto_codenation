package br.com.codenation.desafioexe;

import java.util.ArrayList;
import java.util.List;

public class DesafioApplication {

	private static Integer tamanho = 350; 

	static int calcula(int n) {
		int F = 0;     // atual
        int ant = 0;   // anterior
  
        for (int i = 1; i <= n; i++) {
            if (i == 1) {
                F = 1;
                ant = 0;
            } else {
                F += ant;
                ant = F - ant;
            }
        }
  
        return F;
    }

	public static List<Integer> fibonacci() {

		List<Integer> lista = new ArrayList<Integer>();
		int resultado = 0;
		int i = 0;	
		while(resultado < tamanho){
			resultado = calcula(i);
			lista.add(resultado);
			i++;
		}
		
		return lista;
	}

	public static Boolean isFibonacci(Integer a) {
		List<Integer> lista = fibonacci();
		return lista.contains(a);
	}
}