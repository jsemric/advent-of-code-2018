import scala.io._

object Main {

    case class Rule(input: String, output: Char)

    def applyRules(state: List[Char], rules: Map[String,Char]): Char =
        rules.getOrElse(state.take(5).foldLeft("")(_+_),'.')

    def applyRulesLast4(state: List[Char], rules: Map[String,Char]):
        List[Char] =
    {
        def go(state: List[Char], n: Int): List[Char] = state match {
            case h::t => applyRules(state ++ List.fill(n)('.'),rules)::go(t,n+1)
            case _ => List()
        }
        go(state,1).reverse.dropWhile(_ == '.').reverse
    }

    def countPlants(ls: List[Char]) = {
        var i = -1
        ls.foldLeft(0)((a,b) => {i += 1; if(b == '#') a+i else a})
    }

    var idx = 0

    def nextState(state: List[Char], n: Int, rules: Map[String,Char], p: Int):
        Int =
    {
        def go(state: List[Char]): List[Char] = state match {
            case h::t if state.length < 5 => applyRulesLast4(state,rules)
            case h::t => applyRules(state,rules) :: go(t)
            case _ => List()
        }

        // killing purity
        idx +=  1
        val z = countPlants(state.drop(p)) -
            countPlants('.' :: state.take(p).reverse)
        println(s"${idx} ${z}")

        if (n > 0) {
            val rpad = Math.max(0,2-state.indexOf('#'))
            nextState(go(List.fill(rpad + 2)('.') ++ state),
                n-1, rules, p + rpad)
        }
        else {
            countPlants(state.drop(p)) -
                countPlants('.' :: state.take(p).reverse) 
        }
    }

    def main(args: Array[String]): Unit = {
        /*
        To solve the second part print first 500 results. The difference keeps
        repeating after some time. My result was 6346 + 55 * (N - 117), where
        N is 50000000000
        */
        val re = "initial state: (.*)".r
        val re(init) = StdIn.readLine

        var line = ""
        var rules = Map[String,Char]()
        while ({line = StdIn.readLine; line != null}) {
            if (line != "") {
                val tmp = line.split(" => ")
                rules = rules ++ Map(tmp(0) -> tmp(1)(0))
            }
        }
        val res = nextState(init.toCharArray.toList,500,rules,0)
    }
}