cd /home/deivid/Documents/faculdade-8-semestre/sistemas-distribuidos/SD
terminator -x "go run chat-URBTest.go 127.0.0.1:7001 127.0.0.1:7002 127.0.0.1:7003 127.0.0.1:7004 127.0.0.1:7005 127.0.0.1:7006"
terminator -x "go run chat-URBTest.go 127.0.0.1:7002 127.0.0.1:7001 127.0.0.1:7003 127.0.0.1:7004 127.0.0.1:7005 127.0.0.1:7006"
terminator -x "go run chat-URBTest.go 127.0.0.1:7003 127.0.0.1:7002 127.0.0.1:7001 127.0.0.1:7004 127.0.0.1:7005 127.0.0.1:7006"
terminator -x "go run chat-URBTest.go 127.0.0.1:7004 127.0.0.1:7002 127.0.0.1:7003 127.0.0.1:7001 127.0.0.1:7005 127.0.0.1:7006"
terminator -x "go run chat-URBTest.go 127.0.0.1:7005 127.0.0.1:7002 127.0.0.1:7003 127.0.0.1:7001 127.0.0.1:7001 127.0.0.1:7006"
terminator -x "go run chat-URBTest.go 127.0.0.1:7006 127.0.0.1:7002 127.0.0.1:7003 127.0.0.1:7001 127.0.0.1:7005 127.0.0.1:7001"
