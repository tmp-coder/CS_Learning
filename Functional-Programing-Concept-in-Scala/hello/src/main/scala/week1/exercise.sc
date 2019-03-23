import scala.annotation.tailrec

def  fac(n:Int):Int={
    @tailrec
    def reduce(acc:Int,n:Int):Int={
        if(n==0)acc
        else reduce(acc*n,n-1)
    }
    reduce(1,n)
}

fac(5)