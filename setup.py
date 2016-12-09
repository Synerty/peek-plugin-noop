import os
import shutil
from distutils.core import setup

from setuptools import find_packages

package_name = "papp_noop"
package_version = "0.0.0"

egg_info = "papp_noop.egg-info"
if os.path.isdir(egg_info):
    shutil.rmtree(egg_info)


def package_files(directory,
                  excludeDirs=('__pycache__',),
                  excludeFiles=('.pyc', '.js', '.js.map')):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        if [e for e in excludeDirs if e in path]:
            continue

        for filename in filenames:
            if [e for e in excludeFiles if e in filename]:
                continue

            paths.append(os.path.join('..', path, filename))

    return paths


package_data=package_files("frontend") + package_files("alembic")
package_data.append(os.path.join("..", "papp_changelog.json"))
package_data.append(os.path.join("..", "papp_package.json"))

setup(
    name=package_name,
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    package_data={'': package_data},
    version = '0.0.0',
    description='Peek Platform App - This is the No Operation test/example papp',
    author='Synerty',
    author_email='contact@synerty.com',
    url='https://github.com/Synerty/%s' % package_version,
    download_url='https://github.com/Synerty/%s/tarball/%s' % (package_name, package_version),
    keywords=['Peek', 'Python', 'Platform', 'synerty'],
    classifiers=[],
)
