public abstract class Operation extends Expression {
    public Expression operande1;
    public Expression operande2;

    // Constructeur

    public Operation(Expression nb1, Expression nb2){
        this.operande1 = nb1;
        this.operande2 = nb2;
    }

    // Methodes

    public abstract int valeur();

    public Expression getOperande1() {
        return this.operande1;
    }
    public Expression getOperande2() {
        return this.operande2;
    }

}
