#### 1.文件操作
##### 1.1 逐行读取
```
// ex1.go
package main

import (
    "bufio"
    "fmt"
    "io"
    "os"
)

func main() {
    fi, err := os.Open("../ex14.go")
    if err != nil {
        fmt.Printf("Error: %s\n", err)
        return
    }
    defer fi.Close()

    br := bufio.NewReader(fi)
    for {
        a, _, c := br.ReadLine()
        if c == io.EOF {
            break
        }
        fmt.Println(string(a))
    }
}
```

```
// ex2.go
package main

import (
    "bufio"
    "fmt"
    "io"
    "os"
)

func main() {
    fi, err := os.Open("../ex14.go")
    if err != nil {
        panic(err)
    }
    defer fi.Close()

    rd := bufio.NewReader(fi)
    for {
        //以'\n'为结束符读入一行
        line, err := rd.ReadString('\n')
        if err != nil || io.EOF == err {
            break
        }
        fmt.Print(line)
        }
}
```

##### 1.2 一次性读取
```
// ex3.go
package main

import (
    "fmt"
    "io/ioutil"
)

func main() {
    b, e := ioutil.ReadFile("./ex2.go")
    if e != nil {
        fmt.Println("read file error")
        return
    }
    fmt.Println(string(b))
}

```
