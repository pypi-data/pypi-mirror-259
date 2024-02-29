from setuptools import setup, find_packages

dir_paths = ['./Code/em5822_sample',
             './Code/img_sample',
             './Code/mount_sample',
             ]

#   程序打包文件遍历
files = [i + '/*.pyd' for i in dir_paths]


setup(
    name='crydream',
    version='1.0.2',
    packages=find_packages(),
    description='CoreCode',
    author='CryDream',
    license='None'
)
