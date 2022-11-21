#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 15:04:56 2022

@author: anish
"""

class Layout(object):
    def __init__(self):
        self.layout = [[None, None, None, None],
                       [None, None, None, None],
                       [None, None, None, None],
                       [None, None, None, None]]
    
    def __str__(self):
        layout_str = '\nMap:\n' + '-' * 37 + '\n|'
        for i in self.layout:
            for n in i:
                if n == None:
                    n = '    '
                space = 7 - len(str(n))
                layout_str += ' ' + str(n) + ' ' * space + '|'
            layout_str = layout_str[:-1] + '|\n' + '-' * 37 + '\n|'
        return layout_str[:-2] + '\n'
    
    def insert(self, obj):
        if self.layout[obj.x][obj.y] == None:
            self.layout[obj.x][obj.y] = obj
        else:
            raise ValueError("Square already has an object in this location")
    
    def get_object(self, pos: tuple):
        return self.layout[pos[0]][pos[1]]
    
    def remove_object(self, pos: tuple):
        self.layout[pos[1]][pos[1]] = None

# class Square(object):
#     def __init__(self, obstacle_type):
#         pass
    
#     def get_signal(self):
#         pass

class Pit(object):
    def __init__(self, x_pos, y_pos):
        self.x = x_pos
        self.y = y_pos
    
    def get_signal(self):
        return 1
    
    def __str__(self):
        return 'Pit'

class Wumpus(object):
    def __init__(self, x_pos, y_pos):
        self.x = x_pos
        self.y = y_pos
    
    def get_signal(self):
        return 2
    
    def __str__(self):
        return 'Wumpus'

class Gold(object):
    def __init__(self, x_pos, y_pos):
        self.x = x_pos
        self.y = y_pos
    
    def get_signal(self):
        return 4
    
    def __str__(self):
        return 'Gold'

class Robot(object):
    def __init__(self, layout_map):
        self.layout_map = layout_map
        self.x = len(self.layout_map.layout) - 1
        self.y = 0
        self.direction = 1 # 1 - North, 2 - East, 3 - South, 4 - West
        self.layout_map.insert(self)
    
    def set_direction(self, direction: int):
        self.direction = direction
    
    def get_signal(self):
        total_signal = 0
        
        if self.x - 1 >= 0 and self.x - 1 < 4 and self.y >= 0 and self.y < 4:
            if self.layout_map.get_object((self.x - 1, self.y)) != None:
                total_signal += self.layout_map.get_object((self.x - 1, self.y)).get_signal()
        if self.x + 1 >= 0 and self.x + 1 < 4 and self.y >= 0 and self.y < 4:
            if self.layout_map.get_object((self.x + 1, self.y)) != None:
                total_signal += self.layout_map.get_object((self.x + 1, self.y)).get_signal()
        if self.x >= 0 and self.x < 4 and self.y - 1 >= 0 and self.y - 1 < 4:
            if self.layout_map.get_object((self.x, self.y - 1)) != None:
                total_signal += self.layout_map.get_object((self.x, self.y - 1)).get_signal()
        if self.x >= 0 and self.x < 4 and self.y + 1 >= 0 and self.y + 1 < 4:
            if self.layout_map.get_object((self.x, self.y + 1)) != None:
                total_signal += self.layout_map.get_object((self.x, self.y + 1)).get_signal()
        
        return total_signal
    
    def __str__(self):
        if self.direction == 1:
            return '^^^^^^'
        elif self.direction == 2:
            return '>>>>>>'
        elif self.direction == 3:
            return 'vvvvvv'
        elif self.direction == 4:
            return '<<<<<<'

if __name__ == '__main__':
    layout = Layout()
    robot = Robot(layout)
    print(layout)
    
    # Input gold position
    layout.insert(Gold(int(input("Enter gold position x: ").strip()), int(input("Enter gold position y: ").strip())))
    print(layout)
    
    # Input wumpos position
    layout.insert(Wumpus(int(input("Enter wumpus position x: ").strip()), int(input("Enter wumpus position y: ").strip())))
    print(layout)
    
    print("Type STOP to finish adding pits\n")
    
    # Input pit positions
    pos1, pos2 = '', ''
    pos1 = input("Enter pit position x: ").lower().strip()
    if pos1 != 'stop':
        pos2 = input("Enter pit position x: ").lower().strip()
    while pos1 != 'stop' and pos2 != 'stop':
        pos1 = int(pos1)
        pos2 = int(pos2)
        layout.insert(Pit(pos1, pos2))
        print(layout)
        
        pos1 = input("Enter pit position x: ").lower().strip()
        if pos1 != 'stop':
            pos2 = input("Enter pit position x: ").lower().strip()
    del pos1, pos2
    
    print(robot.get_signal())
    
    
    
    
    
    
    
    
    
    
    
    
    