import itertools

def calculate_24(nums):
  """
  计算24点，运算符可以重复使用，使用浮点数计算
  Args:
      nums: 包含四个数字的列表
  Returns:
      如果可以得到24，返回一个字符串表示计算过程；否则返回 None
  """
  operators = ['+', '-', '*', '/']  # 运算符

  def generate_expressions(nums):
    """
    递归生成表达式，包括以减号或除号开头的表达式
    """
    if len(nums) == 1:
      yield str(nums[0])  # 单个数字
    else:
      for i, num in enumerate(nums):
        rest_nums = nums[:i] + nums[i+1:]
        for exp in generate_expressions(rest_nums):
          for op in operators:
            yield f"({num} {op} {exp})"  # 常规情况
            yield f"({exp} {op} {num})"

  for expression in generate_expressions(nums):
    try:
      result = eval(expression)  # 使用浮点数计算
      if abs(result - 24) < 1e-5:  # 调整容差范围以适应浮点数精度
        return expression
    except ZeroDivisionError:
      pass  # 忽略除零错误
  return None

from itertools import combinations

def get_all_permutations(nums):
  """
  获取数字数组 `nums` 的所有排列。

  参数：
    nums：数字数组

  返回值：
    所有排列的列表，其中每个排列都是一个长度与 `nums` 相同的列表
  """
  result = []
  from itertools import permutations
  for perm in permutations(nums):
    result.append(list(perm))
  return result


# 输入四个数字
nums = [int(x) for x in input("请输入四个数字，用空格分隔: ").split()]

all_combinations = get_all_permutations(nums)

bFind = False

for oneNums in all_combinations:
  print(oneNums)
  # 计算并输出结果
  result = calculate_24(oneNums)
  if result:
    print(f"可以得到24: {result}")
    bFind = True
    break
  
if bFind == False:
  print("无法得到24")
    
  