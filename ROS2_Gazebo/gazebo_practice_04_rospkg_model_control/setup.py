import os
from glob import glob

from setuptools import setup

package_name = 'gazebo_practice_04_rospkg_model_control'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),

        (os.path.join('share', package_name), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='luwis',
    maintainer_email='luwis93choi@hotmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'main = gazebo_practice_04_rospkg_model_control.main:main',
            'drive_control_node = gazebo_practice_04_rospkg_model_control.drive_control_node:main'
        ],
    },
)
