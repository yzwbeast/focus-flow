# 将文件夹标记为一个包
# 在 Python 2.x 以及 Python 3.2 及以下版本中，__init__.py 是 必须的，否则 Python 无法识别该文件夹是一个包，也无法从中导入模块
# __init__.py 的重要性：虽然在 Python 3.3+ 中 __init__.py 文件不是强制的，但添加它是个好习惯，确保兼容性。

# 支持包初始化
# 你可以在 __init__.py 中编写代码，初始化整个包的功能，比如定义包的版本、暴露特定的模块、导入子模块等

# 提高组织性和可维护性
# 使用 __init__.py 可以让代码更加模块化，比如可以控制哪些模块是包的公共接口（通过 __all__ 定义），隐藏内部实现。

# 向后兼容性
# 即使在现代 Python 中，__init__.py 不是强制的，但添加它可以确保你的包与旧版本的 Python 保持兼容。

