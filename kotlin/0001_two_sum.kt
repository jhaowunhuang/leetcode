fun twoSum(nums: IntArray, target: Int): IntArray {
    // To keep previous result
    val result = hashMapOf<Int, Int>()

    nums.forEachIndexed { index, value ->
        // If there is value in the map, than return its value as our index
        if (result.contains(target - value)) {
            // To prevent if it's null
            result[target - value]?.let {
                return intArrayOf(it, index)
            }
        }
        result[value] = index
    }
    return intArrayOf()
}
