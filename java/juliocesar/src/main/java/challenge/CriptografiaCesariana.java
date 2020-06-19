package challenge;

public class CriptografiaCesariana implements Criptografia {

    int quantidadeDeCaracteres = 0;
    String texto;
    int decimalDoCaractere;
    int decimalComSalto = 0;

    @Override
    public String criptografar(String texto) {

        texto = new String();
        quantidadeDeCaracteres = texto.length();

        try{
            verificaTextoValido(texto);

            for (int i = 0; i < quantidadeDeCaracteres; i++) {
                decimalDoCaractere = texto.toLowerCase().charAt(i);
                if (decimalDoCaractere > 96 && decimalDoCaractere < 120) {
                    decimalComSalto = decimalDoCaractere + 3; 
                }else if (decimalDoCaractere > 119) {
                    decimalComSalto = decimalDoCaractere - (26 - 3);
                } else {
                    decimalComSalto = decimalDoCaractere;
                }
                texto += (char) decimalComSalto;
            }
        }
        catch(Exception ex){
            
        }
        
        return texto;
    }

    @Override
    public String descriptografar(String texto) {

        texto = new String();
        quantidadeDeCaracteres = texto.length();

        try{
            verificaTextoValido(texto);

            for (int i = 0; i < quantidadeDeCaracteres; i++) {
                decimalDoCaractere = texto.toLowerCase().charAt(i);
                if (decimalDoCaractere > 99 && decimalDoCaractere < 122) {
                    decimalComSalto = decimalDoCaractere - 3; 
                }else if (decimalDoCaractere > 96 && decimalDoCaractere < 100) {
                    decimalComSalto = decimalDoCaractere + (26 - 3);
                } else {
                    decimalComSalto = decimalDoCaractere;
                }
                texto += (char) decimalComSalto;
            }
        }
        catch(Exception ex){
            
        }  
        return texto;
    }

    private void verificaTextoValido(String texto) throws Exception {
        if (texto.isEmpty()) {
            throw new Exception("O texto não pode estar vazio");
        }
    }
}
