def p06(nums = [2,7,11,15], target = 9):
    output_list=None
    # ↓程式區域↓
class Solution {
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
        
        for leftIndex in 0 ..< nums.count {
            
            let lackValue = target - nums[leftIndex]
            let nextElementIndex = leftIndex + 1
            
            for rightIndex in nextElementIndex ..< nums.count
                where lackValue == nums[rightIndex] {
                    return [leftIndex, rightIndex]
            }
        }
        return [-1]
    }
}
    # ↑程式區域↑
    return output_list
