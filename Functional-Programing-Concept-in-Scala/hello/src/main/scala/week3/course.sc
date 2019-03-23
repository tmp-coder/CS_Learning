abstract class IntSet{
  def incl(x:Int):IntSet
  def contains(x:Int):Boolean
}

class Empty extends IntSet{
  override def incl(x: Int) = ???

  override def contains(x: Int) = false
}

class NonEmpty(ele:Int,left:IntSet,right:IntSet) extends IntSet{
  override def incl(x: Int) = ???

  override def contains(x: Int) = ???
}

val x = null
val tmp:Int = null
val s :String = x

