class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [1]
        final_list = []
        final_list.append(res)
        if numRows == 1:
            return final_list
        else:
            for i in range(1,numRows):
                prev_list = final_list[-1]
                new_row = [1]
                for j in range(0, i-1):
                    new_row.append(prev_list[j] + prev_list[j+1])
                new_row.append(1)
                final_list.append(new_row)
        return final_list
        