import java.time.LocalDateTime;

public class Atendimento {
    private int idAtendimento;
    private LocalDateTime comecoAtendimento;
    private LocalDateTime finalAtendimento;
    private int guiche;
    private String tipoAtendimento;
    private boolean preferencial;

    public void abrirAtendimento(){};

    public void encerrarAtendimento(){};


    public int getIdAtendimento() {
        return idAtendimento;
    }

    public void setIdAtendimento(int idAtendimento) {
        this.idAtendimento = idAtendimento;
    }

    public LocalDateTime getComecoAtendimento() {
        return comecoAtendimento;
    }

    public void setComecoAtendimento(LocalDateTime comecoAtendimento) {
        this.comecoAtendimento = comecoAtendimento;
    }

    public LocalDateTime getFinalAtendimento() {
        return finalAtendimento;
    }

    public void setFinalAtendimento(LocalDateTime finalAtendimento) {
        this.finalAtendimento = finalAtendimento;
    }

    public int getGuiche() {
        return guiche;
    }

    public void setGuiche(int guiche) {
        this.guiche = guiche;
    }

    public String getTipoAtendimento() {
        return tipoAtendimento;
    }

    public void setTipoAtendimento(String tipoAtendimento) {
        this.tipoAtendimento = tipoAtendimento;
    }

    public boolean isPreferencial() {
        return preferencial;
    }

    public void setPreferencial(boolean preferencial) {
        this.preferencial = preferencial;
    }
}
