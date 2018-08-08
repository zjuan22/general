from utils.misc import addError, addWarning
from utils.hlir import getTypeAndLength
import p4_hlir.hlir.p4_stateful as p4_stateful

#[ #include "dataplane.h"
#[ #include "actions.h"
#[ #include "data_plane_data.h"
#[
#[ lookup_table_t table_config[NB_TABLES] = {
for table in hlir.p4_tables.values():
    table_type, key_length = getTypeAndLength(table)
    #[ {
    #[  .name= "${table.name}",
    #[  .id = TABLE_${table.name},
    #[  .type = ${table_type},
    #[  .key_size = ${key_length},
    #[  .val_size = sizeof(struct ${table.name}_action),
    #[  .min_size = 0, //${table.min_size},
    #[  .max_size = 255 //${table.max_size}
    #[ },
#[ };

#[ counter_t counter_config[NB_COUNTERS] = {
for counter in hlir.p4_counters.values():
    #[ {
    #[  .name= "${counter.name}",
    if counter.instance_count is not None:
        #[ .size = ${counter.instance_count},
    elif counter.binding is not None:
        btype, table = counter.binding
        if btype is p4_stateful.P4_DIRECT:
            #[ .size = ${table.max_size},
    else:
        #[ .size = 1,
    #[  .min_width = ${32 if counter.min_width is None else counter.min_width},
    #[  .saturating = ${1 if counter.saturating else 0}
    #[ },
#[ };

#[ p4_register_t register_config[NB_REGISTERS] = {
for register in hlir.p4_registers.values():
    if register.binding is not None:
        addWarning("", "direct and static registers currently treated as plain registers, no optimization occurs")
        continue
    if register.layout is not None:
        addError("", "registers with custom layouts are not supported yet")
        continue
    #[ {
    #[  .name= "${register.name}",
    #[  .size = ${register.instance_count},
    #[  .width = ${(register.width+7)/8},
    #[ },
#[ };
