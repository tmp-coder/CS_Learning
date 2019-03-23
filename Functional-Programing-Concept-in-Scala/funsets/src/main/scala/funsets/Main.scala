package funsets

object Main extends App {
  import FunSets._
  println(contains(singletonSet(1), 1))
  println(exists({x:Int=>x%2==0},{ele2:Int =>ele2==3}))
}
