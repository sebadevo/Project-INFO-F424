from copy import deepcopy

class Node:
    def __init__(self, constraints, upperbound, lowerbound, parent, root, non_int, cutting_planes, depth, is_done):
        """

        :param constraints:
        :param upperbound:
        :param lowerbound:
        :param parent:
        :param root:
        :param non_int:
        :param depth:
        :param is_done:
        """
        self.cutting_planes = cutting_planes
        self.upperbound = upperbound
        self.lowerbound = lowerbound
        self.constraints = constraints
        self.parent = parent
        self.root = root
        self.childs = []
        self.non_int = non_int
        self.is_done = is_done
        self.depth = depth
        
    def get_cutting_planes(self):
        return self.cutting_planes

    def set_cutting_planes(self, cutting_planes):
        self.cutting_planes = cutting_planes
    
    def get_depth(self):
        return deepcopy(self.depth)

    def set_depth(self, depth):
        self.depth = depth

    def get_non_int(self):
        return self.non_int

    def set_non_int(self, non_int):
        self.non_int = non_int

    def get_root(self):
        return self.root

    def set_root(self, root):
        self.root = root
    
    def get_is_done(self):
        return self.is_done
    
    def toggle_is_done(self):
        self.is_done = not self.is_done

    def set_is_done(self, is_done):
        self.is_done = is_done
    
    def get_parent(self):
        return self.parent

    def set_parent(self, parent):
        self.parent = parent

    def get_childs(self):
        return self.childs
    
    def add_child(self, child):
        self.childs.append(child)
    
    def set_childs(self, childs):
        self.childs = childs
                
    def get_upperbound(self):
        return self.upperbound

    def set_upperbound(self, upperbound):
        self.upperbound = upperbound
    
    def get_lowerbound(self):
        return self.lowerbound
    
    def set_lowerbound(self, lowerbound):
        self.lowerbound = lowerbound
    
    def get_constraints(self):
        if self.constraints is None:
            return []
        return deepcopy(self.constraints)
    
    def set_constraints(self, constraints):
        self.constraints = constraints