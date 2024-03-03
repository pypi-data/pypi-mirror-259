import sys


def struct_table_name(table_name):
    return table_name.replace(".", "__p__").replace(":", "__c__")


def restore_table_name(table_name):
    return table_name.replace("__p__", ".").replace("__c__", ":")


def struct_queue_name(db_name, table_name):
    return sys.intern(f"__{db_name}_{table_name}_queue__")


