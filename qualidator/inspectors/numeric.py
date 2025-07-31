
class NumericInspector:

    def __init__(self, column_name):
        self.column_name = column_name

    def column_max_is_between(self, lower_bound, upper_bound):
        query = (
            f"SELECT\n"
            f"    CASE WHEN MAX({self.column_name})>= {lower_bound}\n"
            f"          AND MAX({self.column_name})<= {upper_bound}\n"
            f"           THEN 1 ELSE 0\n"
            f"    END AS result\n"
            f"\n"
            f"FROM ...;\n"
        )
        return query
    

    def column_min_is_between(self, lower_bound, upper_bound):
        query = (
            f"SELECT\n"
            f"    CASE WHEN MIN({self.column_name})>= {lower_bound}\n"
            f"          AND MIN({self.column_name})<= {upper_bound}\n"
            f"           THEN 1 ELSE 0\n"
            f"    END AS result\n"
            f"\n"
            f"FROM ...;\n"
        )
        return query
    

    def column_sum_is_between(self, lower_bound, upper_bound):
        query = (
            f"SELECT\n"
            f"    CASE WHEN SUM({self.column_name})>= {lower_bound}\n"
            f"          AND SUM({self.column_name})<= {upper_bound}\n"
            f"           THEN 1 ELSE 0\n"
            f"    END AS result\n"
            f"\n"
            f"FROM ...;\n"
        )
        return query
    

    def column_values_are_between(self, lower_bound, upper_bound):
        query = (
            f"SELECT\n"
            f"    CASE WHEN {self.column_name}>= {lower_bound}\n"
            f"          AND {self.column_name}<= {upper_bound}\n"
            f"           THEN 1 ELSE 0\n"
            f"    END AS result\n"
            f"\n"
            f"FROM ...;\n"
        )
        return query
    

    def column_mean_is_between(self, lower_bound, upper_bound):
        query = (
            f"SELECT\n"
            f"    CASE WHEN AVG({self.column_name})>= {lower_bound}\n"
            f"          AND AVG({self.column_name})<= {upper_bound}\n"
            f"           THEN 1 ELSE 0\n"
            f"    END AS result\n"
            f"\n"
            f"FROM ...;\n"
        )
        return query