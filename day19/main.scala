import scala.io._
import scala.language.implicitConversions

object Main {

    implicit def bool2int(b:Boolean) = if (b) 1 else 0

    // instructions
    val insMap = Map[String,(Int, Int, Array[Int]) => Int](
        "addr" ->
        ((op1: Int, op2: Int, regs: Array[Int]) => regs(op1) + regs(op2)),
        "addi" ->
        ((op1: Int, op2: Int, regs: Array[Int]) => regs(op1) + op2),
        "mulr" ->
        ((op1: Int, op2: Int, regs: Array[Int]) => regs(op1) * regs(op2)),
        "muli" ->
        ((op1: Int, op2: Int, regs: Array[Int]) => regs(op1) * op2),
        "setr" ->
        ((op1: Int, op2: Int, regs: Array[Int]) => regs(op1)),
        "seti" ->
        ((op1: Int, op2: Int, regs: Array[Int]) => op1),
        "banr" ->
        ((op1: Int, op2: Int, regs: Array[Int]) => regs(op1) & regs(op2)),
        "bani" ->
        ((op1: Int, op2: Int, regs: Array[Int]) => regs(op1) & op2),
        "borr" ->
        ((op1: Int, op2: Int, regs: Array[Int]) => regs(op1) | regs(op2)),
        "bori" ->
        ((op1: Int, op2: Int, regs: Array[Int]) => regs(op1) | op2),
        "gtir" ->
        ((op1: Int, op2: Int, regs: Array[Int]) => op1 > regs(op2)),
        "gtrr" ->
        ((op1: Int, op2: Int, regs: Array[Int]) => regs(op1) > regs(op2)),
        "gtri" ->
        ((op1: Int, op2: Int, regs: Array[Int]) => regs(op1) > op2),
        "eqir" ->
        ((op1: Int, op2: Int, regs: Array[Int]) => op1 == regs(op2)),
        "eqrr" ->
        ((op1: Int, op2: Int, regs: Array[Int]) => regs(op1) == regs(op2)),
        "eqri" ->
        ((op1: Int, op2: Int, regs: Array[Int]) => regs(op1) > op2)
    )

    case class Instr(ins: String, op1: Int, op2: Int, op3: Int)

    def main(args: Array[String]): Unit = {
        val pattern = "#ip (\\w)".r
        val pattern(ipStr) = StdIn.readLine
        val ip = ipStr.toInt

        var line = ""
        var input = List[Instr]()
        while ({line = StdIn.readLine; line != null}) {
            val x = line.split(' ')
            input = input :+ Instr(x(0),x(1).toInt,x(2).toInt,x(3).toInt)
        }
        
        val program = input.toArray
        var finished = false
        var regs = Array.fill(6)(0)
        regs.update(0,1)

        while (! finished) {

            if (regs(ip) >= program.size)
                finished = true
            else {
                // println(program(regs(ip)) + " " + regs.toList)
                val ins = program(regs(ip))
                val f = insMap.get(ins.ins).get
                regs.update(ins.op3,f(ins.op1,ins.op2,regs))
                regs.update(ip,regs(ip)+1)
            }
            // println(regs.toList)
        }

        println(regs.toList)
    }
}