#### 1. 文件头
```
#!/bin/bash
# 注释信息
# Perform hot backups of Oracle databases.

# 环境变量
export PATH='/usr/xpg4/bin:/usr/bin:/opt/csw/bin:/opt/goog/bin'
```

#### 2. 函数注释
```
#######################################
# 所有的错误信息都应该被导向STDERR
# Globals:
#   BACKUP_DIR
#   ORACLE_SID
# Arguments:
#   None
# Returns:
#   None
#######################################
err() {
    echo "[$(date +'%Y-%m-%dT%H:%M:%S%z')]: $@" >&2
}
```

#### 3. TODO
```
# TODO(用户): 内容Handle the unlikely edge cases (bug #### 权限编码)
```

#### 4. 缩进
* 缩进两个空格，没有制表符。
* 行的长度和长字符串

```
# DO use 'here document's
cat <<END;
I am an exceptionally long
string.
END

# Embedded newlines are ok too
long_string="I am an exceptionally
  long string."
```

* 如果一行容不下整个管道操作，那么请将整个管道操作分割成每行一个管段。

```
# All fits on one line
command1 | command2

# Long commands
command1 \
  | command2 \
  | command3 \
  | command4
```

* `; do` , `; then` 应该和 `if/for/while` 放在同一行

* 匹配表达式比 `case` 和 `esac` 缩进一级。多行操作要再缩进一级

```
case "${expression}" in
  a)
    variable="..."
    some_command "${variable}" "${other_expr}" ...
    ;;
  absolute)
    actions="relative"
    another_command "${actions}" "${other_expr}" ...
    ;;
  *)
    error "Unexpected expression '${expression}'"
    ;;
esac
```

```
verbose='false'
aflag=''
bflag=''
files=''
while getopts 'abf:v' flag; do
  case "${flag}" in
    a) aflag='true' ;;
    b) bflag='true' ;;
    f) files="${OPTARG}" ;;
    v) verbose='true' ;;
    *) error "Unexpected option ${flag}" ;;
  esac
done
```

#### 5.引用
* 使用 `$(command)` 而不是反引号。嵌套的反引号要求用反斜杠转义内部的反引号。而` $(command)` 形式嵌套时不需要改变，而且更易于阅读。

```
# This is preferred:
var="$(command "$(command1)")"

# This is not:
var="`command \`command1\``"

```

* 推荐使用 `[[ ... ]]`

```
# Do this:
if [[ "${my_var}" = "some_string" ]]; then
  do_something
fi

# -z (string length is zero) and -n (string length is not zero) are
# preferred over testing for an empty string
if [[ -z "${my_var}" ]]; then
  do_something
fi

# This is OK (ensure quotes on the empty side), but not preferred:
if [[ "${my_var}" = "" ]]; then
  do_something
fi

if [[ -n "${my_var}" ]]; then
  do_something
fi
```

* 当进行文件名的通配符扩展时，请使用明确的路径。因为文件名可能以 `-` 开头，所以使用扩展通配符 `./*` 比 `*` 来得安全得多。

```
rm -v ./*
```

* 请使用过程替换或者for循环，而不是管道导向while循环。在while循环中被修改的变量是不能传递给父shell的，因为循环命令是在一个子shell中运行的。
```
total=0
# Only do this if there are no spaces in return values.
for value in $(command); do
  total+="${value}"
done
```

#### References
http://zh-google-styleguide.readthedocs.io/en/latest/google-shell-styleguide/contents/
