name := course.value + "-" + assignment.value

scalaVersion := "2.12.7"

scalacOptions ++= Seq("-deprecation")

// grading libraries
libraryDependencies += "junit" % "junit" % "4.10" % Test

// for funsets
libraryDependencies += "org.scala-lang.modules" %% "scala-parser-combinators" % "1.0.6"

// include the common dir
commonSourcePackages += "common"

courseId := "bRPXgjY9EeW6RApRXdjJPw"

