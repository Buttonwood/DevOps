#### Goroutines and Channels
1.	Goroutines are like threads, but use far less memory and require less code to use.
2.	Channels are data structures that let you send typed messages between goroutines with synchronization built in. 

```
func log(msg string){
	//... some logging code here
}

// Elsewhere in our code after we've discovered an error.
go log("something dire happened")
```

#### 不定参数
1.	`... type` 表示具有不定个type类型的参数		
2.	变量中所有参数的类别必须是同一种	
3.	不定参数实质上是一个slice类型，故可以使用range对其参数进行取值

```
func myfunc(args ... int){
	for _, arg := range args {
		fmt.Println(arg)
	}
}
```


#### 构造函数
1.	go语言中没有构造函数的概念，对象的构建通常交给一个全局构建函数来构建，通常以`NewXXX`来命名，表示构造函数

```
func NewRect(x, y, width, height float64) *Rect {
    return &Rect{x, y, width, height}
}
```

#### 多个返回值
允许多个返回值，并且返回值有两种形式，一种只是指定类型，还有一种指定返回值名称

```
// 指定类型
func SumAndProduct(a, b int) (int, int) {
    return a+b, a*b
}
  
// 指定返回值名称
// 当定义函数时指定返回参数变量(名称)时，可以直接返回而不用带变量名
// 如果命令的返回参数跟函数代码块中的变量同名，会被隐藏，此时需显示return返回结果
// 建议使用不指定返回值名称的形式
func SumAndProduct(a, b int) (add int, Multiplied int) {
    add = a + b;
    Multiplied = a * b;
    return
}
```

#### 先执行`defer`语句，然后才执行`return`语句
1.	可以利用这个来进行资源安全关闭，解加锁，记录执行情况等
2.	`defer`是采用先进后出的模式的，这种情形与栈的情况一致


#### `import`
```
// 最常用的一种形式
import "fmt"

// 导入同一目录下test包中的内容
import "./test"

// 导入fmt，并给他启别名f，用于同名冲突
import f "fmt"

// 将fmt启用别名"."，这样就可以直接使用其内容
import . "fmt"

// 当import时就执行了fmt包中的init函数，而不能够使用该包的其他函数
import  _ "fmt"
```
All `init` functions in any code file that are part of the program will get called before
the `main` function.

```
// init is called prior to main.
func init() {
	// Change the device for logging to stdout.
	log.SetOutput(os.Stdout)
}
```



#### `setter` and `getter`
```
// getter
owner := obj.Owner()
if owner != user {
	// setter
    obj.SetOwner(user)
}
```

#### Interface 
1.	Interfaces allow you to express the behavior of a type. If a value of a type implements
an interface, it means the value has a specific set of behaviors. 数据类型实现接口之后,该类型数据用用了一些行为.
2.	If your type implements the methods of an interface, a value of your type can be stored in a value of that interface type. No special declarations are required.

```
Reader, Writer, Formatter, CloseNotifier
```

```
type Reader interface {
	Read(p []byte) (n int, err error)
}
```

#### exported or unexported identifiers
1.	An exported identifier can be directly accessed by code in other packages when the respective
package is imported. These identifiers start with a capital letter. 首字母大写
2.	Unexported identifiers start with a lowercase letter and can’t be directly accessed by code in other packages. 首字母小写
3.	A function can return a value of an unexported type and this value is accessible by any calling function, even if the calling function has been declared in a different package.




```
// 错误检查
go vet
// 格式化
go fmt
// 文档
go doc
```


####  Array, Slice, Map
```
// 一旦声明，类型和长度不得改变
var arr1 [5]int

// 声明并初始化
arr2 := [5]int{10, 20, 30, 40, 50}

// ... 根据初始化列表自动计算长度
arr3 := [...]int{10, 20, 30, 40, 50}

// 特别指定元素初值,前提是知道长度,其他为默认值
arr4 := [5]int{1: 10, 2: 20}

//
arr4[2] = 35

// An array of pointers that point to integers
parr := [5]*int{0:new(int), 1: new(int)}
*parr[0] = 10
*parr[1] = 20

var array1 [3]*string

array2 := [3]*string{new(string), new(string), new(string)}

*array2[0] = "Red"
*array2[1] = "Blue"
*array2[2] = "Green"

array1 = array2


var array1 [4][2]int

array2 := [4][2]int{{10, 11}, {20, 21}, {30, 31}, {40, 41}}

array3 := [4][2]int{1: {20, 21}, 3: {40, 41}}

array4 := [4][2]int{1: {0: 20}, 3: {1: 41}}
```

Passing a large array by pointer between functions
```
// Allocate an array of 8 megabytes.
var array [1e6]int

// Pass the address of the array to the function foo.
foo(&array)

// Function foo accepts a pointer to an array of one million integers.
func foo(array *[1e6]int) {
	//...
}
```


##### Slice
```
slice := make([]string, 5)

// length=3, capacity=5
slice := make([]int, 3, 5)

slice := []string{"Red", "Blue", "Green", "Yellow", "Pink"}

// Initialize the 100th element with an empty string.
slice := []string{99: ""}

// Create a nil slice of integers.
var slice []int

// Use make to create an empty slice of integers.
slice := make([]int, 0)

// Use a slice literal to create an empty slice of integers.
slice := []int{}

slice := []int{10, 20, 30, 40}
newSlice := append(slice, 50)
```

```
For slice[i:j:k] or [2:3:4]
Length: j - i or 3 - 2 = 1
Capacity: k - i or 4 - 2 = 2

source := []string{"Apple", "Orange", "Plum", "Banana", "Grape"}
slice := source[2:3:3]
slice = append(slice, "Kiwi")
```

```
slice := [][]int{{10}, {100, 200}}
slice[0] = append(slice[0], 20)

slice := make([]int , 1000000)

slice = foo(slice)

func foo(slice []int) []int {
	return slice
}
```

##### Map
1.	The map key can be a value from any built-in or struct type as long as the value can be used in an expression with the `==` operator. 
2. Slices, functions, and struct types that contain slices can’t be used as map keys. 
3. Passing a map between two functions doesn’t make a copy of the map.
4. The built-in function `len` can be used to retrieve the length of a slice or map.
5. The built-in function `cap` only works on slices.


```
dict := make(map[string]int)
dict := map[string]string{"Red": "#da1337", "Orange": "#e95a22"}

// Create a map using a slice of strings as the value.
dict := map[int][]string{}

colors := map[string]string{}
colors["Red"] = "#da1337"
```

```
// Create a nil map by just declaring the map.
var colors map[string]string

// Retrieve the value for the key "Blue".
value, exists := colors["Blue"]
// Did this key exist?
if exists {
    fmt.Println(value)
}
```


```
// Create a map of colors and color hex codes.
colors := map[string]string{
    "AliceBlue":   "#f0f8ff",
    "Coral":       "#ff7F50",
    "DarkGray":    "#a9a9a9",
    "ForestGreen": "#228b22",
}

// Remove the key/value pair for the key "Coral".
delete(colors, "Coral")

// Display all the colors in the map.
for key, value := range colors {
    fmt.Printf("Key: %s  Value: %s\n", key, value)
}
```

#### User-defined types
```
type user struct {
	name	string
	email	string
	ext		int
	privileged	bool
}

var bill user
```

```
// Declare a variable of type user and initialize all the fields.
lisa := user {
	name:	"Lisa",
	email:	"",
	ext: 123,
	privileged: true,
}
```

Creating a struct type value using a struct literal
```
user {
	name:	"Lisa",
	email:	"",
	ext: 123,
	privileged: true,
}

// Creating a struct type value without declaring the field names
lisa := user{"Lisa", "lisa@email.com", 123, true}
```


If you specify a value inside the `[ ]` operator, you’re creating an array. If
you don’t specify a value, you’re creating a slice.


http://play.golang.org

http://golang.org/pkg/fmt/
http://golang.org/pkg/strings/
