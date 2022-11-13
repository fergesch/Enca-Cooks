# Enca Cooks Backend

Add dependencies to `go.mod`

`go mod tidy` to install 

`go run .` to run the app


### For automatica reloading 
https://github.com/codegangsta/gin

To find `GOPATH`
```
go env | grep GOPATH
```
and then  `export PATH=$PATH:{GOPATH}/bin`

Now you can run 
```
gin --appPort 8080  -i --notifications
``` 
which will automatially reload on code changes