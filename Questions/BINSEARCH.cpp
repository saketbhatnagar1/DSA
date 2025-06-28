#include <iostream>
#include <vector>
using namespace std;
//search in rotated sorted array
int search(vector<int>& nums, int target) {
    int low = 0;
    int high = nums.size() - 1;

    while (low <= high) {
        int mid = low + (high - low) / 2;

        if (nums[mid] == target) return mid;

        // Left half is sorted
        if (nums[low] <= nums[mid]) {
            if (nums[low] <= target && target < nums[mid]) {
                high = mid - 1; // Search in left half
            } else {
                low = mid + 1;  // Search in right half
            }
        }
        // Right half is sorted
        else {
            if (nums[mid] < target && target <= nums[high]) {
                low = mid + 1;  // Search in right half
            } else {
                high = mid - 1; // Search in left half
            }
        }
    }
    return -1; // Target not found
}

int main() {
    vector<int> nums = {4, 5, 6, 7, 0, 1, 2};
    int target = 0;

    int result = search(nums, target);
    if (result != -1) {
        cout << "Target found at index: " << result << endl;
    } else {
        cout << "Target not found." << endl;
    }
    return 0;
}


