/* The isBadVersion API is defined in the parent class VersionControl.
      fun isBadVersion(version: Int) : Boolean {} */

class Solution: VersionControl() {
    override fun firstBadVersion(n: Int) : Int {
            var l: Long = 1
    var r: Long = n.toLong() + 1
    
    while (l < r) {
        val m = l + (r - l) / 2

        if (isBadVersion(m.toInt()))
            r = m
        else
            l = m + 1
    }

    return l.toInt()
	}
}