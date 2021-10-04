import time
def test_case(n):
  print("test case:",n)
  start1 = time.time()
  breed(n)
  cost1 = time.time()-start1

  start2 = time.time()
  dynamic_breed(n)
  cost2 = time.time()-start2

  print(" breed:{:.8f}".format(cost1))
  print("dbreed:{:.8f}".format(cost2))
for i in range(1,20):
  test_case(i)