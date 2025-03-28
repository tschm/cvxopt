from setuptools import setup, Extension
from glob import glob
import os, sys, platform

# Default names of BLAS and LAPACK libraries
BLAS_LIB = ['blas']
LAPACK_LIB = ['lapack']
BLAS_EXTRA_LINK_ARGS = []

# Set environment variable BLAS_NOUNDERSCORES=1 if your BLAS/LAPACK do
# not use trailing underscores
BLAS_NOUNDERSCORES = False

# Set to 1 if you are using the random number generators in the GNU
# Scientific Library.
BUILD_GSL = 0

# Set to 1 if you are installing the fftw module.
BUILD_FFTW = 0

# Set to 1 if you are installing the glpk module.
BUILD_GLPK = 0

# Set to 1 if you are installing the DSDP module.
BUILD_DSDP = 0

# Guess prefix and library directories
if platform.system() == "Darwin":
    # macOS
    if platform.processor() == "arm":
        # Apple Silicon
        PREFIX = '/opt/homebrew'
    else:
        # Intel
        PREFIX = '/usr/local'
    BLAS_LIB_DIR = PREFIX + '/opt/openblas/lib'
    SUITESPARSE_LIB_DIR = PREFIX + '/lib'
    SUITESPARSE_INC_DIR = PREFIX + '/include/suitesparse'
    DSDP_INC_DIR = PREFIX + '/include/dsdp'
    DSDP_LIB_DIR = PREFIX + '/lib'
    FFTW_INC_DIR = PREFIX + '/include'
    FFTW_LIB_DIR = PREFIX + '/lib'
    GSL_INC_DIR = PREFIX + '/include'
    GSL_LIB_DIR = PREFIX + '/lib'
    GLPK_INC_DIR = PREFIX + '/include'
    GLPK_LIB_DIR = PREFIX + '/lib'
else:
    SUITESPARSE_INC_DIR = "/usr/include/suitesparse"
    PREFIX= '/usr'
    if glob("/usr/lib/x86_64-linux-gnu/libsuitesparse*"):
        # Ubuntu/Debian
        BLAS_LIB_DIR = PREFIX + "/lib/x86_64-linux-gnu"
        SUITESPARSE_LIB_DIR = PREFIX + "/lib/x86_64-linux-gnu"
    elif glob("/usr/lib/aarch64-linux-gnu/libsuitesparse*"):
        # Ubuntu/Debian
        BLAS_LIB_DIR = PREFIX + "/lib/aarch64-linux-gnu"
        SUITESPARSE_LIB_DIR = PREFIX + "/lib/aarch64-linux-gnu"
    elif glob("/usr/lib64/libsuitesparse*"):
        # CentOS/Fedora/RedHat/AlmaLinux x86_64
        BLAS_LIB_DIR = PREFIX + "/lib64"
        SUITESPARSE_LIB_DIR = PREFIX + "/lib64"
    else:
        # Default
        BLAS_LIB_DIR = PREFIX + "/lib"
        SUITESPARSE_LIB_DIR = PREFIX + "/lib"

    DSDP_INC_DIR = PREFIX + "/include/dsdp"
    DSDP_LIB_DIR = PREFIX + "/lib"
    FFTW_INC_DIR = PREFIX + "/include"
    FFTW_LIB_DIR = PREFIX + "/lib"
    GLPK_INC_DIR = PREFIX + "/include"
    GLPK_LIB_DIR = PREFIX + "/lib"
    GSL_INC_DIR = PREFIX + "/include/gsl"
    GSL_LIB_DIR = PREFIX + "/lib"


if sys.platform.startswith("win"):
    GSL_MACROS = [('GSL_DLL',''),('WIN32','')]
    FFTW_MACROS = [('FFTW_DLL',''),('FFTW_NO_Complex','')]
else:
    GSL_MACROS = []
    FFTW_MACROS = []

# Directory containing SuiteSparse source
SUITESPARSE_SRC_DIR = ''

# Set to 1 if compiling with MSVC 14 or later
MSVC=0

# No modifications should be needed below this line.
BLAS_NOUNDERSCORES = int(os.environ.get("CVXOPT_BLAS_NOUNDERSCORES",BLAS_NOUNDERSCORES)) == True
BLAS_LIB = os.environ.get("CVXOPT_BLAS_LIB",BLAS_LIB)
LAPACK_LIB = os.environ.get("CVXOPT_LAPACK_LIB",LAPACK_LIB)
BLAS_LIB_DIR = os.environ.get("CVXOPT_BLAS_LIB_DIR",BLAS_LIB_DIR)
BLAS_EXTRA_LINK_ARGS = os.environ.get("CVXOPT_BLAS_EXTRA_LINK_ARGS",BLAS_EXTRA_LINK_ARGS)
if type(BLAS_LIB) is str: BLAS_LIB = BLAS_LIB.strip().split(';')
if type(LAPACK_LIB) is str: LAPACK_LIB = LAPACK_LIB.strip().split(';')
if type(BLAS_EXTRA_LINK_ARGS) is str: BLAS_EXTRA_LINK_ARGS = BLAS_EXTRA_LINK_ARGS.strip().split(';')
BUILD_GSL = int(os.environ.get("CVXOPT_BUILD_GSL",BUILD_GSL))
GSL_LIB_DIR = os.environ.get("CVXOPT_GSL_LIB_DIR",GSL_LIB_DIR)
GSL_INC_DIR = os.environ.get("CVXOPT_GSL_INC_DIR",GSL_INC_DIR)
BUILD_FFTW = int(os.environ.get("CVXOPT_BUILD_FFTW",BUILD_FFTW))
FFTW_LIB_DIR = os.environ.get("CVXOPT_FFTW_LIB_DIR",FFTW_LIB_DIR)
FFTW_INC_DIR = os.environ.get("CVXOPT_FFTW_INC_DIR",FFTW_INC_DIR)
BUILD_GLPK = int(os.environ.get("CVXOPT_BUILD_GLPK",BUILD_GLPK))
GLPK_LIB_DIR = os.environ.get("CVXOPT_GLPK_LIB_DIR",GLPK_LIB_DIR)
GLPK_INC_DIR = os.environ.get("CVXOPT_GLPK_INC_DIR",GLPK_INC_DIR)
BUILD_DSDP = int(os.environ.get("CVXOPT_BUILD_DSDP",BUILD_DSDP))
DSDP_LIB_DIR = os.environ.get("CVXOPT_DSDP_LIB_DIR",DSDP_LIB_DIR)
DSDP_INC_DIR = os.environ.get("CVXOPT_DSDP_INC_DIR",DSDP_INC_DIR)
SUITESPARSE_LIB_DIR = os.environ.get("CVXOPT_SUITESPARSE_LIB_DIR",SUITESPARSE_LIB_DIR)
SUITESPARSE_INC_DIR = os.environ.get("CVXOPT_SUITESPARSE_INC_DIR",SUITESPARSE_INC_DIR)
SUITESPARSE_SRC_DIR = os.environ.get("CVXOPT_SUITESPARSE_SRC_DIR",SUITESPARSE_SRC_DIR)
MSVC = int(os.environ.get("CVXOPT_MSVC",MSVC)) == True
PYTHON_REQUIRES = (
    '>=3, !=3.0.*, !=3.1.*, '
    '!=3.2.*, !=3.3.*, !=3.4.*')
INSTALL_REQUIRES = os.environ.get("CVXOPT_INSTALL_REQUIRES",[])
if type(INSTALL_REQUIRES) is str: INSTALL_REQUIRES = INSTALL_REQUIRES.strip().split(';')

RT_LIB = ["rt"] if sys.platform.startswith("linux") else []
M_LIB = ["m"] if not MSVC else []
UMFPACK_EXTRA_COMPILE_ARGS = ["-Wno-unknown-pragmas"] if not MSVC else []

extmods = []

# Macros
MACROS = []
if BLAS_NOUNDERSCORES: MACROS.append(('BLAS_NO_UNDERSCORE',''))

# optional modules

if BUILD_GSL:
    gsl = Extension('gsl', libraries = M_LIB + ['gsl'] + BLAS_LIB,
        include_dirs = [ GSL_INC_DIR ],
        library_dirs = [ GSL_LIB_DIR, BLAS_LIB_DIR ],
        define_macros = GSL_MACROS,
        extra_link_args = BLAS_EXTRA_LINK_ARGS,
        sources = ['src/C/gsl.c'] )
    extmods += [gsl];

if BUILD_FFTW:
    fftw = Extension('fftw', libraries = ['fftw3'] + BLAS_LIB,
        include_dirs = [ FFTW_INC_DIR ],
        library_dirs = [ FFTW_LIB_DIR, BLAS_LIB_DIR ],
        define_macros = FFTW_MACROS,
        extra_link_args = BLAS_EXTRA_LINK_ARGS,
        sources = ['src/C/fftw.c'] )
    extmods += [fftw];

if BUILD_GLPK:
    glpk = Extension('glpk', libraries = ['glpk'],
        include_dirs = [ GLPK_INC_DIR ],
        library_dirs = [ GLPK_LIB_DIR ],
        sources = ['src/C/glpk.c'] )
    extmods += [glpk];

if BUILD_DSDP:
    dsdp = Extension('dsdp', libraries = ['dsdp'] + LAPACK_LIB + BLAS_LIB,
        include_dirs = [ DSDP_INC_DIR ],
        library_dirs = [ DSDP_LIB_DIR, BLAS_LIB_DIR ],
        extra_link_args = BLAS_EXTRA_LINK_ARGS,
        sources = ['src/C/dsdp.c'] )
    extmods += [dsdp];

# Required modules

base = Extension('base', libraries = M_LIB + LAPACK_LIB + BLAS_LIB,
    library_dirs = [ BLAS_LIB_DIR ],
    define_macros = MACROS,
    extra_link_args = BLAS_EXTRA_LINK_ARGS,
    sources = ['src/C/base.c','src/C/dense.c','src/C/sparse.c'])

blas = Extension('blas', libraries = BLAS_LIB,
    library_dirs = [ BLAS_LIB_DIR ],
    define_macros = MACROS,
    extra_link_args = BLAS_EXTRA_LINK_ARGS,
    sources = ['src/C/blas.c'] )

lapack = Extension('lapack', libraries = LAPACK_LIB + BLAS_LIB,
    library_dirs = [ BLAS_LIB_DIR ],
    define_macros = MACROS,
    extra_link_args = BLAS_EXTRA_LINK_ARGS,
    sources = ['src/C/lapack.c'] )

if not SUITESPARSE_SRC_DIR:
    umfpack = Extension('umfpack',
        libraries = ['umfpack','cholmod','amd','colamd','suitesparseconfig'] + LAPACK_LIB + BLAS_LIB + RT_LIB,
        include_dirs = [SUITESPARSE_INC_DIR],
        library_dirs = [SUITESPARSE_LIB_DIR, BLAS_LIB_DIR],
        sources = ['src/C/umfpack.c'])
else:
    umfpack = Extension('umfpack',
        include_dirs = [ SUITESPARSE_SRC_DIR + '/UMFPACK/Include',
            SUITESPARSE_SRC_DIR + '/AMD/Include',
            SUITESPARSE_SRC_DIR + '/UMFPACK/Source',
            SUITESPARSE_SRC_DIR + '/AMD/Source',
            SUITESPARSE_SRC_DIR + '/SuiteSparse_config' ],
        library_dirs = [ BLAS_LIB_DIR ],
        define_macros = MACROS + [('NTIMER', '1'), ('NCHOLMOD', '1')],
        libraries = LAPACK_LIB + BLAS_LIB,
        extra_compile_args = UMFPACK_EXTRA_COMPILE_ARGS,
        extra_link_args = BLAS_EXTRA_LINK_ARGS,
        sources = [ 'src/C/umfpack.c',
            SUITESPARSE_SRC_DIR + '/UMFPACK/Source/umfpack_tictoc.c',
            SUITESPARSE_SRC_DIR + '/SuiteSparse_config/SuiteSparse_config.c'] +
            glob('src/C/SuiteSparse_cvxopt_extra/umfpack/*'))

if not SUITESPARSE_SRC_DIR:
    amd = Extension('amd',
        libraries = ['amd','suitesparseconfig'] + RT_LIB,
        include_dirs = [SUITESPARSE_INC_DIR],
        library_dirs = [SUITESPARSE_LIB_DIR],
        sources = ['src/C/amd.c'])
else:
    amd = Extension('amd',
        include_dirs = [SUITESPARSE_SRC_DIR + '/AMD/Include',
            SUITESPARSE_SRC_DIR + '/SuiteSparse_config' ],
        define_macros = MACROS + [('NTIMER', '1')],
        sources = [ 'src/C/amd.c', SUITESPARSE_SRC_DIR + '/SuiteSparse_config/SuiteSparse_config.c'] +
        glob(SUITESPARSE_SRC_DIR + '/AMD/Source/*.c') )

if not SUITESPARSE_SRC_DIR:
    cholmod = Extension('cholmod',
        libraries = ['cholmod','colamd','amd','suitesparseconfig'] + LAPACK_LIB + BLAS_LIB + RT_LIB,
        include_dirs = [SUITESPARSE_INC_DIR],
        library_dirs = [SUITESPARSE_LIB_DIR, BLAS_LIB_DIR],
        sources = [ 'src/C/cholmod.c' ])
else:
    cholmod = Extension('cholmod',
        library_dirs = [ BLAS_LIB_DIR ],
        libraries = LAPACK_LIB + BLAS_LIB,
        include_dirs = [ SUITESPARSE_SRC_DIR + '/CHOLMOD/Include',
            SUITESPARSE_SRC_DIR + '/COLAMD',
            SUITESPARSE_SRC_DIR + '/AMD/Include',
            SUITESPARSE_SRC_DIR + '/COLAMD/Include',
            SUITESPARSE_SRC_DIR + '/SuiteSparse_config' ],
        define_macros = MACROS + [('NPARTITION', '1'), ('NTIMER', '1')],
        extra_link_args = BLAS_EXTRA_LINK_ARGS,
        sources = [ 'src/C/cholmod.c' ] +
            [SUITESPARSE_SRC_DIR + '/AMD/Source/' + s for s in ['amd_postorder.c', 'amd_l_postorder.c', 'amd_post_tree.c', 'amd_l_post_tree.c', 'amd_2.c', 'amd_l2.c']] +
            [SUITESPARSE_SRC_DIR + '/COLAMD/Source/' + s for s in ['colamd.c', 'colamd_l.c']] + 
            [SUITESPARSE_SRC_DIR + '/SuiteSparse_config/SuiteSparse_config.c'] +
            glob(SUITESPARSE_SRC_DIR + '/CHOLMOD/Core/c*.c') +
            glob(SUITESPARSE_SRC_DIR + '/CHOLMOD/Cholesky/c*.c') +
            glob(SUITESPARSE_SRC_DIR + '/CHOLMOD/Utility/c*.c') +
            [SUITESPARSE_SRC_DIR + '/CHOLMOD/Check/' + s for s in ['cholmod_check.c', 'cholmod_l_check.c']] +
            glob(SUITESPARSE_SRC_DIR + '/CHOLMOD/Supernodal/c*.c') )

misc_solvers = Extension('misc_solvers',
    libraries = LAPACK_LIB + BLAS_LIB,
    library_dirs = [ BLAS_LIB_DIR ],
    define_macros = MACROS,
    extra_link_args = BLAS_EXTRA_LINK_ARGS,
    sources = ['src/C/misc_solvers.c'] )

extmods += [base, blas, lapack, umfpack, cholmod, amd, misc_solvers]

setup (name = 'cvxopt',
    description = 'Convex optimization package',
    long_description = '''
CVXOPT is a free software package for convex optimization based on the
Python programming language. It can be used with the interactive Python
interpreter, on the command line by executing Python scripts, or
integrated in other software via Python extension modules. Its main
purpose is to make the development of software for convex optimization
applications straightforward by building on Python's extensive standard
library and on the strengths of Python as a high-level programming
language.''',
    author = 'M. Andersen, J. Dahl, and L. Vandenberghe',
    author_email = 'martin.skovgaard.andersen@gmail.com, dahl.joachim@gmail.com, vandenbe@ee.ucla.edu',
    url = 'https://cvxopt.org',
    project_urls = {'Source': 'https://github.com/cvxopt/cvxopt'},
    license = 'GNU GPL version 3',
    ext_package = "cvxopt",
    ext_modules = extmods,
    package_dir = {"cvxopt": "src/python"},
    package_data = {'': [".libs/*.dll", "LICENSE*"]},
    packages = ["cvxopt"],
    python_requires=PYTHON_REQUIRES,
    install_requires = INSTALL_REQUIRES,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: C',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering',
        ],
    zip_safe=False
    )
