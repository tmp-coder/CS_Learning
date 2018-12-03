fun map(f,xs) =
    case xs of
       [] => []
     | x::xs' => f(x) ::map(f,xs')

fun filter(f,xs)=
    case xs of
       [] => []
     | x::xs' => if f x then x::(filter(f,xs'))
                 else filter(f,xs')

val x =1

fun f y =
    let
      val x = y +1
    in
      fn z => x +y +z
    end

fun f g =
    let
      val x = 3
    in
      g 2
    end

val x = 4

fun h y = x + y

val x = 3 
val z = f h