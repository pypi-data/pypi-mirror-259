from setuptools import setup, find_packages
import sys

is_windows = sys.platform.startswith('win')


required_packages = ['numpy', 'tensorflow','opencv-python','spams',
                     'openslide-python','scikit-image','scipy','torch',
                     'torchvision', 'dominate', 'visdom', 'pillow', 'visdom',
                     'imageio', 'tqdm', 'lmdb', 'staintools', 'fitter'
                     ]

if is_windows:
    required_packages.append('spams-bin') 
else:
    required_packages.append('spams') 
setup(
    
    name='LBBNorm',
    version='11.2.0',
    packages=find_packages('src'),
    author='Laboratory of Systems Biology and Bioinformatics (LBB)',
    author_email='amasoudin@ut.ac.ir',
    description='Empower Your Tomorrow, Conquer the Future!',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license='MIT',
    package_dir={'': 'src'},
    classifiers=[
        'Development Status :: 4 - Beta', 
        
        'Intended Audience :: Science/Research',
        'Intended Audience :: Healthcare Industry',
        'Intended Audience :: Information Technology',
        
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Medical Science Apps.',
        'Topic :: Scientific/Engineering :: Image Recognition',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Operating System :: OS Independent',
    ],

    keywords='Healthcare Bio-Informatics',

    install_requires= required_packages,

)
