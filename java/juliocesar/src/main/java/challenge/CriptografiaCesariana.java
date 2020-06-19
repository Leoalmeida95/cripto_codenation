package challenge;

public class CriptografiaCesariana implements Criptografia {

    int quantidadeDeCaracteres = 0;
    String resultado;
    int decimalDoCaractere;
    int decimalComSalto = 0;

    @Override
    public String criptografar(String texto) {

        verificaTextoValido(texto);
        resultado = new String();
        quantidadeDeCaracteres = texto.length();

        for (int i = 0; i < quantidadeDeCaracteres; i++) {
            decimalDoCaractere = texto.toLowerCase().charAt(i);
            if (decimalDoCaractere > 96 && decimalDoCaractere < 120) {
                decimalComSalto = decimalDoCaractere + 3; 
            }else if (decimalDoCaractere > 119) {
                decimalComSalto = decimalDoCaractere - (26 - 3);
            } else {
                decimalComSalto = decimalDoCaractere;
            }
            resultado += (char) decimalComSalto;
        }

        return resultado;
    }

    @Override
    public String descriptografar(String texto) {

        verificaTextoValido(texto);
        resultado = new String();
        quantidadeDeCaracteres = texto.length();

        for (int i = 0; i < quantidadeDeCaracteres; i++) {
            decimalDoCaractere = texto.toLowerCase().charAt(i);
            if (decimalDoCaractere > 99 && decimalDoCaractere < 122) {
                decimalComSalto = decimalDoCaractere - 3; 
            }else if (decimalDoCaractere > 96 && decimalDoCaractere < 100) {
                decimalComSalto = decimalDoCaractere + (26 - 3);
            } else {
                decimalComSalto = decimalDoCaractere;
            }
            resultado += (char) decimalComSalto;
        }

        return resultado;
    }

    private void verificaTextoValido(String texto) {
        if (texto.isEmpty() || texto == null) {
            throw new IllegalArgumentException("O texto não pode estar vazio");
        }
    }
}
