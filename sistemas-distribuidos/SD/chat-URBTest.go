// Construido como parte da disciplina de Sistemas Distribuidos
// PUCRS - Escola Politecnica
// Professor: Fernando Dotti  (www.inf.pucrs.br/~fldotti)

/*
LANCAR N PROCESSOS EM SHELL's DIFERENTES, PARA CADA PROCESSO, O SEU PROPRIO ENDERECO EE O PRIMEIRO DA LISTA
go run chat.go 127.0.0.1:5001  127.0.0.1:6001    ...
go run chat.go 127.0.0.1:6001  127.0.0.1:5001    ...
go run chat.go ...  127.0.0.1:6001  127.0.0.1:5001
*/

package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
	"time"

	. "SD/URB"
)

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Please specify at least one address:port!")
		fmt.Println("go run chat.go 127.0.0.1:5001  127.0.0.1:6001    ...")
		fmt.Println("go run chat.go 127.0.0.1:6001  127.0.0.1:5001    ...")
		fmt.Println("go run chat.go ...  127.0.0.1:6001  127.0.0.1:5001")
		return
	}

	var registro []string
	addresses := os.Args[1:]
	fmt.Println(addresses)

	failLast := true //Set if want to fail last message to last ip

	// Failure simulation // Discomment if want to fail all messages from specific IP to last address
	// if addresses[0] == "127.0.0.1:7001" {
	// 	addresses = addresses[:len(addresses)-2]
	// }

	urb := UrbMajorityAck_Module{
		Req:          make(chan URB_Req_Message, 100),
		Ind:          make(chan URB_Ind_Message, 100),
		Destinations: addresses}

	urb.Init(addresses[0])

	go func() {
		for i := 0; i < 100; i++ {
			msg := strconv.Itoa(i) + " " + addresses[0][10:len(addresses[0])] + "§" + addresses[0]
			req := URB_Req_Message{
				Addresses: addresses,
				Message:   msg}
			urb.Req <- req
		}
		time.Sleep(1 * time.Second)

		//Fail last simulation to last ip
		if failLast {
			msg := "Last " + addresses[0][10:len(addresses[0])] + "§" + addresses[0]
			req := URB_Req_Message{
				Addresses: addresses[:len(addresses)-1],
				Message:   msg}
			urb.Req <- req
		}
	}()

	go func() {
		receivedMessages := 0
		for {
			in := <-urb.Ind
			receivedMessages++
			message := strings.Split(in.Message, "§")
			in.From = message[1]
			registro = append(registro, in.Message)
			in.Message = message[0]
			// imprime a mensagem recebida na tela
			fmt.Printf("Message from %v: %v\n", in.From, in.Message)
		}
	}()

	blq := make(chan int)
	<-blq
}
