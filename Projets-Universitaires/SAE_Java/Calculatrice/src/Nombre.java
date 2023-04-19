public class Nombre extends Expression {
    private int valeurNombre;    //Attribut

    //  Constructeur

    public Nombre(int nombre){
        this.valeurNombre = nombre;
    }

    //  Methodes

    public int valeur() {
        return this.valeurNombre;
    }

    public String toString() {
        return ""+ this.valeurNombre +"";
    }


}
