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

If you specify a value inside the `[ ]` operator, you’re creating an array. If
you don’t specify a value, you’re creating a slice.

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

```
// admin represents an admin user with privileges.
type admin struct {
	person	user
	level	string
}

// Declare a variable of type admin
fred := admin {
	person: user{
		name: "Lisa",
		email: "lisa@email.com",
		ext: 123,
		privileged: true,
	},
	level: "super",
}
```


#### Mdethods
1.	Methods provide a way to add behavior to user-defined types.
2.	The parameter between the keyword `func` and the function name is called a `receiver` and binds the function to the specified type.
3.	When a function has a `receiver`, that function is called a `method`.
4.	`value receiver`传值拷贝,返回新值; `pointer receiver`传地址指向,改变值

```
type user struct {
	name 	string
	email	string
}

// notify implements a method with a value receiver
func (u user) notify(){
	fmt.Printf("Sending User Email To %s<%s>\n", u.name, u.email)
}

// changeEmail implements a method with a pointer receiver
func (u *user) changeEmail(email string){
	u.email = email
}

func main(){
	bill := user{"Bill","bill@msn.com"}
	bill.notify()

	lisa := &user{"Lisa", "lisa@email.com"}
	lisa.notify()
	//(*lisa).notify()

	bill.changeEmail("bill@newdomain.com")
	bill.notify()

	lisa.changeEmail("lisa@comcast.com")
	lisa.notify()
	//(&bill).notify()
}
```

#### Reference types
1.	Reference types in Go are the set of slice, map, channel, interface, and function types.

```
type IP []byte

func (ip IP) MarshalText() ([]byte, error) {
	if len(ip) == 0 {
		return []byte(""), nil
	}
	if len(ip) != IPv4len && len(ip) != IPv6len{
		return nil, errors.New("Invalid IP address")
	}
	return []byte(ip.String()), nil
}

func ipEmptyString(ip IP) string{
	if len(ip) == 0 {
		return ""
	}
	return ip.String()
}
```

####  package
1.	包内访问,小写开头的type/interface/func等(private)
2.	包外访问,大写开头的type/interface/func等(public)


#### Concurrency
1.	Parallelism is about doing a lot of things at once.
2.	Concurrency is about managing a lot of things at once.
3.	Parallelism can only be achieved when multiple pieces of code are executing simultaneously against different physical processors.

```
// wg is used to wait for the program to finish.
var wg sync.WaitGroup

// When the value of a WaitGroup is greater than zero, the Wait method will block.
wg.Add(2)

go func(){
	// Schedule the call to Done to tell main we are done.
	defer wg.Done()
}
```

```
import "runtime"
// Allocate a logical processor for every available core.
runtime.GOMAXPROCS(runtime.NumCPU())
```

##### Race conditions

```
go build -race // Build the code using the race detector flag
./example // Run the code
```

##### Locking shared resources
```
import (
	"fmt"
	"runtime"
	"sync"
	"sync/atomic"
)

var (
	counter int64
	wg sync.WaitGroup
)

func main() {
	wg.Add(2)
	go incCounter(1)
	go incCounter(2)
	wg.Wait()
	fmt.Println("Final Counter:", counter)
}

func incCounter(id int) {
	defer wg.Done()
	for count := 0; count < 2; count++ {
		atomic.AddInt64(&counter, 1)
		runtime.Gosched()
	}	
}
```

```
atomic.LoadInt64(&aInt)
atomic.StoreInt64(&aInt, 1)
```

##### Mutexes
A mutex is used to create a critical section around code that ensures only one goroutine at a time can execute that code section.

```
package main
import (
	"fmt"
	"runtime"
	"sync"
	//"sync/atomic"
)

var (
	counter int64
	wg sync.WaitGroup
	mutex sync.Mutex
)

func main() {
	wg.Add(2)
	go incCounter(1)
	go incCounter(2)
	wg.Wait()
	fmt.Println("Final Counter:", counter)
}

func incCounter(id int) {
	defer wg.Done()
	for count := 0; count < 2; count++ {
		mutex.Lock()
		{
			value := counter
			runtime.Gosched()
			value++
			counter = value
		}
		mutex.Unlock()
	}
}
```

##### Channels
*	You also have `channels` that synchronize goroutines as they send and receive the resources they need to share between each other.
*	When declaring a channel, the type of data that will be shared needs to be specified.
*	Values and pointers of built-in, named, struct, and reference types can be shared through a channel.
*	Creating a channel in Go requires the use of the built-in function `make`.
*	Sending a value or pointer into a channel requires the use of the `<-` operator.
*	For another goroutine to receive that string from the channel, we use the same `<-` operator

```
// Unbuffered channel of integers.
unbuffered := make(chan int)
// Buffered channel of strings.
buffered := make(chan string, 10)
// Send a string through the channel.
buffered <- "Gopher"
// Receive a string from the channel.
value := <- buffered
```

###### Unbuffered channels
An unbuffered channel is a channel with no capacity to hold any value before it’s
received. These types of channels require both a sending and receiving goroutine to
be ready at the same instant before any send or receive operation can complete. 

```
package main
import (
	"fmt"
	"math/rand"
	"sync"
	"time"
)

var wg sync.WaitGroup

func init(){
	rand.Seed(time.Now().UnixNano())
}

func main() {
	// Create an unbuffered channel
	cnt := make(chan int)
	wg.Add(2)
	go player("Nadal", cnt)
	go player("Djokovic", cnt)
	// Start the set.
	cnt <- 1
	// Wait for the game to finish.
	wg.Wait()
}

func palyer(name string, cnt chan int){
	defer wg.Done()
	for {
		ball, ok := <- cnt
		if !ok {
			fmt.Printf("Player %s Won\n", name)
			return
		}
		n := rand.Intn(100)
		if n%13 == 0 {
			fmt.Printf("Player %s Missed\n", name)
			// Close the channel to signal we lost.
			close(cnt)
			return
		}
		// Display and then increment the hit count by one.
		fmt.Printf("Player %s Hit %d\n", name, ball)
		ball++
		// Hit the ball back to the opposing player.
		cnt <- ball
	}
}
```

###### Buffered channels
*	A buffered channel is a channel with capacity to hold one or more values before they’re received. These types of channels don’t force goroutines to be ready at the same instant to perform sends and receives. 
*	A receive will block only if there’s no value in the channel to receive. 
*	A send will block only if there’s no available buffer to place the value being sent. 
*	Unbuffered channels provide a guarantee between an exchange of data. Buffered channels do not.

```
package main
import (
	"fmt"
	"math/rand"
	"sync"
	"time"
)

const (
	// Number of goroutines to use.
	nGoroutines = 4
	// Amount of work to process.
	taskLoad = 10
)

// wg is used to wait for the program to finish.
var wg sync.WaitGroup

func init(){
	rand.Seed(time.Now().UnixNano())
}

func main() {
	// Create a buffered channel to manage the task load.
	tasks := make(chan string, taskLoad)

	// Launch goroutines to handle the work.
	wg.Add(numberGoroutines)
	for gr := 1; gr <= numberGoroutines; gr++ {
		go worker(tasks, gr)
	}

	// Add a bunch of work to get done.
	for post := 1; post <= taskLoad; post++ {
		tasks <- fmt.Sprintf("Task : %d", post)
	}

	// Close the channel so the goroutines will quit
	// when all the work is done.
	close(tasks)

	// Wait for all the work to get done.
	wg.Wait()
}

func worker(tasks chan string, worker int) {
	defer wg.Done()
	for {
		// Wait for work to be assigned.
		task, ok := <- tasks
		if !ok {
			// This means the channel is empty and closed.
			fmt.Printf("Worker: %d : Shutting Down\n", worker)
			return
		}
		
		// Display we are starting the work.
		fmt.Printf("Worker: %d : Started %s\n", worker, task)

		// Randomly wait to simulate work time.
		sleep := rand.Int63n(100)
		time.Sleep(time.Duration(sleep) * time.Millisecond)

		// Display we finished the work.
		fmt.Printf("Worker: %d : Completed %s\n", worker, task)
	}
}
```

#### Concurrency Patterns
##### Runner
*	channels can be used to monitor the amount of time a program is running and terminate the program if it runs too long. 
*	This pattern is useful when developing a program that will be scheduled to run as a background task process. 

```
package runner
import (
	"errors"
	"os"
	"os/signal"
	"time"
)

type Runner struct {
	interrupt chan os.Signal
	complete chan error
	timeout <- chan time.Time
	tasks []func(int)
}

var ErrTimeout = errors.New("received timeout")
var ErrInterrupt = errors.New("received interrupt")

func New(d time.Duration) *Runner {
	return &Runner{
		interrupt: make(chan os.Signal, 1),
		complete: make(chan error),
		timeout: time.After(d),
}

func (r *Runner) Add(tasks ...func(int)) {
	r.tasks = append(r.tasks, tasks...)
}

func (r *Runner) Start() error {
	signal.Notify(r.interrupt, os.Interrupt)
	go func() {
		r.complete <- r.run()
	}()
	select {
		case err := <- r.complete: return err
		case <- r.timeout: return ErrTimeout
	}
}

func (r *Runner) run() error {
	for id, task := range r.tasks {
		if r.gotInterrupt() {
			return ErrInterrupt
		}
		task(id)
	}
	return nil
}

func (r *Runner) gotInterrupt() bool {
	select {
		case <- r.interrupt:
			signal.Stop(r.interrupt)
			return true
		default:
			return false
	}
}
```
##### Pooling
*	use a buffered channel to pool a set of resources that can be shared and individually used by any number of goroutines.
*	This pattern is useful when you have a static set of resources to share, such as database connections or memory buffers.

```
package pool

import (
	"errors"
	"log"
	"io"
	"sync"
)

type Pool struct {
	m sync.Mutex
	resources chan io.Closer
	factory func() (io.Closer, error)
	closed bool
}

var ErrPoolClosed = errors.New("Pool has been closed.")

func New(fn func() (io.Closer, error), size uint) (*Pool, error) {
	if size <= 0 {
		return nil, errors.New("Size value too small.")
	}
	return &Pool{
		factory: fn,
		resources: make(chan io.Closer, size),
	}, nil
}

func (p *Pool) Acquire() (io.Closer, error) {
	select {
		case r, ok := <- p.resources:
			log.Println("Acquire:", "Shared Resource")
			if !ok {
				return nil, ErrPoolClosed
			}
			return r, nil
		default:
			log.Println("Acquire:", "New Resource")
			return p.factory()
	}
}

func (p *Pool) Release(r io.Closer) {
	p.m.Lock()
	defer p.m.Unlock()
	if p.closed {
		r.Close()
		return
	}
	select {
		case p.resources <- r:
			log.Println("Release:", "In Queue")
		default:
			log.Println("Release:", "Closing")
			r.Close()
	}
}

func (p *Pool) Close() {
	p.m.Lock()
	defer p.m.Unlock()
	if p.closed {
		return
	}
	p.closed = true
	close(p.resources)
	for r := range p.resources {
		r.Close()
	}
}
```

##### Work
*	Use an unbuffered channel to create a pool of goroutines that will perform and control the amount of work that gets done concurrently.
*	Unbuffered channels provide a guarantee that data has been exchanged between two goroutines.

```
package work
import "sync"

// Worker must be implemented by types that want to use the work pool.
type Worker interface {
	Task()
}

// Pool provides a pool of goroutines that can execute any Worker tasks that are submitted.
type Pool struct {
	work chan Worker
	wg sync.WaitGroup
}

// New creates a new work pool.
func New(maxGoroutines int) *Pool {
	p := Pool{ work: make(chan Worker),}
	p.wg.Add(maxGoroutines)
	for i := 0; i < maxGoroutines; i++ {
		go func() {
			for w := range p.work {
				w.Task()
			}
			p.wg.Done()
		}()
	}
	return &p
}

// Run submits work to the pool.
func (p *Pool) Run(w Worker) {
	p.work <- w
}

// Shutdown waits for all the goroutines to shutdown.
func (p *Pool) Shutdown() {
	close(p.work)
	p.wg.Wait()
}
```

#### STL
##### log
```
package main
import "log"

func init() {
	log.SetPrefix("TRACE: ")
	log.SetFlags(log.Ldate | log.Lmicroseconds | log.Llongfile)
}

func main() {
	log.Println("message")
	log.Fatalln("fatal message")
	log.Panicln("panic message")
}
```

```
const (
	Ldate = 1 << iota 	// 1 << 0 = 000000001 = 1
	Ltime 				// 1 << 1 = 000000010 = 2
	Lmicroseconds 		// 1 << 2 = 000000100 = 4
	Llongfile 			// 1 << 3 = 000001000 = 8
	Lshortfile 			// 1 << 4 = 000010000 = 16
	LstdFlags = Ldate(1) | Ltime(2) // 00000011 = 3
)
```

```
package main
import (
	"io"
	"io/ioutil"
	"log"
	"os"
)

var (
	// Logger type pointer variables
	Trace 	*log.Logger
	Info 	*log.Logger
	Warning *log.Logger
	Error 	*log.Logger
)

func init() {
	file, err := os.OpenFile("errors.txt", os.O_CREATE|os.O_WRONLY|os.O_APPEND, 0666)
	if err != nil {
		log.Fatalln("Failed to open error log file:", err)
	}
	Trace = log.New(ioutil.Discard, "TRACE: ", log.Ldate|log.Ltime|log.Lshortfile)
	Info  = log.New(os.Stdout,      "INFO: ",  log.Ldate|log.Ltime|log.Lshortfile)
	Warning = log.New(os.Stdout, "WARNING: ", log.Ldate|log.Ltime|log.Lshortfile)
	Error = log.New(io.MultiWriter(file, os.Stderr), "ERROR: ", log.Ldate|log.Ltime|log.Lshortfile)
}

func main() {
	Trace.Println("I have something standard to say")
	Info.Println("Special Information")
	Warning.Println("There is something you need to know about")
	Error.Println("Something has failed")
}
	
```



http://play.golang.org

http://golang.org/pkg/fmt/
http://golang.org/pkg/strings/
