class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rightMax = arr[-1]
        for i in range(len(arr)-1, -1, -1):
            if arr[i]>= rightMax:
                temp = rightMax
                rightMax =arr[i]
                arr[i] = temp
            else:
                arr[i] = rightMax
            

        arr[-1] = -1

        return arr    


        
        