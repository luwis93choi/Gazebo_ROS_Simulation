import os
from glob import glob

from setuptools import setup

package_name = 'gazebo_practice_03_Model_Injection'

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
            'agent_gazebo = gazebo_practice_03_Model_Injection.agent_gazebo:main'
        ],
    },
)
