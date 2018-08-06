#!/bin/bash

# Definicion de variables:
INTERFACE_IN="eth5"
INTERFACE_OUT="eth6"

# Liberacion de filtros:
tc qdisc del dev $INTERFACE_IN root 2>/dev/null
tc qdisc del dev $INTERFACE_IN ingress 2>/dev/null
tc qdisc del dev $INTERFACE_OUT root 2>/dev/null

# Mensaje de culminacion:
echo
echo Navegacion liberada.
echo
