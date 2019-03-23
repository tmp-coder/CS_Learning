import math.abs
import math.sin

val tol = .0001

def isCloseEnough(x:Double,y:Double)=
    abs(1 - x/y) < tol

def fixedPoint(f:Double=>Double) = {
    def iterate(guess:Double):Double={
        val next = f(guess)
        if (isCloseEnough(guess,next)) next
        else iterate(next)
    }
    val firstGuess=1.0
    iterate(firstGuess)
}

fixedPoint(x=>sin(x))


def aveDamp(f:Double=>Double)(x:Double)=
    (x+f(x))/2

def sqrt(x:Double)= fixedPoint(aveDamp(y=>x/y))

sqrt(2)


