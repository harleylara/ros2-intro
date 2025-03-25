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
            f"bare = {package_name}.bare:main",
            f"logger = {package_name}.logger:main",
            f"my_node = {package_name}.class:main",
            f"publisher = {package_name}.publisher:main",
            f"subscriber = {package_name}.subscriber:main",
            f"server = {package_name}.services.server:main",
            f"client = {package_name}.services.client:main",
            f"parameters = {package_name}.parameters:main",
        ],
    },
)
