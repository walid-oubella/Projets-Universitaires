public class Division extends Operation {

    //Constructeur

    public Division(Expression nb1, Expression nb2) {
        super(nb1, nb2);
    }
    //Methodes

    public int valeur() {
        int d = 0;
        try {
            d = this.getOperande1().valeur() / this.getOperande2().valeur();
        } catch (ArithmeticException e) {
            System.out.println("Division impossible, il y a une erreur "+e.toString());
        }
        return d;
    }
    public String toString() {
        return "(" + this.getOperande1() +" / "+ this.getOperande2() + ")";
    }
}
