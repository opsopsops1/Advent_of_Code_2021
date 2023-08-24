# -*- coding: utf-8 -*-
# @Author: Bobo
# @Date:   2023-02-07 01:07:00
# @Last Modified by:   Bobo
# @Last Modified time: 2023-02-07 19:23:41
from utils.solution_base import SolutionBase

class Solution(SolutionBase):
  def part1(self, data):
    g = {}
    for line in data:
      u, v = [list(map(int, x.split(","))) for x in line.split("->")]
      # return u, v

      dx, dy = v[0]-u[0], v[1]-u[1]
      x_min, x_max = min(u[0], v[0]), max(u[0], v[0])
      y_min, y_max = min(u[1], v[1]), max(u[1], v[1])
      if dx == 0 or dy == 0:
        for x in range(x_min, x_max+1):
          for y in range(y_min, y_max+1):
            g[(x, y)] = g.get((x, y), 0) + 1

    return len([v for v in g.values() if v >= 2])


  def part2(self, data):
    g = {}
    for line in data:
      u, v = [list(map(int, x.split(","))) for x in line.split("->")]
      # return u, v

      dx, dy = v[0]-u[0], v[1]-u[1]
      x_min, x_max = min(u[0], v[0]), max(u[0], v[0])
      y_min, y_max = min(u[1], v[1]), max(u[1], v[1])
      if dx == 0 or dy == 0:
        for x in range(x_min, x_max+1):
          for y in range(y_min, y_max+1):
            g[(x, y)] = g.get((x, y), 0) + 1
      elif dx == dy or dx == -dy:
        for x in range(abs(dx)+1):
          new_x, new_y = u[0]+(x if dx>0 else -x), u[1]+(x if dy>0 else -x)
          g[(new_x, new_y)] = g.get((new_x, new_y), 0) + 1

    return len([v for v in g.values() if v >= 2])
  
