def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Midpoint
        left = arr[:mid]     # Left half
        right = arr[mid:]    # Right half

        # Recursive sort on both halves
        merge_sort(left)
        merge_sort(right)

        # Merging process
        i = j = k = 0

        # Compare and merge left and right arrays
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # Copy any remaining elements of left
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        # Copy any remaining elements of right
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

# Example usage
arr = [12,8,9,3,11,5,4]
merge_sort(arr)
print("Sorted array:", arr)
