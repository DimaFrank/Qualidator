
class UniqInspector:

    def __init__(self, column_name):
        self.column_name = column_name

    def column_values_are_unique(self):
        query = (
            f"SELECT {self.column_name}, COUNT(*)\n"
            f"FROM ...\n"
            f"GROUP BY {self.column_name}\n"
            f"HAVING COUNT(*)>1;\n"
        )
        return query
    
    def column_unique_value_count_is_between(lower_bound, upper_bound):
        query = (
            f"SELECT\n"
            f"    CASE WHEN COUNT(DISTINCT {{self.column_name}}) >= {{lower_bound}} AND COUNT(DISTINCT {{self.column_name}}) <= {{upper_bound}}\n"
            f"    THEN 1 ELSE 0 END AS result\n"
            f"FROM ...\n"
        )
        return query
