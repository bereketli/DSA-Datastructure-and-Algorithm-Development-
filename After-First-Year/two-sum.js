/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const dict={}
    var result=[1,1]
    nums.forEach((currValue, idx, arr)=>{
        if (target-currValue in dict){
            result= [dict[target-currValue], idx]
        }
        dict[currValue]=idx
    })
    return result
};