### GC
```
sys.runtime.gc()

val runtime = sys.runtime
val free = runtime.freeMemory()
val total = runtime.totalMemory()
```

### Variables
*	`val` (`final` in java); once initialized, can never be ressigned
* 	`var` can be ressigned

```
val hello: String = "Hello world"
var world = "Hello world"
```

### Basic Types

|Type|Bits|
|---|:--:|
Byte|8-bit
Short|16-bit
Int|32-bit
Long|64-bit
Char|16-bit
String|Chars
Float|32-bit
Double|64-bit
Boolean|true/false

![](https://docs.scala-lang.org/resources/images/tour/unified-types-diagram.svg)

*	`Any` is the supertype of all types.
	*	equals()
	* 	hashCode()
	*  toString()

*	`AnyVal` represents value types. 
	*	Double
	* 	Float
	*	Long
	*	Int
	* 	Short
	*	Byte
	* 	Char
	* 	Int
	* 	Boolean 	

*	`Unit` is a value type which carries no meaningful information. `()`

*	`AnyRef` represents reference types. All non-value types are defined as reference types. Every user-defined type in Scala is a subtype of `AnyRef`.

```
val list: List[Any] = List(
	"a string",
	111,
	'c',
	true,
	() => "an anonymous function returning a string"
)

list.foreach(ele => prinln(ele))
```

#### Type Casting
![](https://docs.scala-lang.org/resources/images/tour/type-casting-diagram.svg)

### Loops
#### `while`
```
var idx = 0
while(idx < args.length){
	println(args(idx))
}
```

#### `foreach`
```
args.foreach(arg => prinln(arg))
args.foreach((arg: String) => prinln(arg))
args.foreach(println)
```

#### `for`
```
for(arg <- args)
	println(arg)
```

### Collections
```
scala.collection.mutable
scala.collention.immutable

scala.collection.IndexedSeq[T]
scala.collection.mutable.IndexedSeq[T]
scala.collention.immutable.IndexedSeq[T]
```

![](https://docs.scala-lang.org/resources/images/collections.png)

![immutable](https://docs.scala-lang.org/resources/images/collections.immutable.png)

![mutable](https://docs.scala-lang.org/resources/images/collections.mutable.png)

```
Traversable(1,2,3)
Iterable("x","y","z")
Map("x" -> 24, "y" -> 25, "z" -> 26)
Set(Color.red, Color.green, Color.blue)
SortedSer("aaa","abc")
Buffer(x,y,z)
IndexedSeq(1.0, 2.0)
LinearSeq(a, b, c)
List(1,2,3)
HashMap(a,b,c)
```

### Arrays
*	A mutable sequence of objects that all share the same type

```
val greetStrings = new Array[String](3)
// val greetStrings: Array[String] = new Array[String](3)

greetStrings(0) = "Hello"
greetStrings(1) = ","
greetStrings(2) = "world"
// greetStings.update(2,"world\n")

for(i <- 0 to 2)
	print(greetStrings(i))
	
val numNames = Array("zero","one","two")
val numNames = Array.apply("zero","one","two")
```

### Trait Traversable

```
def froeach[U](f: Elem => U)
```

```
++

// map
map
flatMap
collect

// Conversions
toArray
toList
toItereable
toSeq
toIndexedSeq
toStream
toSet
toMap

// copy 
copyToBuffer
copyToArray

// size info
isEmpty
nonEmpty
size
hasDefiniteSize

// element retrieval
head
last
headOption
lastOption
find

// sub-collention retrieval operations
tail
init
slice
take
drop
takeWhile
dropWhile
filter
filterNot
withFilter

// subdivsion 
splitAt
span
partition
groupBy

// Element tests
exists
forall
count

// Folds
foldLeft
foldRight
/:
:\
reduceLeft
reduceRight

// specific folds
sum
product
min
max

// String
mkString
addString
stringPredix

// view
view 
```

### Trait Iterable
```
def foreach[U](f: Elem => U): Uint = {
	val it = iterator
	while(it.hashNext)
		f(it.next())
}

xs.iterator
xs grouped size
xs sliding size

xs takeRight n
xs dropRight n

xs zip yx
xs zipAll(ys,x,y)
xs zipWithIndex
xs sameElements ys

List(1,2,3).sliding(3).next()(2)

List("a","b","c") zip List(1,2,3) //List((a,1), (b,2), (c,3))
List("a","b","c") zipAll (List(1,2),0,1) //List((a,1), (b,2), (c,1))
List("a","b","c") zipAll (List(1,2,3,4),0,1) //List((a,1), (b,2), (c,3), (0,4))
```

### Seq/IndexedSeq/LinearSeq
```
// indexing
xs(i)
xs apply i
xs isDefinedAt i
xs.length
xs lengthCompare n
xs.indices

// index search
xs indexOf x
xs lastIndexOf x
xs indexOfSlice ys
xs lastIndexOfSlice yx
xs indexWhere p
xs segmentLength(p,i)
xs prefixLength p

// additions
x +: xs
xs :+ x
xs padTo (len,x)

// updates
xs patch (i, ys, r)
xs updated (i,x)
xs(i) = x

// sorting
xs.sorted
xs sortWith lt
xs sortBy f

// Reversals
xs.reverse
xs.reverseIterator
xs reverseMap f

// Comparisons
xs startsWith ys
xs endsWith ys
xs contains x
xs containsSlice ys
(xs corresponds ys)(p)

// multiset 
xs intersect ys
xs diff ys
xs union ys
xs.distinct 
```

### Lists
*	An immutable sequence of objects that all share the same type(Java List can be mutable)

```
val one = List(1,2)
val two = List(3,4)
val three = one ::: two //(1,2,3,4)
val four = 0 :: three //(0,1,2,3,4)
val five = 0 :: 1 :: 2 :: Nil

five.count(a => a > 1)
five.dropRight(2)
five.drop(2)
five.exists()
five.forall()
five.filter()
five.foreach()
five.head
five.tail
five.init
five.isEmpty
five.last
five.length
five.map()
five.mkString(",")
five.reverse
five.sort((s,t) => s > t)
```

### Vectors
```
val vec = scala.collection.immutable.Vector.empty
val vec2 = vec :+ 1 :+ 2
val vec3 = 100 +: vec2

val vec4 = Vector(1,2,3)
vec4 updated (2,4)
```

### Tuples
*	immutable
* 	can containe different types of elements

```
val pair = (99, "Tom")
println(pair._1)
println(pair._2)
```


### Sets and Maps
*	 Can be mutable and imutable

```
// mutable Set
import scala.collection.mutable

var testSet = Set("Apple","Amzon")
testSet += "Google"
prinln(testSet.contains("Facebook"))
println(testSet)

// immutable HashSet
import scala.collection.immutable.HashSet
val hashSet = HashSet("Apple","Google")
println(hashSet + "Amazon")
```

```
// mutable Map
import scala.collection.mutable
val aMap = mutable.Map[Int, String]()
aMap += (1 -> "Apple")
aMap += (2 -> "Google")
aMap += (3 -> "Amazon")
println(aMap(2))
```

*	immutable is the default map

```
val bMap = Map(
	1 -> "Apple",
	2 -> "Google",
	3 -> "Amazon"
)
println(bMap(2))
```

```
val x = new HashMap[Int, String]()
val x: Map[Int, String] = new HashMap()
```

```
// lookups
ms get k
ms(k)
ms getOrElse(k,d)
ms contains k
ms isDefinedAt k

// additions and updates
ms + (k->v)
ms + (k->v,l->w)
ms ++ kvs
ms updated(k,v)

// removals
ms - k
ms - (k,l,m)
ms -- ks

// subcollections
ms.keys
ms.keySet
ms.keysIterator
ms.values
ms.valuesIterator

// transformation
ms filterKeys p
ms mapValues f
```

### IO
```
import scala.io.Source

val file = args(0)

for(line <- Source.fromFile(file)).getLines())
	// line.length
	println(line)

val lines = Source.fromFile(file)).getLines().toList
```

### References
*	https://docs.scala-lang.org/overviews/collections/introduction.html
