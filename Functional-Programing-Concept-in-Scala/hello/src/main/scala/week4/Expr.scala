package week4

trait Expr{
  def numValue : Int
  def leftOp:Expr
  def rightOp:Expr
}

case class Number(n:Int) extends Expr{

  override def numValue = n

  override def leftOp = throw new NoSuchElementException("Number.leftOP")

  override def rightOp = throw new NoSuchElementException("Number.rightOP")
}

case class Sum(e1:Expr,e2:Expr) extends Expr {

  override def leftOp = e1

  override def rightOp = e2

  override def numValue = throw new NoSuchElementException("sum.numValue")

}
