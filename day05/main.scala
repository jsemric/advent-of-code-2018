object Advent5 {
    def reduce(s: String): String = {

        def reacts(a: Char, b: Char): Boolean = 
            Math.abs(a - b) == 32 

        @annotation.tailrec
        def go(input: List[Char], stack: List[Char]): List[Char] = {
            (input,stack) match {
                case (h1::t1, h2::t2) if reacts(h1,h2) => go(t1,t2)
                case (h1::t1, _) => go(t1,h1::stack)
                case (_,_) => stack
            }
        }
        go(s.toList,List[Char]()).foldLeft("")((a,b) => b+a)
    }



    def main(args: Array[String]): Unit = {
        val line = scala.io.StdIn.readLine()
        val result = reduce(line)

        println(s"First answer: ${result.length}")

        var min = 10000000

        // just try all possibilities and find minimal length
        for (i <- 'a' until '{') {
            val a = result.replaceAll(s"(?i)${i}","")
            val l = reduce(a).length
            if (min > l) min = l
        }

        println(s"Second answer: ${min}")
    }
}