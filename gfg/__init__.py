class selectionSort:
    def selectionSort(arr, n):

        for ind in range(n):
            # set index to first position in list
            low_ind = ind

            # Create a loop
            for i in range(ind + 1, n):

                # Go through each element and compare the values
                if arr[i] < arr[low_ind]:
                    low_ind = i

            # Swap the elements
            (arr[ind], arr[low_ind]) = (arr[low_ind], arr[ind])

        return arr

class insertionSort:
    def insertionSort(arr, n):

        # Iterate through the list
        for i in range(1, n):
            key = arr[i]

            # Compare arr[i] to arr[swap]
            while arr[i] < arr[i-1] and i > 0:

                # swap
                swap = i - 1

                arr[i]  = arr[swap]

                arr[i-1] = key

                i -= 1

        return arr



