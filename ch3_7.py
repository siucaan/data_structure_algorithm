"""判断一个数组是否是二叉查找树的后续遍历序列"""


def is_post_order(arr, start, end):
    # 考虑特殊情况
    if not arr:
        return False

    # 根据二叉查找树的性质，数组的最后一个元素是根节点
    root = arr[end]
    # 根节点的左子树所有节点小于根节点
    i = start
    while i < end:
        if root < arr[i]:
            break
        i += 1
    # 右子树所有节点大于根节点
    j = i
    while j < end:
        if root > arr[j]:
            return False
        j += 1
    left_tree = True
    right_tree = True

    # 左右子树也满足二叉查找树的性质，递归调用本函数即可
    if i > start:
        left_tree = is_post_order(arr, start, i-1)
    if j < end:
        right_tree = is_post_order(arr, i, end)

    return left_tree and right_tree


if __name__ == '__main__':
    arr = [1, 3, 2, 5, 7, 6, 4]
    res = is_post_order(arr, 0, len(arr)-1)
    if res:
        print('is a binary search tree!')
    else:
        print('not a binary search tree!')