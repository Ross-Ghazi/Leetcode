       def bisect_left(a, x):
            left, right = 0, len(a)
            while left < right:
                mid = (left + right) // 2
                if a[mid] < x:
                    left = mid + 1
                else:
                    right = mid
            return left
        def bisect_right(a, x):
            left, right = 0, len(a)
            while left < right:
                mid = (left + right) // 2
                if a[mid] <= x:
                    left = mid + 1
                else:
                    right = mid
            return right

        arr=[1,3,3,5,7,9]
        print(bisect_left(arr,100)-bisect.bisect_left(arr,100))
        print(bisect_right(arr, 100)-bisect.bisect_right(arr,100))
        print(bisect_left(arr,4)-bisect.bisect_left(arr,4))
        print(bisect_right(arr, 4)-bisect.bisect_right(arr,4))  
        print(bisect_left(arr,3)-bisect.bisect_left(arr,3))
        print(bisect_right(arr, 3)-bisect.bisect_right(arr,3))
        print(bisect_left(arr,0)-bisect.bisect_left(arr,0))
        print(bisect_right(arr, 0)-bisect.bisect_right(arr,0))
