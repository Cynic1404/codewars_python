'''Mikhail Nekhaenok, [09.04.17 20:41]
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([false,1,0,1,2,0,1,3,"a"]) # returns[false,1,1,2,1,3,"a",0,0]'''



def move_zeros(array):
	count = 0
	n = []
	
	for i in array:
		if (not isinstance(i, bool)) and (i == 0):
			count += 1
		else:
			n.append(i)
	
	for i in range(count):
		n.append(0)
		print n
	
	return n

'''Test.describe("Basic tests")
Test.assert_equals(move_zeros([1,2,0,1,0,1,0,3,0,1]),[ 1, 2, 1, 1, 3, 1, 0, 0, 0, 0 ])
Test.assert_equals(move_zeros([9,0.0,0,9,1,2,0,1,0,1,0.0,3,0,1,9,0,0,0,0,9]),[9,9,1,2,1,1,3,1,9,9,0,0,0,0,0,0,0,0,0,0])
Test.assert_equals(move_zeros(["a",0,0,"b","c","d",0,1,0,1,0,3,0,1,9,0,0,0,0,9]),["a","b","c","d",1,1,3,1,9,9,0,0,0,0,0,0,0,0,0,0])
Test.assert_equals(move_zeros(["a",0,0,"b",None,"c","d",0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9]),["a","b",None,"c","d",1,False,1,3,[],1,9,{},9,0,0,0,0,0,0,0,0,0,0])
Test.assert_equals(move_zeros([0,1,None,2,False,1,0]),[1,None,2,False,1,0,0])
Test.assert_equals(move_zeros(["a","b"]),["a","b"])
Test.assert_equals(move_zeros(["a"]),["a"])
Test.assert_equals(move_zeros([0,0]),[0,0])
Test.assert_equals(move_zeros([0]),[0])
Test.assert_equals(move_zeros([]),[])'''