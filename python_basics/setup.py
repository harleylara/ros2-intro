from setuptools import setup

package_name = 'python_basics'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='jazzy',
    maintainer_email='harley.lara@outlook.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "bare = python_basics.bare:main",
            "logger = python_basics.logger:main",
            "my_node = python_basics.class:main"
        ],
    },
)
