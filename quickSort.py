import random
def quicksort(nums):
	qsort(nums,0,len(nums)-1)
	print nums
def qsort(nums,first,last):
	if first<last:
		partition_index = partition(nums,first,last)
		qsort(nums,first,partition_index-1)
		qsort(nums,partition_index+1,last)


def partition(nums,first,last):
	pivot = first + random.randrange(last-first+1)
	nums[pivot],nums[first]=nums[first],nums[pivot]
	partition_index = first
	for i in range(first,last+1):
		if nums[i]<nums[first]:
			partition_index+=1
			nums[partition_index],nums[i]=nums[i],nums[partition_index]
	nums[partition_index],nums[first]=nums[first],nums[partition_index]
	return partition_index


quicksort([2])
quicksort([3,2])
quicksort([4,2,7,1,9,1,8,1,0,3,5,6,3,5,2,43,6,5])
quicksort([5,3,1,2,6,7,8,5,5])