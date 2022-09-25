cd /home/deivid/Documents/faculdade-8-semestre/sistemas-distribuidos/SD
terminator -x "go run chat-BEBTest.go 127.0.0.1:7001 127.0.0.1:7002 127.0.0.1:7003 127.0.0.1:7004"
terminator -x "go run chat-BEBTest.go 127.0.0.1:7002 127.0.0.1:7001 127.0.0.1:7003 127.0.0.1:7004"
terminator -x "go run chat-BEBTest.go 127.0.0.1:7003 127.0.0.1:7002 127.0.0.1:7001 127.0.0.1:7004"
terminator -x "go run chat-BEBTest.go 127.0.0.1:7004 127.0.0.1:7002 127.0.0.1:7003 127.0.0.1:7001"

