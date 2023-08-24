# -*- coding: utf-8 -*-
# @Author: Bobo
# @Date:   2023-02-06 23:27:14
# @Last Modified by:   Bobo
# @Last Modified time: 2023-02-07 00:11:10
from utils.solution_base import SolutionBase

class Solution(SolutionBase):
  def part1(self, data):
    for line in data:
      return [x.split(",") for x in line.split("->")]

  def part2(self, data):
    return self.find_marker(data[0], 14)
  
