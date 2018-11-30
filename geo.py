#!/bin/bash
def coord_2d_area_triangle():
	a_x = 15
	a_y = 15
	b_x = 23
	b_y = 30
	c_x = 50
	c_y = 25
	
	area = float(abs((a_x * (b_y - c_y)+(b_x * (c_y - a_y))+(c_x * (a_y - b_y)))/2.0))
	print(area)

def main():
	coord_2d_area_triangle()

if __name__ == '__main__':
	main()
