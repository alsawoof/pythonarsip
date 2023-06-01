#Untuk melakukan input dengan dicari angka terkecil dan terbesarnya
largest = None
smallest = None

while True:
    num = input("Enter a number:")
    if num == 'done':
        break

    try:
        num = int(num)
        if largest is None or num > largest:
            largest = num
        if smallest is None or num < smallest:
            smallest = num

    except:
        print("Invalid input")

if largest != None and smallest != None:
    print("Maximum is", largest)
    print("Minimum is", smallest)