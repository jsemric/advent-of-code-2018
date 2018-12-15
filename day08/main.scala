import scala.io._

object Advent8 {

    def makeTree(as: List[Int]): Tree = {
        def go(as: List[Int], nChilds: Int, nMeta: Int, childs: List[Tree]):
            (List[Int],Tree) =
        {
            if (nChilds > 0) {
                val (ls, tree) = go(as.drop(2), as(0), as(1), List())
                val res = go(ls, nChilds-1, nMeta, childs :+ tree)
                (res._1, res._2)
            } else {
                (as.drop(nMeta), Tree(childs,as.take(nMeta)))
            }
        }

        go(as.drop(2),as(0),as(1), List())._2
    }

    case class Tree(childs: List[Tree], meta: List[Int]) {

        def sum: Int =
            meta.foldLeft(0)(_+_) + childs.foldLeft(0)((a,b) => a+b.sum)

        def rootNumber: Int = {
            if (childs.isEmpty) meta.foldLeft(0)(_+_)
            else {
                val len = childs.length
                meta.filter(_ <= len).foldLeft(0)((a,b) =>
                    a + childs(b-1).rootNumber)
            }
        }
    }

    def main(args: Array[String]): Unit = {
        val line = StdIn.readLine().split(' ').map(_.toInt).toList
        val tree = makeTree(line)
        println(tree.sum)
        println(tree.rootNumber)
    }
}