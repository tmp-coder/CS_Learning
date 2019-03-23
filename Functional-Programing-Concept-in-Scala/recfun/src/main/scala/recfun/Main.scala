package recfun

object Main {
  def main(args: Array[String]) {
    println("Pascal's Triangle")
    for (row <- 0 to 10) {
      for (col <- 0 to row)
        print(pascal(col, row) + " ")
      println()
    }
  }

  /**
   * Exercise 1
   */
    def pascal(c: Int, r: Int): Int = {
        if(c==0 || r==c || r==0)1
        else pascal(c,r-1)+pascal(c-1,r-1)
    }
  
  /**
   * Exercise 2
   */
    def balance(chars: List[Char]): Boolean = {
        def fanBracket(back:Int,list: List[Char]):Int={
            if(list.isEmpty||back<0) back
            else if(list.head==')') fanBracket(back-1,list.tail)
            else fanBracket(back+(if (list.head=='(') 1 else 0),list.tail)

        }
        fanBracket(0,chars)==0
    }
  /**
   * Exercise 3
   */
    def countChange(money: Int, coins: List[Int]): Int = {
        if(coins.isEmpty){
            if(money==0)1
            else 0
        }else if(coins.head > money)countChange(money,coins.tail)
        else countChange(money-coins.head,coins)+countChange(money,coins.tail)
    }
  }
