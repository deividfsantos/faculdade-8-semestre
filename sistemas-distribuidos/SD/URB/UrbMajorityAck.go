package UrbMajorityAck

import (
	. "SD/BEB"
	"fmt"
)

type URB_Req_Message struct {
	Message string
}

type URB_Ind_Message struct {
	From    string
	Message string
}

type UrbMajorityAck_Module struct {
	Ind          chan URB_Ind_Message
	Req          chan URB_Req_Message
	beb          BestEffortBroadcast_Module
	pending      []string
	delivered    []string
	acks         [][]string
	Destinations []string
}

func (module UrbMajorityAck_Module) Init(address string) {
	fmt.Println("Init URB!")
	module.beb = BestEffortBroadcast_Module{
		Req: make(chan BestEffortBroadcast_Req_Message, 100),
		Ind: make(chan BestEffortBroadcast_Ind_Message, 100)}

	module.beb.Init(address)
	module.Start()
}

func (module UrbMajorityAck_Module) Start() {
	go func() {
		for {
			select {
			case y := <-module.Req:
				module.Broadcast(y)
			case y := <-module.beb.Ind:
				if module.canDeliver(URB2BEB(y)) && module.isPending(URB2BEB(y)) && !module.isDelivered(URB2BEB(y)) {
					module.Deliver(URB2BEB(y))
				} else {
					module.Ack(URB2BEB(y))
				}
			}
		}
	}()
}

func URB2BEB(message BestEffortBroadcast_Ind_Message) URB_Ind_Message {
	return URB_Ind_Message{
		From:    message.From,
		Message: message.Message}
}

func (module *UrbMajorityAck_Module) Broadcast(message URB_Req_Message) {
	module.pending = append(module.pending, message.Message)
	Req := BestEffortBroadcast_Req_Message{
		Addresses: module.Destinations,
		Message:   message.Message}
	module.beb.Req <- Req
}

func (module *UrbMajorityAck_Module) Deliver(message URB_Ind_Message) {
	module.delivered = append(module.delivered, message.Message)

	index := -1
	for i := 0; i < len(module.pending); i++ {
		if module.pending[i] == message.Message {
			index = i
		}
	}

	module.pending[index] = module.pending[len(module.pending)-1]
	module.Ind <- message
}

func (module *UrbMajorityAck_Module) Ack(message URB_Ind_Message) {
	added := false
	for i := 0; i < len(module.acks); i++ {
		if module.acks[i][0] == message.Message {
			module.acks[i] = append(module.acks[i], message.From)
		}
	}
	if !added {
		newMessage := []string{message.Message, message.From}
		module.acks = append(module.acks, newMessage)
	}

	contains := false
	for i := 0; i < len(module.pending); i++ {
		if module.pending[i] == message.Message {
			contains = true
		}
	}

	if !contains {
		module.pending = append(module.pending, message.Message)
		Req := BestEffortBroadcast_Req_Message{
			Addresses: module.Destinations,
			Message:   message.Message}
		module.beb.Req <- Req
	}
}

func (module *UrbMajorityAck_Module) canDeliver(message URB_Ind_Message) bool {
	for i := 0; i < len(module.acks); i++ {
		if message.Message == module.acks[i][0] {
			if len(module.acks[i]) > ((len(module.Destinations) - 1) / 2) {
				return true
			}
		}
	}
	return false
}

func (module *UrbMajorityAck_Module) isPending(message URB_Ind_Message) bool {
	for i := 0; i < len(module.pending); i++ {
		if message.Message == module.pending[i] {
			return true
		}
	}
	return false
}

func (module *UrbMajorityAck_Module) isDelivered(message URB_Ind_Message) bool {
	for i := 0; i < len(module.delivered); i++ {
		if message.Message == module.delivered[i] {
			return true
		}
	}
	return false
}
