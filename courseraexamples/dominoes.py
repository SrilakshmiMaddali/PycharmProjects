for left in range(7):
    for right in range(left,7):
        print("["+str(left)+"|"+str(right)+"]",end=" ")
    print()


def retry(operation, attempts):
  for n in range(attempts):
    if operation():
      print("Attempt " + str(n) + " succeeded")
      break
    else:
      print("Attempt " + str(n) + " failed")

#retry(create_user, 3)
#retry(stop_service, 5)