#### 1. Fundation

Code less, compile quicker, execute faster => have more fun!

##### 1.1 ENV
```
export GOROOT=$HOME/go
export GOBIN=$GOROOT/bin
export GOARCH=amd64
export GOOS=linux
export PATH=$GOBIN:$PATH

sudo apt-get install bison ed gawk gcc libc6-dev make
```

##### 1.2 Interacting with C
```
package rand

// #include <stdlib.h>
import “C”

func Random() int {
	return int(C.random())
}

func Seed(i int) {
	C.srandom(C.uint(i))
}
```

```
package print

// #include <stdio.h>
// #include <stdlib.h>
import “C”
import “unsafe”

func Print(s string) {
   cs := C.CString(s)
   defer C.free(unsafe.Pointer(cs))
   C.fputs(cs, (*C.FILE)(C.stdout))
}
```

##### 1.3 Basic constructs
Programs consist out of `keywords`, `constants`, `variables`, `operators`, `types` and `functions`.

*	`keywords`

```
break
default
func
interface
select case
defer
go
map
struct
chan
if else
goto
package
switch case
const
fallthrough
range
type
continue
for
import
return
var
```

*	`predeclared indetifiers`

```
append
bool
byte
cap
close
complex
complex64
complex128
unint
unit8
unit16
unit32
unit64
unintptr
copy
false
float32
float64
imag
int
int8
int16
int32
int64
iota
len
make
new
nil
panic
print
println
real
recover
sting
true
```

* `delimiters`

```
()
{}
[]
.
,
;
:
...
```

*	`types`

`Variables` (like `constants`) contain `data`, and `data` can be of different `data types`, or `types` for short. 

1.	elementary(primitive):`int`,`float`,`bool`,`string`
2. structured(composite):`struct`,`array`,`slice`,`map`,`channel`
3. interfaces: which only describe the behavior of a type



```
const (
	Sunday = iota //0
	Monday //1
	Tuesday //2
	Wednesday
	Thursday
	Friday
	Saturday
)
```

*	`var`

```
var identifier type

var a, b *int

var (
	a int
	b bool
	str string
)
```

```
var identifier [type] = value

var (
	a = 15
	b   = false
	str = “Go says hello to the world!”
	numShips = 50
	city string
)

var (
	HOME = os.Getenv(“HOME”)
	USER = os.Getenv(“USER”)
	GOROOT = os.Getenv(“GOROOT”)
)

```

*	initializing declaration(`:=`)

```
a, b, c := 5, 7, “abc”
```
It can only be used inside functions, not in package scope.


*	reference types(pointers)

```
slice
map
channel
```

The variables that are referenced are stored in the heap, which is garbage collected and which is a much larger memory space than the stack.

*	printing

```
fmt.Sprintf
fmt.Print
fmt.Println
```

*	`init()`

```
package trans
import “math”

var Pi float64
func init() {
	// init() function computes Pi
	Pi = 4 * math.Atan(1)
}

package main
import (
	“fmt”
	“./trans” )

var twoPi = 2 * trans.Pi
func main() {
	// 2*Pi = 6.283185307179586
	fmt.Printf(“2*Pi = %g\n”, twoPi)
}
```

```
 func init() {
	// setup preparations
	go backend()
}
```

*	`const`

```
type ByteSize float64
const (
	_ = iota  // ignore first value by assigning to blank identifier
	KB ByteSize = 1<<(10*iota)
	MB
	GB
	TB
	PB
	EB
	ZB
	YB
)

type BitFlag int
const (
	Active	BitFlag = 1 << iota // 1 << 0 == 1
	Send							// 1 << 1 == 2
	Receive						// 1 << 2 == 4
)

flag := Active | Send// == 3
```


*	`string`

```
strings.HasPrefix(s, prefix string) bool
strings.HasSuffix(s, suffix string) bool
strings.Contains(s, substr string) bool
strings.Index(s, str string) int
strings.LastIndex(s, str string) int
//If ch is a non-ASCII character
strings.IndexRune(s string, ch int) int
//if n = -1 all occurrences are replaced
strings.Replace(str, old, new, n)
strings.Count(s, str string) int
strings.Repeat(s, count int) string
strings.ToLower(s) string
strings.ToUpper(s) string
strings.TrimSpace(s)
strings.Trim(s, “cut”)
strings.Trim(s, “\r\n”)
strings.TrimLeft(s, “\r\n”)
strings.TrimRight(s, “\r\n”)
// split
strings.Fields(s)
strings.Split(s, sep)
Strings.Join(sl []string, sep string)
strings.NewReader(str)
```

*    [`strconv`](http://golang.org/pkg/strconv/)

```
strconv.IntSize
strconv.Itoa(i int) string
strconv.FormatFloat(f float64, fmt byte, prec int, bitSize int) string
strconv.Atoi(s string) (i int, err error)
strconv.ParseFloat(s string, bitSize int) (f float64, err error)
```

*    [Times and dates](http://golang.org/pkg/time/)

```
var t Time = time.Now()
t.Day()
t.Minute()
fmt.Printf(“%02d.%02d.%4d\n”, t.Day(), t.Month(), t.Year()) 
func (t Time) Format(layout string) string
fmt.Println(t.Format(“02 Jan 2006 15:04”)) // outputs now: 21 Jul 2011 10:31
// timestamp
time.Now().Unix()
// 
time.Parse()
```

*    Pointers


```
// 取地址(type modifier)
&
// 取值(dereference operator)
*
// 指针变量
var i1 = 5
fmt.Printf(“An integer: %d, it’s location in memory: %p\n”, i1, &i1)
var intP *int
// intP points to i1
// intP stores the memory address of i1; it points to the location of i1, it references the variable i1.
intP = &i1
//  * gives the value which the pointer is pointing to
*intP 
fmt.Printf(“The value at memory location %p is %d\n”, intP, *intP)
// ture
varType == *(&varType)
```

You cannot take the address of a literal or a constant.

```
const i = 5
ptr := &i //error: cannot take the address of i
ptr2 := &10 //error: cannot take the address of 10
c = *p++ // is invalid Go code!!没有指针运算,类似java等的reference
```

*    Control structures

```
if else
switch case
select //for the switching between channels 
for (range) // break,continue,return,goto
```

###### `if-else if-else`

```
if val := 10; val > max {
   // do something
}

if value := process(data); value > max {
    //...
}


// multiple returns
value, err := pack1.Function1(param1)
if err != nil {
    fmt.Printf(“An error occurred in pack1.Function1 with parameter %v”, param1)
    return err
    //os.Exit(1)
}
// normal case, continue execution:
```

###### `switch`
```
switch var1 {
    case val1: //
    case val2: //
    //case val3, val4, val5:
    default://
}
```

```
switch i {
     //empty case body, nothing is executed when i==0
    case 0:
    case 1:
        // f is not called when i==0!
        f() 
}
```

```
switch i {
    case 0: fallthrough
    case 1:
        // f is called when i==0!
        f()
}
```

###### `for`
```
for init; condition; modif { }
for condition { }
for ix, val := range coll { } //range
```

```
for i:=0; i<10; i++ {
    fmt.Printf(“%v\n”, i)
}
```

```
for i, j := 0, N; i < j; i, j = i+1, j-1 {}
```

```
i := 5
for i > 0 {
    i = i -1
    fmt.Printf(“The variable i is now: %d\n”, i)
}
```

```
// infinite loops
for i:=0; ; i++ {}
for { }
for ;; { }
```

```
for t, err = p.Token(); err == nil; t, err = p.Token() {}
```

```
for pos, char := range str { }
```

###### Functions
1.    Function overloading is not allowed in Go.
2.    Call by value / Call by reference

    ```
    funcName1(arg1)
    funcName2(&arg2)
    ```

3.    Reference types like `slices`, `maps`, `interfaces` and `channels` are pass by reference by default; but the default way in Go is to pass a variable as an argument to a function by value.
4.    Passing a variable number of parameters 
    
    ```
    func myFunc(a,b, arg ...int){}
    func Greeting(prefix string, who ...string)
    Greeting(“hello:”, “Joe”, “Anna”, “Eileen”)
    ```
    
5.    If the parameters are stored in an array `arr`, the function can be called with the parameter `arr...`

    ```
    func Min(a ...int) int {
        if len(a)==0 {
            return 0
        }
        min := a[0]
        for _, v := range a {
            if v < min {
                min = v
            }
        }
        return min
    }
    
    x := Min(1, 3, 2, 0)
    arr := []int{7,9,3,5,1}
    x = Min(arr...)    
    ```

6.    The variable number parameter can be passed as such or as a `slice` of its type.

    ```
    func F1(s ...string){
        F2(s)
        F3(s)
    }
    
    func F2(s ...string){}
    func F3(s []string){}
    ```
7.    以上4-6参数类型必须相同,否则需借用`struct`构造

    ```
    type Options struct {
        par1 type1,
        par2 type2,
        //...
    }
    F1(a, b, Options{})
    F1(a, b, Options{par1:val1, par2:val2})
    ```

8.    `interface {}`作为参数

    ```
    fund TypeCheck(.., .., values ... interface{}){
        for _, value := range values {
            switch v : value.(type) {
                case int: //
                case float: //
                case string: //
                case bool: //
                default: //
            }
        }
    }
    ```

9.    Defer and tracing
    +    The defer keyword allows us to postpone the execution of a statement or a function until the end of the enclosing (calling) function.

        ```
        // LIFO:the last defer is first executed, and so on
        // 4 3 2 1 0
        func f() {
            for i := 0; i < 5; i++ {
                defer fmt.Printf(“%d “, i)
           }
        }
        ```

    +    `defer` allows us to guarantee that certain clean-up tasks are performed before we return from a function
        
        ```
        // closing a file stream
        defer file.Close()
        // unlocking a locked resource (a mutex)
        mu.Lock()
        defer mu.Unlock()
        // printing a footer in a report
        printHeader()
        defer printFooter()
        // closing a database connection
        connectToDB()
        defer disconnectFromDB()
        ```
 
    +    Tracing with defer
    
        ```
        func trace(s string)   { fmt.Println(“entering:”, s) }
        func untrace(s string) { fmt.Println(“leaving:”, s) }
        ```
        
        ```
        package main
        import "fmt"
        func trace(s string) string {
            fmt.Println("entering:", s)
            return s
        }
        func un(s string) {
            fmt.Println("leaving:", s)
        }
        func a() {
            defer un(trace("a"))
            fmt.Println("in a")
        }
        func b() {
            defer un(trace("b"))
            fmt.Println("in b")
            a()
        }
        func main() {
            b()
        }
        ```
        
        ```
        func func1(s string) (n int, err error) {
            defer func() {
                log.Printf(“func1(%q) = %d, %v”, s, n, err)
             }()
            return 7, io.EOF
        }
        ```

10.    Built-in functions

    ```
    close
    //len gives the length of a number of types (strings, arrays, slices, maps, channels)
    len
    // cap is the capacity, the maximum storage (only applicable to slices and maps)
    cap
    // new for value types and user-defined types like structs,
    // new(T) allocates zeroed storage for a new item of type T and returns its address, a value of type *T
    // &T{}
    new
    // make for built-in reference types (slices, maps, channels)
    // make(T) returns an initialized value of type T
    make
    //  for copying and concatenating slices 
    copy
    append
    // for handling errors
    panic
    recover
    // fmt
    print
    println
    // complex numbers 
    complex
    real
    imag
    ```

11.    Recursive functions
    +    A function that call itself in its body is called recursive. 
    +    An important problem when using recursive functions is stack overflow, use `lazy evaluation`
    +    Mutually recursive functions can also be used in Go


12.    Functions as parameters

    ```
    package main
    import (
        "fmt"
    )
    func main() {
        callback(1, Add)
    }
    func Add(a,b int) {
        fmt.Printf("The sum of %d and %d is: %d\n", a, b, a+b)
    }
    func callback(y int, f func(int, int)) {
        f(y, 2)  // this becomes Add(1, 2)
    }
    ```


13.    Closures (function literals)(a lambda function, a function literal, or a closure)

    ```
    // lambda functions can be assigned to variables and treated as values.
    fplus := func(x, y int) int { return x + y }
    fplus(3,4)
    func(x, y int) int { return x + y } (3, 4)
    ```
    
    ```
    func() {
        sum = 0.0
        for i := 1; i<= 1e6; i++ {
            sum += i
        }
    }()
    ```


##### 1.4 Arrays and Slices

```
var identifier [len]type
var arr1 [5]int
var arr1 = new([5]int)
for i:=0; i < len(arr1); i++ {
    arr1[i]= ...
}


for i := range arr1 {
    // ...
}

// a copy of the array is made
func1(arr1)
func1(&arr1)
```

```
package main
import "fmt"

func f(a [3]int)   { fmt.Println(a) }
func fp(a *[3]int) { fmt.Println(a) }

func main() {
    var ar [3]int
    f(ar)   // passes a copy of ar
    fp(&ar) // passes a pointer to ar
}
``` 

1.    Passing an array to a function
    +    Pass a point to the array
    +    Use a slice of the array
    
    ```
    package main
    import "fmt"
    func main(){
        array := [3]float64{7.0,8.5,9.1}
        x := Sum(&array)
        fmt.Printf("Sum is: %f",x)
    }
    func Sum(a *[3]float64)(sum float64){
        for _, v := range a {
            sum += v
        }
        return 
    }
    ```
   
##### 1.５ Slices
+    Multiple slices can share data if they represent pieces of the same array; multiple arrays can never share data. 
+    slices are references
```
0 <= len(s) <= cap(s)
```
    
```
var identifier []type
var slice1 []type = arr1[start:end]
var slice2 []type = arr1[:]
last = slice1[:len(slice1)-1]
var x = []int{2, 3, 5, 7, 11}
```

+    Passing a slice to a function

    ```
    func sum(a []int) int {
        s := 0
        for i := 0; i < len(a); i++ {
            s += a[i]
        }
        return s
    }
    
    func main {
        var arr = [5]int{0,1,2,3,4}
        sum(arr[:])
    }
    ```
    
+    Creating a slice with `make()`

    ```
    var slice1 []type = make([]type, len)
    s2 := make([]int, 10)
    
    slice1 := make([]type, len, cap)
    make([]int, 50, 100)
    new([100]int)[0:50]
    ```
    
    ```
    var p *[]int = new([]int) // *p == nil; with len and cap 0
    p := new([]int) // 地址
    p := make([]int, 0)
    
    var v []int = make([]int, 10, 50)
    v := make([]int, 10, 50)
    ```
 
 +    The bytes package
 
     ```
     import "bytes"
     type Buffer struct {
         //
     }
     func NewBuffer(buf []byte) *Buffer {}
     var r *bytes.Buffer = new(bytes.Buffer)
     ```   
    
 +    `for range`
 
    ```
    for ix, value := range slice1 { 
         //
    }
     
    var b []byte
    var s string
    b = append(b, s...)

    // Strings are immutable. 
    s:=“hello”
    c:=[]byte(s)
    c[0]=’c’
    s2:= string(c) // s2 == “cello”
    ```   
 
+    [Searching and sorting slices and arrays](https://golang.org/pkg/sort/)  
    
    ```
    func Ints(a []int)
    func InsAreSorted(a []int) bool
    func Float64s(a []float64)
    func Strings(a []string)
    func SearchFloat64s(a []float64, x float64) int
    func SearchStrings(a []string, x string) int
    ```

+    `append`

    ```
    a = append(a, b...)
    b = make([]T, len(a))
    copy(b,a)
    // Delete item at index i
    a = append(a[:i], a[i+1:]...)
    a = append(a[:i], a[j:]...)
    a = append(a, make([]T, j)...)
    a = append(a[:i], append([]T{x},a[i:]...)...)
    a = append(a[:i], append(make([]T,j), a[i:]...)...)
    a = append(a[:i], append(b,a[i:]...)...)
    x, a = a[len(a)-1], a[:len(a)-1]
    a = append(a, x)
    ```  
    
##### 1.6 Maps

+    A map is a reference type 

```
var map1 map[keytype]valuetype
// e.g.
var map1 map[string]int
// assignment
map1[key1] = val1
// 
v:= map1[key1] 

mapCreated := make(map[string]float)
// or
mapCreated := map[string]float{}
// or a map pointer
mapCreated := new(map[string]float)

// the value can be any type
MapOfFunc := map[int]func() int {
    1: func() int {return 0},
    2: func() int {return 2},
    3: func() int {return 3},
}

//  map capacity
map2 := make(map[string]float, 100)
```
    
+     Slices as map values

    ```
    mp1 := make(map[int][]int)
    mp2 := make(map[int]*[]int)
    ``` 
    
+    exists or delete

    ```
    if _, ok := map1[key1]; ok {
        // ...
        delete(map1, key1)
    }
    ```  

+    `for range`

    ```
    // key and value
    for key, val := range map1{
        //
    }
    // only value
    for _, val := range map1 {
        //
    }
    // only key
    for key := range map1 {
        //
    }
    ```

+     A slice of maps

    ```
    items := make([]map[int]int, 5)
    for i := range items{
        items[i] = make(map[int]int, 1)
        items[i][1] = 2
    }
    fmt.Printf(“Version A: Value of items: %v\n”, items)
    ```
  
  
+     Sorting a map

    If you want a sorted map, copy the keys (or values) to a `slice`, sort the `slice` (using the `sort` package), and then print out the keys and/or values using a `for-range` on the `slice`.
  
    ```
    barVal = map[string]int{"a":31,"b":22,"c":43}
    for k, v := range barVal {
        fmt.Printf("Key: %v, Value: %v / ", k, v)
    }

    keys := make([]string, len(barVal))
    i := 0
    for k, _ := range barVal {
        keys[i] = k
        i++
    }
    sort.Strings(keys)
    for _, k := range keys {
        fmt.Printf("Key: %v, Value: %v / ", k, barVal[k])
    }
    ```
    
    ```
    type struct {
        key string
        value int
    }
    ```
    

#### 2. Packages
##### 2.1 [STL](https://golang.org/pkg/)   

```
os
os/exec
syscall
archive/tar
fmt
io
bufio
path/filepath
flag
strings
strconv
unicode
regexp
bytes
index/suffixarray
math
math/cmath
math/rand
sort
math/big
list
ring
time
log
encoding/json
encoding/xml
net
http
html
runtime
reflect
sync
```
    
    
```
import "sync"
type Info struct {
    mu sync.Mutex
    //
    Str string
}

func Update(info *Info) {
    info.mu.Lock()
    // critical section:
    info.Str = // new value
    // end critical section
    info.mu.Unlock()
}
```

```
type SyncedBuffer struct{
    lock sync.Mutex
    buffer bytes.Buffer
}
```

#### 3. Structs and Methods

```
type identifier struct {
    f1 type1
    f2 type2
    // ... 
}


type T struct { a, b int }
var s T
s.a = 5
s.b = 10

//  an instance or object of the type T
var t *T = new(T)
// or 
t := new(T)
```
   
```
type struct1 struct {
    i1   int
    f1   float32
    str  string
}

var v struct1 // v has struct type
var p *struct1 // p is a pointer to a struct 
v.i1
p.i1
//  ms is of type *struct1
ms := &struct1{10, 15.5, “Chris”}

var mt struct1
mt = struct1{10, 15.5, “Chris”}
``` 


```
// Linked List
type Node struct {
    data float64
    su *Node
}

// doubly linked list 
type Node struct {
    pr    *Node
    data  float64
    su    *Node
}

//  Tree
type Tree struct {
    le    *Tree
    data    float64
    ri    *Tree
}
```

###### 3.1 A factory for structs
Its name starts with `new` or `New`.

```
type File struct {
    fd int // file descriptor number
    name string // file name
}

fund NewFile(fd int, name string) *File{
    if fd < 0 {
        return nil
    }
    return &File{fd, name}
}

f := NewFile(10, “./test.txt”)
// If File is defined as a struct type
f1 := new(File)
f2 := &File{10, “./test.txt”}

// size
size := unsafe.Sizeof(T{})
```  
   
+    Forcing the use of the factory method and forbid using new and effectively making our type private.

    ```
    package matrix
    // 小写,私有
    type mat struct {}
    
    func NewMat(params) *mat {
        m := new(mat)
        // m is initialized
        return m
    }
    
    // in main package
    package main
    import "matrix"
    right := matrix.NewMatrix(...)
    ```

###### 3.2  Structs with tags
*    A field in a struct can, apart from a name and a type, also optionally have a tag.
*    The tag-content cannot be used in normal programming, only the package reflect can access it. 

```
package main
import (
    "fmt"
    "reflect"
)

type TagType struct { // tags
    f1 bool "An important answer"
    f2 string "The name of the thing"
    f3 int "How much there are"
}

func main(){
    tt := TagType{true,"nalfhahf",1}
    for i := 0; i<3, i++ {
        refTag(tt, i)
    }
}

func refTag(tt TagType, ix int){
    rtType := reflect.TypeOf(tt)
    ixFiled := rtType.Field(ix)
    fmt.Printf("%v\n", ixField.Tag)
}
```

###### 3.3 Anonymous fields and embedded structs
1.    用于继承或组合
2.    In Go composition is of favoured over inheritance.
3.    Anonymous (or embedded) fields, that is fields with no explicit name.

```
package main
import "fmt"

type innerS struct {
    in1    int
    in2    int
}

type outerS struct {
    b int
    c float32
    // anonymous field
    int
    // anonymous field
    innerS
}

func main() {
    outer := new(outerS)
    outer.b = 6
    outer.c = 7.5
    outer.int = 60
    outer.in1 = 5
    outer.in2 = 10
    // with a struct-literal:
    outer2 := outerS{6, 7.5, 60, innerS{5, 10}}
    fmt.Println("outer2 is: ", outer2)
}
```

###### 3.4 Confilcting names
1.    An outer name hides an inner name. This provides a way to override a field or method. 外层覆盖内层,需严格指定
2.    If the same name appears twice at the same level, it is an error if the name is used by the program. (If it’s not used, it doesn’t matter.) There are no rules to resolve the ambiguity; it　must be fixed.　尽量避免同层同名,需严格指定
   
###### 3.6 Methods

```
func (recv receiver_type) methodName(parameter_list) (return_value_list) { ... }
// invocation
// recv is like the this- or self- existing in OO-languages
recv.methodName()

// the method does not need to use the value recv
func (_ receiver_type) methodName(parameter_list) (return_value_list) { ... }

// Difference between a function and a method
// A function has the variable as a parameter
// A method is called on the variable
Function1(recv)
recv.Method1()
```

*    A Go method is a function that acts on variable of a certain type, called the `receiver`. So a method is a special kind of function.
*    The `receiver` type can be (almost) anything, not only a `struct` type: any type can have methods, even a function type or alias types for int, bool, string or array.
*    The `receiver` also cannot be an `interface` type, since an interface is the abstract definition and a method is the implementation. 不是是接口
*    Lastly it cannot be a pointer type, but it can be a pointer to any of the allowed types. 不能是指针类型,但可以是类型指针.
*    The combination of a (struct) type and its methods is the Go equivalent of a class in OO.可独立于不同文件,但需在同一个包中.
*    no method overloading没有同名方法重载,但基于接受者不同,可以重载

    ```
    func (a *denseMatrix) Add(b Matrix) Matrix
    func (a *sparseMatrix) Add(b Matrix) Matrix
    ```

*    Pointer or value as receiver
    +    `recv` is most often a pointer to the `receiver_type` for performance reasons (because we don’t make a copy of the instance, as would be the case with call by value)
    +    Define the method on a pointer type if you need the method to modify the data the receiver points to. Otherwise, it is often cleaner to define the method on a normal value type.
    
####  4. Interfaces and reflection
 
 
   
   
   
   
   
   
   
    
    
    
#### References
The way Go
