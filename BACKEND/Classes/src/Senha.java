public class Senha {
    private int idSenha;
    private boolean prioritaria;
    private boolean senhaAtendida;


    public void gerarSenha(){};

    public int getIdSenha() {
        return idSenha;
    }

    public void setIdSenha(int idSenha) {
        this.idSenha = idSenha;
    }

    public boolean isPrioritaria() {
        return prioritaria;
    }

    public void setPrioritaria(boolean prioritaria) {
        this.prioritaria = prioritaria;
    }

    public boolean isSenhaAtendida() {
        return senhaAtendida;
    }

    public void setSenhaAtendida(boolean senhaAtendida) {
        this.senhaAtendida = senhaAtendida;
    }
}
