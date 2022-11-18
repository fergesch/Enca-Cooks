# Enca Cooks Backend

Add dependencies to `go.mod`

`go mod tidy` to install 

`go run .` to run the app


### For automatica reloading 
https://github.com/codegangsta/gin

Install gin via `go install github.com/codegangsta/gin` for 1.17+ or `go get github.com/codegangsta/gin`for older versions

To find `GOPATH`
```
go env | grep GOPATH
```
and then `export PATH=$PATH:{GOPATH}/bin`

Now you can run 
```
gin --appPort 8080  -i --notifications
``` 
which will automatially reload on code changes

### Gcloud storage account authentication
need to run/authenticate before running with `gcloud auth application-default login`