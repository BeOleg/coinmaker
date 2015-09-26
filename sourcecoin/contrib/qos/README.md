### Qos ###

This is a Linux bash script that will set up tc to limit the outgoing bandwidth for connections to the CM_UppercaseCoinName network. It limits outbound TCP traffic with a source or destination port of CM_Port, but not if the destination IP is within a LAN (defined as 192.168.x.x).

This means one can have an always-on CM_LowercaseCoinNamed instance running, and another local CM_LowercaseCoinNamed/CM_LowercaseCoinName-qt instance which connects to this node and receives blocks from it.
