"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        if not employees:
            return 0
        dict_ = {int:list}
        for ee in employees:
            dict_[ee.id] = [ee.importance,ee.subordinates]
        queue = collections.deque()
        for ee in employees:
            if ee.id == id:
                queue.append(ee.id)
                break;
        res = dict_[id][0]
        while queue:
            er_id = queue.popleft()
            er_sub = dict_[er_id][1]
            for sub_id in er_sub:
                res += dict_[sub_id][0]
                queue.append(sub_id)
        return res