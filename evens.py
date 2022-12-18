def even_no_ofevens(numbers):
    if isinstance(numbers, list):
        even = sum(1 for n in numbers if n % 2 == 0)
        return True if even and even % 2 == 0 else False
    
    else:
        raise TypeError("list was not passed in to function")


if __name__ == "__main__":
    print(even_no_ofevens([6,8]))
    
