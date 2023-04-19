public class Addition extends Operation{

    //Constructeur

    public Addition(Expression nb1, Expression nb2){
        super(nb1,nb2);
    }

    //Methodes

    public int valeur() {
        return this.getOperande1().valeur() + this.getOperande2().valeur();
    }

    public String toString() {
        return "(" + this.getOperande1() +" + "+ this.getOperande2() + ")";
    }
}
