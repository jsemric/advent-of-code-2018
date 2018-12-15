import scala.io._
import scala.collection.mutable.Map

object Advent7 {

    def resolve(as: scala.collection.Map[
        Char,scala.collection.immutable.Set[Char]]): List[Char] =
    {
        if (as.isEmpty) List()
        else {
            val n = as.filter(_._2.isEmpty).keySet.toList.sorted.head
            n :: resolve(as.filter(_._1 != n).mapValues(_ - n))
        }
    }

    def resolveTime(as: scala.collection.Map[
        Char,scala.collection.immutable.Set[Char]], n: Int = 5,
        t: Int = 60): Int =
    {
        def min(l: List[(Char,Int)]): Int = 
            l.map(_._2).foldLeft(l(0)._2)(Math.min (_,_))

        @annotation.tailrec
        def go(as: scala.collection.Map[
            Char,scala.collection.immutable.Set[Char]],
            workers: List[(Char,Int)], acc: Int): Int = 
        {
            var tmp = workers

            if (as.isEmpty) {
                acc + workers.map(_._2).foldLeft(0)(Math.max (_,_))
            } else {
                val m = n - workers.length
                val noDeps = as.filter(_._2.isEmpty).keySet.toList.sorted
                    .take(m)
                tmp ++= noDeps.map(a => (a, t + a.toInt - 64))
                val min_ = min(tmp)
                tmp = tmp.map(a => (a._1, a._2- min_))
                val resolved = tmp.filter(_._2 == 0).map(_._1)
                go(as.filter(a => !noDeps.contains(a._1))
                    .mapValues(_ -- resolved), tmp.filter(_._2 > 0), acc + min_)
            }
        }

        go(as, List(), 0)
    }

    def main(args: Array[String]): Unit = {
        val pattern =
            "Step ([A-Z]) must be finished before step ([A-Z]) can begin.".r

        var m: Map[Char,List[Char]] = Map()
        var line: String = ""

        while ({line = StdIn.readLine(); line != null}) {
            val pattern(a,b) = line
            val k: Char = b(0)
            val v: Char = a(0)
            m += (k -> (v :: m.getOrElse(k, List())))
            if (!m.contains(v)) {
                m += (v -> List())
            }
        }

        val res1 = resolve(m.mapValues(_.toSet))
        println("First answer: " + res1.foldLeft("")(_+_))

        val res2 = resolveTime(m.mapValues(_.toSet),5,60)
        println("Second answer: " + res2)
    }
}