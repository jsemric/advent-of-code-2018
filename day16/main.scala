import scala.language.implicitConversions
import scala.io._

object Main {

    // https://stackoverflow.com/questions/2633719/is-there-an-easy-way-to-
    // convert-a-boolean-to-an-integer
    implicit def bool2int(b:Boolean) = if (b) 1 else 0

    // instructions
    val insList = List[(List[Int], List[Int]) => Int](
        // addr
        (a: List[Int], b: List[Int]) => b(a(1)) + b(a(2)),
        // addi
        (a: List[Int], b: List[Int]) => b(a(1)) + a(2),
        // mulr
        (a: List[Int], b: List[Int]) => b(a(1)) * b(a(2)),
        // muli
        (a: List[Int], b: List[Int]) => b(a(1)) * a(2),
        // setr
        (a: List[Int], b: List[Int]) => b(a(1)),
        // addi
        (a: List[Int], b: List[Int]) => a(1),
        // banr
        (a: List[Int], b: List[Int]) => b(a(1)) & b(a(2)),
        // bani
        (a: List[Int], b: List[Int]) => b(a(1)) & a(2),
        // borr
        (a: List[Int], b: List[Int]) => b(a(1)) | b(a(2)),
        // bori
        (a: List[Int], b: List[Int]) => b(a(1)) | a(2),
        // gt
        (a: List[Int], b: List[Int]) => a(1) > b(a(2)),
        (a: List[Int], b: List[Int]) => b(a(1)) > b(a(2)),
        (a: List[Int], b: List[Int]) => b(a(1)) > a(2),
        // equal
        (a: List[Int], b: List[Int]) => a(1) == b(a(2)),
        (a: List[Int], b: List[Int]) => b(a(1)) == b(a(2)),
        (a: List[Int], b: List[Int]) => b(a(1)) == a(2)
    )

    // perform the instruction and save the result
    def doInstr(ins: List[Int], regs: List[Int])
        (f: (List[Int], List[Int]) => Int): List[Int] =
        regs.patch(ins(3),Seq(f(ins, regs)),1)


    // simple parsing of instructions and registers
    def parseSeq(s: String): List[Int] =
        s.replaceAll("[^\\d]"," ").trim.split(" ").filter(_ != "").map(_.toInt)
            .toList

    case class BeforeAfter(before: List[Int], ins: List[Int], after: List[Int])

    // Warning: no exception/error handling
    def readTask1(): List[BeforeAfter] = {
        val beforeStr = StdIn.readLine
        if (!beforeStr.startsWith("Before")) return List()
        val before = parseSeq(beforeStr)
        val ins = parseSeq(StdIn.readLine)
        val after = parseSeq(StdIn.readLine)
        StdIn.readLine
        BeforeAfter(before, ins, after) :: readTask1()
    }

    // compare the results from all instructions to the after state
    def checkIns(ba: BeforeAfter): Set[Int] = {
        var i = -1
        insList.foldLeft(Set[Int]())((a,b) => {
            i += 1
            if (doInstr(ba.ins, ba.before)(b) == ba.after) a + i
            else a
        })
    }

    def resolveOpcodes(m: Map[Int,Set[Int]]): Map[Int,Set[Int]] = {
        val ones = m.filter(_._2.size == 1)
        if (ones.isEmpty) return m
        val drop = ones.foldLeft(Set[Int]())((a,b) => (b._2 ++ a))
        ones ++ resolveOpcodes(m.filterKeys(!ones.contains(_))
            .mapValues(_ -- drop))
    }

    def main(args: Array[String]): Unit = {
        val t = readTask1()
        val m = t.map(a => (a.ins(0),checkIns(a)))
        val answer1 = m.foldLeft(0)((a,b) => a + (b._2.size > 2))
        println("Answer 1: " + answer1)

        // Part 2
        // resolving opcodes using map and sets
        val defVal = List.range(0,16).toSet
        var res = m.foldLeft(Map[Int,Set[Int]]())((a,b) =>
                a ++ Map(b._1 -> (a.getOrElse(b._1,defVal) & b._2)))

        val resolved = resolveOpcodes(res)
        val isResolved = resolved.foldLeft(true)((a,b) => a && b._2.size == 1)

        if (isResolved) {

            // read and execute the instructions the ugly imperative way
            val opcodes = resolved.mapValues(_.head)
            var regs = List(0,0,0,0)
            var line = ""

            while ({line = StdIn.readLine; line != null}) {
                if (line != "") {
                    val ins = parseSeq(line)
                    regs = doInstr(ins, regs)(insList(opcodes.getOrElse(
                        ins(0),-1)))
                }
            } 

            println("Answer 2: " + regs(0))
        } else {
            println("Error: opcodes have not been resolved")
        }
    }
}