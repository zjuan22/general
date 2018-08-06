#!/bin/bash

# ======================================================================================
# Sección 1: Seccion para definicion de variables y limites de ancho de banda
# mediante comando tc:
# ======================================================================================
# Definicion de variables:
#INTERFACE_IN="enp2s0"
INTERFACE_IN="eth5"
INTERFACE_OUT="eth6"
IN="tc filter add dev $INTERFACE_IN parent 1:0 protocol ip prio 1 u32 match ip dst "
OUT="tc filter add dev $INTERFACE_OUT parent 1:0 protocol ip prio 1 u32 match ip src "
PUERTO="match ip sport "
REGLA="0xffff flowid"

# Cargar y habilitar interfaces virtuales para ccontrol de uploads. Luego redirigir
# el trafico entrante de la intefaz fisica a la interfaz virtual.
modprobe ifb numifbs=1
ip link set dev $INTERFACE_OUT up
tc qdisc del dev $INTERFACE_IN root 2>/dev/null
tc qdisc del dev $INTERFACE_IN ingress 2>/dev/null
tc qdisc del dev $INTERFACE_OUT root 2>/dev/null
tc qdisc add dev $INTERFACE_IN handle ffff: ingress
tc filter add dev $INTERFACE_IN parent ffff: protocol ip u32 match u32 0 0 action mirred egress redirect dev $INTERFACE_OUT

# Definicion de limites de ancho de banda para download:
tc qdisc add dev $INTERFACE_IN root handle 1: htb
tc class add dev $INTERFACE_IN parent 1: classid 1:1 htb rate 1mbit
#tc class add dev $INTERFACE_IN parent 1:1 classid 1:10 htb rate 1mbit
tc class add dev $INTERFACE_IN parent 1:1 classid 1:10 htb rate 10000mbit
tc class add dev $INTERFACE_IN parent 1:1 classid 1:20 htb rate 200mbit
tc class add dev $INTERFACE_IN parent 1:1 classid 1:30 htb rate 3mbit
tc class add dev $INTERFACE_IN parent 1:1 classid 1:40 htb rate 4mbit
tc qdisc add dev $INTERFACE_IN parent 1:10 handle 10: sfq perturb 10
tc qdisc add dev $INTERFACE_IN parent 1:20 handle 20: sfq perturb 10
tc qdisc add dev $INTERFACE_IN parent 1:30 handle 30: sfq perturb 10
tc qdisc add dev $INTERFACE_IN parent 1:40 handle 40: sfq perturb 10

# Definicion de limites de ancho de banda para upload:
tc qdisc add dev $INTERFACE_OUT root handle 1: htb
tc class add dev $INTERFACE_OUT parent 1: classid 1:1 htb rate 1024kbit
#tc class add dev $INTERFACE_OUT parent 1:1 classid 1:10 htb rate 1024kbit
tc class add dev $INTERFACE_OUT parent 1:1 classid 1:10 htb rate 10000mbit
tc class add dev $INTERFACE_OUT parent 1:1 classid 1:20 htb rate 2048kbit
tc class add dev $INTERFACE_OUT parent 1:1 classid 1:30 htb rate 3072kbit
tc class add dev $INTERFACE_OUT parent 1:1 classid 1:40 htb rate 4096kbit
tc qdisc add dev $INTERFACE_OUT parent 1:10 handle 10: sfq perturb 10
tc qdisc add dev $INTERFACE_OUT parent 1:20 handle 20: sfq perturb 10
tc qdisc add dev $INTERFACE_OUT parent 1:30 handle 30: sfq perturb 10
tc qdisc add dev $INTERFACE_OUT parent 1:40 handle 40: sfq perturb 10

# ======================================================================================
# Sección 2: Sección de habilitación de dispositivos o redes (respetar orden):
# ======================================================================================
# Limite individual por equipo (mayor prioridad):
#$IN 192.168.1.90/32 $PUERTO 3128 $REGLA 1:40
#$OUT 192.168.1.90/32 flowid 1:40

# Limite por defecto para todos los equipos de la red (menor prioridad):
#$IN 192.168.1.0/24 $PUERTO 3128 $REGLA 1:20
$IN 4.0.0.1/24 $REGLA 1:10
#$IN 10.0.0.1/24 $PUERTO 80 $REGLA 1:10
#$OUT 192.168.1.0/24 $PUERTO 80 $REGLA 1:10
#$OUT 192.168.1.0/24 flowid 1:10

# Mensaje de finalizacion en la aplicacion de reglas:
echo
echo "Se han aplicado exitosamente las reglas de control de ancho de banda!"
echo
