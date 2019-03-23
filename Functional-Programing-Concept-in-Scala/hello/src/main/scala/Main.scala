import week4._

object Main extends App {

    def eval(e:Expr):Int = e match {
        case Number(n) => n
        case Sum(e1,e2) => eval(e1)+eval(e2)
    }
    def show(e:Expr):String = e match {
        case Number(n) => String.valueOf(n)
        case Sum(e1,e2) =>show(e1)+'+'+show(e2)
    }

    val expr = new Sum(new Number(3),new Sum(new Number(2),new Number(4)))
    val a = eval(expr)
    println(show(expr))
}
